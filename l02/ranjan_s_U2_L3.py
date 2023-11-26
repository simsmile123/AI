# Name: Simrith Ranjan
# Date: 11/15/2021

def check_complete(assignment, csp_table):
   if assignment.find('.') != -1: return False
   for hexa in csp_table:
      if len(set([assignment[i] for i in hexa])) != 9: return False
   return True
   
def select_unassigned_var(assignment, variables, csp_table):
   if '.' in assignment:
       return assignment.index('.')

def isValid(value, var_index, assignment, variables, csp_table):
    for table in csp_table:
      if var_index in table: #for x in range(len(assignment)):
       for z in table:
           if z != var_index and assignment[z] == value: #y in csp_table[y][var_index] and 
               return False
    ##for place, possibility in variables.items():
    #     #if len(possibility) == 0: return False
    if len(variables) == 0: return False
    return True

def ordered_domain(assignment, variables, csp_table):
   return []

def update_variables(value, var_index, assignment, variables, csp_table):
   alrtaken = {k:{v for v in vals} for k, vals in variables.items() if k != var_index} # a dict with the already taken values?
   for tx in csp_table:
      if var_index == tx:
         for nine in tx:
            if nine in alrtaken: alrtaken[nine] -= {value}
   return alrtaken

def backtracking_search(puzzle, variables, csp_table): 
   return recursive_backtracking(puzzle, variables, csp_table)

def recursive_backtracking(assignment, variables, csp_table):
      """ your code goes here """
      if check_complete(assignment,csp_table):
          return assignment
      temp_index = select_unassigned_var(assignment,variables,csp_table) #{K:V  for k, v in variables.items()
      domain = '123456789'
      for x in domain:  
          #for index in csp_table[x]:
              if isValid(x, temp_index, assignment, variables, csp_table):
                  assignment = assignment[:temp_index] +x +assignment[temp_index+1:]
                  var1 = update_variables(x, temp_index, assignment, variables, csp_table)
                  result = recursive_backtracking(assignment,var1, csp_table)
                  if result != None:return result
             #draw_shape(shapes[temp],frame,x)  
                  assignment = assignment[:temp_index] +'.' +assignment[temp_index+1:]
      return None
      

def display(solution):
   first_box = [0,1,2,9,10,11,18,19,20]
   multi_factor = [0,3,6,27,30,33,54,57,60] #wrote down? why not 36 tho
   for z in range(81):
      if z %3 == 0:
          print(" ", end = "")
      if z % 9 ==0:
          print(" ")
      if z % 27 == 0 and z != 0: 
          print("\n", end = "")
      print(solution[z], end= "")
   #print('\n')
   return solution

  # return ""

def sudoku_csp(): #use slicing?? [0,1,2,9,10,11,18,19,20] first box (then add three for second and 6 for third and 9 (not 9 actually use 27 since 9+0 is 9?) for fourth and so on)
   i = 9
   csp_table= [[k for k in range(x*i, (x+1)*i)] for x in range(i)]#rows
   csp_table+= [[k for k in range(x, i*i, i)] for x in range(i)]#colums
   #for y in range(i):
   #   for x in range(y,i*i, i): #columns?
   #      csp_table[y][x] += x
   first_box = [0,1,2,9,10,11,18,19,20]
   multi_factor = [0,3,6,27,30,33,54,57,60] #wrote down? why not 36 tho
   #for z in multi_factor:
   #   for f in first_box: #real index value??????
   csp_table +=[[f+h for h in first_box] for f in multi_factor]
   return csp_table

def initial_variables(puzzle, csp_table):
    temp = {}
    #print(len(puzzle))
    for y in range(81):
        if puzzle[y] == ".":
            temp[y] = {x for x in "123456789"}
    return temp
   
def main():
   puzzle = input("Type a 81-char string:") 
   while len(puzzle) != 81:
      print ("Invalid puzzle")
      puzzle = input("Type a 81-char string: ")
   csp_table = sudoku_csp()
   print (csp_table)
   variables = initial_variables(puzzle, csp_table)
  # print (variables)
   print ("\nInitial:\n" + display(puzzle))
   solution = backtracking_search(puzzle, variables, csp_table)
   if solution != None: print ("\nsolution\n" + display(solution))
   else: print ("No solution found.\n")
   
if __name__ == '__main__': main()

