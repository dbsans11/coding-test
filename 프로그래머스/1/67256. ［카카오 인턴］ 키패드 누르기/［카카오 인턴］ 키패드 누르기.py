def solution(numbers, hand):
    keypad={1:(0,0),2:(0,1),3:(0,2),
           4:(1,0),5:(1,1),6:(1,2),
           7:(2,0),8:(2,1),9:(2,2),0:(3,1)}
    LR,res={'L':[3,0],'R':[3,2]},''
    hand=hand.upper()[0]
    
    for n in numbers:
        (nx,ny),(Lx,Ly),(Rx,Ry)=keypad[n],LR['L'],LR['R']
        if ny==1:
            if (Ldist:=abs(Lx-nx)+abs(Ly-ny)) == (Rdist:=abs(Rx-nx)+abs(Ry-ny)): temp=hand
            else: temp='L' if Ldist<Rdist else 'R'
        else: temp='L' if ny==0 else 'R'
        LR[temp]=[nx,ny]
        res+=temp
    
    return res