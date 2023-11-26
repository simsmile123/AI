import numpy as np
import math
import random
import pickle

training_set = []

with open("mnist_train.csv") as f: #this is requirement 2 on your doc as it reads the training set and creates nice structure
    for line in f:
        line = line.strip().split(",")
        x = np.empty((1, 784)) #W LIST AND B LIST
        y = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        y[0,int(line[0])] = 1
        for i in range(1, len(line)):
            x[0, i-1] = int(line[i])/255 
        training_set.append((x, y))
        

file = open("training_set.pkl", 'rb')
training_set = pickle.load(file)
#use numpy cause its easier
bias_list = [None, 2 * np.random.rand(784, 300) - 1, 2 * np.random.rand(300, 100) - 1, 2 * np.random.rand(100, 10) - 1] #step 3, random bias
weight_list = [None, 2 * np.random.rand(1, 300) - 1, 2 * np.random.rand(1, 100) - 1, 2 * np.random.rand(1, 10) - 1] #random weights

def T3(num):
    return 1/(1 + math.exp(-1 * num))

def nn(A, x, w_list, b_list):
    new_A = np.vectorize(A)
    a = [x]
    for i in range(1, len(w_list)):
        a.append(new_A(a[i-1] @ w_list[i] + b_list[i]))
    return a[len(w_list) - 1]

NUM_EPOCHS = 100 

#calc the error
def error_calc(weight_list, bias_list, epoch, data_set):
    num_of_missed = 0
    for point in data_set:
        if np.argmax(nn(T3, point[0], weight_list, bias_list)) != np.where(point[1] == 1)[1][0]:
            num_of_missed += 1
    print(f"Epoch {epoch}: {num_of_missed/len(data_set)}")
    
#instead of a class NN, i just did ff and bp together
def train(w_list, bi_list, data_set):
    newX = np.vectorize(T3)
    error_calc(w_list, bi_list, 0, data_set)
    for i in range(NUM_EPOCHS):
        for data in data_set:
            x, y = data[0], data[1]
            a, dot, delta = [x], [None], [None] * len(w_list)
            LAMB = 0.1
            N = len(w_list) - 1
            for weight in range(1, len(w_list)):
                dot.append((a[weight - 1] @ w_list[L]) + bi_list[L])
                a.append(newX(dot[L]))
            delta[N] = (newX(dot[N]) * (1 - newX(dot[N]))) * (y - a[N])
            for n in range(N - 1, 0, -1):
                delta[n] = (newX(dot[n]) * (1 - newX(dot[n]))) * (delta[n + 1] @ (w_list[n + 1]).T)
            for L in range(1, len(w_list)):
                w_list[L] = w_list[L] + LAMB * ((a[L-1]).T @ delta[L])
                bi_list[L] = bi_list[L] + LAMB * delta[L]
        file = open("current_net.pkl", 'wb')
        pickle.dump((w_list, bi_list), file) #store the lists in a file
        file.close()
        error_calc(w_list, bi_list, i+1, data_set)
    return (w_list,bi_list)


weight_list,bias_list = train(weight_list, bias_list, training_set)