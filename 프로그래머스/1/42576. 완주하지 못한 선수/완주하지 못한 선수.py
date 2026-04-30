from collections import Counter
def solution(p,c):
    p,c=Counter(p),Counter(c)
    for k,v in p.items():
        if v!=c.get(k): return k