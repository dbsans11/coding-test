def solution(s,n):
    r = ''
    for c in s:
        if c!=' ':
            t = 97 if c.islower() else 65
            c = chr((ord(c)-t+n)%26 + t)
        r+=c
    return r