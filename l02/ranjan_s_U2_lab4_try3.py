import sys; args = sys.argv[1:]
#puzzles = open(args[0], "r").read().splitlines()
import time
with open('puzzles.txt') as f:
     puzzles = [line.strip() for line in f]
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
def initialize_ds(puzzle, neighbors):
   ''' Your code goes here '''
   #print (vars, puzzle, q_table)
   variables = {}
   for x in range(len(puzzle)):
      num_v ={'1','2','3','4','5','6','7','8','9'}
      if puzzle[x] == '.':
        #   for z in neighbors[int(x)]:
        #       if puzzle[z] in num_v: 
        #           num_v.remove(puzzle[z])
          variables[x]= ''.join(num_v)
      else:
          variables[x] = puzzle[x]
   return variables,puzzle #, q_table #{}, "", {} #what do you do for vars here


# sum of all ascii code of each char - (length of the solution * ascii code of min char)
def checksum(solution):
   ''' write your code here'''
   sum = 0
   for num in solution: 
      sum +=ord(num)
   sum -= ord('1')*81
   return sum
#find all solved value from get sorted values
def solvelist(puzzle):
    return {x for x in puzzle if len(puzzle[x]) == 1} #solvedlist
#anotha method--forwardlooks 
def constraintprop(variables, csp_table): #list with possible values for the boxes in csp in 1-9 
    for table in csp_table:
        for x in table:
            for z in variables[x]:
                if x == '.':
                    if len(z)==1: x = variables[z] 
    return variables

def forwardlooks(variables, solvedlist, new):
    while new: 
        s = new.pop()
        neigh_s = neighors[s]
        for j in neigh_s:
           v = variables[j]
           if variables[s] in variables[j]:
                variables[j]= v[0:v.index(variables[s])] + v[v.index(variables[s])+1:]
        #    print(solvedlist, new)
        #    input()    
           if len(variables[j]) == 0 : return None
           if j not in solvedlist and len(variables[j]) == 1: 
               solvedlist.add(j)
               new.add(j)
    return (solvedlist, variables)
#while new
#store the popped value
#find neighors of popped values
#loop the neighors for j in neighbors
#in here, find the value of the temp index in variables
# remove the number in j remove value in variables[j]
#if the length variables[j] == 0 : return None
#if j is not in second param AND varaibles[j] == 1: add it to new and add it to solved list (second param)
#return first and sec param
#3 arg dict, solved lists ^^, anotha set with new variables to add
def select_unassigned_var(assignment):
   if '.' in assignment:
       return assignment.index('.')
neighors = sudoku_neighbors(sudoku_csp())
possible_values = {str(i) for i in range(1, 10)}
def get_sorted_values(puzzle, var):
    return puzzle[var]
def mcv(variables):
    return min([(k, variables[k]) for k in variables if 1 < len(variables[k]) <= 9], key = lambda v: v[1])[0]
def check_complete(variables):
    for x in variables:
       # print(variables[x])
        if len(variables[x]) > 1: return False
    return True
def csp_backtracking_w_mcv(variables,csp_table):
    if check_complete(variables): return variables
    var = mcv(variables)
    for i in get_sorted_values(variables, var):
        c_variables = variables.copy()
        c_variables[var]=i
        t_set = {var}
        forward = forwardlooks(c_variables, solvelist(c_variables), t_set)
        if forward is None:continue
        result = csp_backtracking_w_mcv(forward[1], csp_table)
        if result is not None:
            return result
    return None
def convert_to_string(d):
    x=''
    for k in d:
        x += d[k]
    return x
def solve(puzzle, neighbors, csp_table):  
   # initialize_ds function is optional helper function. You can change this part. 
   variables, puzzle = initialize_ds(puzzle, neighbors)  # q_table is quantity table {'1': number of value '1' occurred, ...}
   #print(q_table)
   s = forwardlooks(variables, solvelist(variables), solvelist(variables))
   #print(neighbors)
   #print(variables)
   return convert_to_string(csp_backtracking_w_mcv(s[1], csp_table))
def main():
#    csp_table = sudoku_csp()   # rows, cols, and sub_blocks
   neighbors = sudoku_neighbors(sudoku_csp())
   start_time = time.time()
   for line, puzzle in enumerate(puzzles):
      line, puzzle = line, puzzle.rstrip()
      print ("{}: {}".format(line+1, puzzle)) 
      solution = solve(puzzles[line], neighbors, sudoku_csp())
      if solution == None:print ("No solution found."); break
      print ("{}{} {}".format(" "*(len(str(line))+2), solution, checksum(solution)))
   print ("Duration:", (time.time() - start_time))

if __name__ == '__main__': main()
# for i in range(len(puzzles)):
#     print(i, puzzles[i])
#     print("  ", solve(puzzles[i], neighors)) #, checksum(convert_to_string(csp_backtracking_w_mcv(puzzles[i]))))
# Simrith Ranjan, Period 5, 2023