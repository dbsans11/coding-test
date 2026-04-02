import math
solution = lambda n,m: [(g:=math.gcd(n,m)), n*m//g]