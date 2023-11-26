# Name:   Simrith Ranjan       Date:  09/29/2021
import random, time, math

class HeapPriorityQueue():
   # copy your HeapPriorityQueue() from Lab3
      
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
   #pass

def inversion_count(new_state, width = 4, N = 4):
   ''' 
   Depends on the size(width, N) of the puzzle, 
   we can decide if the puzzle is solvable or not by counting inversions.
   If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
   If N is even, puzzle instance is solvable if
      the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is even.
      the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is odd.
   ''' 
   y = new_state.index("_")
   count = 0
   # Your code goes here
   for x in range(len(new_state)):
       for z in range((x), len(new_state)):
          if(y != x) and (y != z):
            if (new_state[z] > new_state[x]):
               count = count+1
   #if (N % 2 == 1): #odd
     # print(count)
      #return (count%2 == 0)
   #print(count)
   if N%2 == 1:
      if count % 2 == 0:
            return True
      else:
            return False
   else:
     # for x in range(1, N, 2)(N*width) - (width*x)
      if int(y/N)%2 == 0 and count%2 == 1:
            return True
      elif int(y/N)%2 == 1 and count%2 == 0:
            return True
      else:
            return False  

def check_inversion():
   t1 = inversion_count("_42135678", 3, 3)  # N=3
   f1 = inversion_count("21345678_", 3, 3)
   t2 = inversion_count("4123C98BDA765_EF", 4) # N is default, N=4
   f2 = inversion_count("4123C98BDA765_FE", 4)
   return t1 and t2 and not (f1 or f2)


def getInitialState(sample, size):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   while not inversion_count(new_state, size, size): 
      random.shuffle(sample_list)
      new_state = ''.join(sample_list)
   return new_state
   
def swap(n, i, j):
   n = list(n)
   n[i], n[j] = n[j], n[i]
   # Your code goes here
   return n
  
      
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state, size=4):
   children = []
   y = state.index('_')
   #print(y)
   N = size
   right, left, up, down = y+1, y-1, y-N, y +N
   if down < len(state): children.append(swap(state, y, down))
   if right % size != 0: children.append(swap(state, y, right))
   if left % size != size-1: children.append(swap(state, y, left))
   if up > -1: children.append(swap(state, up, y))
   return children
   # if(y%N == 0):
   #    children.append(swap(state, y - 1,y))
   # if(y%N==3):
   #    children.append(swap(state, y,y+1))
   # if(y%N == 1 or y%N == 2):
   #    children.append(swap(state, y,y+1))
   # if (y > size - 1): #this checks if the index of the space is near the middle/not at the end of the string so we know we can move it up as a possibility
   #     children.append(swap(state, y - n,y))
   # if (y%n == 1): #can move left
   #     children.append(swap(state, y - 1,y))
   # if (y <= 5):
   #     children.append(swap(state, y,y+n)) #adds it in its possible to move down
   # if(y%n == 1):
   #     children.append(swap(state, y,y+1)) #possible to move right
    #print (array)
   # if(n> 3):
   #     if (y%n == 2): #can move left
   #         children.append(swap(state, y - 1,y))
   #     if (y%n == 2): #can move right
   #         children.append(swap(state, y + 1,y))
   '''your code goes here'''

def display_path(path_list, size):
   for n in range(size):
      for path in path_list:
         print (path[n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

''' You can make multiple heuristic functions '''
def dist_heuristic(state, goal = "_123456789ABCDEF", size=4):
   # Your code goes here
   temp_array, g, s = [],0,0 
    # for each point, finding distance
    # to rest of the point
   for x in goal:
      s = state.index(x) 
      g = goal.index(x)
      if s != g:
         temp_array.append(abs(s// size - g //size) + abs(s%size - g%size)) #ex index 10 and 14 are on top of each other
   return sum(temp_array)
   # ret = 0
   # for (x,y) in zip(state, goal):
   #     if x!=y:
   #         ret = ret +1
   # return ret

def check_heuristic():
   a = dist_heuristic("152349678_ABCDEF", "_123456789ABCDEF", 4)
   b = dist_heuristic("8936C_24A71FDB5E", "_123456789ABCDEF", 4)
   return (a < b) 

def a_star(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size = 4):
   frontier = HeapPriorityQueue()
   h = heuristic(start, goal, size)
   visited = {start:h}
   frontier.push((h, start, [start]))
   while not frontier.isEmpty():
      curr = frontier.pop()
      if curr[1] == goal:
         #curr[2].append(goal)
         #display_path(curr[2])
         return curr[2]
     # if not curr[1] in visited:
         #visited.add(curr[1])
        # print(curr[1])
      for a in generate_children(curr[1]):
         a = ''.join(a)
         g = len(curr[2]) +1
         h = heuristic(a)
         if a not in visited: #or visited[a] > h+g:
              # curr[2].append(a)
              #curr[0]+dist_heuristic(a, goal, size)
            visited[a] = h+g 
            frontier.push((h+g, a, curr[2]+[a]))
   return None

def main():
    # A star
   print ("Inversion works?:", check_inversion())
   print ("Heuristic works?:", check_heuristic())
   #initial_state = getInitialState("_123456789ABCDEF", 4)
   initial_state = input("Type initial state: ")
   if inversion_count(initial_state):
      cur_time = time.time()
      path = (a_star(initial_state))
      if path != None: display_path(path, 4)
      else: print ("No Path Found.")
      print ("Duration: ", (time.time() - cur_time))
   else: print ("{} did not pass inversion test.".format(initial_state))
   
if __name__ == '__main__':
   main()



   # frontier = HeapPriorityQueue()
   # if start == goal: return []
   # # Your code goes here
   # path = []
   # cost = 0
   # visited = set()
   # heuristic = dist_heuristic(start, goal, size)
   # frontier.push((heuristic, start, [start]))
   # while not frontier.isEmpty():
   #    curr = frontier.pop()
   #    heuristic = dist_heuristic(curr)
   #    if curr[1] == goal:
   #       return curr[2]
   #    if not curr[1] in visited:
   #       for a in generate_children(curr):
   #          if not a in visited:
   #             #add heuristic and regular path cost in another variable push cost  goes into the first part
   #             #do smth to list (add)
   #             path = path + a
   #             cost = heuristic + dist_heuristic(a, goal, size)
   #             visited.add(curr[1])
   #             frontier.push(cost, a, path)