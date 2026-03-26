def solution(a):
    d = {x:a.count(x) for x in a}
    t = max(d.values())
    m = [k for k,v in d.items() if t==v]
    return m[0] if len(m)==1 else -1