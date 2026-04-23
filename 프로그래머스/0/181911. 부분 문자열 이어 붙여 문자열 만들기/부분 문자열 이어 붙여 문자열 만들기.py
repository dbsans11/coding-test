def solution(ms, pt):
    r=""
    for c,(s,e) in zip(ms,pt): r+=c[s:e+1]
    return r