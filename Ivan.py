



#board = [[["O", "X", "O"],      використовував для самоперевірки
#            ["X", "O", "X"],
#            ["X", "O", "O"]]]  



def win_board_Hor(board):
    for row_1 in board[0]:
        print("1",row_1)
        if row_1[0] == "X" and row_1[1] == "X" and row_1[2] == "X":
            return "X"
            
    
        elif row_1[0] == "O" and row_1[1] == "O" and row_1[2] == "O":
            return "O"
            
    return None
            
            
    

def win_board_Ver(board):
   for i in range(3):
        if board[0][0][i]=="X" and board[0][1][i]=="X" and board[0][2][i]=="X":
            return "X"
            
            
        elif board[0][0][i]=="O" and board[0][1][i]=="O" and board[0][2][i]=="O":
            return "O"
            
        
   return None
            
   

def win_board_Dia(board):
    if board[0][0][0]=="X" and board[0][1][1]=="X" and board[0][2][2]=="X" or board[0][0][2]=="X" and board[0][1][1]=="X" and board[0][2][0]=="X":
            return "X"
    elif board[0][0][0]=="O" and board[0][1][1]=="O" and board[0][2][2]=="O" or board[0][0][2]=="O" and board[0][1][1]=="O" and board[0][2][0]=="O":
        return "O"
        
    return None




    
win_board_Hor(board)
win_board_Ver(board)
win_board_Dia(board)
    



def free_cell_board(board):
    free_found = False
    for i in range(3):
        for j in range(3):
            cell = board[0][i][j]
            if cell == "":
                free_found = True  
            else:
                pass
    if free_found is True:
        print("free")
    else:
        print("busy")




free_cell_board(board)

