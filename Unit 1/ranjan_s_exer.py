# Name: Simrith Ranjan
# Date: 09/08/21
# Do not forget to change the file name -> Save as                                                            
''' Tasks '''
import PIL
from PIL import Image
# import io,sys
# 1. Given an input of a space-separated list of any length of integers, output the sum of them.
# 2. Output the list of those integers (from #1) that are divisible by three.
l = [int(x) for x in input("list of numbers: ").strip().split()]
#print(l)
print(f"1. sum = {sum(l)}")
print(f"2. list of multiples of 3: {[int(x) for x in  l if int(x) % 3== 0]}")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

# 3. Given an integer input, print the first n Fibonacci numbers. eg. n=6: 1, 1, 2, 3, 5, 8
def fib(n): 
    print("3. fibonacci:", end = " ")
    f1 = 1
    f2 = 1
    if (n < 1):
        return
    print(f1, end=" ")
    for x in range(1, n):
        print(f2, end=" ")
        next = f1 + f2
        f1 = f2
        f2 = next
#    for n in range(x):
#    if x < 2: print 
#    else fib(x-1) + fib(x-2))
# for x in range(n)
s = int(input("Type n for Fibonacci sequence: "))
fib(s)
#n if n < 2 else fib(n-1) + fib(n-2))
##def fib(msg):
   # second = 1
   ##for x in range(msg):
     #   y = prev + second
       # prev = second
       # second = y
       # print(y + ", ")


# 4. Given an input, output a string composed of every other character. eg. Aardvark -> Arvr
s = input("\n" + "Type a string: ")
print(f"4. every other str: {s[::2]}")


# 5. Given a positive integer input, check whether the number is prime or not.
def prime(n, i):
    if (n == 0 or n == 1):
        return False
    if (n == i):
        return True
    if (n % i == 0):
        return False   
    i += 1     
    return prime(n, i)
num = int(input("Type a number to check prime:"))
print("Is prime?", prime(num,2))

# 6. Calculate the area of a triangle given three side lengths.  eg. 13 14 15 -> 84
arr = [int(x) for x in input("Type three sides of a triangle:").split()]
#arr = [int(input("\n" + "Type three sids of a triangle:").split())]
#int(input("\n" + "Type three sids of a triangle:")).split()
p = (sum(arr) / 2.0)
print(f"The area of {arr[0]} {arr[1]} {arr[2]} is {((p)*(p-arr[0])*(p-arr[1])*(p-arr[2]))**0.5}")

s=""
inputt = input("Type a sentence:") 
punct = '''!()-[]{};:!'"\,<>./?@{#$%^&*}_~''' #''' !()-[]{};:!'"\,<>./?@#$%^&*_'~'''
for y in inputt:
     if y not in punct:
         s += y #inputt.replace(y,"")    
s = s.replace(" ", "")
print("7. Punct removed:" + s)    

# 7. Given a input of a string, remove all punctuation from the string. 
# eg. "Don't quote me," she said. -> Dontquotemeshesaid
# 8. Check whether the input string (from #7, lower cased, with punctuation removed) is a palindrome.
print(f"8. Is palindrome? {(s.lower() == s.lower()[::-1]) > 0}")
# 9. Count the number of each vowel in the input string (from #7).
#c = 0
#vow = 'aeiou'
#for z in input:
#    if z in vow:
#        c+=1
v_dict = {} 
for z in "aeiou":
    count = inputt.count(z)
    v_dict[z] = count
print("9. Count each vowel:", v_dict)
#print(v_dict)
#10. given two integers do math
# eg. 2 5 -> 0, 2, 6, 12
#arr = [int(l) for l in input("Type two integers (lower bound and upper bound): ").split(" ")]
#ret = []
#for x in range(arr[0],arr[1]+1):
#    temp = (x **2 - 3 *x+ 2)
#    ret.append(temp)
s_10 = input("Type two integers (lower bound and upper bound): ")
bounds = [int(l) for l in s_10.split(" ")]
result = ""
for i in range(bounds[0], bounds[1]+1):
    result = result + (" " + str((i**2-3*i+2)))
print(f"10. Evaluate f(k) = k^2-3k+2 from {bounds[0]} to {bounds[1]}: {result}") 
# 11. Given an input of a string, determines a character with the most number of occurrences.
inputs = input("11-15. Type a string:")
inputt = inputs.strip().split(" ")
all = {}
for i in inputs:
    if i in all:
        all[i] += 1
    else:
        all[i] = 1
        
m = 0
chars = []
for key in all.keys():
    if all[key] > m:
        m = all[key]
        chars = [key]
    elif all[key] == m:
        chars.append(key)

print("11. Most occured char:", end=" ")
print(*chars, end = " ")
#(res)
# 12. With the input string from #11, output a list of all the words that start and end in a vowel.
arr = [str(x) for x in inputt]
temp = []
vowel = 'aeiouAEIOU'
# for x in range(input.count(" ")+2):
#     if !(arr[x][0] in [aeiou]) or (arr[x][x] in [aeiou]):
#         arr.pop(x)
for i in inputt:
    if(i[0] in vowel and i[-1] in vowel):
    # if any((i.startswith(x) for x in "aeiou")) and any((i.endswith(x) for x in "aeiou")):
        temp.append(i)
print("\n" +"12. List of words starting and ending with vowels:", end = " ")
print(temp)
# 13. With the input string from #11, capitalizes the starting letter of every word of the string and print it.
thirteen = []
for i in inputt:
    thirteen.append(i.capitalize())
    #print(thirteen)
print("13. Capitalize starting letter of every word:", end = " ")
print(*thirteen, sep= " ")
# 14. With the input string from #11, prints out the string with each word in the string reversed.
four = []
for y in inputt:
    four.append(y[::-1])
