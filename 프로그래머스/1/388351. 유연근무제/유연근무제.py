def solution(schedules, timelogs, startday):
    res=0
    for sch, tlg in zip(schedules, timelogs):
        sch, temp=sch//100*60+sch%100+10, 1
        for d,t in enumerate(tlg, start=startday):
            d%=7
            if d==6 or d==0: continue
            t=t//100*60+t%100
            if t>sch:
                temp=0
                break
        res+=temp
    return res