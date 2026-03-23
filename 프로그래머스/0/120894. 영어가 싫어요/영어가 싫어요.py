def solution(n):
    w = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i,v in enumerate(w): n=n.replace(v,str(i))
    return int(n)
