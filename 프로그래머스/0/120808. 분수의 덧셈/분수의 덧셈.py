import math
def solution(s1,m1,s2,m2):
    m=m1*m2//math.gcd(m1,m2)
    s=s1*(m//m1) + s2*(m//m2)
    return [s//(t:=math.gcd(s,m)), m//t]