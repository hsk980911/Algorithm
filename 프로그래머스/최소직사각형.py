def solution(sizes):
    answer = 0
    big = []
    small = []
    
    for i in range(len(sizes)):
        big.append(max(sizes[i]))
        small.append(min(sizes[i]))

    return max(big)*max(small)