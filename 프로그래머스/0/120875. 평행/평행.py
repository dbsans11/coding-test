def solution(d):
    inc = lambda d1, d2: (d1[1]-d2[1]) / (d1[0]-d2[0])
    return (inc(d[0],d[1])==inc(d[2],d[3]) or inc(d[0],d[2])==inc(d[1],d[3]) or inc(d[0],d[3])==inc(d[1],d[2]))*1
