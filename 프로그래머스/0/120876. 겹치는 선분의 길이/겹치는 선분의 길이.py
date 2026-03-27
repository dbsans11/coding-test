def solution(lines):
    lines, stack, res = sorted([(v, i%2) for r in lines for i,v in enumerate(r)]), [], 0
    for i, (v,t) in enumerate(lines):
        if not t: 
            stack.append(t)
            if len(stack) >= 3: res+=v-lines[i-1][0]
        else: 
            stack.pop()
            if len(stack): res+=v-lines[i-1][0]
    return res