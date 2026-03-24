def solution(d):
    d.sort()
    return abs(d[0][0]-d[2][0]) * abs(d[0][1] - d[1][1])