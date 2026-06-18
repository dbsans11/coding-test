def solution(price, money, count):
    total = price*(count*(1+count))//2
    return max(0, total-money)