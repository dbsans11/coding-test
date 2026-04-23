def solution(p):
    x,n=0,0
    for c in p.split(' + '):
        if c.endswith('x'): x += int(c[:-1]) if c!='x' else 1
        else: n+=int(c)
    r=[]
    if x: r.append(f'{x}x' if x!=1 else 'x')
    if n: r.append(str(n))
    return ' + '.join(r)