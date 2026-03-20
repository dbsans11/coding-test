def solution(ms,q):
    ms = list(ms)
    for s,e in q: ms[s:e+1] = ms[s:e+1][::-1]
    return ''.join(ms)