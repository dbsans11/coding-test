def solution(n, t, m, p):
    def convert(num, n):
        if num == 0: return '0'
        digits, res = '0123456789ABCDEF', ''
        while num > 0:
            res += digits[num % n]
            num //= n
        return res[::-1]
        
    answer, i = '', 0
    while len(answer) < t*m:
        answer += convert(i, n)
        i += 1
        
    return answer[p-1::m][:t]