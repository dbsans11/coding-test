def solution(num_list):
    s, m=0,1
    for n in num_list:
        s+=n
        m*=n
    return (m < s**2 )*1