def solution(a, f):
    r=[]
    for i,v in enumerate(f):
        if v: r+=[a[i]]*a[i]*2
        else: del r[len(r)-a[i]:]
    return r