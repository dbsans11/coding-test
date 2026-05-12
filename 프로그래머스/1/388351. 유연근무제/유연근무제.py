def solution(schedules, timelogs, startday):
    res=0
    for sch, tlg in zip(schedules, timelogs):
        sch, temp=str(sch), 1
        sch=int(sch[:-2])*60+int(sch[-2:])+10
        for d,t in enumerate(tlg, start=startday):
            d%=7
            if d==6 or d==0: continue
            t=str(t)
            t=int(t[:-2])*60+int(t[-2:])
            if t>sch:
                temp=0
                break
        res+=temp
    return res