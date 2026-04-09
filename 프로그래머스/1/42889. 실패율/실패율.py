from collections import Counter
def solution(N,st):
    tot,cnt,res=len(st),Counter(st),{}
    for i in range(1,N+1):
        if i not in cnt: res[i]=0
        else: 
            res[i]=cnt[i]/tot
            tot-=cnt[i]
    return sorted(res,key=res.__getitem__,reverse=1)