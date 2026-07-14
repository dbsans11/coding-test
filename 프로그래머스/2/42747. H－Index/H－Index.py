def solution(citations):
    citations.sort()
    length = len(citations)
    for i, c in enumerate(citations):
        if c >= length - i:
            return length - i
    return 0