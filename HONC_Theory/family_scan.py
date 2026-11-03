# Собственный разбор Клода (плавающая точка, не ядро): семейство навесов H1 на T2 с касанием T1,
# зависимость границы ψ* (кольцо R1 входит в тело H1, G-5а) от δ и стороны навеса. Построение — § 2 интерфейса v6.
#   python3 family_scan.py <side> <delta1,delta2,...>
import math, sys, json
def add(a,b): return [a[i]+b[i] for i in range(3)]
def sub(a,b): return [a[i]-b[i] for i in range(3)]
def mul(a,k): return [x*k for x in a]
def dot(a,b): return sum(a[i]*b[i] for i in range(3))
def cross(a,b): return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def norm(a): return math.sqrt(dot(a,a))
def unit(a): n=norm(a); return [x/n for x in a]
def rot(v,k,al): return add(add(mul(v,math.cos(al)), mul(cross(k,v),math.sin(al))), mul(k, dot(k,v)*(1-math.cos(al))))
X,Y,Z=[1,0,0],[0,1,0],[0,0,1]; A1,A2=[0,0,2],[0,0,4]
def basis(T):
    c=cross(T,Z); u=unit(c) if norm(c)>1e-9 else X; return u, cross(T,u)
def dpc(P,A,T):
    w=sub(P,A); ax=dot(w,T); return math.hypot(ax, norm(sub(w,mul(T,ax)))-0.5)
def gap(A,T,B,U,N=360):
    u,v=basis(T); f=lambda t: dpc(add(A, mul(add(mul(u,math.cos(t)),mul(v,math.sin(t))),0.5)),B,U)
    vals=[f(2*math.pi*j/N) for j in range(N)]; j=min(range(N),key=vals.__getitem__)
    lo,hi=2*math.pi*(j-1)/N,2*math.pi*(j+1)/N
    for _ in range(40):
        m1,m2=lo+(hi-lo)*0.382,lo+(hi-lo)*0.618
        if f(m1)<f(m2): hi=m2
        else: lo=m1
    return min(vals[j], f((lo+hi)/2))-1
def hang(r,p,dl,d,s):
    e=add(mul(X,s*math.cos(r)), mul(add(mul(Z,-math.cos(p)),mul(Y,math.sin(p))),math.sin(r)))
    n=unit(cross(e,Y)); Tp=sub(Y, mul(e,2*dot(Y,e)))
    return add(A2,mul(e,d)), rot(Tp,n,dl)
def solve_d(r,p,dl,s):
    lo,hi=0.5,3.0
    if not (gap(*hang(r,p,dl,lo,s),A2,Y)<0<gap(*hang(r,p,dl,hi,s),A2,Y)): return None
    for _ in range(40):
        m=(lo+hi)/2
        if gap(*hang(r,p,dl,m,s),A2,Y)<0: lo=m
        else: hi=m
    return (lo+hi)/2
def g1(rd,pd,dd,s):
    r,p,dl=map(math.radians,(rd,pd,dd)); d=solve_d(r,p,dl,s)
    return None if d is None else gap(*hang(r,p,dl,d,s),A1,Y)
def roots(pd,dd,s,a=20.0,b=88.0,step=1.0):
    xs=[a+step*k for k in range(int((b-a)/step)+1)]; fs=[g1(x,pd,dd,s) for x in xs]; out=[]
    for i in range(len(xs)-1):
        if fs[i] is None or fs[i+1] is None or (fs[i]>0)==(fs[i+1]>0): continue
        lo,hi,flo=xs[i],xs[i+1],fs[i]
        for _ in range(30):
            m=(lo+hi)/2; fm=g1(m,pd,dd,s)
            if fm is None: break
            if (fm>0)==(flo>0): lo,flo=m,fm
            else: hi=m
        out.append((lo+hi)/2)
    return out, sum(1 for f in fs if f is None)
def margin(rd,pd,dd,s,N=1440):
    r,p,dl=map(math.radians,(rd,pd,dd)); d=solve_d(r,p,dl,s); A,T=hang(r,p,dl,d,s)
    f=lambda t: dpc([0,math.sin(t),3-math.cos(t)],A,T)-0.5
    vals=[f(2*math.pi*k/N) for k in range(N)]; k=min(range(N),key=vals.__getitem__)
    lo,hi=2*math.pi*(k-1)/N,2*math.pi*(k+1)/N
    for _ in range(40):
        m1,m2=lo+(hi-lo)*0.382,lo+(hi-lo)*0.618
        if f(m1)<f(m2): hi=m2
        else: lo=m1
    return min(vals[k],f((lo+hi)/2)), d
side=int(sys.argv[1]); deltas=[float(x) for x in sys.argv[2].split(',')]
for dd in deltas:
    rows=[]
    for pd in [30,35,40,45,50,55,60,65,70,75]:
        rs,undef=roots(pd,dd,side)
        rows.append({'psi':pd,'roots':[round(x,4) for x in rs],'margins':[round(margin(x,pd,dd,side)[0],5) for x in rs],'d_undefined_points':undef})
        print(json.dumps({'side':side,'delta':dd,**rows[-1]}),flush=True)
    # граница: смена знака запаса на единственном корне
    single=[r for r in rows if len(r['roots'])==1]
    for a,b in zip(single,single[1:]):
        if (a['margins'][0]>0)!=(b['margins'][0]>0) and b['psi']-a['psi']==5:
            lo,hi=a['psi'],b['psi']; mlo=a['margins'][0]
            for _ in range(9):
                m=(lo+hi)/2; rs,_=roots(m,dd,side,a=min(a['roots'][0],b['roots'][0])-3,b=max(a['roots'][0],b['roots'][0])+3,step=0.5)
                if len(rs)!=1: break
                mm=margin(rs[0],m,dd,side)[0]
                if (mm>0)==(mlo>0): lo=m
                else: hi=m
            rs,_=roots((lo+hi)/2,dd,side,a=min(a['roots'][0],b['roots'][0])-3,b=max(a['roots'][0],b['roots'][0])+3,step=0.5)
            print(json.dumps({'side':side,'delta':dd,'boundary_psi':[round(lo,3),round(hi,3)],'rho_at_boundary':[round(x,3) for x in rs],'sense':'admissible below' if mlo>0 else 'admissible above'}),flush=True)
