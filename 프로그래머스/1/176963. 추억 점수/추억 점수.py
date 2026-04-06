def solution(n,y,p):
    d={k:v for k,v in zip(n,y)}
    return [sum([d.get(x,0) for x in r]) for r in p]