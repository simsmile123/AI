# Name: Simrith Ranjan
# Period: 11/05/2021

from tkinter import *
from graphics import *
import random

def check_complete(assignment, vars, adjs):
   # check if assignment is complete or not. Goal_Test  check all the states are in the assignment and 
   ''' your code goes here ''' 

   # bool = False
   # for x in adjs:
   #    for y in adjs[x]: 
   #       if vars.keys != assignment.keys():
   #          bool = True
   return len(vars)==len(assignment) #and bool 

def select_unassigned_var(assignment, vars, adjs):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable 
   ''' your code goes here ''' #forward checking 
   temp =[]
   for x in vars:
      if x not in assignment:
          temp.append(x)
   return random.choice(temp)
   pass

   
def isValid(value, var, assignment, variables, adjs):
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.
   ''' your code goes here '''
   if var in adjs:
   #for x in assignment:
     # if value != adjs[var]:
       for y in adjs[var]:
          if y in assignment and assignment[y] == value:
                 return False
   return True

def backtracking_search(variables, adjs, shapes, frame): 
   return recursive_backtracking({}, variables, adjs, shapes, frame)

def recursive_backtracking(assignment, variables, adjs, shapes, frame):
   # Refer the pseudo code given in class.
   ''' your code goes here '''
   if check_complete(assignment,variables,adjs):
      return assignment
   temp = select_unassigned_var(assignment,variables,adjs) #{K:V  for k, v in variables.items()}
   for x in variables[temp]:  
      if isValid(x,temp, assignment, variables, adjs):
         assignment[temp] =  x
         draw_shape(shapes[temp],frame,x)
         #del assignment[temp]
         result = recursive_backtracking(assignment, variables, adjs, shapes, frame)
         if result != None:return result
         #draw_shape(shapes[temp],frame,x)  
         del assignment[temp]
   return None
# return shapes as {region:[points], ...} form
def read_shape(filename):
   infile = open(filename)
   region, points, shapes = "", [], {}
   for line in infile.readlines():
      line = line.strip()
      if line.isalpha():
         if region != "": shapes[region] = points
         region, points = line, []
      else:
         x, y = line.split(" ")
         points.append(Point(int(x), 300-int(y)))
   shapes[region] = points
   return shapes

# fill the shape
def draw_shape(points, frame, color):
   shape = Polygon(points)
   shape.setFill(color)
   shape.setOutline("black")
   shape.draw(frame)
   space = [x for x in range(9999999)] # give some pause
   
def main():
   regions, variables, adjacents  = [], {}, {}
   # Read mcNodes.txt and store all regions in regions list
   ''' your code goes here '''
   # mcNodesFile = open("McNodes.txt", "r")
   # allmcNodes = mcNodesFile.readlines()
   # for mc in allmcNodes:
   #    regions += mc
   #allmcNodes = []
   for i in open("McNodes.txt").readlines():
       arr = i.strip().split(" ")

       regions+= [arr[0]]
   # Fill variables by using regions list -- no additional code for this part
   for r in regions: variables[r] = {'red', 'green', 'blue'}

   # Read mcEdges.txt and fill the adjacents. Edges are bi-directional.
   ''' your code goes here '''
   # mcEdges = open("McEdges.txt", "r")
   # allmcEdges = mcEdges.readlines()
   # #allmcEdges = allmcEdges.split(" ")
   # for mcE in allmcEdges:
   #    adjacents[mcE] = allmcEdges[mcE+1]
   for i in open("McEdges.txt").readlines():
       ar1, ar2 = i.strip().split(" ")
       if ar1 in adjacents:
           adjacents[ar1].add(ar2)
       else: 
           adjacents[ar1] = {ar2}
       if ar2 in adjacents:
           adjacents[ar2].add(ar1)
       else: 
           adjacents[ar2] = {ar1}
   # Set graphics -- no additional code for this part
   frame = GraphWin('Map', 300, 300)
   frame.setCoords(0, 0, 299, 299)
   shapes = read_shape("mcPoints.txt")
   for s, points in shapes.items():
      draw_shape(points, frame, 'white')
  
   # solve the map coloring problem by using backtracking_search -- no additional code for this part  
   solution = backtracking_search(variables, adjacents, shapes, frame)
   print (solution)
   
   mainloop()

if __name__ == '__main__':
   main()
   
''' Sample output:
{'WA': 'red', 'NT': 'green', 'SA': 'blue', 'Q': 'red', 'NSW': 'green', 'V': 'red', 'T': 'red'}
By using graphics functions, visualize the map.
'''