def solution(elements):
    tmp = elements*2
    nums = []
    for i in range(1,len(elements)+1):
        for j in range(1, len(elements)+1):
            nums.append(sum(tmp[i:i+j]))
    return len(set(nums))