
#Simrith Ranjan
#Nicole Kim
#array123([1,2,3,4,4,5])
def string_times(str, n):
  return str * n
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
  #([(i for i in range(0,3) if(nums[i:i+1] == 9))]) else False
def array123(nums):
   #return True if(for i in range(len(nums)+2) if nums[i:i+3] == [1, 2, 3])
   #return True if ((nums[i:i+3]==[1,2,3]) for i in range(len(nums)-2)) else False
   #return True if (for i in range(len(nums)-2) if nums[i:i+3] == [1,2,3] if (len(nums))>0) else False
  # return nums[x:x+3] == [1,2,3] for x in range(len(nums) - 2)
 return True if len([i for i in range(len(nums)) if (nums[i:i+3] == [1,2,3])]) else False
def string_match(a, b):
    return sum([i for i in range(len(a) - 1) if (a[i:i+2] == b[i:i+2])])
def lone_sum(a, b, c):
  return sum(i for i in [a, b, c] if [a, b, c].count(i) < 2) 
  #a + b + c if a != b != c 
def lucky_sum(a, b, c):
  #return sum(for i in [a, b, c] if not ([a, b, c][i] == 13) and [a, b, c][i] < [a, b, c][13])
  #a + b + c if a != b != c 
  #return [0,a,a+b, a+b+c,13][]
  return sum([a,b,c][i] for i in range(3) if not(13 in [a,b,c][:i+1]))
def no_teen_sum(a, b, c):
  return sum(i for i in [a, b, c] if not(i in [13,14,17,18,19]))
def round_sum(a, b, c):
  return sum( x+5 // 10 * 10 for x in [a,b,c])
  #return int(round(a+.1,-1)) + int(round(b+.1,-1))+int(round(c+.1,-1))
def close_far(a, b, c):
  return (abs(a-b) <= 1 and abs(b-c) >=2 and abs(a-c) >=2) or (abs(a-b) >= 2 and abs(b-c) >=2 and abs(a-c) <=1)
def make_chocolate(small, big, goal):
  return -1 if(small<goal%5 or 5*big+small<goal) else (goal-5*big)%5 if not(small < goal%5 or 5*big+small<goal)
 # return (goal-5*big)%5
 #[___] + [-1] [index]
 #return -1 if(small<goal%5 or 5*big+small<goal) else (goal-5*big)%5 if (goal-5*big) < 0 else goal - 5*big
   #-1 if (small < goal%5 or 5*big+small<goal )
  #else goal-5*big
 def double_char(str):
  return "".join( x *2 for x in str)
def count_hi(str):
  return str.count("hi")
def cat_dog(str):
  return str.count("dog") == str.count("cat")
def count_code(str):
   return sum((str[i:i+2] == 'co' and str[i+3] == 'e') for i in range(len(str)-3))  
def end_other(a, b):
  return (a.lower().endswith(b.lower()) or b.lower().endswith(a.lower()))
def xyz_there(str):
  return str.count("xyz") > str.count(".xyz")
def count_evens(nums):
  ##return len([i for i in nums if i%2==0])
  return sum(x for x in nums if x%2 ==0)
def big_diff(nums):
  return max(nums)-min(nums)
def centered_average(nums):
  # max(nums)
  # min(nums)
  return sorted(nums)[1:-1] // (len(nums) -2)
  #return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2)
def sum13(nums):
  #return sum(nums[i] for i in range(len(nums)) if not(13 in nums[i+1:i+2]))
  return sum([nums[i] for i in range(len(nums)) if list([0]+nums)[i] != 13 and nums[i]!=13])
def sum67(nums):
  return sum67(nums[:x] + nums[x+1:][nums[x+1:].index(7)+1:]) if 6 in nums and 7 in nums[x:nums.index(6) +1] else sum(nums)
 # return sum(nums[i] for i in range(len(nums)) if nums[i] != 6 and (not(6 in nums[:i]) or (7 in nums[:i] and (nums[:i][::-1].index(6) > nums[:i][::-1].index(7)))))
def has22(nums):
  return len([i for i in range(len(nums)-1) if (nums[i],nums[i+1])==(2,2)])>0
 
