def solution(n,m,sec):
    cur,cnt=sec[0],1
    for s in sec:
        if cur+m-1 < s: cur,cnt=s,cnt+1
    return cnt