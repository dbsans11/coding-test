def solution(land):
    h, w = len(land), len(land[0])
    for i in range(1, h):
        for j in range(w):
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])
    return max(land[h-1])
            