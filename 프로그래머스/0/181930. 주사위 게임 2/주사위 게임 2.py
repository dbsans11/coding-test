def solution(a, b, c):
    r = a+b+c
    if len({a,b,c})<=2: r*=(a**2+b**2+c**2)
    if len({a,b,c})==1: r*=(a**3+b**3+c**3)
    return r
