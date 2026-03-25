def solution(ch):
    res=0
    while ch>=10:
        ser,t=ch//10,ch%10
        res+=ser
        ch=ser+t
    return res