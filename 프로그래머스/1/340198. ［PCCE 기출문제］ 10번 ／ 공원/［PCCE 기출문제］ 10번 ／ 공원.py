def solution(mats, park):
    def check(r,c,m):
        for i in range(r, r+m):
            if park[i][c:c+m] != ['-1']*m: return False
        return True
    
    height, width = len(park), len(park[0])
    for mat in sorted(mats, reverse=1):
        for i in range(height-mat+1):
            for j in range(width-mat+1):
                if check(i,j,mat): return mat
    return -1