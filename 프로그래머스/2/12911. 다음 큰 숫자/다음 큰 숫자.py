def solution(n):
    answer = n+1
    t = bin(n).count('1')
    while 1:
        if bin(answer).count('1') == t:
            return answer
        answer += 1