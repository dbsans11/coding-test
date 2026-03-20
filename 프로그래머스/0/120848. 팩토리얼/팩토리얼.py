def solution(n):
    f=[1,2,6,24,120,620,5040,40320,362880]
    for i in range(9):
        if f[i]>n: return i
    return 10