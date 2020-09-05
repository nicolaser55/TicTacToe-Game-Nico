def tic_tac_toe():
    board = [1,2,3,4,5,6,7,8,9]
    end = False
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    name1 = input('Player 1, what is your name?')
    name2 = input('Player 2, what is your name?')

    def draw():
        print('       |       |       ')
        print('   '+str(board[0])+'   |   '+str(board[1])+'   |   '+str(board[2])+'   ')
        print('       |       |       ')
        print('-----------------------')
        print('       |       |       ')
        print('   '+str(board[3])+'   |   '+str(board[4])+'   |   '+str(board[5])+'   ')
        print('       |       |       ')
        print('-----------------------')
        print('       |       |       ')
        print('   '+str(board[6])+'   |   '+str(board[7])+'   |   '+str(board[8])+'   ')
        print('       |       |       ')
        print()

    def state_name():
        name1 = input('Player 1, what is your name?')
        name2 = input('Player 2, what is your name?')

    def p1():
        n = choose_number()
        if board[n] == 'X' or board[n] == 'O':
            print('\nYou cant go there. Try again')
            p1()
        else:
            board[n] = 'X'

    def p2():
        n = choose_number()
        if board[n] == 'X' or board[n] == 'O':
            print('\nYou cant go there. Try again')
            p2()
        else:
            board[n] = 'O'

    def choose_number():
        while True:
            while True:
                a = input().upper()
                if a == 'ENDGAME':
                    print('A player has ended the game')
                    print('\nThank you for playing!')
                    exit()
                else:
                    try:
                        a = int(a)
                        a -= 1
                        if a in range(0,9):
                            return a
                        else:
                            print('\nThat is not on the board. Try again')
                            continue
                    except ValueError:
                        print('\nThat is not a number. Try again')
                    continue

    def check_board():
        count = 0
        for a in win_combinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == 'X':
                print(str(name1)+' Wins!\n')
                print('Congratulations!\n')
                return False

            if board[a[0]] == board[a[1]] == board[a[2]] == 'O':
                print(str(name2)+' Wins!\n')
                print('Congratulations!\n')
                return False

        for a in range(9):
            if board[a] == 'X' or board[a] == 'O':
                count +=1
            if count == 9:
                print('The game ends in a tie\n')
                return False

    def end_game():
        if choose_number() == False:
            return True

    print('Welcome to TicTacToe')
    if input('Ready to play? (y/n)\n').lower() == 'y':
        pass
    else:
        return end

    while not end:
        draw()
        end = check_board()
        if end == False:
            break
        print(str(name1)+' choose where to place a X')
        p1()

        print()
        draw()
        end = check_board()
        if end == False:
            break
        print(str(name2)+' choose where to place an O')
        p2()

        print()

    if input('Play again? (y/n)\n').lower() == 'y':
        print()
        tic_tac_toe()
    else:
        print('Thanks for playing!')

tic_tac_toe()
