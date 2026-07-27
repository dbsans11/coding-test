def solution(numbers, target):
    answer = 0
    
    def dfs(idx, total):
        nonlocal answer
        if idx == len(numbers):
            answer += (total==target)
            return
        dfs(idx+1, total+numbers[idx])
        dfs(idx+1, total-numbers[idx])
    
    dfs(0, 0)
    
    return answer