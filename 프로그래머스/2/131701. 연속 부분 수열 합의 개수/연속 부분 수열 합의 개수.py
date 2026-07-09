def solution(elements):
    answer = set()
    for n in range(len(elements)):
        temp = elements + elements[:n]
        for i in range(len(elements)):
            answer.add(sum(temp[i:i+n+1]))
    return len(answer)