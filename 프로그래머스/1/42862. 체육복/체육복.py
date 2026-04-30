def solution(n, lost, reserve):
    l,r = sorted(list(set(lost)-set(reserve))), set(reserve)-set(lost)
    for i in l:
        if i-1 in r: r.remove(i-1)
        elif i+1 in r: r.remove(i+1)
        else: n-=1
    return n
    