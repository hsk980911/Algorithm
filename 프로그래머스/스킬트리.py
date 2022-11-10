def solution(skill, skill_trees):
    cnt = 0
    for orders in skill_trees:
        tmp = 0
        flag = 1
        for o in orders:
            if o in skill:
                if tmp == skill.index(o):
                    tmp += 1
                else:
                    flag=0
                    break
        if flag:
            cnt+=1
    return cnt