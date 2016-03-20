#!/usr/bin/python
#Find the princess!
#The princess will be in one of the four corners of an m by m grid.

import math

def displayPathtoPrincess(n,grid):
    #print all the moves here

    #The princess's coordinates:
    prinPosY = 0
    prinPosX = 0
    i = 0
    for row in grid:
        pPos = row.find("p")
        if pPos > -1:
            prinPosY = i
            prinPosX = pPos
        i += 1
    #DEBUG:
        #print("PRINCESS: %s,%s" % (str(prinPosX), str(prinPosY)))
    #the hero's X and Y are equal to the floor of n / 2.
    heroPosX = math.floor(n/2)
    heroPosY = heroPosX
    #DEBUG:
        #print("HERO: %s,%s" % (str(heroPosX), str(heroPosY)))
    #Compare coordinates to determine which way to move.
    #Alternate between moving on X and moving on Y to step
    #along the hypotenuse of the right triangle created
    #between the grid's bounds, the hero and the princess.
    #Your hero will make n-1 steps.
    
    #Step-by-step, go from your current position to 0,0 using
    #the princess as the origin point.
    heroToZeroX = heroPosX - prinPosX
    heroToZeroY = heroPosY - prinPosY

    for i in range(n - 1):
        #DEBUG:
            #print("DISTANCE: %s,%s" % (str(heroToZeroX), str(heroToZeroY)))
        if i%2 == 0:
            if heroToZeroX > 0:
                heroToZeroX -= 1
                print("LEFT")
            elif heroToZeroX < 0:
                heroToZeroX += 1
                print("RIGHT")
        else:
            if heroToZeroY > 0:
                heroToZeroY -= 1
                print("UP")
            elif heroToZeroY < 0:
                heroToZeroY += 1
                print("DOWN")
    
    
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
