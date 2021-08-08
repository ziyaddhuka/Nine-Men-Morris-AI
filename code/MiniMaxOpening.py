from helper_functions import *
import sys

class MiniMaxOpening:
    def __init__(self):
        self.count_pos = 0
        
    def MaxMin(self, board, depth):
        if depth == 0:
            self.count_pos = self.count_pos + 1
            return static_estimation_opening(board), board
        else:
            v = -10**305
            L = GenerateMovesOpening(board)
              # print("W", L)
            init_board = None
            for a_board in L:
                v_temp,new_board = self.MinMax(a_board, depth-1)
                if v_temp > v:
                    v = v_temp
                    init_board = a_board.copy()
                # v = max(v, MinMax(a_board, depth-1))
            return v, init_board


    def MinMax(self, board, depth):
        if depth == 0:
            self.count_pos = self.count_pos + 1
            return static_estimation_opening(board), board
        else:
            v = 10**305
            L = GenerateMovesOpening(flip_board(board))
            init_board = None
            for a_board in L:
                v_temp, new_board = self.MaxMin(flip_board(a_board), depth-1)
                if v_temp < v:
                    v = v_temp 
                    init_board = a_board.copy()
                # v = min(v, MaxMin(flip_board(a_board), depth-1))
            return v, init_board
        
        

if __name__=='__main__':
    board_file = sys.argv[1]
    board_output = sys.argv[2]
    depth = int(sys.argv[3])
    with open(board_file, 'r') as f:
        board = f.readline()
    board = list(board)
    game = MiniMaxOpening()
    static, next_move = game.MaxMin(board, depth)
    with open(board_output,'w') as f:
        f.write(''.join(next_move))
    print_the_board(next_move)
    print(f"Input position: {''.join(board)} Output position: {''.join(next_move)}")
    print("Positions evaluated by static estimation: ", game.count_pos)
    print("MINIMAX estimate: ",static)