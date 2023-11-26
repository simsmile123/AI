# Name:      Simrith Ranjan  Data: 10/20/21
import random, pickle, math, time
from math import pi, acos, sin, cos
from tkinter import *

class HeapPriorityQueue():
   # copy your PriorityQueue here
   def __init__(self):
      self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
      self.current = 1        # to make this object iterable

   def next(self):            # define what __next__ does
      if self.current >=len(self.queue):
         self.current = 1     # to restart iteration later
         raise StopIteration
    
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def __iter__(self):
      return self

   __next__ = next

   def isEmpty(self):
      return len(self.queue) == 1    # b/c index 0 is dummy

   def swap(self, a, b):
      self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

   # Add a value to the heap_pq
   def push(self, value):
      self.queue.append(value)
      # write more code here to keep the min-heap property
      # if self.queue is None:
      #      self.queue = value
      # else:
      #      value.next = self.queue
      #      self.queue = value
      if(len(self.queue)> 1):
        self.heapUp(len(self.queue)-1)

   # helper method for push      
   def heapUp(self, k):
      parent = int(k / 2)
      if(parent<1):
         return
      else:
         if(self.queue[k] < self.queue[parent]):
            self.swap(k, parent)
            self.heapUp(parent)
         else:
            return
      
               
   # helper method for reheap and pop
   def heapDown(self, k, size):
      left = (2*k)
      right = (2 * k) + 1
      if(left > size or k > size):
         return
      elif(right > size):
         if(self.queue[k] > (self.queue[left])):
            self.swap(k, left)
      elif((self.queue[k] > (self.queue[right])) or (self.queue[k] > (self.queue[left]))): #if k is less than either the right child or left child
            if(self.queue[left] < (self.queue[right])):
               self.swap(left, k)
               self.heapDown(left, size)
            else:
               self.swap(right, k)
               self.heapDown(right, size)
      
   
   # make the queue as a min-heap            
   def reheap(self):
      for x in range(int(len(self.queue)/2), 0,-1):
         self.heapDown(x, len(self.queue)-1)
   
   # remove the min value (root of the heap)
   # return the removed value            
   def pop(self):
      # Your code goes here
      #self.remove(0)
      return self.remove(0)    # change this
      
   # remove a value at the given index (assume index 0 is the root)
   # return the removed value   
   def remove(self, index):
      # Your code goes here
      #if len(self.queue) > index:
      #index = index+1
      temp = self.queue[index+1] 
      f = self.queue.remove(self.queue[index+1])
      self.reheap()
      return temp   # change this
     # return "you did it wrong
   pass
   
def calc_edge_cost(y1, x1, y2, x2):
   #
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees

   # if (and only if) the input is strings
   # use the following conversions

   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   #
   R   = 3958.76 # miles = 6371 km
   #
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   #
   # approximate great circle distance with law of cosines
   #
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
   #


