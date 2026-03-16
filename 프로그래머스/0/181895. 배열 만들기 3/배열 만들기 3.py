def solution(a, i):
    r=[]
    for x,y in i: r+=a[x:y+1]
    return r