print("14. Reverse every word:", end = ' ')
print(*four, sep = " ")
# 15. With the input string from #11, treats the first word of the input as a search string to be found in the rest 
# of the string, treats the second word as a replacement for the first, and treats the rest of the input as the string to be searched.
# 	eg.    b Ba baby boy ->  BaaBay Baoy
# lol = inputt[2:len(inputt)]
# lol = ''.join(lol)
# lol.replace(inputs[0], inputs[1])
# search = inputt[0]
# search_int = len(inputt[0])
# second = inputt[1]
# for x in range(2, len(inputt)+1):
#     for y in range(len(inputt) - search_int):
#         if(inputt[y:y+search_int] == search):
#             lol.replace(y, second)
if len(inputt) > 1:
    first = inputt[0]
    second = inputt[1]
    r = " ".join(inputt[2:])
    ans = r.replace(first, second)
    print("15. Find the first and replace with the second:", end = " ")
    print(ans)
 
# 16. With an input of a string, removes all duplicate characters from a string.  Eg. detection -> detcion
sr = ([x for x in input("Type a string to remove all duplicate chars:")])
dup = ""
for x in sr:
    if x not in dup:
        dup += x
    dup.replace(" ", "")
print(f"16. Remove all duplicate chars: {dup}")

# 17. Given an input of a string, determines whether the string contains only digits.
dig = input("Type a string to check if it has only digits or not:")
print(f"17. Is a number?: {dig.isdecimal()}")
# 18. If #17 prints True, determines whether the string contains only 0 and 1 characters, and if so assumes it is a binary string, 
# converts it to a number, and prints out the decimal value.

def bistring(x):
    check = False
    for i in range(len(x)):
        if(x[i] == "1" or "0"):
            check = True
        else:
            check = False
    if check:
        x=int(x, 2)
        print("18. It is a binary number:", end = " ")
        print(x)
    else:
        return "18. It is not a binary number"
if(dig.isdecimal()) : bistring(dig)

# 19. Write a script that accepts two strings as input and determines whether the two strings are anagrams of each other.
s1 = input("Type the first string to check anagram:").lower()
s2 = input("Type the second string to check anagram:").lower()
print("Are", s1, "and", s2, "anagrams?:", end="")
if(len(s1) == len(s2)):
    # sort the strings
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    # if sorted char arrays are same
    if(sorted_s1 == sorted_s2):
        print(True)
    else:
        print(False)
# 20. Given an input filename, if the file exists and is an image, find the dimensions of the image.
# # print(PIL.PILLOW_VERSION)
# # URL = sys.argv[0] #link of the file
# # # f = io.BytesIO(urllib.request.urlopen(URL).read())
# # f= Image.open("tj_logo")
# # print(img.size)
# # pix = img.load() 
# # img= img.show()
# filename = input("Type the image file name:")
# try:
#     with Image.open(filename) as f:
#         print(f.width())
#         print(f.height())
# except FileNotFoundError: 
#     print("file not found")
# print("20. print smth")
file = input("Type the image file name:")
import os
if not os.path.isfile(file):
    print("20. It is not a file")
else:
    img = Image.open(file)
    width, height = img.size
    print("20. Image dimension:", width, "by",height)

# 21. Given an input of a string, find the longest palindrome within the string.
tease = input("Type a string to find the longest palindrome:")
tease = tease.replace(" ", "")
# # palindrome = ""
# # for i in range(int(len(tease)/2)):
# #     if tease[:i] == tease[::-1][:i]:
# #         palindrome = tease
# #         break
# # print(palindrome)
#def helper(t, l, h):1
#    while l >=0 and t[l] == t[h] and h < len(t):
#        l = l -1
#        h = h +1
#    return t[l +1:h]
start = 0 
end = 0
#max_str = ''
#max_length = 0
for x in range(len(tease)):
    for i in range(x,len(tease)):
        if(tease[x:i] == tease[i:x:-1] and (i - x > end - start)):
            start = x
            end = i

#    current = helper(tease, i, i) #ODD
#    length_current= len(current)
#    if length_current > max_length:
#        max_length = length_current
#        max_str = current
#    current = helper(tease, i, i + 1) #EVEN
#    length_current= len(current)
#    if length_current > max_length: #change if even is greater than odd
#        max_length = length_current
#        max_str = current
print("21. Longest palindrome within the string:", tease[start:end+1])
# max_length = 1
# start = 0
# for l in range(len(tease)+1):
#     for i in range(len(tease)-l+1):
#         end = i+l
#         if l==2:
#             if tease[i] == tease[end-1]:
#                 max_length = l
#                 start = i
#             else:
#                if tease[i] == tease[end-1]:
#                   max_length = l
#                   start = i
#     print(tease[start:start+1])
# 22. Given an input of a string, find all the permutations of a string.
# 23. Given the input string from #22, find all the unique permutations of a string.
def permutations(s):
    if len(s) == 1:
        return s
    perms = []
    for c in s:
        for p in permutations(s.replace(c,'', 1)):
            perms.append(c+p)
    return perms
    
ans = permutations(input("Type a string to do permutation:"))
print("22. all permutations:", ans)
print("23. all unique permutation:", set(ans))

 
# 24. Given an input of a string, find a longest non-decreasing subsequence within the string (according to ascii value).

   
s = (input("Type a string to find the longest non-decreasing sub:")).strip()
l = [] 
i = 0
ls = []
while i <len(s)-1:
    if ord(s[i]) <= ord(s[i+1]): l.append(s[i])
    else:
       # l.append(s[i+1])1
        ls.append(''.join(l))
        l = []
    i +=1
longest_sub = 0
for x in range(len(ls)):
    if len(ls[x]) > longest_sub:
        longest_sub = x
print("24. longest non-decreasing sub:", ls[x])
