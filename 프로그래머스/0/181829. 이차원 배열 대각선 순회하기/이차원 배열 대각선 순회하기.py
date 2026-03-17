def solution(b, k):
    r =0
    for i in range(len(b)):
        for j in range(len(b[i])):
            if i+j > k: break
            r+=b[i][j]
    return r