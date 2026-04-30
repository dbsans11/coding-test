from collections import Counter
solution = lambda p,c: (list((Counter(p)-Counter(c)).keys()))[0]