def solution(a,q):
    for s,e,k in q:
        for i in range(s,e+1): a[i]+=(i%k==0)
    return a