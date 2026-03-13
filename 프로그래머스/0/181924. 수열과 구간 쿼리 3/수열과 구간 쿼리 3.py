def solution(a, q):
    for s in q: a[s[0]], a[s[1]] = a[s[1]], a[s[0]]
    return a