import heapq
def solution(k, score):
    answer = []
    mh = []
    
    for s in score:
        heapq.heappush(mh, s)
        
        if len(mh) > k:
            heapq.heappop(mh)
        
        answer.append(mh[0])
    return answer