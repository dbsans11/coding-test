def solution(word):
    words, alpha = [], "AEIOU"
    
    def dfs(cur):
        if len(cur) > 5:
            return 
        
        if cur != '':
            words.append(cur)
        
        for c in alpha:
            dfs(cur + c)
    
    dfs('')
    
    return words.index(word) + 1