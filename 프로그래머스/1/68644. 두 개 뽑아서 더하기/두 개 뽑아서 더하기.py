from itertools import combinations
solution = lambda n: sorted(set([sum(v) for v in combinations(n,2)]))