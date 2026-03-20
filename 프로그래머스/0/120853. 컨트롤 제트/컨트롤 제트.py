def solution(s):
    t=[]
    for v in s.split():
        if v=='Z': t.pop()
        else: t.append(int(v))
    return sum(t)