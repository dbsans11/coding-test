def solution(n):
    e=[1]*(n+1)
    e[0]=e[1]=0
    for i in range(2,int(n**0.5)+1):
        if e[i]:
            for j in range(i*i,n+1,i):
                e[j]=0
    return e.count(1)