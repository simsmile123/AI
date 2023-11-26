import sys; args = sys.argv[1:]
import re, random

BLOCKCHAR = '#'
OPENCHAR ='-'
PROTECTEDCHAR = '~'
# args = '9x13 18 V0x1Tvs'.split()         a
def initialize(board, prefilled_word_dict, height, width):
    xword = '-'*(height*width)
    # display(xword, height, width) #(word, direction, row, col)
    for package in prefilled_word_dict:
        direct, r, c, word = package
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
def combine(board, new_board):
    nb_list = list(new_board)
    for x in range(len(board)):
        if board[x] not in {BLOCKCHAR, PROTECTEDCHAR, OPENCHAR}:
            nb_list[x] = board[x]
    return ''.join(nb_list)
def cc_helper(b_list, sp, width): 
    if sp <0 or sp>= len(b_list): return b_list
    if (b_list[sp] == OPENCHAR) or (b_list[sp] == PROTECTEDCHAR):
        b_list[sp] = '?'
        if sp % width !=0 and sp-1 >= 0: cc_helper(b_list, sp-1, width)
        if sp not in range(0, width) and sp-width >=0: cc_helper(b_list, sp-width, width)
        if sp % width != width-1 and sp+1 >= len(b_list): cc_helper(b_list, sp+1, width)
        if sp not in range(len(b_list)-width, len(b_list)) and sp+width < len(b_list): cc_helper(b_list, sp+width, width)
    return b_list
def check_connectivity(board,x, numberblocks, height, width):
    if x > numberblocks or board.count(OPENCHAR)==0:
        return True
    count, start_pos = 0, 0 
    while start_pos < len(board) and board[start_pos] == BLOCKCHAR: start_pos += 1
    board_list = list(board)
    temp_board = ''.join(cc_helper(board_list, start_pos, width))
    count = len([x for x in range(len(temp_board)) if temp_board[x] == '?'])
    count2 = board.count(OPENCHAR) + board.count(PROTECTEDCHAR)
    return count == count2
def block_helper(board, num_of_blocks, height, width):
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
    # board = make_palindrome(board, num_of_blocks, height, width) 
    return new_board, new_board.count(BLOCKCHAR)
def combine(board, new_board):
    nb_list = list(new_board)
    for x in range(len(board)):
        if board[x] not in {BLOCKCHAR, PROTECTEDCHAR, OPENCHAR}:
            nb_list[x] = board[x]
    return ''.join(nb_list)
def add_block_helper(board, number_of_blocks, height, width, x, pos_list):
    if x == number_of_blocks: return board, x
    if len(pos_list) == 0: return board, x
    pick = random.randit(0, len(pos_list)-1)
    picked_pos = pos_list[pick]
    pos_list = pos_list[0:pick] + pos_list[pick+1:]
    board = board[0:picked_pos] + BLOCKCHAR + board[picked_pos+1:]
    new_board, x = block_helper(board, number_of_blocks, height, width)
    if x > number_of_blocks:
            board = board[0:picked_pos] + OPENCHAR + board[picked_pos+1:]
            x = board.count(BLOCKCHAR)   
    else:
        new_board, x = make_palindrome(new_board,number_of_blocks, height, width)
        if x > number_of_blocks:
            board = board[0:picked_pos] + OPENCHAR + board[picked_pos+1:]
            x = board.count(BLOCKCHAR)   
        else: board = new_board
    pos_list = [z for z in pos_list if board[z] == OPENCHAR]
    return add_block_helper(board, number_of_blocks, height, width, x, pos_list)
def add_blocked_squares(board, number_of_blocks, height, width):
    temp_list = []
    for smth in board:
        if smth != BLOCKCHAR and smth != OPENCHAR: temp_list.append(PROTECTEDCHAR)
        else: temp_list.append(smth)
    if height*width % 2 == 1 and number_of_blocks % 2 == 1: temp_list[len(board) // 2]= BLOCKCHAR
    elif height*width % 2 == 1 and number_of_blocks % 2 == 0: temp_list[len(board) // 2]= PROTECTEDCHAR
    new_board = ''.join(temp_list)
    new_board, x = block_helper(new_board, number_of_blocks, height, width) #this is the issue
    if x >= number_of_blocks: return combine(board, new_board)
    new_board, x = make_palindrome(new_board, number_of_blocks, height, width)
    if x >= number_of_blocks: return combine(board, new_board)
    #print('after added words:')
    #display(new_board, height, width)
    pos_list = [z for z in range(len(new_board)) if new_board[z] == OPENCHAR and new_board[len(new_board)-z-1] == OPENCHAR]
    temp_board, x = add_block_helper(new_board, number_of_blocks, height, width, x, pos_list)
    temp_board, x = block_helper(temp_board, number_of_blocks, height, width)
    if x == number_of_blocks:
        board = combine(board, temp_board)
        return board
    while check_connectivity(temp_board, x, number_of_blocks, height, width)== False or x !=number_of_blocks: 
         pos_list = [z for z in range(len(new_board)) if new_board[z] == OPENCHAR and new_board[len(new_board)-z-1] == OPENCHAR]
         temp_board, x = add_block_helper(new_board, number_of_blocks, height, width, x, pos_list)
         temp_board, x = block_helper(temp_board, number_of_blocks, height, width)    
    return board
def main():
    inputTest = [r'^(\d+)x(\d+)$', r'^\d+$', r'^(V|H)(\d+)x(\d+)(.+)$']
    height, width, block_count, dict_seen = 4, 4, 0, True
    input_words = []
    for arg in args:
        # if os.path.isfile(arg):
        #     dict_lines = open(arg, 'r').read().splitlines()
        #     dict_seen = True
        #     continue
        for test_num, retest in enumerate(inputTest):
            match = re.search(retest, arg, re.I)
            if not match: continue
            if test_num == 0: height, width = int(match.group (1)), int (match.group (2)) #13, 13
            elif test_num == 1: block_count = int(arg)
            else:
                vpos, hpos, word = int(match.group(2)), int(match.group (3)), match.group(4).upper()
                input_words.append([arg[0].upper(), vpos, hpos, word])
    if not dict_seen: exit("Input args are not valid.")
    size = height * width
    board = OPENCHAR * size
    if block_count == size:
        board = BLOCKCHAR*size
    else:
        board = initialize(board, input_words, height, width)
        display(board, height, width)
        board = add_blocked_squares(board, block_count, height, width) # change each word char to ~, check #s and ~s,
        board = clean_protect(board)
        print(block_count, board.count(BLOCKCHAR))

    print(board)
    display (board, height, width)

if __name__ == '__main__':

    main()
#Simrith Ranjan, 5, 2023
