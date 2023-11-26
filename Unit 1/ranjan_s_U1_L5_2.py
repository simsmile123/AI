# Name:    Simrith Ranjan      Date: 10/04/21
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
       if(len(self.queue) > 2):
           ret = self.queue[1]
           self.queue[1] = self.queue[len(self.queue)-1]
           self.queue.pop()
           self.heapDown(1, len(self.queue) -1)
           return ret
       else:
           ret = self.queue[1]
           self.queue.pop()
           return ret
      # Your code goes here
      #if len(self.queue) > index:
      #index = index+1
      #temp = self.queue[index+1] 
      #f = self.queue.remove(self.queue[index+1])
      #self.reheap()

      #return temp   # change this
def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it'''
   adj_set = set()
   # TODO 1: adjacents
   # Your code goes here
   
   alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   for x in "abcdefghijklmnopqrstuvwxyz": #range(len(current)):
        for y in range(len(current)):
            temp = current[:y],x,current[y+1:]
            temp = ''.join(temp)
            if not temp == current:
                if temp in words_set:
                    adj_set.add(temp)
    #add code here
   return adj_set

def check_adj(words_set):
   # This check method is written for words_6_longer.txt
   adj = generate_adjacents('listen', words_set)
   target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
   return (adj == target)
def display_path(n, explored):
    #add stuf here so you can call this once goal is found
    #combine two lists and return middle node??
   l = []
   while explored[n] != "": #"s" is initial's parent
      l.append(n)
      n = explored[n]
   #print ()
   l.append(n)
   l = l[::-1]
  # print(l, "\nThe number of steps:", len(l))
   return l
    #return None


def getInitialState(sample, size):
   sample_list = list(sample)
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

def display_path(path_list, size):
   for n in range(size):
      for path in path_list:
         print (path[n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

def dist_heuristic(state, goal): #CHANGE THIS
   # Your code goes here
  # temp_array, g, s = [],0,0 
    # for each point, finding distance
    # to rest of the point
   count = 0
   for x in range(len(state)):
        if state[x] != goal[x]:
            count = count+1
   return count


def a_star(start, goal, words, heuristic=dist_heuristic): #change this
   frontier = HeapPriorityQueue()
   h = heuristic(start, goal)
   visited = {start:h}
   frontier.push((h, start, [start]))
   while not frontier.isEmpty():
      curr = frontier.pop()
      if curr[1] == goal:
         return curr[2]
     # if not curr[1] in visited:
         #visited.add(curr[1])
        # print(curr[1])
      for a in generate_adjacents(curr[1], words):
         a = ''.join(a)
         g = len(curr[2]) +1
         h = heuristic(a, goal)
         if a not in visited: #or visited[a] > h+g:
              # curr[2].append(a)
              #curr[0]+dist_heuristic(a, goal, size)
            visited[a] = h+g 
            frontier.push((h+g, a, curr[2]+[a]))
   return None
def main():
   filename = input("Type the word file: ")
   words_set = set()
   file = open(filename, "r")
   for word in file.readlines():
      words_set.add(word.rstrip('\n'))
   #print ("Check generate_adjacents():", check_adj(words_set))
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   cur_time = time.time()
   path = (a_star(initial, goal, words_set))
   if path != None:
      print (path)
      print ("The number of steps: ", len(path))
      print ("Duration: ", time.time() - cur_time)
   else:
      print ("There's no path")
 
if __name__ == '__main__':
   main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''

