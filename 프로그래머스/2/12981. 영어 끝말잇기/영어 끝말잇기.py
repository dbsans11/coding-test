def solution(n, words):
    for num in range(1, len(words)):
        if words[num] in words[:num] or (words[num])[0] != (words[num-1])[-1]:
            return [num%n+1, num//n+1]
    return [0,0]