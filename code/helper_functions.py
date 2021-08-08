def GenerateAdd(board):
    l = []
    for location in range(0,21):
        if board[location] == 'x':
            b = board.copy()
            b[location] = 'W'
            if CloseMill(location, b):
                l = GenerateRemove(b, l)
            else:
                l.append(b)
    return l

def GenerateRemove(board, L):
    flag = 0
    for i in range(0, 21):
        if board[i] == 'B':
            if not CloseMill(i, board):
                flag = 1
                b = board.copy()
                b[i] = 'x'
                L.append(b)
    if flag==0:
        L.append(board)
    return L


def CloseMill(location, b):
    if ((b[location] == 'W') or (b[location] == 'B')):
        C = b[location]
    else:
        return False
    if location == 0:
        return True if ((b[6]==C and b[18]==C) or ((b[2]==C and b[4]==C))) else False
    elif location == 1:
        return True if (b[11]==C and b[20]==C) else False
    elif location == 2:
        return True if ((b[0]==C and b[4]==C) or ((b[7]==C and b[15]==C))) else False
    elif location == 3:
        return True if (b[10]==C and b[17]==C) else False
    elif location == 4:
        return True if ((b[0]==C and b[2]==C) or ((b[8]==C and b[12]==C))) else False
    elif location == 5:
        return True if (b[9]==C and b[14]==C) else False
    elif location == 6:
        return True if ((b[0]==C and b[18]==C) or ((b[7]==C and b[8]==C))) else False
    elif location == 7:
        return True if ((b[6]==C and b[8]==C) or ((b[2]==C and b[15]==C))) else False
    elif location == 8:
        return True if ((b[6]==C and b[7]==C) or ((b[4]==C and b[12]==C))) else False
    elif location == 9:
        return True if ((b[5]==C and b[14]==C) or ((b[10]==C and b[11]==C))) else False
    elif location == 10:
        return True if ((b[3]==C and b[17]==C) or ((b[9]==C and b[11]==C))) else False
    elif location == 11:
        return True if ((b[1]==C and b[20]==C) or ((b[9]==C and b[10]==C))) else False
    elif location == 12:
        return True if ((b[4]==C and b[8]==C) or ((b[13]==C and b[14]==C))) else False
    elif location == 13:
        return True if ((b[12]==C and b[14]==C) or ((b[16]==C and b[19]==C))) else False
    elif location == 14:
        return True if ((b[5]==C and b[9]==C) or ((b[12]==C and b[13]==C))) else False
    elif location == 15:
        return True if ((b[2]==C and b[7]==C) or ((b[16]==C and b[17]==C))) else False
    elif location == 16:
        return True if ((b[15]==C and b[17]==C) or ((b[13]==C and b[19]==C))) else False
    elif location == 17:
        return True if ((b[3]==C and b[10]==C) or ((b[15]==C and b[16]==C))) else False
    elif location == 18:
        return True if ((b[0]==C and b[6]==C) or ((b[19]==C and b[20]==C))) else False
    elif location == 19:
        return True if ((b[13]==C and b[16]==C) or ((b[18]==C and b[20]==C))) else False
    elif location == 20:
        return True if ((b[1]==C and b[11]==C) or ((b[18]==C and b[19]==C))) else False
    else:
        return False


def GenerateHopping(board):
    L = []
    for i in range(0,21):
        if board[i] == 'W':
            for j in range(0,21):
                if board[j] == 'x':
                    b = board.copy()
                    b[i] = 'x'
                    b[j] = 'W'
                    if CloseMill(j, b):
                        L = GenerateRemove(b, L)
                    else:
                        L.append(b)
    return L

def neighbors(location):
    neighbors_given_position_dict = {
      0:[1, 2, 6],           # g0, b1, a3
      1:[0, 11],             # a0, g3
      2:[0, 3, 4, 7],        # a0, f1, c2, b3
      3:[2, 10],             # b1, f3
      4:[2, 5, 8],           # b1, e2, c3
      5:[4, 9],              # c2, e3
      6:[0, 7, 18],          # a0, b3, a6
      7:[2, 6, 8, 15],       # b1, a3, c3, b5
      8:[4, 7, 12],          # c2, b3, c4
      9:[5, 10, 14],         # e2, f3, e4
      10:[3, 9, 11, 17],     # f1, e3, g3, f5
      11:[1, 10, 20],        # g0, f3, g6
      12:[8, 13],            # c3, d4
      13:[12, 14, 16],       # c4, d4, e5
      14:[9, 13],            # e3, d4
      15:[7, 16],            # b3, d5
      16:[13, 15, 17, 19],   # d4, b5, f5
      17:[10, 16],           # f3, d5
      18:[6, 19],            # a3, d6
      19:[16, 18, 20],       # d5, a6, g6
      20:[11, 19]            # g3, d6
    }
    return neighbors_given_position_dict.get(location)

