import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image
from enemy import *



class Player():
    def __init__ (self):
        self.health = 20
        self.x = 0
        self.y = 0
    
    def __repr__ (self):
        return f'{self.x, self.y}' + "health" + f'self.health'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def __hash__(self):
        return id(self)

def keyPressed(app, event):
    if app.gameOver or not app.playerTurn:
        return
    app.playerTurn = False
    if event.key == "h":
        app.playerTurn = True
        app.p1.health += 30
        app.playerTurn, app.enemyTurn = False, True
        updatePlayerLocation(app, False, False, False, False)
    if event.key == "w":
        app.playerTurn, app.enemyTurn = False, True
        updatePlayerLocation(app, False, False, False, False)
    if event.key == "Right":
        app.playerTurn, app.enemyTurn = False, True
        updatePlayerLocation(app, False, True, False, False)
    if event.key == "Left":
        app.playerTurn, app.enemyTurn = False, True
        updatePlayerLocation(app, True, False, False, False)
    if event.key == "Up":
        app.playerTurn, app.enemyTurn = False, True
        updatePlayerLocation(app, False, False, False, True)
    if event.key == "Down":
        app.playerTurn, app.enemyTurn = False, True
        updatePlayerLocation(app, False, False, True, False)

def updatePlayerLocation(app, left, right, down, up):
    newX = app.p1.x
    newY = app.p1.y
    if left:
        newX = app.p1.x - 1
    if right:
        newX = app.p1.x + 1
    if down:
        newY = app.p1.y + 1
    if up:
        newY = app.p1.y - 1
    nTile = fight(app, newX, newY)
    if nTile != None:
        nTile.health -= 5
        if nTile.health <= 0:
            print(nTile)
            app.enemies.remove(nTile)
    else:
        app.p1.x = newX
        app.p1.y = newY

def fight(app, x, y):
    for enemy in app.enemies:
        if (x, y) == (enemy.x, enemy.y):
            print(enemy)
            return enemy

def drawPlayer(app, canvas):
    canvas.create_rectangle(app.p1.x * app.size, app.p1.y * app.size, (app.p1.x + 1) * app.size, (app.p1.y + 1) * app.size, fill = "red")
