def solution(p):
    x,n=0,0
    for v in p.split(' + '):
        if v.endswith('x'): x+= (int(v[:-1]) if v!='x' else 1)
        else: n+=int(v)
    res = []
    if x: res.append(f'{x}x' if x!=1 else 'x')
    if n: res.append(f'{n}')
    return ' + '.join(res)