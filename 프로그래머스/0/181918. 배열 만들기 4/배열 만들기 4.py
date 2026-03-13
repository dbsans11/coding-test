def solution(a):
    s, i=[], 0
    while i<len(a):
        if not s or s[-1] < a[i]:
            s.append(a[i])
            i+=1
        else: s.pop()
    return s