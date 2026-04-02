def solution(d,b):
    d.sort()
    for i in range(len(d),0,-1):
        if sum(d[:i]) <= b: return i
    return 0