def solution(s):
    answer = []
    for c in s:
        if c == ' ': answer.append(c)
        elif not answer or answer[-1] == ' ': answer.append(c.upper())
        else: answer.append(c.lower())
    return ''.join(answer)