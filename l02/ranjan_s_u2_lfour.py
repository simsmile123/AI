import sys; args = sys.argv[1:]
puzzles = open(args[0], "r").read().splitlines()
import time
# with open('puzzles.txt') as f:
#     puzzles = [line.strip() for line in f]
def sudoku_csp(): #use slicing?? [0,1,2,9,10,11,18,19,20] first box (then add three for second and 6 for third and 9 (not 9 actually use 27 since 9+0 is 9?) for fourth and so on)
   i = 9
   csp_table= [[k for k in range(x*i, (x+1)*i)] for x in range(i)]#rows
   csp_table+= [[k for k in range(x, i*i, i)] for x in range(i)]#colums
   first_box = [0,1,2,9,10,11,18,19,20]
   multi_factor = [0,3,6,27,30,33,54,57,60] #wrote down? why not 36 tho
   csp_table +=[[f+h for h in first_box] for f in multi_factor]
   return csp_table

def sudoku_neighbors(csp_table): # {0:[0, 1, 2, 3, 4, ...., 8, 9, 18, 27, 10, 11, 19, 20], 1:
   ''' Your code goes here ''' #DICT of each index
   neighbors = {}
   for x in range(81):
      value_set = set()
      for y in csp_table:
            if x in y:
                for val in y:
                   value_set.add(val)
      value_set-={x}
      neighbors[x] = value_set
   return neighbors
# Optional helper function
# def initialize_ds(puzzle, neighbors):
#    ''' Your code goes here '''
#    #print (vars, puzzle, q_table)
#    variables = {}
#    num_count = 0
#    q_table = {'.': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7':0, '8':0, '9':0}
#    for x in range(len(puzzle)):
#       #if x != '.':
#       num_count = puzzle.count(puzzle[x])
#       q_table[puzzle[x]] =num_count
#       num_v ={'1','2','3','4','5','6','7','8','9'}
#       if puzzle[x] == '.':
#           for z in neighbors[int(x)]:
#               if puzzle[z] in num_v: #;lkjad;lkfja;sldkfjlasdkfjj 
#                   num_v.remove(puzzle[z])
#           variables[x]=num_v
#       else:
#           variables[x] = list(puzzle[x])
#    del q_table['.']

   return variables,puzzle, q_table #{}, "", {} #what do you do for vars here


# sum of all ascii code of each char - (length of the solution * ascii code of min char)
def checksum(solution):
   ''' write your code here'''
   sum = 0
   for num in solution: 
      sum +=ord(num)
   sum -= ord('1')*81
   return sum


def select_unassigned_var(assignment):
   if '.' in assignment:
       return assignment.index('.')
neighors = sudoku_neighbors(sudoku_csp())
possible_values = {str(i) for i in range(1, 10)}
def get_sorted_values(puzzle, var):
    p_copy = possible_values.copy()
    n1 = neighors[var]
    for i in n1:
        value = puzzle[i]
        if value in p_copy: p_copy.remove(value)
    return p_copy
#def mcv(puzzle, neighbors,variables):



def csp_backtracking(puzzle):
    if puzzle.count('.')==0: return puzzle
    var = select_unassigned_var(puzzle)
    for i in get_sorted_values(puzzle, var):
        new_state = puzzle[0:var] + i + puzzle[var+1:]
        result = csp_backtracking(new_state)
        if result is not None:
            return result
    return None
# def csp_backtracking_w_mcv(puzzle,variables):
#     if puzzle.count('.')==0: return puzzle
#     var = mcv(puzzle, neighors, variables)
#     for i in get_sorted_values(puzzle, var):
#         new_state = puzzle[0:var] + i + puzzle[var+1:]
#         checked = csp_backtracking_w_mcv(new_state, variables)
#         if checked is not None:
#             result = csp_backtracking_w_mcv(checked, variables)
#             if result is not None:
#                 return result
#     return None
def solve(puzzle, neighbors):  
   # initialize_ds function is optional helper function. You can change this part. 
   #variables, puzzle, q_table = initialize_ds(puzzle, neighbors)  # q_table is quantity table {'1': number of value '1' occurred, ...}
   #print(q_table)
   #print(neighbors)
   #print(variables)
   #return csp_backtracking_w_mcv(puzzle)
   return csp_backtracking(puzzle)
def main():
#    csp_table = sudoku_csp()   # rows, cols, and sub_blocks
   neighbors = sudoku_neighbors(sudoku_csp())
   start_time = time.time()
   for line, puzzle in enumerate(puzzles):
      line, puzzle = line, puzzle.rstrip()
      print ("{}: {}".format(line+1, puzzle)) 
      solution = solve(puzzles[line], neighbors)
      if solution == None:print ("No solution found."); break
      print ("{}{} {}".format(" "*(len(str(line))+2), solution, checksum(solution)))
   print ("Duration:", (time.time() - start_time))

if __name__ == '__main__': main()
# for i in range(1, len(puzzles)):
#     print(i, puzzles[i])
#     print(csp_backtracking(puzzles[i]), checksum(csp_backtracking(puzzles[i])))
# Simrith Ranjan, Period 5, 2023