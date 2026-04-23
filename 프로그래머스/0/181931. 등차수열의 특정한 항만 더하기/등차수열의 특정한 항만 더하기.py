def solution(a,d,included):
    r=0
    for i,v in enumerate(included):
        r+= v*(a+d*i)
    return r