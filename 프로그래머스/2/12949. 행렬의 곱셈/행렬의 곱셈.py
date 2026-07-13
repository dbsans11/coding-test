def solution(arr1, arr2):
    row, col, n = len(arr1), len(arr2[0]), len(arr2)
    answer = [[0]*col for _ in range(row)]
    
    for r in range(row):
        for c in range(col):
            for i in range(n):
                answer[r][c] += arr1[r][i] * arr2[i][c]
    
    return answer