def solution(n):
    i,v=0,0
    while i<n:
        v+=1
        if v%3!=0 and '3' not in str(v): i+=1
    return v