def solution(s):
    x,y=0,0
    for a,b in s:
        if a > b: a,b=b,a
        x,y=max(x,a),max(y,b)
    return x*y