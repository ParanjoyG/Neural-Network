import pygame
import nn
import numpy as np
from save_filter import Save_filter

and_brain = nn.Network([2,2,1])
gate = "demonstration"

and_training_set = [{'inputs': [0,0], 'outputs' : [0]},
                {'inputs': [1,1], 'outputs' : [0]}, 
                {'inputs': [1,0], 'outputs' : [1]},
                {'inputs': [0,1], 'outputs' : [1]}]

or_brain = nn.Network([2,2,1])

or_training_set = [{'inputs': [0,0], 'outputs' : [0]},
                {'inputs': [1,1], 'outputs' : [0]}, 
                {'inputs': [1,0], 'outputs' : [1]},
                {'inputs': [0,1], 'outputs' : [1]}]

def train_and () :
    for x in range (100) :
        np.random.shuffle(and_training_set)
        for data in and_training_set :
            and_brain.train(data['inputs'], data['outputs'])

def train_or () :
    for x in range (100) :
        np.random.shuffle(or_training_set)
        for data in or_training_set :
            or_brain.train(data['inputs'], data['outputs'])

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
fs = Save_filter()

filter = fs.create_array(SCREEN_WIDTH, SCREEN_HEIGHT)

running  = True
x = 0

while running :

    #screen.fill ((255,255,255))
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                pygame.image.save(screen.copy(), f'images/{gate}/output_{x}.png')
                x += 1

    pxarray = pygame.PixelArray(screen)

    train_and()
    train_or()

    for x in range(SCREEN_WIDTH) :
        for y in range(SCREEN_HEIGHT) :
            a = x/SCREEN_WIDTH
            b = y/SCREEN_HEIGHT
            guess = (and_brain.feed_forward([a,b])[0][0])# + or_brain.feed_forward([a,b])[0][0])/2# and_brain.feed_forward([or_brain.feed_forward ([a,b])[0][0],or_brain.feed_forward ([a,b])[0][0]])[0][0]
            filter[x][y] = guess
            color = int(guess*255)
            pxarray[x][y] = (color,color,color)



    pygame.display.update()
