def divCnt(n):
    r=0
    for i in range(1, int(n**0.5)+1):
        if n%i==0: r+=2
    return r - (n**0.5).is_integer()

solution = lambda num,li,po: sum([po if (d:=divCnt(i))>li else d for i in range(1,num+1)])