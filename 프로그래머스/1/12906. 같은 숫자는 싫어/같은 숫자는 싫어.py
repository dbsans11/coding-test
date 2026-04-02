def solution(a):
    r = [a[0]]
    for v in a[1:]:
        if v!=r[-1]: r.append(v)
    return r