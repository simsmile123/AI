# Name: Simrith Ranjan
# Date: 12/12/21
import random

class RandomPlayer:
   #global first_turn
   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 5 # None
      self.y_max = 5 #None
      self.first_turn = 0
      
   def best_strategy(self, board, color):
       self.first_turn +=1
       best_move = list(self.find_moves(board,color))
       #if (len(best_move) == 0): return (-1,-1),0
       ##print(best_move)
       random.shuffle(best_move)
       #print(best_move)
       return (best_move[0]//5,best_move[0]%5),0     
       # Terminal test: when there's no more possible move
      #                return (-1, -1), 0
      # returns best move
      # (column num, row num), 0
      #temp = random.choice(len(best_move))
      #best_move = random.shuffle(best_move)
   def find_moves(self, board, color): 
      # first_turn = 0
       moves_found = set()
       for i in range(len(board)):
           for j in range(len(board[i])):
               if self.first_turn < 2 and board[i][j] == '.': 
                   moves_found.add(i*self.y_max+j)
               elif (color == self.black and board[i][j] == 'X') or (color == self.white and board[i][j] == 'O'):
                   for incr in self.directions:
                       x_pos = i + incr[0]
                       y_pos = j + incr[1]
                       stop = False
                       while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
                           if board[x_pos][y_pos] != '.':
                              stop = True
                           if not stop:    
                              moves_found.add(x_pos*self.y_max+y_pos)
                           x_pos += incr[0]
                           y_pos += incr[1]
       return moves_found
       # finds all possible moves
      # returns a set, e.g., {0, 1, 2, 3, ...., 24} 
      # 0 5 10 15 20
      # 1 6 11 16 21
      # 2 7 12 17 22
      # 3 8 13 18 23
      # 4 9 14 19 24
      # if 2 has 'X', board = [['.', '.', 'X', '.', '.'], [col 2], .... ]
class CustomPlayer:

   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 5
      self.y_max = 5
      self.first_turn = 0

   def best_strategy(self, board, color): #this one
      # returns best move
       self.first_turn +=1
       best_move = list(self.find_moves(board,color))
       random.shuffle(best_move)
       #print(best_move)
       return (best_move[0]//5,best_move[0]%5),0   
     # return best_move, 0
   def successors(state, turn):
       sli = [i for i in range(len(state)) if state[i] == '.']
       ret = [(state, state[0:i] + turn + state[i+1:]) for i in sli]
       return ret  # [(previous state, new state), ...]

   def terminal_test(state, tc):
       if state.find('.') < 0: return True    # check empty spot
       for li in tc:
          check_li = [state[x] for x in li]
          if len(set(check_li)) == 1 and check_li[0] != '.':
             return True
       return False
   def minimax(self, board, color, search_depth): #this one
      # search_depth: start from 2
      # returns best "value"
       return max_value(board, color, search_depth)[1],1   # returns state

   def max_value(state, turn, tc):
       # return value and state: (val, state)
       if terminal_test(state,tc): return (utility(turn, tc, state),state)
       v = (-999, state)
       temp1 = turn
       #turn = 'O' if turn == 'X' else 'X'
       for a, s in successors(state, turn):
          min = min_value(s, turn, tc)
        #  temp = max(v[0], min[0])
          #if turn == 'X': turn = 'O'
          #elif turn == 'O': turn = 'X']
          if v[0] < min[0]:
              v = (min[0], s)
       return v
         # return best_move, 1
   def min_value(state, turn, tc):
       # return value and state: (val, state)
       if terminal_test(state,tc): return (utility(turn, tc, state), state)
       v = (999, state)
       temp1 = turn
       turn = 'O' if turn == 'X' else 'X'
       for a, s in successors(state, turn):
          max = max_value(s,temp1,tc)
         # x = min(v[0], max[0])
          #if turn == 'X': turn = 'O'
          #elif turn == 'O': turn = 'X'
          if v[0] > max[0]:
              v = (max[0], s)
       return v
   def negamax(self, board, color, search_depth): #min/max
      # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
      # returns best "value" while also pruning
      pass

   def make_move(self, board, color, move): #this one
      # returns board that has been updated
      return board

   def evaluate(self, board, color, possible_moves): #this one
      # returns the utility value
      # count possible_moves (len(possible_moves)) of my turn at current board
      # opponent's possible_moves: self.find_moves(board, self.opposite_color(color))
      #if len(possible_moves)
      return len(possible_moves) -self.find_moves(board, self.opposite_color(color))

   def find_moves(self, board, color):
      # finds all possible moves
      moves_found = set()
      for i in range(len(board)):
           for j in range(len(board[i])):
               if self.first_turn < 2 and board[i][j] == '.': 
                   moves_found.add(i*self.y_max+j)
               elif (color == self.black and board[i][j] == 'X') or (color == self.white and board[i][j] == 'O'):
                   for incr in self.directions:
                       x_pos = i + incr[0]
                       y_pos = j + incr[1]
                       stop = False
                       while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
                           if board[x_pos][y_pos] != '.':
                              stop = True
                           if not stop:    
                              moves_found.add(x_pos*self.y_max+y_pos)
                           x_pos += incr[0]
                           y_pos += incr[1]
      return moves_found
      #return set()
   