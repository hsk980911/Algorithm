def solution(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i < 1 or j < 1:
                continue
                
            if board[i][j] == 0 or board[i-1][j]==0 or\
            board[i][j-1]==0 or board[i-1][j-1]==0:
                continue
                
            elif board[i-1][j-1] == board[i-1][j] and board[i-1][j-1] == board[i][j-1]:
                board[i][j] = int((board[i-1][j-1]**0.5+1)**2)
            else:
                board[i][j] = int((min(board[i-1][j-1], board[i][j-1], board[i-1][j])\
                                   **0.5+1)**2)
    max_num = board[i][j]    
    print(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if max_num < board[i][j]:
                max_num = board[i][j]
    return max_num