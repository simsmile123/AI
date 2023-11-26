import sys; args = sys.argv[1:]
import re, random

BLOCKCHAR = '#'
OPENCHAR ='-'
PROTECTEDCHAR = '~'

def initialize(prefilled_word_dict, height, width):
    xword = '-'*(height*width)
    display(xword, height, width) #(word, direction, row, col)
    for package in prefilled_word_dict:
        word, direct, r, c = package
        if direct.lower() == 'h':
            start = r*width + c
            xword = xword[:start]+ word + xword[start+len(word):]
        else: 
            xword_list = list(xword)
            for i in range(len(word)):
                xword_list[(r+i)*width+c] =  word[i]
                xword = ''.join(xword_list)
        return xword
   #one for V
    #pass
def display(xword, height, width):
    print('\n'.join([xword[width*k:width*(k+1)] for k in range(height)]))
    #pass

#after all blocks added change al protected into open
#add prefilled words back

def hashtag(board, block_count, height, width):
   board = initialize(board, height, width)

def add_helper(board, num_of_blocks, height, other, width):
#    if num_of_blocks == curr_num_of_blocks: return board and num_of_blocks
    xw = BLOCKCHAR*(width+3) +(BLOCKCHAR*2).join([board[p:p+width] for p in range(0, len(board), width)]) +BLOCKCHAR*(width+3)
    illegRE = "[{}](.?[{}]|[{}].?)[{}]".format(BLOCKCHAR, PROTECTEDCHAR, PROTECTEDCHAR, BLOCKCHAR)
    newH = len(xw) // (width+2)
    for turn in range(2):
        if re.search(illegRE, xw): return board, len(board)
        xw = transpose (xw, len(xw) // newH)
        newH = len(xw) // newH
    subRE="[{}]{}(?=({})". format(BLOCKCHAR, OPENCHAR, BLOCKCHAR)
    subRE2 ="[{}{}(?=[{}])".format(BLOCKCHAR, OPENCHAR, OPENCHAR, BLOCKCHAR)
    subRE3="[#](-~-|--~|~--|~~-|-~~|~-~)(?=[#])"
    newH = len(xw) // (width + 2)
    for turn in range (2):
        xw = re.sub(subRE, BLOCKCHAR*2, xw)
        xw = re. sub (subRE2, BLOCKCHAR*3, xw)
        xw = re. sub (subRE3, BLOCKCHAR+PROTECTEDCHAR*3, xw)
        xw = transpose(xw, len(xw) // newH)
        newH = len(xw) // newH
    new_board = ''
    for row in range (width+2, len(xw) - (width+2), width+2): new_board += xw[row+1:width+row+1]
    return new_board, new_board.count(BLOCKCHAR)

def clean_words(xword):
    xword = re.sub(r'\w', PROTECTEDCHAR, xword)
    xword = make_palindrome(xword)
    return xword
def area_fill(board, xword, width, height): #connectivity
    pass
def checkIllegal(board, xw, height, width):
    illegRE = "[{}](.?[{}]|[{}].?)[{}]".format(BLOCKCHAR, PROTECTEDCHAR, PROTECTEDCHAR, BLOCKCHAR)
    newH = len(xw) // (width+2)
    for turn in range(2):
        if re.search(illegRE, xw): return board

def make_palindrome(xword):
    xword_list, n = list(xword), len(xword)-1
    for i in range(len(xword_list)//2):
        if {xword_list[i], xword_list[n-i]} == {OPENCHAR, BLOCKCHAR}:
            xword_list[i], xword_list[n-i] = BLOCKCHAR, BLOCKCHAR
        elif {xword_list[i], xword_list[n-i]} == {OPENCHAR, PROTECTEDCHAR}:
            xword_list[i], xword_list[n-i] = PROTECTEDCHAR, PROTECTEDCHAR
    return ''.join(xword_list)
def transpose(xword, newWidth): 
    return "".join([xword[col::newWidth] for col in xword])
def initialboard(xword):
    xword_list, temp = list(xword), []
    for x in xword_list:
        if x not in {OPENCHAR, BLOCKCHAR}: temp.append('~')
        else: temp.append(x)
    return ''.join(temp)
def main():
    number_of_blocks, height, width, prefilled_words = 0,0,0,[]
    for arg in args:
        arg = arg.upper()
        #if os.path.isfile(arg): continue
        if re.search(r'^\d+$', arg):
            number_of_blocks = int(arg)
        elif re.search(r'^\d+X\d+$', arg, re.I):
            x = arg.lower().index('x')
            height = int(arg[:x])
            width = int(arg[x+1:])
        elif re.search(r'^\w\d+X\d+\w+', arg, re.I):
            direction = arg[0] 
            x = arg.lower().index('x')
            row = int(arg[1:x])
            m = 0
            for z in range(x + 1, len(arg)):
                if not arg[z] in ['0','1','2','3','4','5','6','7','8','9']:
                    m = z
                    break
            col = int(arg[x+1:m])
            word = arg[m:]
            prefilled_words.append((word, direction, row, col))
    print(number_of_blocks)
    if number_of_blocks == height*width:
        s = "#"*(width*height)
        display(s, height, width)
    # xword = initialize(prefilled_words, height, width)
    # print("\n \bnew board:")
    # display(xword, height, width)
main()
#Simrith Ranjan, 5, 2023