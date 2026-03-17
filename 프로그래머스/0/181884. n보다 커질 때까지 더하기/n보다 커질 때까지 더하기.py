def solution(numbers, n):
    r=0
    for i in numbers:
        r+=i
        if r>n: return r
    return r