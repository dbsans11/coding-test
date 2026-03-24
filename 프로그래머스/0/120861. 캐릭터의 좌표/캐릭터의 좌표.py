def solution(keys,b):
    d={'up':[0,1],'down':[0,-1],'left':[-1,0],'right':[1,0]}
    limx,limy,nx,ny = b[0]//2,b[1]//2,0,0
    for k in keys:
        tx,ty=d[k]
        nx,ny=min(limx,max(-limx,nx+tx)),min(limy,max(-limy,ny+ty))
    return [nx,ny]