import sys; args = sys.argv[1:]
import re, random

BLOCKCHAR = '#'
OPENCHAR ='-'
PROTECTEDCHAR = '~'
# args = '9x13 18 V0x1Tvs'.split()         a
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
def clean_protect(xword):
    return xword.replace(PROTECTEDCHAR, OPENCHAR)
def main():
    number_of_blocks, height, width, prefilled_words, dict_seen = 0,4,4,[], False
    # print(len(args))
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