# Name: Simrith R
# Date: 11/10/21
import random
def check_complete(assignment, csp_table):
   if assignment.find('.') != -1: return False
   for hexa in csp_table:
      if len(set([assignment[i] for i in hexa])) != 6: return False
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
   


#def backtracking_search(input, csp_table): 
#   return recursive_backtracking(input, csp_table)

#def recursive_backtracking(assignment, csp_table):
#   """ your code goes here """
#   if check_complete(assignment,csp_table):
#      return assignment
#   temp_index = select_unassigned_var(assignment,csp_table) #{K:V  for k, v in variables.items()
#   domain = [str(i) for i in range(20)]
#   for x in domain:  
#      if isValid(x, temp_index, assignment, csp_table):
         
#         result = recursive_backtracking(assignment, csp_table)
#         if result != None:return result
#         else: 
#   return None

def icosahedral(csp_table):
    assignment = {19}
    tally = 0 
    domain = [i for i in range(20)]
    for x in domain:
     for z in assignment: #i want to go thro every variable that I think will result in the largest independent set
         v = isValid(z, csp_table, assignment)
         if v[0]:
              assignment.add(x)
              return v[1], assignment
#def inset(csp_table, temp):  

def isValid(value, csp_table, assignment):
   """ your code goes here """
   temp_calc = 0
  # WHAT I WANT THIS METHOD TO DO: if value> every individual thing in csp[values] AND is not in the adjacents/csp[values] of any number in the existing assignment
  #OR if it is in the adjacents/csp[values] of any number alr existing, if we remove that number and add value is the sum greater?
   for y in range(20):
       if y in csp_table[value]:
               for t in assignment:
                   temp_calc+=t
       temp_calc += y
       new_calc = temp_calc - y + value
       if temp_calc > new_calc: return False, temp_calc
       else: return True, new_calc
   
def main():
   csp_table = [[1,10,19],[0,8,2],[1,6,3],[2,4,19],[5,3,17],[6,4,15],
                [5,2,7],[6,8,14],[1,7,9],[10,8,13],[9,11,0],[12,10,18],
                [13,11,16],[12,14,9],[13,15,7], [14,16,5],[15,17,12],[18,16,4],
                [17,19,11],[18,3,0]]
   solution = icosahedral(csp_table)
   #backtracking_search(input("this is icosahedral index part 2 of the quiz type . to continue "), csp_table)
   if solution != None:
      print (solution[1])
    #  print (check_complete(solution, csp_table))
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