def solution(d,b):
    d.sort()
    while b < sum(d): d.pop()
    return len(d)