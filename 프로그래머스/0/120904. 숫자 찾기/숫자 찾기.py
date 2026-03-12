def solution(num, k):
    num, k = str(num), str(k)
    return -1 if k not in num else num.index(k)+1