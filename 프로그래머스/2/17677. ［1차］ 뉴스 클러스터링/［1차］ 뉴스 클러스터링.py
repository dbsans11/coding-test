from collections import Counter

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    str1 = Counter([t for i in range(len(str1) - 1) if (t:=str1[i] + str1[i+1]).isalpha()])
    str2 = Counter([t for i in range(len(str2) - 1) if (t:=str2[i] + str2[i+1]).isalpha()])
    
    intersection = sum((str1 & str2).values())
    union = sum((str1 | str2).values())
    
    answer = intersection / union if union else 1
    return int(answer*65536)