def solution(s):
    s = s[2:-2]
    tuples = sorted(s.split('},{'), key=len)
    tuples = [list(map(int, tp.split(','))) for tp in tuples]
    
    answer = []
    for tp in tuples:
        for n in tp:
            if n not in answer:
                answer.append(n)
    return answer