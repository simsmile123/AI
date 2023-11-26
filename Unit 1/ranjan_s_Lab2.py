#Simrith Ranjan
#09/22/2021
def generate_dict(filename):
    temp_dict = {}
    return temp_dict
def generate_adjacents(current, word_list):
    adj_list = set()
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for x in "abcdefghijklmnopqrstuvwxyz": #range(len(current)):
        for y in range(len(current)):
            temp = current[:y],x,current[y+1:]
            temp = ''.join(temp)
            if not temp == current:
                if temp in word_list:
                    adj_list.add(temp)
    #add code here
    return adj_list
       
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
   

def display_path(n, explored): #key: current, value: parent
   l = []
   while explored[n] != " ": #"s" is initial's parent
      l.append(n)
      n = explored[n]
   #print ()
   l.append(n)
   l = l[::-1]
   print(l, "\nThe number of steps:", len(l))
   return ""
def display_pathh(z, n, explored): #key: current, value: parent
   l = []
   while explored[n] != " ": #"s" is initial's parent
      l.append(n)
      n = explored[n]
   #print ()
   l.append(n)
   l = l[::-1]
   print(l, f"\nsteps within {z} limit:", len(l))
   return ""
def BFS(start, end, word_dict):
   explored = {start: " "}
   Q = [start]
   #Q.append(initial_state)
   #oal = end
   #frontier = {initial_state: "s"}
   while True:
       if len(Q) == 0: return "No solution"
       s = Q.pop(0)
       #explored[s] = frontier[s]
       if s == end: return display_path(s, explored)
          #goal = s 
       for a in generate_adjacents(s, word_dict):
           if not a in explored:# and not a in Q:
               explored[a] = s
               Q.append(a)
       #return(["No solution"])
def recur(start,end, word_dict, explored, limit, x):
    #code
    cutoff_occured = False
    if start == end: return display_pathh(x, start, explored)
    elif limit == 0: return "cutoff"
    else:
        #print(generate_adjacents(start, word_dict))
        # cutoff_occured = False
        for a in generate_adjacents(start, word_dict):
            #start = 
            if not a in explored:
                new_explored = explored
                new_explored[a] = start
                #explored[a] = start
            result = recur(a, end, word_dict, explored, limit-1,x)
            if result == "cutoff": cutoff_occurred = True
            elif result != "cutoff": return result
        if cutoff_occurred : return "cutoff"
        #del explored[a]

    return None
def DLS(start, end, word_dict, limits):
    explored = {start:" "}
    return recur(start, end, word_dict, explored, limits-1, limits)
def IDS(start, end, word_dict):
    limits = 1
    while True:
        result = DLS(start, end, word_dict, limits)
        limits = limits+1
        if result != "cutoff": return result
    return None
def main():
    word=[]
    s = input("BFS. Type the starting word:")
    e = input("BFS. Type the goal word:")
    li = []
    with open("G:/My Drive/AI/words.txt", 'r') as infile: #open("C:/Users/1795730/Documents/words.txt", 'r') as infile:
      lines = infile.readlines()
      for x in lines:
          li.append(x.strip())
   # print(li)
    #print(generate_adjacents(s, li))
    print(BFS(s,e,li), end = '')
    #print(DLS(s,e, li, 10))
    steps = input("Type the limit (1-20):")
    start = input("Type the starting word:")
    end = input("Type the goal word:")
    print("Shortest Path:", DLS(start,end, li, int(steps)), end = '')
    print(IDS(start,end,li))
    #print("Steps:" )

if __name__ == '__main__':
   main()