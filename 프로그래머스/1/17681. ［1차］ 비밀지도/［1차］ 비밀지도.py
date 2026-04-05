def solution(n,a1,a2):
    a1,a2 = map(lambda x: str(format(x,'b').zfill(n)), a1),map(lambda x: str(format(x,'b')).zfill(n), a2)
    return [''.join(['#' if int(x) or int(y) else ' ' for x,y in zip(r1,r2)]) for r1,r2 in zip(a1,a2)]