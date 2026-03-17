def solution(a):
    for i in range(n:=len(a)):
        for j in range(n-i):
            if a[i][j] != a[j][i]: return 0
    return 1
