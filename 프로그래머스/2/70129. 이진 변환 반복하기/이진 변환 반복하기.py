def solution(s):
    zero, cnt = 0, 0
    while s != '1':
        zero += (z:=s.count('0'))
        s = bin(len(s) - z)[2:]
        cnt += 1
    return [cnt, zero]
        