import sys; args = sys.argv[1:]
puzzles = open(args[0], "r").read().splitlines()
import time

# def check_complete(assignment, csp_table):
#    if assignment.find('.') != -1: return False
#    for hexa in csp_table:
#       if len(set([assignment[i] for i in hexa])) != 9: return False
#    return True
# optional helper function
def select_unassigned_var(assignment, variables, csp_table):
   if '.' in assignment:
       return assignment.index('.')

# optional helper function
def ordered_domain(var_index, variables, q_table):
    #new dict 
    q2 = []
    for x in variables[var_index]:
       tuple_temp=(q_table[x],x)
       q2.append(tuple_temp)
       #q2+=x
   #  for a in q_table:S
   #      if a in q2: q2[a] = q2[a]+1
   #  for val,num in q2.items():
   #      q3[num] = val
    q2.sort(reverse= True)
    return [y for z,y in q2]
   #pass
#def isValid(value, var_index, assignment, variables, csp_table):
#    for table in csp_table:
#      if var_index in table: #for x in range(len(assignment)):
#       for z in table:
#           if z != var_index and assignment[z] == value: #y in csp_table[y][var_index] and 
#               return False
#    ##for place, possibility in variables.items():
#    #     #if len(possibility) == 0: return False
#    if len(variables) == 0: return False
#    return True
# optional helper function
def update_variables(value, var_index, assignment, variables, neighbors):
   temp = True
   copy_variables = {k:{v for v in vals} for k, vals in variables.items() }#if k != var_index} # a dict with the already taken values?
   for x in copy_variables:
      #for smth in neighbors
      if x in neighbors[var_index] and assignment[x]=='.': 
         copy_variables[var_index] -= {value}
     # if value in copy_variables[var_index]: copy_variables[var_index] -= {value}
         if len(copy_variables[var_index])==0: temp = False
  # if assignment[var_index] == value: temp = False          
   # for place, possibility in variables.items():
   #    if len(possibility) == 0: temp =  False
   #if len(variables) == 0: temp = False
   return copy_variables, temp
      #set comphresnion of all the values of the neighbors
def solve(puzzle, neighbors):  
   # initialize_ds function is optional helper function. You can change this part. 
   variables, puzzle, q_table = initialize_ds(puzzle, neighbors)  # q_table is quantity table {'1': number of value '1' occurred, ...}
   #print(q_table)
   #print(neighbors)
   #print(variables)
   return recursive_backtracking(puzzle, variables, neighbors, q_table)

# optional helper function: you are allowed to change it
def recursive_backtracking(assignment, variables,neighbors, q_table): #fix this
      """ your code goes here """
      if assignment.find('.') == -1: #if check_complete(assignment,csp_table):
          return assignment
      temp_index = select_unassigned_var(assignment,variables,q_table) #{K:V  for k, v in variables.items()
      domain = ordered_domain(temp_index, variables, q_table) #'123456789'#table
      for x in domain:  
            #for index in csp_table[x]:
               var1, valid = update_variables(x, temp_index, assignment, variables, neighbors)
               if valid:
                     c_assignment = assignment[:temp_index] +x +assignment[temp_index+1:]
                     q_table[x]+=1
                     result = recursive_backtracking(c_assignment,var1, neighbors, q_table)
                     if result != None:return result
                     else: q_table[x]-=1
      return None

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
   # for x in range(81):
   #       temp = neighbors[f"{x}"]
   #       neighbors[f"{x}"].append((x)+9)  
   #       neighbors[f"{x}"].append((x)*3) 
   #       neighbors[f"{x}"].append([(x)+9])
   #           #rows, col, sublock
   print(csp_table)
   return neighbors

# Optional helper function
def initialize_ds(puzzle, neighbors):
   ''' Your code goes here '''
   #print (vars, puzzle, q_table)
   variables = {}
   num_count = 0
   q_table = {'.': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7':0, '8':0, '9':0}
   for x in range(len(puzzle)):
      #if x != '.':
      num_count = puzzle.count(puzzle[x])
      q_table[puzzle[x]] =num_count
      num_v ={'1','2','3','4','5','6','7','8','9'}
      if puzzle[x] == '.':
          for z in neighbors[int(x)]:
              if puzzle[z] in num_v: #;lkjad;lkfja;sldkfjlasdkfjj 
                  num_v.remove(puzzle[z])
          variables[x]=num_v
      else:
          variables[x] = list(puzzle[x])
   del q_table['.']
     # variables = update_variables(x, )
      #     if v == '.':
      #         #do smth with numbers that v can be
      #vars[v]== num_v
   #print(variables)
   return variables,puzzle, q_table #{}, "", {} #what do you do for vars here


# sum of all ascii code of each char - (length of the solution * ascii code of min char)
def checksum(solution):
   ''' write your code here'''
   sum = 0
   for num in solution: 
      sum +=ord(num)
   sum -= ord('1')*81
   return sum
 

def main():
   csp_table = sudoku_csp()   # rows, cols, and sub_blocks
   neighbors = sudoku_neighbors(csp_table)   # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
   start_time = time.time()
   for line, puzzle in enumerate(puzzles):
      line, puzzle = line+1, puzzle.rstrip()
      print ("{}: {}".format(line, puzzle)) 
      solution = solve(puzzle, neighbors)
      if solution == None:print ("No solution found."); break
      print ("{}{} {}".format(" "*(len(str(line))+2), solution, checksum(solution)))
   print ("Duration:", (time.time() - start_time))

if __name__ == '__main__': main()
# Required comment: Simrith Ranjan, Period 5, Ms. Kim
# Check the example below. You must change the line below before submission.
# Simrith Ranjan, Period 5, 2023
