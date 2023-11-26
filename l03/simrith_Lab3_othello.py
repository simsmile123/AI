# Name: simrith ranjan
# Date: 01/11/22

import random
class RandomBot:
   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      
      ''' Your code goes here '''
      best_move = list(self.find_moves(board,color))
      random.shuffle(best_move)
       #print(best_move)
     # print(stones_left(board))
      return (best_move[0]//self.x_max,best_move[0]%self.y_max),0  
      #best_move = [1, 1] # change this
      #return best_move, 0

   def stones_left(self, board):
    # returns number of stones that can still be placed (empty spots)
      count = 0
      for x in range(len(board)*len(board[0])):
            if board[x//8, x%8] == '.':
                count += count +1
      return count

   def find_moves(self, board, color):
    # finds all possible moves
    moves_found = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
                moves_found.update({i*self.y_max+j: flipped_stones})
    return moves_found
      #return 1

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
    if board[x][y] != ".":
        return []
    if color == self.black:
        color = "@"
    else:
        color = "O"
    flipped_stones = []
    for incr in self.directions:
        temp_flip = []
        x_pos = x + incr[0]
        y_pos = y + incr[1]
        while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
            if board[x_pos][y_pos] == ".":
                break
            if board[x_pos][y_pos] == color:
                flipped_stones += temp_flip
                break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
    return flipped_stones

class Best_AI_bot:

   def __init__(self):
      self.white = "o"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = None
      self.y_max = None

   def best_strategy(self, board, color):
    # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      best_move = list(self.find_moves(board,color))
      random.shuffle(best_move)
       #print(best_move)
      #return self.mini_max(board,color,2)
      return (best_move[0]//self.x_max,best_move[0]%self.y_max),0 
   def terminal_test(self, board):
      if self.stones_left(board) == 0:
          return True
      return False
   def max_value(self, state, turn): #state=board
   # return value and state: (val, state)
     if self.terminal_test(state): return (self.evaluate(turn, state),state)
     v = (-999, state)
     temp1 = turn
   #turn = 'O' if turn == 'X' else 'X'
     for a, s in self.find_moves(state, turn):
       min = self.min_value(s, turn)
       if v[0] < min[0]:
           v = (min[0], s)
     return v
   def min_value(self, state, turn):
   # return value and state: (val, state)
     if self.terminal_test(state): return (self.evaluate(turn, state), state)
     v = (999, state)
     temp1 = turn
     #turn = 'O' if turn == 'X' else 'X'
     for a, s in self.find_moves(state, turn):
        max = self.max_value(s,temp1)
        if v[0] > max[0]:
           v = (max[0], s)
     return v
  # pass

   def minimax(self, board, color, search_depth):
    # returns best "value"
      return self.max_value(board, color, search_depth)[1]   # returns state
   

   def negamax(self, board, color, search_depth):
    # returns best "value"
      return 1
# inputs state, current state in game
#v  Max_Value(state, −∞, ∞)
#return the action in Successors(state) with value v     
   def alphabeta(self, board, color, search_depth, alpha, beta):
       v = self.max_value(board, -10000, 10000)
       return 0
    # returns best "value" while also pruning     
     # pass
       #  function Alpha_Beta_Search(state) returns an action
#inputs state, current state in game
#v  Max_Value(state, −∞, ∞)
#return the action in Successors(state) with value v
#function Max_Value(state, 𝛼, 𝛽) returns a utility value
#if Terminal_Test(state) then return Utility(state) or EVAL(state)
#v  −∞
#for a in ACTIONS(state) do
#v  max(v, Min_Value(RESULT(s, a), 𝛼, 𝛽)) new board
#if v > 𝛽 then return v
#𝛼  max(𝛼, v)
#return v
#function Min_Value(state) returns a utility value
   def make_key(self, board, color):
    # hashes the board
      return 1

   def stones_left(self, board):
    # returns number of stones that can still be placed
      count = 0
      for x in range(len(board)):
            if board[x][x//8] == '.':
                count += count+1
      return count
      #return 1

   def make_move(self, board, color, move, flipped):
    # returns board that has been updated
      return 1

   def evaluate(self, board, color, possible_moves):
    # returns the utility value
      return 1 #-1, 
   def score(self, board, color):
    # returns the score of the board 
      return 1

   def find_moves(self, board, color):
    # finds all possible moves
    moves_found = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
                moves_found.update({i*self.y_max+j: flipped_stones})
    return moves_found

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
    if board[x][y] != ".":
        return []
    if color == self.black:
        color = "@"
    else:
        color = "O"
    flipped_stones = []
    for incr in self.directions:
        temp_flip = []
        x_pos = x + incr[0]
        y_pos = y + incr[1]
        while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
            if board[x_pos][y_pos] == ".":
                break
            if board[x_pos][y_pos] == color:
                flipped_stones += temp_flip
                break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
    return flipped_stones
      #return 1