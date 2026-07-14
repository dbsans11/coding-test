import math

def solution(progresses, speeds):
    ago = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    queue, answer = [], []
    for n in ago:
        if queue and queue[0] < n:
            answer.append(len(queue))
            queue = []
        queue.append(n)
    
    if queue:
        answer.append(len(queue))
    
    return answer