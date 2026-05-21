def solution(n, w, num):
    num_y = (num-1)//w
    num_x = w-1-(num-1)%w if num_y%2 else (num-1)%w
    a=0
    
    while 1:
        next_num = (num_y+a) * w + (w - num_x if (num_y+a)%2 else num_x + 1)
        if next_num > n: break
        else: a+=1
    
    return a