# NodeLocations, NodeToCity, CityToNode, Neighbors, EdgeCost
# Node: (lat, long) or (y, x), node: city, city: node, node: neighbors, (n1, n2): cost
def make_graph(nodes = "rrNodes.txt", node_city = "rrNodeCity.txt", edges = "rrEdges.txt"):
   nodeLoc, nodeToCity, cityToNode, neighbors, edgeCost = {}, {}, {}, {}, {}
   map = {}   # have screen coordinate for each node location
   for i in open(nodes).readlines():
       arr = i.strip().split(" ")
       nodeLoc[arr[0]] = [float(arr[1]),float(arr[2])]
   for i in open(node_city).readlines(): 
       arr2 = i.strip().split()
       nodeToCity[arr2[0]] = ' '.join(arr2[1:])
       cityToNode[' '.join(arr2[1:])] = arr2[0]
   # Your code goes here
   for i in open(edges).readlines():
       ar1, ar2 = i.strip().split(" ")
       if ar1 in neighbors:
           neighbors[ar1].add(ar2)
       else: 
           neighbors[ar1] = {ar2}
       if ar2 in neighbors:
           neighbors[ar2].add(ar1)
       else: 
           neighbors[ar2] = {ar1}
      # cost = calc_edge_cost(*nodeLoc[ar1], *nodeLoc[ar2])
       edgeCost[(ar1,ar2)] = calc_edge_cost(*nodeLoc[ar1], *nodeLoc[ar2])
       edgeCost[(ar2,ar1)] = calc_edge_cost(*nodeLoc[ar1], *nodeLoc[ar2])
       
   #print ("34.90083 -90.218 ?", nodeLoc["2800002"])
   #print ("Las Vegas ?", nodeToCity["3200014"])
   #print ("3200014 ?", cityToNode["Las Vegas"])
   #print ("{'3200044', '3200050', '3200013'} ?", neighbors["3200014"])
   #print ("11.319736091806572 ?", edgeCost[("3200014", "3200044")])

        
   # Un-comment after you fill the nodeLoc dictionary.
   for node in nodeLoc: #checks each
      lat = float(nodeLoc[node][0]) #gets latitude
      long = float(nodeLoc[node][1]) #gets long
      modlat = (lat - 10)/60 #scales to 0-1
      modlong = (long+130)/70 #scales to 0-1
      map[node] = [modlat*800, modlong*1200] #scales to fit 800 1200
   return [nodeLoc, nodeToCity, cityToNode, neighbors, edgeCost, map]

# Retuen the direct distance from node1 to node2
# Use calc_edge_cost function.
def dist_heuristic(n1, n2, graph):
   
   # Your code goes here
   #temp_array, g, s = [],0,0 
   #for x in goal:
   #   s = n1.index(x) 
   #   g = n2.index(x)
   #   if s != g:
   #      temp_array.append(abs(s// size - g //size) + abs(s%size - g%size))
   #return sum(temp_array)
   return calc_edge_cost(*graph[0][n1], *graph[0][n2])
   pass
   
# Create a city path. 
# Visit each node in the path. If the node has the city name, add the city name to the path.
# Example: ['Charlotte', 'Hermosillo', 'Mexicali', 'Los Angeles']
def display_path(path, graph):
   
   # Your code goes here
   s = "["
   #print(type(path), type(graph[1]))
   for x in path:
       if x in graph[1]:
           s += graph[1][x] + ","
   s.rstrip(',')
   s += "]"
   return s
   pass

# Using the explored, make a path by climbing up to "s"
# This method may be used in your BFS and Bi-BFS algorithms.
def generate_path(state, explored, graph):
   # Your code goes here
   path = [state]
   cost = 0
   while explored[state] != "s":
       path.append(explored[state])
       cost+=graph[4][(state, explored[state])]
       state = explored[state]
   return path[::-1], cost

def drawLine(canvas, y1, x1, y2, x2, col):
   x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)   
   canvas.create_line(x1, 800-y1, x2, 800-y2, fill=col)

# Draw the final shortest path.
# Use drawLine function.
def draw_final_path(ROOT, canvas, path, graph, col='red'):
   
   # Your code goes here
   for x in range(len(path) -1):
       drawLine(canvas, *graph[5][path[x]],*graph[5][path[x+1]], col)
       ROOT.update()
   pass

def draw_all_edges(ROOT, canvas, graph):
   ROOT.geometry("1200x800") #sets geometry
   canvas.pack(fill=BOTH, expand=1) #sets fill expand
   for n1, n2 in graph[4]:  #graph[4] keys are edge set
      drawLine(canvas, *graph[5][n1], *graph[5][n2], 'white') #graph[5] is map dict
   ROOT.update()


def bfs(start, goal, graph, col):
   ROOT = Tk() #creates new tkinter
   ROOT.title("BFS")
   canvas = Canvas(ROOT, background='black') #sets background
   draw_all_edges(ROOT, canvas, graph)

   counter = 0
   frontier, explored = [], {start: "s"}
   frontier.append(start)
   while frontier:
      s = frontier.pop(0)
      if s == goal: 
         path, cost = generate_path(s, explored, graph)
         draw_final_path(ROOT, canvas, path, graph)
         return path, cost
      for a in graph[3][s]:  #graph[3] is neighbors
         if a not in explored:
            explored[a] = s
            frontier.append(a)
            drawLine(canvas, *graph[5][s], *graph[5][a], col)
      counter += 1
      if counter % 1000 == 0: ROOT.update()
   return None

