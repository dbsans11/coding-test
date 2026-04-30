from collections import Counter
def solution(l,w):
    low=sum(((l:=Counter(l))-Counter(w)).values())
    high=low-l[0]
    return [min(high+1,6),min(low+1,6)]