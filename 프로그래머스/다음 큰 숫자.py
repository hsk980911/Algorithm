def int2binary(n):
    return str(bin(n)[2:])
        

def solution(n):
    n_b = int2binary(n)
    
    for i in range(n+1, 10000001):
        if int2binary(i).count('1') == n_b.count('1'):
            return i
