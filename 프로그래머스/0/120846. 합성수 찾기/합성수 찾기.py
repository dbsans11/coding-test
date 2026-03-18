def solution(n):
    p = [0]*(n+1)
    for i in range(2, int(n**0.5)+1):
        if not p[i]:
            for j in range(i*i, n+1, i): p[j] =1
    return sum(p)