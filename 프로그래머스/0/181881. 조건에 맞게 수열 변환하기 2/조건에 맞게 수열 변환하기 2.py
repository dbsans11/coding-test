def solution(a):
    cnt=0
    while 1:
        t = list(map(lambda v: v//2 if v>=50 and v%2==0 else v*2+1 if v<50 and v%2 else v, a))
        if t==a: return cnt 
        a=t
        cnt+=1