from collections import Counter
solution = lambda s: ''.join(sorted(c for c,cnt in Counter(s).items() if cnt==1))