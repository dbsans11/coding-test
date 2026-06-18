def solution(t, p):
    p_len = len(p)
    p_int = int(p)
    answer = 0
    
    for i in range(0, len(t) - p_len + 1):
        temp = t[i:i+p_len]
        if int(temp) <= p_int:
            answer += 1
    
    return answer