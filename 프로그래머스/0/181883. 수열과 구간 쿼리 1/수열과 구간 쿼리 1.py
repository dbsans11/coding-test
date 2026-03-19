def solution(a, q):
    for s,e in q: a[s:e+1] = map(lambda x: x+1, a[s:e+1])
    return a