import heapq
def solution(k,s):
    q,r=[],[]
    for v in s:
        heapq.heappush(q,v)
        if len(q)>k: heapq.heappop(q)
        r.append(q[0])
    return r