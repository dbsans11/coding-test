def solution(a, b, c):
    r = 1
    for i in range(1, 5-len({a,b,c})): r *= (a**i + b**i + c**i)
    return r