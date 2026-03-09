def solution(numlist):
    answer = [0,0]
    for n in numlist:
        answer[n%2]+=1
    return answer