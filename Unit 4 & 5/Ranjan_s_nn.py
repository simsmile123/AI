import sys; args = sys.argv[1:]
file = open(args[0], 'r')
import math

def transfer(t_funct, input):
    # print(t_funct)
    if t_funct == "T1":
        return input
    if t_funct == "T2":
        if input <= 0:
            return 0
        else:
            return input
    if t_funct == "T3":
            print(input)
            # return [1/(1+math.e**(-1*int(x))) for x in input]
    if t_funct == "T4":
        return [-1 + 2/(1+math.e**(-1*int(x))) for x in input]
def dot_product(input, weightline):
    bum = []
    x = 0
    for i in input: # 5 2 3 1 4 len(inputs)
        for w in weightline[x]: # first time its 3 groups of 5 then 2 groups of 3 the 2 groups of 1; 5 8 2 0 1 2 2 2 3 7 5 4 4 3 2
                bum.append(w*int(i))     
    x+=1
    return bum

def evaluate(file, input_vals, t_funct):
    #put stuf in file into list with lists
    # with open(f"{file}", 'r') as infile:
    weights = [v.replace('\n',"") for v in file.readlines()]
    # print(weights)
    counter = 0
    # counter2 = 5
    while counter < (len(weights) - 1):
        print('x')
        input_vals = transfer(t_funct, dot_product(input_vals, weights[counter]))
        counter += 1
    # print(input_vals)
    input_vals = dot_product(input_vals, weights[len(weights)])
    return input_vals

    #input_vals = input_vals.append(dot_product(input_vals, weights[len(weights)], counter2))
    # input_vals = transfer(t_funct, dot_product(input_vals))
    
#def make(weigh):
#    for line in 
def main():
    inputs, t_funct, transfer_found = [], 'T1', False
    #weights = make("weights.txt")
    for arg in args[1:]:
        if not transfer_found:
            t_funct, transfer_found = arg, True
        else:
            inputs.append(float(arg))
    li = (evaluate(file, inputs, t_funct))
    for x in li:
        print(x, end ='')
if __name__ == '__main__': main()
# Simrith Ranjan, Period 5, 2023