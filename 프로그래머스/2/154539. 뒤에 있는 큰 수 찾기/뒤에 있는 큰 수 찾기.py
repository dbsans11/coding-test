def solution(numbers):
    answer, stack = [-1]*len(numbers), []
    for i, n in enumerate(numbers):
        while stack and n > numbers[stack[-1]]:
            answer[stack.pop()] = n
        stack.append(i)
    return answer