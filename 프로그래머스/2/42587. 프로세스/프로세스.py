from collections import deque
def solution(priorities, location):
    priorities = deque([(idx, val) for idx, val in enumerate(priorities)])
    answer = 0
    while priorities:
        temp = priorities.popleft()
        if any(temp[1] < n[1] for n in priorities):
            priorities.append(temp)
        else:
            answer += 1
            if temp[0] == location:
                break
    return answer
            