def bi_bfs(start, goal, graph, col):
   ROOT = Tk() #creates new tkinter
   ROOT.title("bi-BFS")
   canvas = Canvas(ROOT, background='black') #sets background
   draw_all_edges(ROOT, canvas, graph)
   # Your code goes here
   counter2 = 0
   counter1 = 0
   if start == goal: return []
   explored, Q = {start: "s"}, [start]
   backexp = {goal: "s"}
   end = [goal]
   while len(Q) > 0 and len(end) > 0:   
      if len(Q) == 0 or len(end) == 0: return "fail"
      s = Q.pop(0)
      if s in backexp:
         path, cost = generate_path(s, explored, graph)
         path2, cost2 = generate_path(s, backexp, graph) 
         draw_final_path(ROOT, canvas, path+path2[::-1], graph)
         print('the number of explored nodes in bi-bfs:', counter2+counter1)
         return path+path2[::-1], cost+cost2
         #return x+y
      for a in graph[3][s]:  #graph[3] is neighbors
         if not a in explored:
               explored[a] = s
               Q.append(a)
               drawLine(canvas, *graph[5][s], *graph[5][a], col)
      counter1 += 1
      if counter1 % 1000 == 0: ROOT.update()
      t = end.pop(0) 
      if t in explored:
         path, cost = generate_path(t, explored, graph)
         path2, cost2 = generate_path(t, backexp, graph) 
         draw_final_path(ROOT, canvas, path+path2[::-1], graph)
         print('the number of explored nodes in bi-bfs:', counter2+counter1)
         return path+path2[::-1], cost+cost2
      for a in graph[3][t]:  #graph[3] is neighbors
         if not a in backexp:
            backexp[a] = t
            end.append(a)
            drawLine(canvas, *graph[5][t], *graph[5][a], col)
      counter2 += 1
      if counter2 % 1000 == 0: ROOT.update()
   return None
   return count
def a_star(start, goal, graph, col, heuristic=dist_heuristic):  
   counter2 =0 
   ROOT = Tk() #creates new tkinter
   ROOT.title("a_star")
   canvas = Canvas(ROOT, background='black') #sets background
   draw_all_edges(ROOT, canvas, graph)
   if start == goal: return []
   frontier = HeapPriorityQueue()
   h = heuristic(start, goal, graph)
   visited = {start:h}
   frontier.push((h, start, [start],0))
   while not frontier.isEmpty():
      curr = frontier.pop()
      c = curr[3]
       #len(curr[2]) +1
      if curr[1] == goal:
         #path, cost = visited[curr[1]], visited[a]
         draw_final_path(ROOT, canvas, curr[2], graph)
         print('the number of explored nodes of a star:', counter2)
         return curr[2], c#path, cost #curr[2], h+g
     # if not curr[1] in visited: 
         #visited.add(curr[1])
        # print(curr[1])
      for a in graph[3][curr[1]]:
         a = ''.join(a)
         g = c+ graph[4][(curr[1],a)]
         h = heuristic(a, goal, graph)
         if a not in visited or visited[a] > h+g:
              # curr[2].append(a)
              #curr[0]+dist_heuristic(a, goal, size)
            visited[a] = h+g 
            frontier.push((h+g, a, curr[2]+[a],g))
            drawLine(canvas, *graph[5][curr[1]], *graph[5][a], col)
      counter2 += 1      
      if counter2 % 1000 == 0: ROOT.update()
  
   # Your code goes here
   
   return None

def generate_paths(start, end, start_exp, back_exp,current_path):
   if current_path[0] is start:
      return current_path[:-1] + back_exp[::-1] 
   elif current_path[0] is end:
      return start_exp[:-1] + current_path[::-1]
   return None

def calc_total_cost(path,graph):
    cost  = 0
    for p in range(len(path)-1):
        cost += graph[4][(path[p],path[p+1])]
    return cost   

