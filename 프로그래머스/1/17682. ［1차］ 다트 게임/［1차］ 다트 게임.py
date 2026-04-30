def solution(d):
    d,r,b=d.replace('10','t'),[],{'S':1,'D':2,'T':3}
    for c in d:
        if c.isdigit(): r.append(int(c))
        elif c=='t': r.append(10)
        elif c.isalpha(): r[-1]**=b[c]
        elif c=='#': r[-1]*=-1
        elif len(r)==1: r[-1]*=2
        else: r[-1],r[-2]=r[-1]*2,r[-2]*2
    return sum(r)