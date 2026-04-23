def solution(quiz):
    res=[]
    for q in quiz:
        x,op,y,_,z=q.split(' ')
        res.append('O' if (int(x)+int(y) if op=='+' else int(x)-int(y))==int(z) else 'X')
    return res