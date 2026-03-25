def solution(s):
    s = [(x+y)/2 for x,y in s]
    t=sorted(s,reverse=1)
    return [t.index(v)+1 for v in s]