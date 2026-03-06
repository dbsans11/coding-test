def solution(array, height):
    array.append(height)
    return sorted(array, reverse=1).index(height)