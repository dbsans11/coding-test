def solution(bab):
    r=0
    for b in bab:
        if 'ayaaya' in b or 'yeye' in b or 'woowoo' in b or 'mama' in b: continue
        if not b.replace('aya', ' ').replace('ye', ' ').replace('woo', ' ').replace('ma',' ').strip(): r+=1
    return r