#!/usr/bin/python

'''
-----------------------------------
Capture Trajectory Demonstrations 
from a Pointer Device

Usage:
    1- run the file
    2- press mouse left-button and hold
    3- start drawing
    4- release mouse left-button to stop
    5- program shows the captured data
    6- use terminal to save data


Author: Reza Ahmadzadeh, 2020
-----------------------------------
'''

import numpy as np
import pygame 
from scipy.interpolate import interp1d, InterpolatedUnivariateSpline
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# variables 
W = 400
H = 400
r = 2
rate = 100 # recording rate
bgColor = pygame.Color("White")
fgColor = pygame.Color("Black")
X = []
Y = []
Np = 100 # number of points to be resampled uniformly


def save_data(X,Y):
    fname = input('Enter a filename (e.g. data.txt, ENTER to exit):')
    if fname == '':
        print("Data was not saved.")
        return False
    else:
        try:
            with open(fname, 'wb') as f:
                #np.savetxt(f,np.column_stack((np.array(X),np.array(Y))))
                np.savetxt(f,np.column_stack((X,Y)))
                print("data saved.")
        except IOError:
            print("Error in saving data")
    #f.close()
    
    
def draw_result(X,Y):
    print("Data can be saved after closing the plot.")
    print("Number of resampling points: "+str(Np))
    t = np.linspace(0,1,len(X))
    tt = np.linspace(0,1,Np)
    print(len(t))
    fx = interp1d(t,np.array(X), kind = 'cubic')
    fy = interp1d(t,np.array(Y), kind = 'cubic')
    fxu = InterpolatedUnivariateSpline(t, np.array(X))
    fyu = InterpolatedUnivariateSpline(t, np.array(Y))
    plt.figure()
    plt.gca().invert_yaxis()
    plt.plot(X,Y,'.--',label="demonstration")
    plt.plot(fx(tt),fy(tt),label="1D Interpolate")
    plt.plot(fxu(tt),fyu(tt),label="Univariate Spline")
    plt.title("captured raw and smoothed demonstration")
    plt.xlabel("x")
    plt.ylabel("inverted y")
    plt.show()
    save_data(fx(tt),fy(tt))

def main():
    pygame.init()
    screen = pygame.display.set_mode((W,H))
    screen.fill(bgColor)
    pygame.display.set_caption("Draw a demonstration using your pointer devices")
    pygame.draw.rect(screen, bgColor, pygame.Rect((0,0),(W,H)))
    clock = pygame.time.Clock()
    press = False    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        (x,y) = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed() == (1,0,0):
            # record if in drawing mode
            X.append(x)
            Y.append(y)
            pygame.draw.circle(screen, fgColor, (x,y), r)
            
        if event.type == pygame.MOUSEBUTTONUP:
            press == False
            print("Number of points captured: " +str(len(X)))
            print("Plotting the captured demonstratio ...")
            draw_result(X,Y)
            running = False
            
        pygame.display.flip()
        pygame.display.update()
        clock.tick(rate)
        
if __name__ == "__main__":
    main()
    
