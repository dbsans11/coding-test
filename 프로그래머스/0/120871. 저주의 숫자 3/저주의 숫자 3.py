def solution(n):
    i,m=0,0
    while i!=n:
        m+=1
        if m%3!=0 and '3' not in str(m):
            i+=1
    return m