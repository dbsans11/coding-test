def solution(a,q):
    r=[]
    for s,e,k in q:
        r.append(min([v for v in a[s:e+1] if v>k],default=-1))
    return r