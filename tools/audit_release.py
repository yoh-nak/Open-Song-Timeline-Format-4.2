#!/usr/bin/env python3
"""Read-only OSTF 4.2.0 package/field-coverage audit. MIT; see LICENSE-CODE.

Checks static structure and package completeness, NOT synth/DAW operation,
acoustic output, or every normative semantic rule. No network access is used.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import re
import sys
from decimal import Decimal
from pathlib import Path
from urllib.parse import unquote, urlsplit
try:
    from jsonschema import Draft202012Validator
except ImportError:
    raise SystemExit('Install the declared dependency: python -m pip install -r requirements.txt')


def strict_json(path: Path):
    def pairs(items):
        obj = {}
        for key, value in items:
            if key in obj:
                raise ValueError(f'Duplicate property: {key}')
            obj[key] = value
        return obj
    def number(token):
        value = float(token)
        if not math.isfinite(value) or (value == 0 and Decimal(token) != 0):
            raise ValueError(f'Non-finite or underflowed number: {token}')
        return value
    def constant(token):
        raise ValueError(f'Non-JSON numeric token: {token}')
    text = path.read_text(encoding='utf-8-sig')
    data = json.loads(text, object_pairs_hook=pairs, parse_float=number, parse_constant=constant)
    def strings(value):
        if isinstance(value, str):
            value.encode('utf-8', errors='strict')
        elif isinstance(value, dict):
            for key, item in value.items():
                strings(key); strings(item)
        elif isinstance(value, list):
            for item in value: strings(item)
    strings(data)
    return data


def escape(value: str) -> str:
    return value.replace('~', '~0').replace('/', '~1')


def resolve(schema: dict, ref: str):
    if not ref.startswith('#/'):
        raise ValueError(f'Non-local reference forbidden in this audit: {ref}')
    item = schema
    for key in ref[2:].split('/'):
        key = key.replace('~1', '/').replace('~0', '~')
        item = item[int(key)] if isinstance(item, list) else item[key]
    return item


def catalog(schema: dict):
    """Reachable declared properties, excluding duplicate conditional tests.

    Conditions are constraints, not separate writable parameters. Definitions
    referenced by conditional payload schemas are nevertheless fully cataloged.
    Arbitrary map keys/open vendor JSON do not form a finite field vocabulary.
    """
    fields, nodes, seen = {}, {}, set()
    def visit(node, pointer='#', conditional=False):
        if not isinstance(node, dict) or (pointer, conditional) in seen:
            return
        seen.add((pointer, conditional)); nodes[pointer] = node
        if '$ref' in node:
            visit(resolve(schema, node['$ref']), node['$ref'])
        for name, child in node.get('properties', {}).items():
            p = pointer + '/properties/' + escape(name)
            if not conditional:
                fields[p] = {'owner': pointer, 'field': name,
                             'required': name in node.get('required', []), 'schema': child}
            visit(child, p, conditional)
        for keyword in ('items', 'additionalProperties', 'contains', 'propertyNames'):
            if isinstance(node.get(keyword), dict):
                visit(node[keyword], pointer + '/' + keyword, conditional)
        for pattern, child in node.get('patternProperties', {}).items():
            visit(child, pointer + '/patternProperties/' + escape(pattern), conditional)
        for keyword in ('allOf', 'oneOf', 'anyOf', 'prefixItems'):
            for i, child in enumerate(node.get(keyword, [])):
                visit(child, f'{pointer}/{keyword}/{i}', conditional)
        for keyword in ('if', 'then', 'else', 'not'):
            if isinstance(node.get(keyword), dict):
                visit(node[keyword], pointer + '/' + keyword, True)
    visit(schema)
    return fields, nodes


def document_coverage(document, schema, fields):
    """A witness includes only a field present in a matching schema branch."""
    validator = Draft202012Validator(schema)
    witnesses, seen = {}, set()
    def valid(instance, node):
        return validator.evolve(schema=node).is_valid(instance)
    def walk(instance, node, pointer='#', location=''):
        if not isinstance(node, dict) or (pointer, location) in seen:
            return
        seen.add((pointer, location))
        if '$ref' in node:
            walk(instance, resolve(schema, node['$ref']), node['$ref'], location)
        if isinstance(instance, dict):
            for name, child in node.get('properties', {}).items():
                if name not in instance: continue
                p = pointer + '/properties/' + escape(name)
                loc = location + '/' + escape(name)
                if p in fields: witnesses.setdefault(p, loc)
                walk(instance[name], child, p, loc)
            for name, value in instance.items():
                matched = False
                for pattern, child in node.get('patternProperties', {}).items():
                    if re.search(pattern, name):
                        matched = True
                        walk(value, child, pointer + '/patternProperties/' + escape(pattern),
                             location + '/' + escape(name))
                extra = node.get('additionalProperties')
                if name not in node.get('properties', {}) and not matched and isinstance(extra, dict):
                    walk(value, extra, pointer + '/additionalProperties', location + '/' + escape(name))
        if isinstance(instance, list) and isinstance(node.get('items'), dict):
            for i, value in enumerate(instance):
                walk(value, node['items'], pointer + '/items', location + '/' + str(i))
        for keyword in ('allOf', 'oneOf', 'anyOf'):
            for i, child in enumerate(node.get(keyword, [])):
                if keyword == 'allOf' or valid(instance, child):
                    walk(instance, child, f'{pointer}/{keyword}/{i}', location)
        if 'if' in node:
            branch = 'then' if valid(instance, node['if']) else 'else'
            if isinstance(node.get(branch), dict):
                walk(instance, node[branch], pointer + '/' + branch, location)
    walk(document, schema)
    return witnesses


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def package_files(root: Path):
    return sorted(p for p in root.rglob('*') if p.is_file()
                  and '__pycache__' not in p.parts and '.git' not in p.parts
                  and p.suffix not in ('.pyc', '.pyo'))


def audit(root: Path):
    schema = strict_json(root / 'schema/ostf-4.2.0.schema.json')
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    fields, nodes = catalog(schema)
    witnesses, examples, errors = {}, [], []
    for path in sorted((root / 'examples').glob('*.ostf')):
        rel = path.relative_to(root).as_posix()
        try:
            document = strict_json(path)
            issues = list(validator.iter_errors(document))
            if issues:
                errors.extend(f'{rel}: /' + '/'.join(map(str, e.absolute_path)) + ': ' + e.message for e in issues)
            coverage = document_coverage(document, schema, fields) if not issues else {}
            for key, pointer in coverage.items():
                witnesses.setdefault(key, {'file': rel, 'instance_pointer': pointer})
            examples.append({'file': rel, 'version': document.get('version'),
                             'schema_valid': not issues, 'fields_covered': len(coverage)})
        except Exception as exc:
            errors.append(f'{rel}: {exc}')
    missing = sorted(set(fields) - set(witnesses))
    if missing: errors.append(f'{len(missing)} declared parameters lack an example witness')
    files = package_files(root)
    if len(files) > 100: errors.append(f'File limit exceeded: {len(files)} > 100')
    broken = []
    for path in files:
        if path.suffix != '.md': continue
        text = re.sub(r'```.*?```', '', path.read_text(encoding='utf-8'), flags=re.S)
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', text):
            target = target.split(' "', 1)[0].strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith('//') or not parsed.path: continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.exists(): broken.append({'file':str(path.relative_to(root)), 'target':target})
    if broken: errors.append(f'{len(broken)} broken local Markdown links')
    checksum_errors, checksum_count = [], 0
    manifest = root / 'SHA256SUMS.txt'
    if manifest.exists():
        declared = set()
        for line in manifest.read_text(encoding='utf-8').splitlines():
            if not line.strip(): continue
            digest, name = line.split('  ', 1)
            target = (root/name).resolve()
            if not target.is_relative_to(root.resolve()):
                checksum_errors.append(name); continue
            declared.add(name); checksum_count += 1
            if not target.is_file() or sha256(target) != digest:
                checksum_errors.append(name)
        expected = {p.relative_to(root).as_posix() for p in files if p != manifest}
        checksum_errors.extend(sorted(expected - declared))
        if checksum_errors: errors.append(f'{len(checksum_errors)} checksum/membership errors')
    legacy = [p for p in fields if p.startswith('#/$defs/legacy33/')]
    core_hash = hashlib.sha256(json.dumps({k:schema[k] for k in ('properties','$defs')},
                            ensure_ascii=False, sort_keys=True, separators=(',',':')).encode()).hexdigest()
    return {'format_version':'4.2.0','scope':'static-package-and-field-coverage-only',
            'external_application_tests':'not performed', 'all_semantic_rules_certified':False,
            'file_count':len(files),'file_limit':100,'examples':examples,
            'parameter_count':len(fields),'covered_parameter_count':len(witnesses),
            'active_core_parameter_count':len(fields)-len(legacy),
            'legacy_preservation_parameter_count':len(legacy),
            'missing_parameters':missing,'witnesses':witnesses,
            'schema_core_sha256':core_hash,'broken_local_links':broken,
            'manifest_entries':checksum_count,'checksum_errors':checksum_errors,
            'errors':errors,'passed':not errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, help='Optional JSON report outside the release folder')
    args = parser.parse_args()
    try: report = audit(args.root.resolve())
    except Exception as exc:
        print('AUDIT ERROR: '+str(exc), file=sys.stderr); return 2
    if args.output:
        args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    summary = {k:v for k,v in report.items() if k not in ('examples','witnesses')}
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    return 0 if report['passed'] else 1
if __name__ == '__main__':
    raise SystemExit(main())
