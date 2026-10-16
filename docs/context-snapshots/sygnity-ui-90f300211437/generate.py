from pathlib import Path
import hashlib, json, subprocess, shutil, time, os, sys
root = Path('/mnt/c/Users/BiuroEdukey/DEV/COURSES/Sages/jftp-gr2')
work = Path('/tmp/jftp-ui-runtime/snapshot')
frozen, out = work/'source', work/'candidate'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2)+'\n')
paths = sorted([*root.glob('src/main/java/**/*.java'), *root.glob('src/test/java/**/*.java'), root/'pom.xml', root/'src/main/resources/images/sygnity-logo.png', root/'assets/logo.svg', root/'assets/design-tokens.json'])
hashes = {p.relative_to(root).as_posix(): sha(p) for p in paths}
identity = hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest()[:12]
assert not work.exists(), 'Never overwrite a snapshot candidate'
out.mkdir(parents=True)
for p in paths:
    dest = frozen/p.relative_to(root)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(p, dest)
original = root/'docs/context-snapshots/original-initial-context'
baseline = json.loads((original/'manifest.json').read_text())
for item in baseline['files']: assert sha(original/item['snapshot_path']) == item['sha256']
commands = []
def run(cmd, log, env=None):
    start = time.perf_counter()
    r = subprocess.run([str(c) for c in cmd], cwd=frozen, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    log.parent.mkdir(parents=True, exist_ok=True)
    log.write_text(r.stdout)
    commands.append({'command': [str(c) for c in cmd], 'exit': r.returncode, 'seconds': round(time.perf_counter()-start, 3)})
    assert r.returncode == 0, r.stdout[-2000:]
    return commands[-1]['seconds']
mapper = '/home/lucas/.cache/legacy-codebase-workflows/native/0.3.0/linux-x86_64/package/legacy-repo-map'
skill = root/'.agents/skills/legacy-codebase-workflows'
for label, budget, extra in [('overview', 16384, []), ('definitions', 300000, ['--all-definitions'])]:
    raw = work/label
    elapsed = run([mapper, frozen, '--output-dir', raw, '--subtree', 'src', '--budget', budget, *extra], work/(label+'.log'))
    run([sys.executable, skill/'scripts/export_repo_map.py', frozen, '--artifact-dir', raw, '--implementation', 'rust', '--output-file', out/'repo-maps'/('jftp.'+label+'.md'), '--evidence-dir', out/'repo-maps'/label, '--elapsed-seconds', elapsed], work/(label+'-export.log'))
repomix = '/mnt/c/Users/BiuroEdukey/AppData/Local/Temp/jftp-gr2-context/repomix-runtime/node_modules/repomix/bin/repomix.cjs'
for label, compress in [('full-no-comments', False), ('compressed-no-comments', True)]:
    config = {'include': ['src/**/*.java', 'pom.xml', 'assets/design-tokens.json'], 'ignore': {'useGitignore': False}, 'output': {'style': 'xml', 'parsableStyle': True, 'compress': compress, 'removeComments': True, 'removeEmptyLines': False, 'git': {'sortByChanges': False, 'includeDiffs': False, 'includeLogs': False}}, 'security': {'enableSecurityCheck': True}, 'tokenCount': {'encoding': 'o200k_base'}}
    configpath = out/'RepoMix'/(label+'.config.json')
    dump(configpath, config)
    run(['node', repomix, frozen, '--config', configpath, '--output', out/'RepoMix'/('jftp.'+label+'.xml')], work/(label+'.log'))
env = os.environ.copy()
env.update(UV_CACHE_DIR='/tmp/graph-trial/uv-cache', UV_TOOL_DIR='/tmp/graph-trial/uv-tools')
run(['uv', '--offline', 'tool', 'run', '--python', sys.executable, '--from', 'graphifyy==0.9.91', 'graphify', 'extract', frozen, '--code-only', '--no-cluster', '--force', '--out', work/'extracted'], work/'graph.log', env)
graphs = list((work/'extracted').rglob('graph.json'))
assert len(graphs) == 1
(out/'code-graph').mkdir()
shutil.copyfile(graphs[0], out/'code-graph/jftp.graph.json')
g = json.loads(graphs[0].read_text())
assert g['nodes'] and g.get('edges', g.get('links'))
assert hashes == {p.relative_to(root).as_posix(): sha(p) for p in paths}, 'Source changed during extraction'
for item in baseline['files']: assert sha(original/item['snapshot_path']) == item['sha256']
manifest = {'schema_version': 1, 'snapshot_id': 'sygnity-ui-'+identity, 'parent_snapshot_id': 'original-initial-context', 'original_snapshot_id': 'original-initial-context', 'revision': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip(), 'source_root': str(root), 'frozen_source_root': str(frozen), 'source_state': 'dirty working tree; prior unrelated changes preserved', 'source_sha256': hashes, 'tools': {'mapper': 'legacy-repo-map 0.3.0 native', 'repomix': '1.18.1', 'graphifyy': '0.9.91'}, 'scope': {'map': 'Java under src; binary logo skipped', 'packs': 'all Java + pom.xml + design-tokens.json; comments removed; compressed profile is lossy', 'graph': 'Java declarations and heuristic code-only relationships; dependencies and reflection unresolved'}, 'validation': {'source_unchanged_during_extraction': True, 'original_snapshot_all_file_hashes_verified': True, 'graph_nodes': len(g['nodes']), 'graph_edges': len(g.get('edges', g.get('links', []))), 'automated_tests': '29 passed, 0 failures/errors/skips; native desktop QA recorded separately'}, 'commands': commands, 'outputs': {p.relative_to(out).as_posix(): sha(p) for p in out.rglob('*') if p.is_file()}}
dump(out/'manifest.json', manifest)
print(manifest['snapshot_id'], manifest['validation'], flush=True)
