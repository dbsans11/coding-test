def solution(code):
    mode = False
    ret=[]
    for i, c in enumerate(code):
        if c=='1': mode = 1 - mode
        else: 
            if i%2==mode*1: ret.append(c)
    return "EMPTY" if not ret else ''.join(ret)