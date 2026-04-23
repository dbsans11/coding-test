def solution(n):
    res=[]
    for i in range(2, int(n**(0.5))+1):
        if n%i==0:
            res.append(i)
            while n%i==0: n//=i
    return res+[n] if n>1 else res