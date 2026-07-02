def solution(n):
    memo = [1]*(n+1)
    
    if n==1: return memo[n]
    
    for i in range(2, n+1):
        memo[i] = (memo[i-1] + memo[i-2])%1234567
    return memo[n]