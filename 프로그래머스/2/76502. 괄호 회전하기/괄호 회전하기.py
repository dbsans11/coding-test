from collections import deque
def solution(s):
    brackets = {')':'(', ']':'[', '}':'{'}
    
    s = deque(s)
    for i in range(len(s)):
        temp, cnt = [], 0
        for c in s:
            if not temp:
                cnt += 1
            
            if temp and temp[-1] == brackets.get(c):
                temp.pop()
            else:
                temp.append(c)
        
        if not temp:
            return cnt
        else:
            s.rotate(-1)
    
    return 0