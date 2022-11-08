from itertools import permutations, combinations

def solution(numbers):
    ## 숫자 만들기
    answer = 0
    numbers = list(numbers)
    nums = []
    
    for length in range(1, len(numbers)+1):
        nums.extend(permutations(numbers, length))
        
    for i in range(len(nums)):
        nums[i] = int(''.join(nums[i]))
    nums = set(nums)
    
    ## 소수 찾기
    flags = [False, False] + [True]*max(nums)
    
    for i in range(2, len(flags)):
        if flags[i] == True:
            tmp = i
            while True:
                i += tmp
                if i >= len(flags):
                    break
                flags[i] = False

    cnt = 0
    for n in nums:
        if flags[n]: cnt+=1
         
    return cnt