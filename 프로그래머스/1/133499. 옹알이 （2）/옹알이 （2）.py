def solution(bab):
    r=0
    for b in bab:
        b=b.replace('aya','1').replace('ye','2').replace('woo','3').replace('ma','4')
        if max(b) not in '1234': continue
        for i,v in enumerate(b[1:]): 
            if b[i]==v: break
        else: r+=1
    return r