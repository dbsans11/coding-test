def solution(n):
    r,i=[],2
    while i*i<=n:
        if n%i==0:
            r.append(i)
            while n%i==0: n//=i
        i+=1
    return r+[n] if n>1 else r