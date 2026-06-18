def solution(s):
    answer = []
    last_idx = {}
    
    for idx, char in enumerate(s):
        if char in last_idx:
            answer.append(idx - last_idx[char])
        else:
            answer.append(-1)
        
        last_idx[char] = idx
    
    return answer