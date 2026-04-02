from itertools import combinations
solution = lambda n: len(list(filter(lambda x: sum(x)==0,combinations(n,3))))