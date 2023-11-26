import sys; args = sys.argv[1:]
file = open(args[0], 'r')
import fnmatch
import math

def transfer(t_funct, input):
    if t_funct == "T1":
        return input
    if t_funct == "T2":
        if input <= 0:
            return 0
        else:
            return input
    if t_funct == "T3":
            return [1/(1+math.e**(-x)) for x in input]
    if t_funct == "T4":
        return [-1 + 2/(1+math.e**(-input)) for x in input]
def dot_product(input, weights, stage):
    bum = []
    for i in input:
        for w in (weights // stage):
            bum.append(input[i] * weights[w])
    return bum

def evaluate(file, input_vals, t_funct):
    #put stuf in file into list with lists
    # with open(f"{file}", 'r') as infile:
      weights = [v.replace('\n',"") for v in file.readlines()]
      print(weights)

      counter = 0
      counter2 = 5
      while counter < (len(weights) - 1):
          input_vals = transfer(t_funct, dot_product(input_vals, weights[counter], counter2))
          counter += 1
          counter2 -=2
          print(counter2)
      input_vals = input_vals.append(dot_product(input_vals, weights[len(weights)], counter2))
    # input_vals = transfer(t_funct, dot_product(input_vals))
      return input_vals
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