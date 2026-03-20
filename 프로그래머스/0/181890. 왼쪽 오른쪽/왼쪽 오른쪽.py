def solution(s):
    for i, x in enumerate(s):
        if x=='l': return s[:i]
        if x=='r': return s[i+1:]
    return []