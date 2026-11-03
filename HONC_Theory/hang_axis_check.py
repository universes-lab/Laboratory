# Собственный разбор Клода (не ядро, не для DeepSeek): навес H1 на T2 по § 2 интерфейса v6, плавающая точка.
# Вариант A — по спецификации: T' = T_h − 2(T_h·u)u, затем поворот T' на δ вокруг n = норм(u × T_h).
# Вариант B — как в скриптах DeepSeek rev5: поворот самой оси хозяина T_h на δ (без отражения).
import math, sys
def add(a,b): return [a[i]+b[i] for i in range(3)]
def sub(a,b): return [a[i]-b[i] for i in range(3)]
def mul(a,k): return [x*k for x in a]
def dot(a,b): return sum(a[i]*b[i] for i in range(3))
def cross(a,b): return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def norm(a): return math.sqrt(dot(a,a))
def unit(a): n=norm(a); return [x/n for x in a]
def rot(v,k,al): return add(add(mul(v,math.cos(al)), mul(cross(k,v),math.sin(al))), mul(k, dot(k,v)*(1-math.cos(al))))
X,Y,Z=[1,0,0],[0,1,0],[0,0,1]
A1,A2=[0,0,2],[0,0,4]
def basis(T):
    u = unit(cross(T, Z)) if norm(cross(T,Z))>1e-9 else X
    return u, cross(T,u)
def d_point_circle(P,A,T):
    w=sub(P,A); ax=dot(w,T); rad=norm(sub(w,mul(T,ax))); return math.hypot(ax, rad-0.5)
def gap(A,T,B,U,N=720):
    u,v=basis(T); best=1e9; bj=0
    for j in range(N):
        f=2*math.pi*j/N; C=add(A, mul(add(mul(u,math.cos(f)),mul(v,math.sin(f))),0.5)); g=d_point_circle(C,B,U)
        if g<best: best,bj=g,j
    lo,hi=2*math.pi*(bj-1)/N, 2*math.pi*(bj+1)/N                     # уточнение золотым сечением
    g=lambda f: d_point_circle(add(A, mul(add(mul(u,math.cos(f)),mul(v,math.sin(f))),0.5)),B,U)
    for _ in range(60):
        m1,m2=lo+(hi-lo)*0.382,lo+(hi-lo)*0.618
        if g(m1)<g(m2): hi=m2
        else: lo=m1
    return min(best,g((lo+hi)/2))-1
def hang(rho,psi,delta,d,variant):
    e=add(mul(X,math.cos(rho)), mul(add(mul(Z,-math.cos(psi)),mul(Y,math.sin(psi))),math.sin(rho)))
    n=unit(cross(e,Y))
    base = sub(Y, mul(e, 2*dot(Y,e))) if variant=='A' else Y
    return add(A2,mul(e,d)), rot(base,n,delta)
def solve_d(rho,psi,delta,variant):
    lo,hi=0.5,3.0
    if not (gap(*hang(rho,psi,delta,lo,variant),A2,Y)<0<gap(*hang(rho,psi,delta,hi,variant),A2,Y)): return None
    for _ in range(50):
        m=(lo+hi)/2
        if gap(*hang(rho,psi,delta,m,variant),A2,Y)<0: lo=m
        else: hi=m
    return (lo+hi)/2
def g1(rhodeg,psideg,variant,delta=10):
    r,p,dl=[math.radians(x) for x in (rhodeg,psideg,delta)]
    d=solve_d(r,p,dl,variant)
    return (None,None) if d is None else (gap(*hang(r,p,dl,d,variant),A1,Y), d)
if len(sys.argv)==1:
  for psideg,(a,b) in [(54,(57.0,57.5)),(56,(45,65))]:
    for variant in "BA":
        pts=[a+(b-a)*k/8 for k in range(9)]; vals=[g1(x,psideg,variant) for x in pts]
        print(f"psi={psideg} вариант {variant}: " + '  '.join(f"{x:.3f}:{v[0]:+.4f}" for x,v in zip(pts,vals)))

def root(psideg,a,b,variant='A'):
    fa=g1(a,psideg,variant)[0]
    for _ in range(40):
        m=(a+b)/2; fm=g1(m,psideg,variant)[0]
        if (fm>0)==(fa>0): a,fa=m,fm
        else: b=m
    return (a+b)/2
if len(sys.argv)>1 and sys.argv[1]=='roots':
    r54=root(54,57.0,57.5); r56=root(56,60.0,62.5)
    print(f"вариант A: корень psi=54 → rho ≈ {r54:.4f}°, d ≈ {g1(r54,54,'A')[1]:.5f};  psi=56 → rho ≈ {r56:.4f}°, d ≈ {g1(r56,56,'A')[1]:.5f}")
def ring_margin(rhodeg,psideg,variant='A',delta=10,N=7200):
    r,p,dl=[math.radians(x) for x in (rhodeg,psideg,delta)]
    d=solve_d(r,p,dl,variant); A,T=hang(r,p,dl,d,variant)
    best=min((d_point_circle([0,math.sin(t),3-math.cos(t)],A,T)-0.5, t) for t in (2*math.pi*k/N for k in range(N)))
    return best[0], math.degrees(best[1])
if len(sys.argv)>1 and sys.argv[1]=='margin':
    for psideg,rho in [(54,57.2609),(56,61.6929)]:
        m,t=ring_margin(rho,psideg); print(f"вариант A, psi={psideg}, rho={rho}: min_θ dist(R1, средняя окружность H1) − ½ = {m:+.5f} при θ ≈ {t:.2f}°")
def root_scan(psideg,a=50.0,b=66.0,step=0.5):
    xs=[a+step*k for k in range(int((b-a)/step)+1)]; fs=[g1(x,psideg,'A')[0] for x in xs]
    ch=[(xs[i],xs[i+1]) for i in range(len(xs)-1) if fs[i] is not None and fs[i+1] is not None and (fs[i]>0)!=(fs[i+1]>0)]
    return ch
if len(sys.argv)>1 and sys.argv[1]=='family':
    for psideg in [54, 54.5, 55, 55.5, 56]:
        ch=root_scan(psideg)
        if len(ch)!=1: print(f"psi={psideg}: смен знака {len(ch)} {ch}"); continue
        r=root(psideg,*ch[0]); m,t=ring_margin(r,psideg,N=3600)
        print(f"psi={psideg:5.2f}: смен знака 1, rho*={r:.4f}°, запас R1–H1 = {m:+.5f} (θ≈{t:.1f}°)", flush=True)
if len(sys.argv)>1 and sys.argv[1]=='critical':
    def M(psideg):
        ch=root_scan(psideg,57.0,62.0,0.5); assert len(ch)==1, ch
        r=root(psideg,*ch[0]); return ring_margin(r,psideg,N=3600)[0], r
    a,b=55.0,55.5
    for _ in range(12):
        m=(a+b)/2; mm,_r=M(m)
        if mm>0: a=m
        else: b=m
    mm,r=M((a+b)/2)
    print(f"критический psi* ≈ {(a+b)/2:.3f}° (вилка бисекции [{a:.4f}; {b:.4f}]), rho*(psi*) ≈ {r:.3f}°, запас {mm:+.5f}")
