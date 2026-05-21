def solution(video_len, pos, op_start, op_end, commands):
    video_mm, video_ss = map(int, video_len.split(':'))
    pos_mm, pos_ss = map(int, pos.split(':'))
    start_mm, start_ss = map(int, op_start.split(':'))
    end_mm, end_ss = map(int, op_end.split(':'))
    
    video_len, pos, op_start, op_end = video_mm*60+video_ss, pos_mm*60+pos_ss, start_mm*60+start_ss, end_mm*60+end_ss
    
    if op_start <= pos < op_end: pos = op_end
    for cmd in commands:
        if cmd=='prev': pos = max(0, pos-10)
        else: pos = min(video_len, pos+10)
        if op_start <= pos < op_end: pos = op_end
    
    mm, ss = divmod(pos, 60)
    return f'{str(mm).zfill(2)}:{str(ss).zfill(2)}'
            