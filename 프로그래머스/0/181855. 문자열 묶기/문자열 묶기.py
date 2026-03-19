def solution(a):
    l = [0]*31
    for c in a: l[len(c)]+=1
    return max(l)