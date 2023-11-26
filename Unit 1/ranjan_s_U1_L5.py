# Name:    Simrith Ranjan      Date: 10/04/21
import time

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
def bi_bfs(start, goal, words_set):
   # frontier = [[start], [goal]]
   # explored = [{start:""}, {goal:""}]
   # k = 1
   # while frontier[0] and frontier[1]:
   #    k = 1-k
   #    temp = frontier[k][:]
   #    frontier[k] = []
   #    while temp:
   #       s= temp.pop(0)
   #       if s in frontier[1-k]:
   #          return display_path(s, explored[0]) +[s] + display_path(s, explored[1])[::-1]
   #       for a in generate_adjacents(s, words_set):
   #          if a not in explored[k]:
   #             frontier[k].append(a)
   #             explored[k][a]=s
   '''The idea of bi-directional search is to run two simultaneous searches--
   one forward from the initial state and the other backward from the goal--
   hoping that the two searches meet in the middle. 
   '''
   if start == goal: return [start]
   explored = {start: ""}
   Q = [start]
   backexp = {goal: ""}
   end = [goal]
   while len(Q) > 0 and len(end) > 0:   
      if len(Q) == 0 or len(end) == 0: return "fail"
       #while len(diff) > 0 :
      
         #intersection right here if 
      s = Q.pop(0)
      if s in backexp:
         x = display_path(s, explored)
         y = display_path(t, backexp)[::-1]
         y.pop(0)
         return x+y
      for a in generate_adjacents(s, words_set):
         if not a in explored:
               explored[a] = s
               Q.append(a)
      # while len(diff)>0:
      t = end.pop(0) 
      if t in explored:
         x = display_path(t, explored)
         y = display_path(t, backexp)[::-1]
         y.pop(0)
         return x+y
      for x in generate_adjacents(t, words_set):
         if not x in backexp:
            backexp[x] = t
            end.append(x)
     
       
   '''Your code goes here'''
   # TODO 2: Bi-directional BFS Search
   # Your code goes here
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
   path = (bi_bfs(initial, goal, words_set))
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
