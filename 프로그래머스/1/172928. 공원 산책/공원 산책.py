def solution(park, routes):
    height, width = len(park), len(park[0])
    nh, nw = 0, 0
    for i, r in enumerate(park):
        if (j:=r.find('S'))!=-1:
            nh, nw = i, j
            break
    
    moves = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)}
    for route in routes:
        a, b = route.split()
        b = int(b)
        dh, dw = moves[a]
        if 0<=(th:=nh+dh*b)<height and 0<=(tw:=nw+dw*b)<width:
            for i in range(1, b+1):
                if park[nh+dh*i][nw+dw*i]=='X': break
            else:
                nh, nw = th, tw
    return [nh, nw]