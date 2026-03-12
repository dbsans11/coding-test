def solution(n):
    a = set()
    for i in range(1, int(n**(0.5))+1):
        if n%i==0: a.update([i, n//i])
    return sorted(list(a))