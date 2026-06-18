def solution(schedules, timelogs, startday):
    def time_to_mm(time):
        return (time//100)*60 + time%100
    
    answer = 0
    
    for log, sch in zip(timelogs, schedules):
        is_success = True
        sch = time_to_mm(sch) + 10
        
        for i, time in enumerate(log):
            cur = (i + startday - 1) % 7 + 1
            
            if cur == 6 or cur == 7:
                continue
            
            mm = time_to_mm(time)
            
            if mm > sch:
                is_success = False
                break
        
        if is_success:
            answer += 1
    
    return answer