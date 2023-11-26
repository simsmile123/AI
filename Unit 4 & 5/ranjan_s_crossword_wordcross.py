import sys; args = sys.argv[1:]
import re, random

BLOCKCHAR = '#'
OPENCHAR ='-'
PROTECTEDCHAR = '~'
#args = '13x13 27 H6x4no#on v5x5ton v0x0instep h0x4Trot H0x9Calf V0x12foot'.split()        
def initialize(prefilled_word_dict, height, width):
    xword = '-'*(height*width)
    # display(xword, height, width) #(word, direction, row, col)
    for package in prefilled_word_dict:
        word, direct, r, c = package
        if word == '#': xword = xword[:r*width+c] + '#' + xword[r*width+c+1:]
        else:
            if direct.lower() == 'h':
                start = r*width + c
                xword = xword[:start]+ word + xword[start+len(word):]
                # display(xword, height, width)
            else: 
                xword_list = list(xword)
                for i in range(len(word)):
                    xword_list[(r+i)*width+c] =  word[i]
                    xword = ''.join(xword_list)
                # display(xword, height, width)
    return xword

def display(xword, height, width):
    print('\n'.join([xword[width*k:width*(k+1)] for k in range(height)]), end='\n\n')
def transpose(xword, newWidth): 
    return "".join([xword[col::newWidth] for col in range(newWidth)])
