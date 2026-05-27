def solution(message, spoiler_ranges):
    spoilers, cur, res = [], (message[0] == ' ')*1, 0
    
    for word in list(message.split()):
        w_start, w_end = cur, cur + len(word) - 1
        for s_start, s_end in spoiler_ranges:
            if w_start <= s_end and w_end >= s_start:
                spoilers.append([word, w_start, w_end])
                message = message[:w_start] + ' ' * (w_end - w_start + 1) + message[w_end + 1:]
                break
        cur += len(word) + 1
    
    for word, start, end in spoilers:
        res += (word not in list(message.split())) * 1   
        message = message[:start] + word + message[end + 1:]
    
    return res