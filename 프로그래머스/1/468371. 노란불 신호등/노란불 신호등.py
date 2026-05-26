import math
import functools
def solution(signals):
    d=[sum(r) for r in signals]
    for t in range(1, math.prod(d)//functools.reduce(math.gcd,d)):
        for i, sign in enumerate(signals):
            if not sign[0]+1 <= t%d[i] <= sign[0]+sign[1]: break
        else:
            return t
    return -1