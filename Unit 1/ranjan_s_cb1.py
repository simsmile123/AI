# Simrith Ranjan
# Aug 25, 2021
 
def sleep_in(weekday, vacation):
  return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  return a + b  if a != b else 2 * ( a + b)

def diff21(n):
  return abs(21 - n) * 2 if n > 21 else abs(n - 21)

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

def makes10(a, b):
  return (a== 10 or b == 10 or a+b == 10)

def near_hundred(n):
  return (90 <= n <= 110 or 190 <= n <= 210)

def pos_neg(a, b, negative):
   # ((negative) and (a < 0 and b <0 )) negative
    # else ((a > 0 and b < 0) or (a <0 and b >0))))
  return negative if (a < 0 and b < 0) else not negative and (((a < 0 and b > 0) or (a > 0 and b < 0)))
# start of the string-1

def hello_name(name):
  return "Hello " + name + "!"

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  return "<%s>%s</%s>" %(tag,word,tag)

def make_out_word(out, word):
  return out[:len(out)//2] + word + out[len(out)//2:] #% (out,out, word, out, out)
  # return "" + out[0,2] + word + out[2,4])

def extra_end(str):
  return str[len(str) -2:len(str)] +str[len(str) -2:len(str)]+str[len(str) -2:len(str)]

def first_two(str):
  return str[:2]

def first_half(str):
  return str[:int(len(str) / 2)]

def without_end(str):
  return str[1: len(str) -1]

def first_last6(nums):
  return (nums[0] == 6 or nums[-1]  == 6)

def same_first_last(nums):
  return (len(nums) >=1 and nums[0] == nums[-1])


#pi one goes here
def make_pi(n):
  #list = [3, 1, 4]
  return [3,1,4,1,5,9,2,6,5,3,5,8,9,7][0:n]

def common_end(a, b):
  return a[-1] == b [ -1] or a[0] == b[0]

def sum3(nums):
  return sum(nums) #nums[0] + nums[1] + nums[2]

def rotate_left3(nums):
  #return nums[1:2] + nums[2:3] + nums[0:1]
  return list(nums[1:]+list(nums[:1]))


def reverse3(nums):
 #list = [nums[-1:], nums[1:2], nums[:1]]
 return nums[::-1] #[nums[-1], nums[1], nums[0]]
 
def max_end3(nums):
 # return [nums[0],nums[0],nums[0]] if (nums[0] > nums[-1]) else [nums[2],nums[2],nums[2]]
  return [nums[0]]*len(nums) if nums[0]>nums[len(nums)-1] else [nums[len(nums)-1]]*(len(nums)) #*3 literally is the same as above^

def cigar_party(cigars, is_weekend):
  return is_weekend if (is_weekend and cigars >= 40) else ((40 <= cigars <= 60))

def date_fashion(you, date):
  return 0 if (you <= 2 or date <= 2) else 1 if(2 < you < 8 and 2 < date < 8) else 2
  #2 if (2 < you >= 8 or 3 < date >= 8) else 1 if (you > 2 and date > 2) else 0

def squirrel_play(temp, is_summer):
  return is_summer if (is_summer and 60 <= temp <=100) else 60 <= temp <=90

#speeding one
def caught_speeding(speed, is_birthday):
  return 0 if (speed <= 65 and is_birthday) else 1 if (66 <= speed <= 85 and is_birthday) else 2 if (is_birthday) else 0 if speed <= 60 else 1 if (61 <= speed <= 80) else 2 

def sorta_sum(a, b):
  return 20 if (10 <= (a+b) <= 19) else a+b
 
#smth goes here too
def alarm_clock(day, vacation):
  return '10:00' if (1 <= day <=5 and vacation) else 'off' if (vacation) else '7:00' if (1 <= day <=5) else '10:00'
  

def love6(a, b):
  return a == 6 or b == 6 or (a + b) == 6 or (abs(a - b)) == 6

def in1to10(n, outside_mode):
  return (n <= 1 or n >=10) if (outside_mode) else 1<=n<=10
