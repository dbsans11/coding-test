def solution(a,b):
    for i in range(len(a)):
        if a[-i:]+a[:-i] == b: return i
    return -1
