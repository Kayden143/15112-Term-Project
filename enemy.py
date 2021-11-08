import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image
from player import *

class Rat():
    def __init__(self, x, y):
        self.health = 5
        self.damage = 2
        self.x = x
        self.y = y

    def __repr__(self):
        return(f'{self.x, self.y, self.health}' + "rat")

    # def __eq__(self, other):
    #     if self.x == other.x and self.y == other.y:
    #         return True
    #     return False
    
    # def __hash__(self):
    #     return id(self)

def keyPressed(app, event):
    if event.key == "e":
        print("hello")
        #createEnemy(app)

def moveEnemy(app):
    for enemy in app.enemies:
        xDist = enemy.x - app.p1.x
        yDist = enemy.y - app.p1.y
        newX = 0
        newY = 0
        if abs(xDist) > abs(yDist):
            if xDist < 0:
                newX = 1
            else:
                newX = -1
            pass
        else:
            if yDist < 0:
                newY = 1
            else:
                newY = -1
        nTile = fight(app, enemy.x + newX, enemy.y + newY, enemy)
        if nTile != None:
            app.p1.health -= nTile.damage
            if app.p1.health <= 0:
                app.gameOver = True
            print(app.p1.health)
        else:
            if tuple([enemy.x + newX, enemy.y + newY]) not in app.enemyLocs:
                enemy.x += newX
                enemy.y += newY
                app.enemyLocs.add(tuple([enemy.x, enemy.y]))
                app.enemyLocs.remove(tuple([enemy.x - newX, enemy.y - newY]))
            else:
                if newY != 0:
                    if xDist < 0:
                        newX = 1
                        newY = 0
                    elif xDist > 0:
                        newX = -1
                        newY = 0
                    pass
                else:
                    if yDist < 0:
                        newY = 1
                        newX = 0
                    elif yDist > 0:
                        newY = -1
                        newX = 0
                if tuple([enemy.x + newX, enemy.y + newY]) not in app.enemyLocs:
                    enemy.x += newX
                    enemy.y += newY
                    app.enemyLocs.add(tuple([enemy.x, enemy.y]))
                    app.enemyLocs.remove(tuple([enemy.x - newX, enemy.y - newY]))

def createEnemy(app):
    if app.turnCounter % 10 == 0 and app.turnCounter != 0:
        app.enemies.add(Rat(20, 20))

def kill(app, enemy):
    if enemy.health <= 0:
        app.enemies.remove(enemy)

def fight(app, x, y, enemy):
    if (x, y) == (app.p1.x, app.p1.y):
        return enemy

def drawEnemies(app, canvas):
    for enemy in app.enemies:
        canvas.create_rectangle(enemy.x * app.size, enemy.y * app.size, (enemy.x + 1) * app.size, (enemy.y + 1) * app.size, fill = "orange")
