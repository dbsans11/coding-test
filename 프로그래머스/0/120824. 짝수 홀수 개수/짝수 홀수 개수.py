def solution(numlist):
    n = len([x for x in numlist if x %2==0])
    return [n, len(numlist)-n]