def solution(n):
    for i in range(501):
        if n==1: return i
        if n%2: n=3*n+1
        else: n/=2
    return -1
