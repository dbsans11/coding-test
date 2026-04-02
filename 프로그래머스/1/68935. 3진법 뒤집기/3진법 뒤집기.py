def solution(n):
    t,r='',0
    while n:
        t+=str(n%3)
        n//=3
    for i,v in enumerate(t[::-1]): r+=int(v)*3**i
    return r