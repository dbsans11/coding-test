def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        total, plus = 0, i
        while total < n:
            total += plus
            plus += 1
        answer += total==n
    return answer