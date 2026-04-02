def solution(k,s):
    t,r=[],[]
    for i in s:
        t.append(i)
        t.sort(reverse=1)
        if len(t)>k: t.pop()
        r.append(t[-1])
    return r