def bi_a_star(start, goal, graph, col, canvas, ROOT, three=False, heuristic=dist_heuristic):
   counter2 =0 
   if start == goal: return []
   frontier = HeapPriorityQueue()
   h = heuristic(start, goal, graph)
   visited = {start:[start]}
   frontier.push((h, start, [start],0))
   frontier2 = HeapPriorityQueue()
   h2 = heuristic(goal, start, graph)
   visited2 = {goal:[goal]}
   frontier2.push((h2, goal, [goal],0))
   path = []
   cost = 0
   while not frontier.isEmpty() and not frontier2.isEmpty():
      curr = frontier.pop()
      c = curr[3]
       #len(curr[2]) +1
      if curr[1] in visited2.keys():
         path =  list(curr[2][:-1]) + list(visited2[curr[1]])[::-1]
         if not three:
             draw_final_path(ROOT, canvas, curr[2], graph)
             draw_final_path(ROOT, canvas, visited2[curr[1]][::-1],graph)
             print('the number of explored nodes of a star:', counter2)
         cost= c
         return path, calc_total_cost(path,graph)
      for a in graph[3][curr[1]]:
         a = ''.join(a)
         g = c+ graph[4][(curr[1],a)]
         h = heuristic(a, goal, graph)
         if a not in visited or curr[3] > g:
              # curr[2].append(a)
              #curr[0]+dist_heuristic(a, goal, size)
            visited[a] = curr[2]+[a]
            frontier.push((h+g, a, curr[2]+[a],g))
            drawLine(canvas, *graph[5][curr[1]], *graph[5][a], col)
      curr2 = frontier2.pop()
      c2 = curr2[3]
       #len(curr[2]) +1
      if curr2[1] in visited.keys():
         #print(curr2[::-1])
         path = list(curr2[2][:-1]) + list(visited[curr2[1]])[::-1]
         if not three:
             draw_final_path(ROOT, canvas, curr2[2], graph)
             draw_final_path(ROOT, canvas, visited[curr2[1]][::-1],graph)
         #draw_final_path(ROOT, canvas, path, graph)
             print('the number of explored nodes of a star:', counter2)
         return path, calc_total_cost(path,graph)#path, cost #curr[2], h+g)
      for a in graph[3][curr2[1]]:
         a = ''.join(a)
         g = c2+ graph[4][(curr2[1],a)]
         h2 = heuristic(a, start, graph)
         cost = c2
         if a not in visited2 or c2 > g:
            visited2[a] = curr2[2]+[a]
            frontier2.push((h2+g, a, curr2[2]+[a],g))
            drawLine(canvas, *graph[5][curr2[1]], *graph[5][a], col)
      counter2 += 1      
      if counter2 % 1000 == 0: ROOT.update()
   # Your code goes here
   
   return None

def tri_directional(city1, city2, city3, graph, col, heuristic=dist_heuristic):
   #counter2 =0 
    ROOT = Tk() #creates new tkinter
    ROOT.title("tri a_star")
    canvas = Canvas(ROOT, background='black') #sets background
    draw_all_edges(ROOT, canvas, graph)
    path1, cost1 = bi_a_star(city1, city2, graph, col, canvas, ROOT, True)
    path2, cost2 = bi_a_star(city2, city3, graph, col,canvas, ROOT, True)
    path3, cost3 = bi_a_star(city3, city1, graph, col,canvas, ROOT, True)
   #  all_cost = [cost1,cost2,cost3]
   #  all_cost = sorted(all_cost) 
   #  toptwo = all_cost[0] + all_cost[1]
   #  toptwopath = []
    cost, path = min([(cost1+cost2,path1[:-1]+path2), (cost2+cost3, path2[:-1]+path3), (cost3+cost1,path3[:-1]+path1)])
   # Your code goes here
    draw_final_path(ROOT, canvas, path, graph)#THIS IS WRONG
    return path, cost
   
