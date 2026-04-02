def solution(t,p):
    r,l=0,len(p)
    for i in range(len(t)-l+1):
        if t[i:i+l] <= p: r+=1
    return r