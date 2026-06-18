def solution(X, Y):
    answer = []
    
    for i in range(9, -1, -1):
        char_i = str(i)
        common_cnt = min(X.count(char_i), Y.count(char_i))
        
        if common_cnt > 0:
            answer.append(char_i * common_cnt)
    
    if not answer:
        return '-1'
    
    answer = ''.join(answer)
    
    if answer[0] == '0':
        return '0'
    
    return answer