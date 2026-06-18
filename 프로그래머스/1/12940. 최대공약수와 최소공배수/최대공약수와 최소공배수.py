def solution(n, m):
    def gcd(a, b):
        while b>0:
            a, b = b, a%b
        return a
    
    gcd_v = gcd(n, m)
    lcm_v = n*m // gcd(n,m)
    
    return [gcd_v, lcm_v]