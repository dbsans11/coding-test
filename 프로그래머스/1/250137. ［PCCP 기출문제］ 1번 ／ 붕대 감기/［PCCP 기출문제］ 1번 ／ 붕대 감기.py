def solution(bandage, health, attacks):
    t,x,y = bandage
    hp, now = health, 0
    for atk in attacks:
        hp = min(hp+x*(time:=atk[0]-now-1)+y*(time//t), health)
        hp, now = hp - atk[1], atk[0]
        if hp<=0: return -1
    return hp
    