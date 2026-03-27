def solution(bab):
    r=0
    for b in bab:
        b = b.replace('aya','*').replace('ye','*').replace('woo','*').replace('ma','*')
        if (b:=set(list(b)))==set('*'): r+=1
    return r