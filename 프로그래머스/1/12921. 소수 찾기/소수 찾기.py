def solution(n):
    e=[1]*(n+1)
    e[0]=e[1]=0
    for i in range(2,int(n**0.5)+1):
        if e[i]: e[i*i:n+1:i]=[0]*len(range(i*i,n+1,i))
    return sum(e)