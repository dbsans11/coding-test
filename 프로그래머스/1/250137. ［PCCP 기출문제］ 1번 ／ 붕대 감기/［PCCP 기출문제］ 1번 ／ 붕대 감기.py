def solution(bandage, health, attacks):
    t,x,y = bandage
    now, time, cnt = health, attacks[-1][0], 0
    attacks = {r[0]:r[1] for r in attacks}
    
    for i in range(1, time+1):
        if i in attacks: 
            now, cnt = now - attacks[i], 0
            if now <= 0: return -1
        else:
            now, cnt = min(now+x, health), cnt+1
            if cnt==t:
                now, cnt = min(now+y, health), 0
    return now
            