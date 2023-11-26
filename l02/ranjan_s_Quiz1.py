# Name: Simrith R
# Date: 11/10/21
import random
def check_complete(assignment, csp_table):
   if assignment.find('.') != -1: return False
   #for hexa in csp_table:
   #if len(set([assignment[i] for i in assignment])) !=12: return False
   return True
   
def select_unassigned_var(assignment, csp_table):
    return assignment.index('.')
    """ your code goes here """
   #temp =[]
   #for y in csp_table:
   #    for x in assignment[y]:
   #       if str(x) not in assignment:
   #           temp.append(x)
   #           return assignment.index('.')
   
def isValid(value, var_index, assignment, csp_table):
   """ your code goes here """
   if value in csp_table:
       if var_index in value:
            for y in value:
                if assignment[y] == value: #value_index - past_index == any other pair past index y in csp_table[y][var_index] and 
                   return False
   return True
def findAllPairIndexes(value, var_index, assignment, csp_table): #this is where we will do the checking constraints
    allpairindex = []
    #allpairindex.append(abs(var_index))
    if value in assignment: #t is in assingment
        for x in csp_table: #12 times##
           # for c in csp_table[x]:
               #print(x) 
               #allpairindex.append(abs(var_index))
               if assignment[x] == value: # in {'T','A','B','C','D'}:#if that index  has one of these letterrs instead of a dot, check if that index
                   #print(assignment[x])
                   for y in allpairindex: #for every existing differences alr stored in all pair index
                       if y == (abs(var_index-x)): #if that number doesn't equal the difference between this certain letter AND the letter we are checking in csp table
                           return False #then  you can add it because it is unique else return false as you can't add smth there
                       elif y!= (abs(var_index-x)): allpairindex.append(abs(var_index-x))
                       #print(allpairindex)
                       #allpairindex.remove(abs(var_index))
  # print(allpairindex)
    if len(allpairindex) == len(set(allpairindex)): return True
    #NOTE: 
    #MY LOGIC was to find the list of the differences between each pair, and ensure there 
    #were no duplicates and that would be it satisfies the constraints listed in the problem
    return False
def backtracking_search(input, csp_table): 
   return recursive_backtracking(input, csp_table)

def recursive_backtracking(assignment, csp_table):
   """ your code goes here """
   if check_complete(assignment,csp_table):
      return assignment
   temp_index = select_unassigned_var(assignment,csp_table)
   domain = 'TABCDE'
  
   for x in domain:  
      if findAllPairIndexes(x,temp_index, assignment, csp_table) and isValid(x, temp_index, assignment, csp_table):
         assignment = assignment[:temp_index] +str(x) +assignment[temp_index+1:]
         #draw_shape(shapes[temp],frame,x)
         #del assignment[temp]
         #print(temp)
         result = recursive_backtracking(assignment, csp_table)
         if result != None:return result
         #draw_shape(shapes[temp],frame,x)  
         else: assignment = assignment[:temp_index] +'.' +assignment[temp_index+1:]
   return None

def display(solution):
   result = solution
   #for i in range(len(solution)):
   #   if i == 0: result += "  "
   #   if i == 5: result += "\n"
   #   if i == 12: result += "\n"
   #   if i == 19: result += "\n  "
   #   result += solution[i] + " "
   return result

def main():
   csp_table = [0,1,2,3,4,5,6,7,8,9,10,11] #[0, 1, 2, 6, 7, 8], [2, 3, 4, 8, 9, 10], [5, 6, 7, 12, 13, 14], [7, 8, 9, 14, 15, 16], [9, 10, 11, 16, 17, 18], [13, 14, 15, 19, 20, 21], [15, 16, 17, 21, 22, 23]] 
   solution = backtracking_search(input("enter 12 dots input: "), csp_table)
   if solution != None:
      print (display(solution))
      #print ('\n'+ solution)
      print (check_complete(solution, csp_table))
   else: print ("It's not solvable.")

if __name__ == '__main__':
   main()
   
"""
Sample Output 1:
24-char(. and 1-6) input: ........................
  1 2 3 1 2 
1 4 5 6 4 5 1 
2 6 3 1 2 3 6 
  2 4 5 4 6 

123121456451263123624546
True

Sample Output 2:
24-char(. and 1-6) input: 6.....34...1.....2..4...
  6 1 2 1 3 
1 3 4 5 6 4 1 
5 6 2 1 3 2 5 
  3 4 5 4 6 

612131345641562132534546
True
"""
