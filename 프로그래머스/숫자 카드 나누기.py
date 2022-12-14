def gcd(a, b):
    if(b>a) : a,b = b,a

    while(b!=0):
        a %= b
        a,b=b,a

    return a

def div(n):
    divisors = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisors.append(i) 
            if ( (i**2) != n) : 
                divisors.append(n // i)
    divisors.sort(reverse=True)
    return divisors

def solution(arrayA, arrayB):
    if len(arrayA) >= 2:
        a = gcd(arrayA[0], arrayA[1])
        b = gcd(arrayB[0], arrayB[1])
        
        if len(arrayA) >= 3:
            for i in arrayA[2:]:
                a = gcd(a, i)
            for j in arrayB[2:]:
                b = gcd(b, j)
    else:
        a = arrayA[0]
        b = arrayB[0]
    
    answer1 = 0
    
    for i in div(a)[:-1]:
        flag = True
        for j in arrayB:
            if j % i == 0:
                flag = False
        if flag:
            answer1 = i
            break
            
    answer2 = 0
    for i in div(b)[:-1]:
        flag = True
        for j in arrayA:
            if j % i == 0:
                flag = False
        if flag:
            answer2 = i
            break

    return max(answer1, answer2)