def solution(a):
    x=max(len(a),max([len(r) for r in a]))
    for r in a: r.extend([0]*(x-len(r)))
    a.extend([[0]*x]*(x-len(a)))
    return a