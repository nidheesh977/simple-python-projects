while True:    
    #board
    #display board
    #play game
    #handle turn
    #check win
        #check rows
        #check columns
        #check diagonals
    #check tie
    #flip player
    print("              ### TIC - TAC - TOE ###")
    print("New Game")
    
    
    #if game still going
    game_still_going=True
    
    #who won or tie?
    winner=None
    
    current_player="X"
    board=["-","-","-",
           "-","-","-",
           "-","-","-"]
    
    def display_board():
        print("| "+board[0] + " | " + board[1] + " | " + board[2] + " | ")
        print("| "+board[3] + " | " + board[4] + " | " + board[5] + " | ")
        print("| "+board[6] + " | " + board[7] + " | " + board[8] + " | ")
        
        
      
    
    def play_game():
        
    #Display initial board
        display_board()
        
        
        
        while game_still_going:
            handle_turn(current_player)
            check_if_game_over()
            flip_player()
            
        #The game has ended
        if winner=="X" or winner=="O":
            print("\n",winner+" Won")
        elif winner==None:
            print("Tie")
        .
    def handle_turn(player):
        
        print("\n",player+"'s turn.")
        position=input("Choose a position from 1 to 9 : ")
        valid=False
        while not valid:
            while position not in ["1","2","3","4","5","6","7","8","9"]:
                print("Invalid input ,try again -\n")
                display_board()
                print("\n",player+"'s turn.")
                
                position=input("Choose a position from 1 to 9 : ")
                
        
            position=int(position)-1
            
            if board[position]=="-":
                valid=True
            else:
                
                print("You can't go there. Go again.")
                
            
        board[position]=player
        
        display_board()
        #print("\n",player+"'s turn.")
      
        
    def check_if_game_over():
        check_for_winner()
        check_if_tie()
        
    def check_for_winner():
        #Set up global variables
        global winner    
        #check rows
        row_winner=check_rows()
        #check_columns
        column_winner=check_columns()
        #check_diagonals
        diagonal_winner=check_diagonals()
        
        if row_winner:
            winner=row_winner
            
        elif column_winner:
            winner=column_winner
            
        elif diagonal_winner:
            winner=diagonal_winner
            
        else:
            #There was no win
            winner=None
        return 
    a
    def check_rows():
        global game_still_going
        #check if any of the rows has same value(and is not empty)
        row_1=board[0]==board[1]==board[2]!="-"
        row_2=board[3]==board[4]==board[5]!="-"
        row_3=board[6]==board[7]==board[8]!="-"
        #if any does have a match ,falg that there is a win
        if row_1 or row_2 or row_3:
            game_still_going=False
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
        return
    
    def check_columns():
        global game_still_going
        
        column_1=board[0]==board[3]==board[6]!="-"
        column_2=board[1]==board[4]==board[7]!="-"
        column_3=board[2]==board[5]==board[8]!="-"
        if column_1 or column_2 or column_3:
            game_still_going=False
        if column_1:
            return board[0]
        elif column_2:
            return board[1]
        elif column_3:
            return board[2]
        return
    
    def check_diagonals():
        global game_still_going
        diagonals_1=board[0]==board[4]==board[8]!="-"
        diagonals_2=board[2]==board[4]==board[6]!="-"
        if diagonals_1 or diagonals_2:
            game_still_going=False
        if diagonals_1:
            return board[0]
        elif diagonals_2:
            return board[2]
        return
    
    def check_if_tie():
        global game_still_going
        if "-" not in board:
            game_still_going=False
        return
    
    
    def flip_player():
        global current_player
        #if current player is X change it to O
        if current_player=="X":
            current_player="O"
        #if current player is O change it to X
        elif current_player=="O":
            current_player="X"
        return
        
    play_game()


