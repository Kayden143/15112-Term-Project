import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image

#This contains the code for collecting and using items

class Potion():
    def __init__(self, type, color, number):
        self.type = type
        self.color = color
        self.number = number

    def __repr__ (self):
        return f'{self.type, self.color, self.number}'

    def drink(self):
        if self.number > 0:
            self.number -= 1
            return self.type
        else:
            print("No potions remaining")
            return False

    def throw(self):
        if self.number > 0:
            self.number -= 1
            return self.type
        else:
            print("No potions remaining")
            return False

class healthPotion(Potion):
    def __init__(self):
        self.type = "health"
        self.color = "red"
        self.number = 2
    
    def drink(self, app):
        if super().drink() != False:
            app.p1.health = app.p1.maxHealth


    def throw(self, app, x, y):
        if app.p1.x == x and app.p1.y == y:
            app.p1.health = app.p1.maxHealth
        elif (x, y) in app.enemyLocations:
            pass

def createItems(app):
    for item in range(3):
        starCell = rm.sample(sorted(app.openSquares), 1)[0]
        starTile = rm.sample(app.openSquares[starCell], 1)[0]
        if starCell in app.itemLocs:
            app.itemLocs[starCell].add(starTile)
        else:
            app.itemLocs[starCell] = {starTile}


def pickupItems(app):
    cellsToPop = set()
    for cell in app.itemLocs:
        tilesToPop = set()
        for tile in app.itemLocs[cell]:
            if app.p1.currCell == cell and app.p1.currTile == tile:
                tilesToPop.add(tile)
                if "health" in app.potionList:
                    app.potionList["health"].number += 1
                    print("potion gained, new total is")
                    print(app.potionList["health"].number)
        for tile in tilesToPop:
            app.itemLocs[cell].remove(tile)
        if len(app.itemLocs[cell]) == 0:
            cellsToPop.add(cell)
    for cell in cellsToPop:
        app.itemLocs.pop(cell)

def drawItems(app, canvas):
    for cell in app.itemLocs:
        for tile in app.itemLocs[cell]:
            if cell == app.p1.currCell:
                tileNumX = tile % app.maxRoomSize
                tileNumY = tile // app.maxRoomSize
                canvas.create_rectangle(app.size * tileNumX, 
                app.size * tileNumY, 
                app.size * (tileNumX + 1), 
                app.size * (tileNumY + 1), fill = "black")






