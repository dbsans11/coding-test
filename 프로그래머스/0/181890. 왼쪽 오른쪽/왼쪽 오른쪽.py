def solution(sl):
    for i,v in enumerate(sl):
        if v=='l': return sl[:i]
        if v=='r': return sl[i+1:]
    return []