def main():
   start, goal = input("Start city: "), input("Goal city: ")
   third = input("Third city for tri-directional: ")
   graph = make_graph("rrNodes.txt", "rrNodeCity.txt", "rrEdges.txt")  # Task 1
   print ("Tri-Search of ({}, {}, {})".format(start, goal, third))
   cur_time = time.time()
   path, cost = tri_directional(graph[2][start], graph[2][goal], graph[2][third], graph, 'pink')
   if path != None: display_path(path, graph)
   else: print ("No Path Found.")
   print('the whole path', path)
   print(display_path(path, graph))
   print ('Tri-A star Path Cost:', cost)
   print ("Tri-directional search duration:", (time.time() - cur_time))
   #print('the whole path', path)
   #print("the whole length of the path:", len(path))
   #cur_time = time.time()
   #path, cost = bfs(graph[2][start], graph[2][goal], graph, 'yellow') #graph[2] is city to node
   #if path != None: display_path(path, graph)
   #else: print ("No Path Found.")
   #print ('BFS Path Cost:', cost)
   #print ('BFS duration:', (time.time() - cur_time))
   #print ()
   #cur_time = time.time()
   #path, cost = bi_bfs(graph[2][start], graph[2][goal], graph, 'green')
   #print('the whole path', path)
   #print("the whole length of the path:", len(path))
   #print(display_path(path, graph))
   #if path != None: display_path(path, graph)
   #else: print ("No Path Found.")
   #print ('Bi-BFS Path Cost:', cost)
   #print ('Bi-BFS duration:', (time.time() - cur_time))
   #print ()
   #cur_time = time.time()
   #path, cost = a_star(graph[2][start], graph[2][goal], graph, 'blue')
   #print('the whole path', path)
   #print("the whole length of the path:", len(path))
   #print(display_path(path, graph))
   #if path != None: display_path(path, graph)
   #else: print ("No Path Found.")
   #print ('A star Path Cost:', cost)
   #print ('A star duration:', (time.time() - cur_time))
   ##print ()
   #cur_time = time.time()
   #ROOT = Tk() #creates new tkinter
   #ROOT.title("bi a_star")
   #canvas = Canvas(ROOT, background='black') #sets background
   #draw_all_edges(ROOT, canvas, graph)
   #path, cost = bi_a_star(graph[2][start], graph[2][goal], graph, 'orange')
   #print('the whole path', path)
   #print("the whole length of the path:", len(path))
   #print(display_path(path, graph))
   #if path != None: display_path(path, graph)
   #else: print ("No Path Found.")
   #print ('Bi-A star Path Cost:', cost)
   #print ("Bi-A star duration: ", (time.time() - cur_time))
   #print ()

   """
   cur_time = time.time()  , ROOT, canvas
   path, cost = bi_bfs(graph[2][start], graph[2][goal], graph, 'green')
   if path != None: display_path(path, graph)
   else: print ("No Path Found.")
   print ('Bi-BFS Path Cost:', cost)
   print ('Bi-BFS duration:', (time.time() - cur_time))
   print ()

   cur_time = time.time()
   path, cost = a_star(graph[2][start], graph[2][goal], graph, 'blue')
   if path != None: display_path(path, graph)
   else: print ("No Path Found.")
   print ('A star Path Cost:', cost)
   print ('A star duration:', (time.time() - cur_time))
   print ()

   cur_time = time.time()
   path, cost = bi_a_star(graph[2][start], graph[2][goal], graph, 'orange', ROOT, canvas)
   if path != None: display_path(path, graph)
   else: print ("No Path Found.")
   print ('Bi-A star Path Cost:', cost)
   print ("Bi-A star duration: ", (time.time() - cur_time))
   print ()

   print ("Tri-Search of ({}, {}, {})".format(start, goal, third))
   cur_time = time.time()
   path, cost = tri_directional(graph[2][start], graph[2][goal], graph[2][third], graph, 'pink', ROOT, canvas)
   if path != None: display_path(path, graph)
   else: print ("No Path Found.")
   print ('Tri-A star Path Cost:', cost)
   print ("Tri-directional search duration:", (time.time() - cur_time))
   """
   mainloop() # Let TK windows stay still
 
if __name__ == '__main__':
   main()