def GenerateMove(board):
    L = []
    for i in range(0,21):
        if board[i] == 'W':
            n = neighbors(i)
            for j in n:
                if board[j] == 'x':
                    b = board.copy()
                    b[i] = 'x'
                    b[j] = 'W'
                    if CloseMill(j, b):
                        L = GenerateRemove(b, L)
                    else:
                        L.append(b)
    return L



def GenerateMovesOpening(board):
    L = GenerateAdd(board)
    return L


def GenerateMovesMidgameEndgame(board):
    if board.count('W') == 3:
        L = GenerateHopping(board)
    else:
        L = GenerateMove(board)
    return L



def static_estimation_opening(board):
    num_black_pieces = board.count('B')
    num_white_pieces = board.count('W')
    return (num_white_pieces - num_black_pieces)


def static_estimation_midgame(board):
    num_black_pieces = board.count('B')
    num_white_pieces = board.count('W')
    L = GenerateMovesMidgameEndgame(flip_board(board))
    num_black_moves = len(L)
    if (num_black_pieces <= 2):
        return 10**300
    elif (num_white_pieces <= 2):
        return -10**300
    elif (num_black_moves == 0):
        return 10**300
    else:
        return (1000*(num_white_pieces - num_black_pieces) - num_black_moves)



def flip_board(board):
    return ([ 'B' if value=='W' else 'W' if value=='B' else value for value in board])


def print_the_board(board):
    print(f"{board[18]}-----------------{board[19]}-----------------{board[20]}")
    print(f"|                 |                 |")
    print(f"|                 |                 |")
    print(f"|     {board[15]}-----------{board[16]}-----------{board[17]}     |")
    print(f"|     |           |           |     |")
    print(f"|     |           |           |     |")
    print(f"|     |     {board[12]}-----{board[13]}-----{board[14]}     |     |")
    print(f"|     |     |           |     |     |")
    print(f"|     |     |           |     |     |")
    print(f"{board[6]}-----{board[7]}-----{board[8]}           {board[9]}-----{board[10]}-----{board[11]}")
    print(f"|     |     |           |     |     |")
    print(f"|     |     |           |     |     |")
    print(f"|     |    _{board[4]}-----------{board[5]}     |     |")
    print(f"|     |  _/                   |     |")
    print(f"|     |_/                     |     |")
    print(f"|     {board[2]}-----------------------{board[3]}     |")
    print(f"|   _/                              |")
    print(f"|__/                                |")
    print(f"{board[0]}-----------------------------------{board[1]}")


def get_mills_count(board):
    count = 0
    for i in range(0,21):
        if board[i] == 'W':
            location = i
            if CloseMill(i, board):
                b = board.copy()
                C = 'W'
                if location == 0:
                    if (b[6]==C and b[18]==C):
                      count += 1
                    if (b[2]==C and b[4]==C):
                      count += 1
                elif location == 1:
                    if (b[11]==C and b[20]==C):
                      count+=1
                elif location == 2:
                    if (b[0]==C and b[4]==C):
                      count+=1
                    if (b[7]==C and b[15]==C):
                      count+=1
                elif location == 3:
                    if (b[10]==C and b[17]==C):
                      count+=1
                elif location == 4:
                    if (b[0]==C and b[2]==C):
                      count+=1
                    if (b[8]==C and b[12]==C):
                      count+=1
                elif location == 5:
                    if (b[9]==C and b[14]==C):
                      count+=1
                elif location == 6:
                    if (b[0]==C and b[18]==C):
                      count+=1
                    if (b[7]==C and b[8]==C):
                      count+=1
                elif location == 7:
                    if (b[6]==C and b[8]==C):
                      count+=1
                    if (b[2]==C and b[15]==C):
                      count+=1
                elif location == 8:
                    if (b[6]==C and b[7]==C):
                      count+=1
                    if (b[4]==C and b[12]==C):
                      count+=1
                elif location == 9:
                    if (b[5]==C and b[14]==C):
                      count+=1
                    if (b[10]==C and b[11]==C):
                      count+=1
                elif location == 10:
                    if (b[3]==C and b[17]==C):
                      count+=1
                    if (b[9]==C and b[11]==C):
                      count+=1
                elif location == 11:
                    if (b[1]==C and b[20]==C):
                      count+=1
                    if (b[9]==C and b[10]==C):
                      count+=1
                elif location == 12:
                    if (b[4]==C and b[8]==C):
                      count+=1
                    if (b[13]==C and b[14]==C):
                      count+=1
                elif location == 13:
                    if (b[12]==C and b[14]==C):
                      count+=1
                    if (b[16]==C and b[19]==C):
                      count+=1
                elif location == 14:
                    if (b[5]==C and b[9]==C):
                      count+=1
                    if (b[12]==C and b[13]==C) :
                      count+=1
                elif location == 15:
                    if (b[2]==C and b[7]==C):
                      count+=1
                    if (b[16]==C and b[17]==C):
                      count+=1
                elif location == 16:
                    if (b[15]==C and b[17]==C):
                      count+=1
                    if (b[13]==C and b[19]==C):
                      count+=1
                elif location == 17:
                    if (b[3]==C and b[10]==C):
                      count+=1
                    if (b[15]==C and b[16]==C):
                      count+=1
                elif location == 18:
                    if (b[0]==C and b[6]==C):
                      count+=1
                    if (b[19]==C and b[20]==C):
                      count+=1
                elif location == 19:
                    if (b[13]==C and b[16]==C):
                      count+=1
                    if (b[18]==C and b[20]==C):
                      count+=1
                elif location == 20:
                    if (b[1]==C and b[11]==C):
                      count+=1
                    if (b[18]==C and b[19]==C):
                      count+=1
    return count


