def solution(num,n):
    return sorted(num, key=lambda v: (abs(v-n), -v))