"""Сводка протокола ядра по ячейкам § 2.10. Запуск: python3 summarize.py protocol_K?.json"""
import json, sys, collections
f = lambda v: '—' if v is None else (f'[{v[0]:.10g}; {v[1]:.10g}]' if isinstance(v, list) and len(v) == 2 and all(isinstance(x, (int, float)) for x in v) else str(v))
for fn in sys.argv[1:]:
    p = json.load(open(fn)); ch = p['checks']
    print('=' * 20, fn, p['kernel'] if 'kernel' in p else '', '\nverdict', json.dumps(p['verdict'], ensure_ascii=False))
    print('j5', json.dumps(p['j5'], ensure_ascii=False)[:900])
    print('unresolved', p['unresolved'])
    by = collections.defaultdict(list)
    for c in ch: by[c['req']].append(c)
    for req, cs in by.items():
        print(f'-- {req}: {len(cs)} шт.; вердикты {dict(collections.Counter(c["verdict"] for c in cs))}; полнота {dict(collections.Counter(c["completeness"] for c in cs))}; величины {set(c["quantity"] for c in cs)}')
        for c in cs:
            extra = ''
            if req.startswith('G-5б'): extra = f' κ_r {f(c["kappa_r"])} вне {f(c["outside_margin"])} край {c["outside_min_at_window_edge"]} касп {c["cusp"]["completeness"]}'
            if req in ('G-4', 'G-5а', 'R-1', 'R-2', 'R-4', 'G-3', 'G-6') or req.startswith('G-5б'):
                print(f'   {c["id"]}: {c["quantity"]} {f(c["value"])} {c["verdict"]} {c["completeness"]}{extra} {("| " + str(c.get("basis"))[:110]) if c.get("basis") else ""} {("| st " + str(c.get("status"))) if c.get("status") else ""}')
    for k in p['contacts']:
        print('   contact', json.dumps({x: k[x] for x in k if x not in ('point', 'normal', 'where')}, ensure_ascii=False)[:400])
