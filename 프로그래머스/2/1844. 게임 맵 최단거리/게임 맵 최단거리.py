from collections import deque
def solution(maps):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    h, w = len(maps), len(maps[0])
    bfs = deque([[0,0]])
    
    while bfs:
        curx, cury = bfs.popleft()
        
        if curx==h-1 and cury==w-1:
            return maps[curx][cury]
        
        for tx, ty in zip(dx, dy):
            x, y = curx+tx, cury+ty
            
            if 0<=x<h and 0<=y<w and maps[x][y]==1:
                bfs.append([x, y])
                maps[x][y] = maps[curx][cury] + 1
    
    return -1
    
                