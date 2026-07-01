def solution(brown, yellow):
    brown //= 2
    for i in range(1, int(yellow**0.5)+1):
        if yellow%i == 0:
            if i+(t:=yellow//i)+2 == brown:
                return [t+2, i+2]
            