def solution(n):
    r = [[0]*n for _ in range(n)]
    # right 0, down 1, left 2, up 3
    dx,dy,x,y,d=[0,1,0,-1],[1,0,-1,0],0,0,0
    for i in range(1,n*n+1):
        r[x][y],nx,ny=i,x+dx[d],y+dy[d]
        if not (0<=nx<n and 0<=ny<n) or r[nx][ny]: d=(d+1)%4
        x,y=x+dx[d],y+dy[d]
    return r
