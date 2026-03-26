def solution(quiz):
    res = []
    for q in quiz:
        q=q.split(' = ')
        e=q[0].split()
        res.append('O' if (int(e[0])+int(e[2]) if e[1]=='+' else int(e[0])-int(e[2]))==int(q[1]) else 'X')
    return res