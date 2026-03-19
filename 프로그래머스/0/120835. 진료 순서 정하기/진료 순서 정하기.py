def solution(e):
    t = sorted(e,reverse=1)
    return [t.index(v)+1 for v in e]