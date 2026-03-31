def solution(a):
    a.remove(min(a))
    return a or [-1]