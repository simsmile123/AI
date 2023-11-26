import random
import pickle
import numpy as np
import math

training_set = []

with open("mnist_train.csv") as f:
    for line in f:
        line = line.strip().split(",")
        x = np.empty((1, 784))
        y = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        y[0,int(line[0])] = 1
        for i in range(1, len(line)):
            x[0, i-1] = int(line[i])/255 
        training_set.append((x, y))
        

# file = open("test_set.pkl", 'wb')
# pickle.dump(test_set, file)
# file.close()

file = open("training_set.pkl", 'rb')
training_set = pickle.load(file)

#Layer Structure
weight_list = [None, 2 * np.random.rand(784, 300) - 1, 2 * np.random.rand(300, 100) - 1, 2 * np.random.rand(100, 10) - 1]
bias_list = [None, 2 * np.random.rand(1, 300) - 1, 2 * np.random.rand(1, 100) - 1, 2 * np.random.rand(1, 10) - 1]

def sigmoid(num):
    return 1/(1 + math.exp(-1 * num))

def p_net(A, x, w_list, b_list):
    new_A = np.vectorize(A)
    a = [x]
    for i in range(1, len(w_list)):
        a.append(new_A(a[i-1] @ w_list[i] + b_list[i]))
    return a[len(w_list) - 1]

NUM_EPOCHS = 100

#Error/Loss Calculation
def testAccuracy(weight_list, bias_list, epoch, data_set):
    numMisclassified = 0
    for point in data_set:
        if np.argmax(p_net(sigmoid, point[0], weight_list, bias_list)) != np.where(point[1] == 1)[1][0]:
            numMisclassified += 1
    print(f"Epoch {epoch}: {numMisclassified/len(data_set)}")
    
#Forward & Backward Prop
def train(w_list, b_list, data_set):
    newSigmoid = np.vectorize(sigmoid)
    testAccuracy(w_list, b_list, 0, data_set)
    for i in range(NUM_EPOCHS):
        for data in data_set:
            x, y = data[0], data[1]
            a, dot, delta = [x], [None], [None] * len(w_list)
            LAMB = 0.1
            N = len(w_list) - 1
            for L in range(1, len(w_list)):
                dot.append((a[L - 1] @ w_list[L]) + b_list[L])
                a.append(newSigmoid(dot[L]))
            delta[N] = (newSigmoid(dot[N]) * (1 - newSigmoid(dot[N]))) * (y - a[N])
            for L in range(N - 1, 0, -1):
                delta[L] = (newSigmoid(dot[L]) * (1 - newSigmoid(dot[L]))) * (delta[L + 1] @ (w_list[L + 1]).T)
            for L in range(1, len(w_list)):
                b_list[L] = b_list[L] + LAMB * delta[L]
                w_list[L] = w_list[L] + LAMB * ((a[L-1]).T @ delta[L])
        file = open("current_net.pkl", 'wb')
        pickle.dump((w_list, b_list), file)
        file.close()
        testAccuracy(w_list, b_list, i+1, data_set)
    return (w_list, b_list)


weight_list, bias_list = train(weight_list, bias_list, training_set)

# file = open("current_net.pkl", 'rb')
# weight_list, bias_list = pickle.load(file)


