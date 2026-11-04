# Собственный разбор Клода: окрестность угла потолка семейства H1 и отрицательные δ / малые ψ по вердикту ядра.
#   python3 corner_scan.py branches <δ1,δ2,...>   — раздельные границы R1:H1 и RH1:T2 (бисекция по вердикту каждой проверки)
#   python3 corner_scan.py points '<ψ:δ;ψ:δ;...>' — вердикты всех проверок в точках
#   python3 corner_scan.py ceiling <δ> <ψ_ok> <ψ_bad> <шагов> — бисекция по общему вердикту
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.realpath(__file__))
saved = sys.argv; sys.argv = ['x', '1', '10']
exec(open(os.path.join(HERE, 'family_scan.py')).read().split('side=int(sys.argv[1])')[0])
sys.argv = saved
cache = {}
def point(psi, delta, side=1):
    key = (round(psi, 5), delta, side)
    if key in cache: return cache[key]
    rs, _ = roots(psi, delta, side, a=0.5, b=88.0, step=1.0)
    if len(rs) != 1: r = {'psi': psi, 'delta': delta, 'side': side, 'geometry': None, 'float_roots': rs}
    else:
        out = subprocess.run(['node', os.path.join(HERE, 'kernel_checks.js'), str(psi), str(round(rs[0]-0.6, 3)), str(round(rs[0]+0.6, 3)), str(delta), str(side)], capture_output=True, text=True).stdout
        r = json.loads(out); r['float_root'] = rs[0]
    print(json.dumps(r, ensure_ascii=False), flush=True); cache[key] = r; return r
def ok(r, which):
    if which == 'all': return r['geometry'] == 'PASSED'
    c = r.get(which); return c is not None and c['verdict'] == 'PASSED'
def bisect(delta, lo, hi, which, steps):
    for _ in range(steps):
        m = round((lo + hi) / 2, 5)
        if ok(point(m, delta), which): lo = m
        else: hi = m
    return [lo, hi]
mode = sys.argv[1]
if mode == 'branches':
    for d in [float(x) for x in sys.argv[2].split(',')]:
        a, b = 54.5, 56.5
        ra, rb = point(a, d), point(b, d)
        res = {'delta': d}
        for which in ('R1_H1', 'RH1_T2'):
            if ok(ra, which) and not ok(rb, which): res[which] = bisect(d, a, b, which, 6)
            else: res[which] = f'нет смены на [{a}; {b}]'
        print(json.dumps({'branch_boundaries': res}, ensure_ascii=False), flush=True)
elif mode == 'points':
    for pr in sys.argv[2].split(';'):
        p_, d_ = map(float, pr.split(':')); point(p_, d_)
elif mode == 'ceiling':
    d, lo, hi, st = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5])
    print(json.dumps({'ceiling': {'delta': d, 'bracket': bisect(d, lo, hi, 'all', st)}}), flush=True)
