def solution(b):
    m = set()
    for x in range((l:=len(b))):
        for y in range(l):
            if b[x][y]:
                for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]:
                    if 0<=(nx:=x+dx)<l and 0<=(ny:=y+dy)<l: m.add((nx,ny))
    return l*l - len(m)