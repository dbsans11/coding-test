def solution(n):
    r=0
    for i in range(1,int(n**(0.5))+1):
        if n%i==0:
            r+=i
            r+=n//i
    return r-n**(0.5) if (n**(0.5)).is_integer() else r