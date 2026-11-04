# Собственный разбор Клода: граница допустимости семейства H1 (касание с T1) по вердикту замороженного ядра.
# Для каждой точки (ψ, δ): корень ρ* оценивается в плавающей точке (family_scan.py), затем ядро получает узкую вилку
# [ρ* − 0,6; ρ* + 0,6] и выносит сертифицированный вердикт по всем проверкам КТ-1.
#   python3 boundary_kernel.py bisect <δ> <ψ_ok> <ψ_bad> <итераций>   — бисекция по вердикту PASSED / не PASSED
#   python3 boundary_kernel.py grid <δ> <ψ1,ψ2,...>                   — вердикты на сетке ψ
import json, os, subprocess, sys
sys.argv_saved = sys.argv; sys.argv = ['x', '1', '10']                 # family_scan.py читает argv при импорте — подменяю
HERE = os.path.dirname(os.path.realpath(__file__))
src = open(os.path.join(HERE, 'family_scan.py')).read().split('side=int(sys.argv[1])')[0]
exec(src)                                                               # только функции, без основного цикла
sys.argv = sys.argv_saved
def kernel(psi, delta, side=1):
    rs, _ = roots(psi, delta, side, a=5.0, b=88.0, step=1.0)
    if len(rs) != 1: return {'psi': psi, 'delta': delta, 'float_roots': rs, 'kernel': None}
    lo, hi = round(rs[0] - 0.6, 3), round(rs[0] + 0.6, 3)
    out = subprocess.run(['node', os.path.join(HERE, 'kernel_psi_scan.js'), str(psi), str(lo), str(hi), str(delta), str(side)], capture_output=True, text=True).stdout
    r = json.loads(out); r['float_root'] = rs[0]; return r
def short(r):
    k = r.get('geometry'); fails = [c.split(' FORBIDDEN')[0].split(' UNRESOLVED')[0] for c in r.get('not_passed', [])]
    return {'psi': r['psi'], 'delta': r['delta'], 'geometry': k, 'fails': fails, 'root_deg': r.get('root_deg'), 'unresolved': r.get('unresolved'), 'float_roots': r.get('float_roots')}
mode = sys.argv[1]
if mode == 'bisect':
    delta, ok, bad, it = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5])
    for psi in (ok, bad):
        print(json.dumps({'endpoint': True, **short(kernel(psi, delta))}, ensure_ascii=False), flush=True)
    for _ in range(it):
        m = round((ok + bad) / 2, 4); r = short(kernel(m, delta)); print(json.dumps(r, ensure_ascii=False), flush=True)
        if r['geometry'] == 'PASSED': ok = m
        else: bad = m
    print(json.dumps({'delta': delta, 'boundary': [ok, bad]}), flush=True)
else:
    delta = float(sys.argv[2])
    for psi in [float(x) for x in sys.argv[3].split(',')]:
        print(json.dumps(short(kernel(psi, delta)), ensure_ascii=False), flush=True)
