import nn
import matrix_math as math_
import numpy as np


matrix = math_.Matrix_Math()

brain = nn.Network([2,2,1])

training_set = [{'inputs': [0,0], 'outputs' : [0]},
                {'inputs': [1,1], 'outputs' : [0]}, 
                {'inputs': [1,0], 'outputs' : [1]},
                {'inputs': [0,1], 'outputs' : [1]}]


for x in range (10000) :
    np.random.shuffle(training_set)
    for data in training_set :
        brain.train(data['inputs'], data['outputs'])

#brain.feed_forward([0,0])
print(brain.feed_forward([0,0]))
print(brain.feed_forward([0,1]))
print(brain.feed_forward([1,0]))
print(brain.feed_forward([1,1]))
# print(len(brain.A))
# print(len(brain.weights))