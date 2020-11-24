import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype = float)
y = np.array(([92], [86], [89]), dtype = float)

X = X/np.amax(X, axis=0)
y = y /100

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def derivatives_sigmoid(x):
    return x * (1 - x)

epoch = 7000
lr = 0.1

inputlayer_neurons = 2
hiddenlayer_neurons = 3
output_neurons = 1

