
#Simrith Ranjan
#Nicole Kim
array123([1,2,3,4,4,5])
def string_times(str, n):
  return ('%s'%(str)) * n
def front_times(str, n):
  return str[:3]*n
def string_bits(str):
  return str[::2]
def string_splosion(str):
  #return "".join([y for x in range(len(str)+1) for y in str[:x]])
  return ''.join([str[:i+1] for x in range(len(str))])
#def last2(str):
    #return (i for i in range(len(str) if (str.count(str[len(str) - 2:])) -1 
    #(str.count([(len(str)-2):]))
    #max([str.count(str[i:i+2]) for i in range(0, len(str)-2)])
    ## print ( [(str[i:i+2]) for i in range(0, len(str)-2)])
#last2("acccddd")
def last2(str):
   return sum(1 for i in range(len(str)) if str[2:] == str[x:x+2])
 #return len([i for i in range(len(str)) if (str[len(str)-2:] == str[i:i+2])]) -1 if len(str) >0 else 0  
def array_count9(nums):
  return nums.count(9)
def array_front9(nums):
  return True if nums[:4].count(9) else False
  #([(i for i in range(0,3) if(nums[i:i+1] == 9))]) else False
def array123(nums):
   #return True if(for i in range(len(nums)+2) if nums[i:i+3] == [1, 2, 3])
   #return True if ((nums[i:i+3]==[1,2,3]) for i in range(len(nums)-2)) else False
   #return True if (for i in range(len(nums)-2) if nums[i:i+3] == [1,2,3] if (len(nums))>0) else False
  return True if len([i for i in range(len(nums)) if (nums[i:i+3] == [1,2,3])]) else False
def string_match(a, b):
  return len([i for i in range(len(a) - 1) if (a[i:i+2] == b[i:i+2])]) if len(a) > 0 else 0 
def lone_sum(a, b, c):
  return sum(i for i in [a, b, c] if [a, b, c].count(i) == 1)
  #a + b + c if a != b != c 
  def lucky_sum(a, b, c):
  #return sum(for i in [a, b, c] if not ([a, b, c][i] == 13) and [a, b, c][i] < [a, b, c][13])
  #a + b + c if a != b != c 
  return sum(i for i in [a,b,c] if not(i == 13)) #break if smth is 13


