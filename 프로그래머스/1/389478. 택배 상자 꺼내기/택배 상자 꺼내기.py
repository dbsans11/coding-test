def solution(n, w, num):
    top_y, num_y = (n-1)//w, (num-1)//w
    top_x = w-1-(n-1)%w if top_y%2 else (n-1)%w
    num_x = w-1-(num-1)%w if num_y%2 else (num-1)%w
    
    if top_y%2: return top_y-num_y + (num_x >= top_x)*1
    else: return top_y-num_y + (num_x <= top_x)*1