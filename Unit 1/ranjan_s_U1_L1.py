import random

def getInitialState():
   x = "_12345678"
   l = list(x)
   random.shuffle(l)
   y = ''.join(l)
   return y
   
'''precondition: i<j
   swap characters at position i and j and return the new state'''
def swap(state, i, j):
   '''your code goes here'''
   n_state = list(state)
   n_state[i], n_state[j] = n_state[j], n_state[i]
   #temp = n_state[i]
   #n_state[i] = n_state[j]
   #n_state[j] = temp
  # n_state[i, j] = n_state[j, i]
   #temp = i #stores the value from i
   return ''.join(n_state) #return ""
   
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state):
    array = []
    y =state.index("_")
    if (y > 2): #this checks if the index of the space is near the middle/not at the end of the string so we know we can move it up as a possibility
        array.append(swap(state, y - 3,y))
    if (y not in [3, 6, 0]): #can move left
        array.append(swap(state, y - 1,y))
    if (y <= 5):
        array.append(swap(state, y,y+3)) #adds it in its possible to move down
    if(y not in [2, 5, 8]):
        array.append(swap(state, y,y+1)) #possible to move right
    #print (array)
    return array
   
def display_path(n, explored): #key: current, value: parent
   l = []
   while explored[n] != "s": #"s" is initial's parent
      l.append(n)
      n = explored[n]
   print ()
   l = l[::-1]
   for i in l:
      print (i[0:3], end = "   ")
   print ()
   for j in l:
      print (j[3:6], end = "   ")
   print()
   for k in l:
      print (k[6:9], end = "   ")
   print ("\n\nThe shortest path length is :", len(l))
   return ""

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def BFS(initial_state):

   explored = {initial_state: "s"}
   Q = [initial_state]
   #Q.append(initial_state)
   goal = "_12345678"
   #frontier = {initial_state: "s"}
   while True:
       if len(Q) == 0: return "fail"
       s = Q.pop(0)
       #explored[s] = frontier[s]
       if s == "_12345678": return display_path(s, explored)
          #goal = s 
       for a in generate_children(s):
           if not a in explored:# and not a in Q:
               explored[a] = s
               Q.append(a)
   '''Your code goes here'''
   return ("No Solution")

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def DFS(initial):
   '''Your code goes here'''
   Q = []
   explored = {initial: "s"}
   Q.append(initial)
   goal = "_12345678"
   #frontier = {initial}
   while True:
       if len(Q) == 0: return "fail"
       s = Q.pop()
       #explored[s] = frontier[s]
       if s == "_12345678": return display_path(s, explored)
          #goal = s 
       for a in generate_children(s):
           if not a in explored:# and not a in Q:
               explored[a] = s
               Q.append(a)
   return ("No solution")


def main():
   initial = getInitialState()
   print ("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   print (BFS(initial))
  # print ("DFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
  # print (DFS(initial))

if __name__ == '__main__':
   main()

   #Simrith Ranjan, Period 5, 2023
