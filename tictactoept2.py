# Tic Tac Toe


import random

class Board():
    def drawBoard(board):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def isSpaceFree(board, move):
            # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def isBoardFull(board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for index in range(1, 10):
            if board[index] == ' ':
                return False

    
    def getBoardCopy(board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

class Player():
    def inputPlayerLetter():
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']


    def whoGoesFirst():
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'player 1'
        else:
            return 'player 2'
        
    def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

    def getPlayerMove(board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not Board.isBoardFull(board):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)


    def getPlayer2Move(board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not Board.isBoardFull(board):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)


    def getComputerMove(board, letter):
        # Given a board and the computer's letter, determine where to move and return that move.
        if computerLetter == 'O':
            playerLetter == 'X'
        else:
            playerLetter == 'O'



    def makeMove(board, letter, move):
        board[move] = (letter)


    def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')



class Game(): 
   print('Welcome to Tic Tac Toe!')
   def start():
        while True:
            # Reset the board
            letter = ''
            theBoard = [' '] * 10
            playerLetter, computerLetter = Player.inputPlayerLetter()
            
            #player.getComputerMove(theBoard, letter)
            turn = Player.whoGoesFirst()    
            print('The ' + turn + ' will go first.')
            gameIsPlaying = True

            while gameIsPlaying:
                if turn == 'player 1':
                    # Player's turn.
                    Board.drawBoard(theBoard)
                    move = Player.getPlayerMove(theBoard)
                    letter = Player.getPlayer2Move(theBoard)
                    Player.makeMove(theBoard, playerLetter, move)
                    if player.isWinner(theBoard, playerLetter):
                        Board.drawBoard(theBoard)
                        print('Hooray! Player 1 has won the game!')
                        gameIsPlaying = False
                    else:
                        if Board.isBoardFull(theBoard):
                            Board.drawBoard(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'Player 2'

                else:
                    Board.drawBoard(theBoard)
                    letter = Player.getComputerMove(theBoard, computerLetter)
                    move = Player.getPlayer2Move(theBoard)
                    Player.makeMove(theBoard, computerLetter, move)
                    if Player.isWinner(theBoard, computerLetter):
                        Board.drawBoard(theBoard)
                        print('Hooray! Player 2 has won the game!')
                        gameIsPlaying = False
                    else:
                        if Board.isBoardFull(theBoard):
                            Board.drawBoard(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'Player 1'

            if not playAgain():
                break

class tictactoe:
   
    Game.start()
