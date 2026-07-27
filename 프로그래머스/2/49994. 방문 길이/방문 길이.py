def solution(dirs):
    move = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1,0)}
    visited = set()
    curx, cury = 0, 0
    
    for d in dirs:
        dx, dy = move[d]
        tx, ty = curx + dx, cury + dy
        
        if -5 <= tx <= 5 and -5 <= ty <= 5:
            visited.add(((curx, cury), (tx, ty)))
            visited.add(((tx, ty), (curx, cury)))
            curx, cury = tx, ty
    
    return len(visited) // 2