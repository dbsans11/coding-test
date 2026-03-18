solution = lambda s: ''.join(c for i,c in enumerate(s) if c not in s[:i])
