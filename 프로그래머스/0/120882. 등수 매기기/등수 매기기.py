def solution(s):
    s=[x+y for x,y in s]
    r = {}
    for i,v in enumerate(sorted(s,reverse=1)):
        if v not in r: r[v]=i+1
    return [r[v] for v in s]