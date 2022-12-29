from collections import deque

def solution(maps):
    dxdy = [[0,-1], [0,1], [1,0],[-1,0]]
    dq = deque([[0,0]])
    
    while dq:
        x, y = dq.popleft()
        for i in dxdy:
            dx = x+i[0]
            dy = y+i[1]
            if 0<=dx<len(maps[0]) and 0<=dy<len(maps) and maps[dy][dx] == 1:
                dq.append([dx,dy])
                maps[dy][dx] = maps[y][x]+1
    
    answer = maps[-1][-1]
    if answer == 1:
        return -1
    else:
        return answer
        

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
solution(maps)