def check_double_mill(board):
    for i in range(0,21):
        flag = 0
        if board[i]=='W':
            if CloseMill(i, board):
                # piece_of_interest = board[i]
                neighbors_ = neighbors(i)
                flag = 0
                for j in neighbors_:
                    if board[j]=='x':
                        b = board.copy()
                        b[i] = 'x'
                        b[j] = 'W'
                        if CloseMill(j, b):
                            flag = 1
                            break
                if flag == 1:
                    break
    if flag==1:
        return True
    else:
        return False


def get_num_of_black_blocked(board):
    count = 0
    for i in range(0,21):
        if board[i]=='B':
            flag = 0
            neighbors_ = neighbors(i)
            for j in neighbors_:
                if board[j] == 'x':
                    flag = 1
                    break

            if flag == 0:
                count += 1

    return count



def improved_static(board):
    tot = 0

    num_black_pieces = board.count('B')
    num_white_pieces = board.count('W')

    # ------------- Moves Blocked -----------
    num_of_black_blocked = get_num_of_black_blocked(board)
    num_of_white_blocked = get_num_of_black_blocked(flip_board(board))

    # --------------Mills count--------------
    num_white_mills = get_mills_count(board)
    num_black_mills = get_mills_count(flip_board(board))
    tot += (num_white_mills*2)- (num_black_mills*3)
    if check_double_mill(board):
        tot += 5
      # print("DOUBLE MILL")
    if check_double_mill(flip_board(board)):
        tot -= 10
    if num_white_pieces>0:
        if (num_of_white_blocked/num_white_pieces) < 0.3:
            tot -= 2
    if num_black_pieces>0:
        if (num_of_black_blocked/num_black_pieces) > 0.3:
            tot += 3

    tot += (num_white_pieces - num_black_pieces)*2

    return tot

#
# def improved_static_midgame(board):
#     num_black_pieces = board.count('B')
#     num_white_pieces = board.count('W')
#     L = self.GenerateMovesMidgameEndgame(flip_board(board))
#     num_black_moves = len(L)
#
#     L = self.GenerateMovesMidgameEndgame(board)
#     num_white_moves = len(L)
#
#     if (num_black_pieces <= 2):
#         return 10**300
#     elif (num_white_pieces <= 2):
#         return -10**300
#     elif (num_black_moves == 0):
#         return 10**300
#     elif num_white_moves == 0:
#         return -10**300
#
#     else:
#         black_blocked = self.get_num_of_black_blocked(board)
#         white_blocked = get_num_of_black_blocked(self.flip_board(board))
#         tot = ((black_blocked/num_black_pieces) - (white_blocked/num_white_pieces)) * (10**5)
#         tot += (10**5)* ((num_white_pieces - num_black_pieces) - num_black_moves)
#         return tot


def improved_static_midgame(board):
    num_black_pieces = board.count('B')
    num_white_pieces = board.count('W')
    L = GenerateMovesMidgameEndgame(flip_board(board))
    num_black_moves = len(L)
    if (num_black_pieces <= 2):
        return 10**300
    elif (num_white_pieces <= 2):
        return -10**300
    elif (num_black_moves == 0):
        return 10**300
    else:
      tot = 0
      # ------------- Moves Blocked -----------
      num_of_black_blocked = get_num_of_black_blocked(board)
      num_of_white_blocked = get_num_of_black_blocked(flip_board(board))

      # --------------Mills count--------------
      num_white_mills = get_mills_count(board)
      num_black_mills = get_mills_count(flip_board(board))

      tot += ((num_white_mills)- (num_black_mills))*50
      if num_white_pieces>0:
          if (num_of_white_blocked/num_white_pieces) > 0.3:
              tot -= (num_of_white_blocked)*10

          if num_black_pieces>0:
              if (num_of_black_blocked/num_black_pieces) > 0.3:
                  tot += (num_of_black_blocked)*10

          # tot += (10*(num_white_pieces - num_black_pieces) - (10*num_black_moves))
    return tot
