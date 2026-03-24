def solution(r,a):
    r = sorted([(v,i) for i,v in enumerate(r) if a[i]])
    return 10000*r[0][1]+100*r[1][1]+r[2][1]