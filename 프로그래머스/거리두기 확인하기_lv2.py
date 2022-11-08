def distance(room):
    ds = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1),(2,0),(-2,0),(0,2),(0,-2)]
    tmp = []
    for row in room:
        tmp.append(list(row))
    for i in range(5):
        for j in range(5):
            if tmp[i][j] == 'P':
                for d in ds:
                    dx = d[0] + i
                    dy = d[1] + j
                    if 0<=dx<5 and 0<=dy<5:
                        if tmp[dx][dy] == 'P':
                            if abs(d[0]+d[1]) == 1:
                                return 0
                            elif abs(d[0]) == 2:
                                print(abs(d[0]))
                                if tmp[(dx+i)//2][j] == 'O':
                                    return 0
                            elif abs(d[1]) == 2:
                                print(abs(d[1]))
                                if tmp[i][(dy+j)//2] == 'O':
                                    return 0
                            else:
                                if tmp[max(dx, i)][min(dy, j)] == 'O' \
                                or tmp[min(dx, i)][max(dy, j)] == 'O':
                                    return 0
    return 1

def solution(places):
    answer = []
    for room in places:
        answer.append(distance(room))
        
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))