# def make_palindrome(xword):
#     xword_list, n = list(xword), len(xword)-1
#     for i in range(len(xword_list)//2): 
#         if {xword_list[i], xword_list[n-i]} == {OPENCHAR, BLOCKCHAR}:
#             xword_list[i], xword_list[n-i] = BLOCKCHAR, BLOCKCHAR
#         elif {xword_list[i], xword_list[n-i]} == {OPENCHAR, PROTECTEDCHAR}:
#             xword_list[i], xword_list[n-i] = PROTECTEDCHAR, PROTECTEDCHAR
# #     return ''.join(xword_list)
# def area_fill(board, sp, dirs = [-1, width, 1, -1*width]):
#     if sp < 0 or sp >= len(board): return board
#     if board[sp] in {OPENCHAR, PROTECTEDCHAR}:
#         board = board[0:sp] + '?' + board[sp+1:]
#     for d in dirs:
#         if d == -1 and sp % width == 0: continue #left edge
#         if d == 1 and sp+1 % width == 0: continue #right edge
#         board = area_fill(board, sp+d, dirs)
#     return board
def make_palindrome(board, num, height, width):
    n = len(board) -1
    b_list = list(board)
    for x in range(0, len(board)//2):
        if board[x] != board[n-x]:
            if BLOCKCHAR in {board[x], board[n-x]} and OPENCHAR in {board[x], board[n-x]}:
                b_list[x], b_list[n-x] = BLOCKCHAR, BLOCKCHAR
            elif PROTECTEDCHAR in {board[x], board[n-x]} and OPENCHAR in {board[x], board[n-x]}:
                b_list[x], b_list[n-x] = PROTECTEDCHAR, PROTECTEDCHAR
            elif BLOCKCHAR in {board[x], board[n-x]} and PROTECTEDCHAR in {board[x], board[n-x]}:
                return board, len(board)
    board = ''. join(b_list)
    return board, board.count(BLOCKCHAR)   
def clean_protect(xword):
    return xword.replace(PROTECTEDCHAR, OPENCHAR)
def illeg(board, width):
    xw = BLOCKCHAR*(width+3) +(BLOCKCHAR*2).join([board[p:p+width] for p in range(0, len(board), width)]) +BLOCKCHAR*(width+3)
    illegRE = "[{}](.?[{}]|[{}].?)[{}]".format(BLOCKCHAR, PROTECTEDCHAR, PROTECTEDCHAR, BLOCKCHAR)
    newH = len(xw) // (width+2)
    for turn in range(2):
        if re.search(illegRE, xw): return True
        xw = transpose(xw, len(xw) // newH)
        newH = len(xw) // newH
    return False    
def block_helper(board, num_of_blocks, height, width):
#    if num_of_blocks == curr_num_of_blocks: return board and num_of_blocks
    xw = BLOCKCHAR*(width+3) +(BLOCKCHAR*2).join([board[p:p+width] for p in range(0, len(board), width)]) +BLOCKCHAR*(width+3)
    illegRE = "[{}](.?[{}]|[{}].?)[{}]".format(BLOCKCHAR, PROTECTEDCHAR, PROTECTEDCHAR, BLOCKCHAR)
    newH = len(xw) // (width+2)
    for turn in range(2):
        if re.search(illegRE, xw): return board, len(board)
        xw = transpose(xw, len(xw) // newH)
        newH = len(xw) // newH
    subRE="[{}]{}(?=[{}])".format(BLOCKCHAR, OPENCHAR, BLOCKCHAR)
    subRE2 ="[{}]{}{}(?=[{}])".format(BLOCKCHAR, OPENCHAR, OPENCHAR, BLOCKCHAR)
    subRE3="[#](-~-|--~|~--|~~-|-~~|~-~)(?=[#])"
    newH = len(xw) // (width + 2)
    for turn in range(2):
        xw = re.sub(subRE, BLOCKCHAR*2, xw)
        xw = re.sub(subRE2, BLOCKCHAR*3, xw)
        xw = re.sub(subRE3, BLOCKCHAR+PROTECTEDCHAR*3, xw)
        xw = transpose(xw, len(xw) // newH)
        newH = len(xw) // newH
    new_board = ''
    for row in range (width+2, len(xw) - (width+2), width+2): 
        new_board += xw[row+1:width+row+1]
    board, x = make_palindrome(board, num_of_blocks, height, width) 
    return new_board, new_board.count(BLOCKCHAR)
def combine(board, new_board):
    nb_list = list(new_board)
    for x in range(len(board)):
        if board[x] not in {BLOCKCHAR, PROTECTEDCHAR, OPENCHAR}:
            nb_list[x] = board[x]
    return ''.join(nb_list)
# def cc_helper(b_list, sp, width): 
#     if sp <0 or sp>= len(b_list): return b_list
#     if (b_list[sp] == OPENCHAR) or (b_list[sp] == PROTECTEDCHAR):
#         b_list[sp] = '?'
#         if sp % width !=0 and sp-1 >= 0: cc_helper(b_list, sp-1, width)
#         if sp not in range(0, width) and sp-width >=0: cc_helper(b_list, sp-width, width)
#         if sp % width != width-1 and sp+1 < len(b_list): cc_helper(b_list, sp+1, width)
#         if sp not in range(len(b_list)-width, len(b_list)) and sp+width < len(b_list): cc_helper(b_list, sp+width, width)
#     return b_list
# def check_connectivity(board,x, numberblocks, height, width):
#     if x > numberblocks or board.count(OPENCHAR)==0:
#         return True
#     count, start_pos = 0, 0 
#     while start_pos < len(board) and board[start_pos] == BLOCKCHAR: start_pos += 1
#     board_list = list(board)
#     temp_board = ''.join(cc_helper(board_list, start_pos, width))
#     count = len([x for x in range(len(temp_board)) if temp_board[x] == '?'])
#     count2 = board.count(OPENCHAR) + board.count(PROTECTEDCHAR)
#     return count == count2
def cc(board, height, width, sp, used_pos):
    if (board[sp] == OPENCHAR) or (board[sp] == PROTECTEDCHAR) and sp!=used_pos:
        used_pos.add(sp)
        if sp % width !=0 and sp-1 >= 0: cc(board, height, width, sp-1)
        if sp not in range(0, width) and sp-width >=0: cc(board, height, width, sp-width)
        if sp % width != width-1 and sp+1 < len(board): cc(board, sp+1, width)
        if sp not in range(len(board)-width, len(board)) and sp+width < len(board): cc(board, sp+width, width)
    return used_pos
def area_fill(board, sp, width): 
    dirs = [-1, width, 1, -1*width]
    if sp < 0 or sp >= len(board): return board
    if board[sp] in {OPENCHAR, PROTECTEDCHAR}:
        board = board[0:sp] + '?' + board[sp+1:]
    for d in dirs:
        if d == -1 and sp % width == 0: continue #left edge
        if d == 1 and sp+1 % width == 0: continue #right edge
        board = area_fill(board, sp+d, width)
    return board
def corners(board, blocks, height, width):
    for m in range(len(board)):
        row = m // width
        col = m % width
        if ((col < width - 1 and board[m+1] == BLOCKCHAR ) or (col > 0 and board[m-1] == BLOCKCHAR)) and ((row < height -1 and board[m+width] == BLOCKCHAR) or (row > 0 and board[m-width] == BLOCKCHAR)):
            board = area_fill(board, m, width)
    return board

def add_helper(board, number_of_blocks, height, width, x, pos_list):
    if x == number_of_blocks: return board, x
    # print ('pos list is:', pos_list)
    # display (board, height, width)
    if len(pos_list) == 0: return board,x
    #pick = random.randint(0, len(pos_list)-1)
    for pick in range(len(pos_list)):
        picked_pos = pos_list[pick]
        #pos_list = pos_list[0:pick] + pos_list[pick+1:]
        board = board[0:picked_pos] + BLOCKCHAR + board[picked_pos+1:]
        new_board, x = block_helper(board, number_of_blocks, height, width)
        # print ("New board", x)
        # display(new_board, height, width)
        if x > number_of_blocks:
            board = board[0:picked_pos] + OPENCHAR + board[picked_pos+1:]
            x = board.count(BLOCKCHAR)
        elif illeg(board,width) == True:
            board = board[0:picked_pos] + OPENCHAR + board[picked_pos+1:]
            x = board.count(BLOCKCHAR)           # new_board, x = make_palindrome(new_board, number_of_blocks, height, width)
        else: board = new_board
        npos_list = [z for z in pos_list if board[z] == OPENCHAR]
        # board, x = make_palindrome(board, number_of_blocks, height, width) 
        board, x = make_palindrome(board, number_of_blocks, height, width)
    return add_helper(board, number_of_blocks, height, width, x, npos_list)

def add_blocked_squares(board, number_of_blocks, height, width):
    temp_list = []
    for smth in board:
        if smth != BLOCKCHAR and smth != OPENCHAR: temp_list.append(PROTECTEDCHAR)
        else: temp_list.append(smth)
    if height*width % 2 == 1 and number_of_blocks % 2 == 1: temp_list[len(board) // 2]= BLOCKCHAR
    elif height*width % 2 == 1 and number_of_blocks % 2 == 0: temp_list[len(board) // 2]= PROTECTEDCHAR
    new_board = ''.join(temp_list)
    new_board, x = block_helper(new_board, number_of_blocks, height, width) #this is the issue
    if x >= number_of_blocks: 
        board= combine(board, new_board)
        return board
    new_board, x = make_palindrome(new_board, number_of_blocks, height, width)
    if x >= number_of_blocks: 
        board= combine(board, new_board)
        return board
    #print('after added words:')
    #display(new_board, height, width)
    pos_list = [z for z in range(len(new_board)) if new_board[z] == OPENCHAR and new_board[len(new_board)-z-1] == OPENCHAR]
    temp_board, x = add_helper(new_board, number_of_blocks, height, width, x, pos_list)
    temp_board, x = block_helper(temp_board, number_of_blocks, height, width)
    if x == number_of_blocks:
        board = combine(board, temp_board)
        return board
    # temp_board = areafill(board, height, width, number_of_blocks)
    display(temp_board, height, width)
    while len(cc(temp_board, height, width, board.find(OPENCHAR), set())) != board.count(OPENCHAR) +board.count(PROTECTEDCHAR) or x !=number_of_blocks or illeg(board,width) ==True: 
         pos_list = [z for z in range(len(new_board)) if new_board[z] == OPENCHAR and new_board[len(new_board)-z-1] == OPENCHAR]
         temp_board, x = add_helper(new_board, number_of_blocks, height, width, x, pos_list)
         temp_board, x = block_helper(temp_board, number_of_blocks, height, width)
        #  temp_board = areafill(board, height, width, number_of_blocks)    
    return board
def main():
    number_of_blocks, height, width, prefilled_words, dict_seen = 0,4,4,[], False
    for arg in args:
        arg = arg.upper()
        # if os.path.isfile(arg): 
        #     dict_lines = open(arg, 'r').read().splitlines()
        #     dict_seen = True
        #     continue
        if re.search(r'^\d+$', arg):
            number_of_blocks = int(arg)
        elif re.search(r'^\d+X\d+$', arg, re.I):
            x = arg.lower().index('x')
            height = int(arg[:x])
            width = int(arg[x+1:])
        elif re.search(r'^\w\d+X\d+.+', arg, re.I):
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
    # if not dict_seen: exit('input args are not valid')
    # print(prefilled_words)
    # print(display(initialize(prefilled_words, height, width), height, width))
    size = height*width
    board = OPENCHAR*size
    if number_of_blocks == size:
        board = BLOCKCHAR*size
        display(board, height, width)
    else:
        board = initialize(prefilled_words, height, width)
        if board.count(BLOCKCHAR) == number_of_blocks: display(board, height, width)
        else:
            # display(board, height, width)
            board = add_blocked_squares(board, number_of_blocks, height, width)
            board = clean_protect(board)
            # print(number_of_blocks, board.count(BLOCKCHAR))
            display(board, height, width)
if __name__ == '__main__': 
    main()
#Simrith Ranjan, 5, 2023