#Simrith Ranjan
f1 = (lambda x: x.count(19) == 2 and x.count(5) >= 3) #prob 1 but with lambda
print(f1([5,5,5,5,19,19]))
def two(y): #prob 2
   # Write a Python program that accept a list of integers and
   #check the length and the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said list
   count = 0
   for z in y:
       if z == y[4]:
           count+=1
   if len(y) == 8 and count == 3: return y
def firsti(nums): #prob 7 
    return all([sum(nums[:i]) == i for i in range(len(nums))])
def nonnegative(n): #prob 17
    return ' '.join(map(str,range(n+1)))
def unique(strs): #prob 28
    return max(strs, key=lambda x: len(set(x)))
def nineninenine(stars):
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100