def solution(a):
    s=[]
    for x in a: s.append(x) if not s or s[-1]!=x else s.pop()
    return s or [-1]