def solution(hp):
    r=hp//5
    hp%=5
    r+=hp//3
    return r+hp%3