def solution(a):
    m1,m2,m3,c = [1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5],[0,0,0]
    for i,v in enumerate(a):
        if v==m1[i%5]: c[0]+=1
        if v==m2[i%8]: c[1]+=1
        if v==m3[i%10]: c[2]+=1
    m = max(c)
    return [i+1 for i,v in enumerate(c) if v==m]