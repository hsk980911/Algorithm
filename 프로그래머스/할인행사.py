def solution(want, number, discount):
    wish_list = []
    for i in range(len(want)):
        wish_list.extend([want[i]]*number[i])
    print(wish_list)
        
    cnt = 0
    for i in range(len(discount) - 9):
        flag = True
        temp = wish_list.copy()
        for j in discount[i:i+10]:
            if j not in temp:
                flag = False
                break
            else:
                temp.remove(j)
        if flag:
            cnt += 1
    
    return cnt