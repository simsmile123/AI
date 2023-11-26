import sys; args = sys.argv[1:]
file = open(args[0], 'r')
import math

def transfer(t_funct, input):
    if t_funct == 'T2': return [x if x > 0 else 0 for x in input]
    elif t_funct == 'T1': return [x for x in input]
    elif t_funct == 'T3': return [1 / (1 + math.e**-x) for x in input]
    elif t_funct == 'T4': return [-1+2/(1+math.e**-x) for x in input]
    else: return 'invalid'
    # if t_funct == "T1":
    #     return input
    # if t_funct == "T2":
    #     if input <= 0:
    #         return 0
    #     else:
    #         return input
    # if t_funct == "T3":
    #         # print(input)
    #     return [1/(1+math.e**(-1*int(x))) for x in input]
    # if t_funct == "T4":
    #     return [-1 + 2/(1+math.e**(-1*int(x))) for x in input]

def dot_product(input, weights, stage):
    # bum = []
    #len(input) = 5 so i want three groups of five multiple first number by input add second by second add third by third
    # for x in input:
    #     for w in weights:
    #         bum.append(input[int(x)] * weights[int(w)])
    # return bum
    return [sum([input[x]*weights[x+s*len(input)] for x in range(len(input))]) for s in range(stage)]

def evaluate(file, input_vals_list, t_funct):
   weights = [v.replace('\n',"") for v in file.readlines()]
   weight_list = []
   for w in weights:
       w = list(map(float, w.split()))
       weight_list.append(w)
   counter = 0
   layers = [len(input_vals_list)]
   while counter < (len(weight_list) - 1):
    #    layers = len(weight_list[counter]) //len(input_vals)
    #    dot = dot_product(input_vals_list,weight_list[counter], layers)
    #    input_vals_list = transfer(t_funct, dot)
       layers.append(len(weight_list[counter])//layers[counter])
       counter +=1
   for layer in range(1, len(layers)):
       input_vals_list = transfer(t_funct, dot_product(input_vals_list, weight_list[layer-1], layers[layer]))
#    input_vals_list = dot_product(input_vals_list, weights[len(weights)-1], len(weight_list[counter]))
#    for x in range(len(input_vals_list)):
#        input_vals_list = [input_vals_list[x]*weight_list[len(weight_list)-1][x]]
   return [input_vals_list[x]*weight_list[len(weight_list)-1][x] for x in range(len(input_vals_list))]
     
def main():
   inputs, t_funct, transfer_found = [], 'T1', False
   for arg in args[1:]:
      if not transfer_found:
         t_funct, transfer_found = arg, True
      else:
         inputs.append(float(arg))
   li =(evaluate(file, inputs, t_funct)) #ff
   for x in li:
      print (x, end=' ') # final outputs
if __name__ == '__main__': main()
# Simrith Ranjan, Period 5, 2023