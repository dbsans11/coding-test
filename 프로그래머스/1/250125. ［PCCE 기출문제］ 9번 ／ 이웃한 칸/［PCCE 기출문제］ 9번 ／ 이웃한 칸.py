def solution(bd,h,w):
    cnt,dpos,co,l=0,[[-1,0],[1,0],[0,-1],[0,1]],bd[h][w],len(bd)
    for dh,dw in dpos:
        if 0<=(nh:=h+dh)<l and 0<=(nw:=w+dw)<l:
            cnt+=bd[nh][nw]==co
    return cnt
            