def solution(a, n):
    a.sort()
    v = [abs(n-i) for i in a]
    return a[v.index(min(v))]