def solution(x):
    r = [x]
    while x!=1:
        x = 3*x+1 if x%2 else x//2
        r.append(x)
    return r