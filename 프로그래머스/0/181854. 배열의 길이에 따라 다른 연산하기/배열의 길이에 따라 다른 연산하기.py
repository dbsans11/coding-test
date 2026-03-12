def solution(a, n):
    if len(a)%2: 
        for i in range(0, len(a), 2): a[i]+=n
    else:
        for i in range(1, len(a), 2): a[i]+=n
    return a