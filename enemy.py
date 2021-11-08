import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image
from player import *
from time import sleep

class Rat():
    def __init__(self, x, y):
        self.health = 5
        self.damage = 2
        self.x = x
        self.y = y

    def __repr__(self):
        return(f'{self.x, self.y, self.health}' + "rat")

def keyPressed(app, event):
    if event.key == "e":
        print("hello")
        #createEnemy(app)

def findBestPath(app, px, py, dx, dy, path):
    print(app.p1.x, app.p1.y, path[-1][0] + dx, path[-1][1] + dy)
    sleep(0.1)
    print(path)
    if app.bestPath == True:
        return
    if path == None:
        path = []
    if path[-1][0] == app.p1.x and path[-1][1] == app.p1.y:
        app.bestPath = True
        return path
    elif px + dx < 0 or px >= len(app.grid) or py < 0 or py >= len(app.grid) or tuple([px + dx, py + dy]) in path:
        return None
    else:
        for nextCoor in [(-1, 0), (0,-1), (1, 0), (0, 1)]:
            path.append(tuple([px + nextCoor[0], py + nextCoor[1]]))
            solution = findBestPath(app, path[-1][0], path[-1][1], nextCoor[0], nextCoor[1], path)
            if solution != None:
                app.bestPath = True
                return solution
            path.pop()

def findNearestHole(app, x, y, side, nMove):
    prevX, prevY = x, y
    upOrRight = 0
    downOrLeft = 0
    if side == "hori":
        while tuple([x + nMove, y]) in app.wallList or tuple([x + nMove, y]) in app.enemyLocs:
            y += 1
            downOrLeft += 1
        y = prevY
        while tuple([x + nMove, y]) in app.wallList or tuple([x + nMove, y]) in app.enemyLocs:
            y -= 1
            upOrRight += 1
        if upOrRight == downOrLeft:
            if abs(app.p1.y - abs(prevY + downOrLeft)) > abs(app.p1.y - abs(prevY - upOrRight)):
                return -1
            else:
                return 1
        if downOrLeft > upOrRight:
            return -1
        else:
            return 1
    else:
        while tuple([x, y + nMove]) in app.wallList or tuple([x, y + nMove]) in app.enemyLocs:
            x += 1
            upOrRight += 1
        x = prevX
        while tuple([x, y + nMove]) in app.wallList or tuple([x, y + nMove]) in app.enemyLocs:
            x -= 1
            downOrLeft += 1
        if downOrLeft == upOrRight:
            if abs(app.p1.x - abs(prevX + downOrLeft)) > abs(app.p1.x - abs(prevX - upOrRight)):
                return 1
            else:
                return -1
        if downOrLeft > upOrRight:
            return 1
        else:
            return -1

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
            if (tuple([enemy.x + newX, enemy.y + newY]) not in app.enemyLocs and 
            tuple([enemy.x + newX, enemy.y + newY]) not in app.wallList):
                enemy.x += newX
                enemy.y += newY
                app.enemyLocs.add(tuple([enemy.x, enemy.y]))
                try:
                    app.enemyLocs.remove(tuple([enemy.x - newX, enemy.y - newY]))
                except:
                    return
            else:
                if newX != 0:
                    newY = findNearestHole(app, enemy.x, enemy.y, "hori", newX)
                    newX = 0
                else:
                    newX = findNearestHole(app, enemy.x, enemy.y, False, newY)
                    newY = 0
                enemy.x += newX
                enemy.y += newY
                app.enemyLocs.add(tuple([enemy.x, enemy.y]))
                try:
                    app.enemyLocs.remove(tuple([enemy.x - newX, enemy.y - newY]))
                except:
                    return

def createEnemy(app):
    if app.turnCounter % 10 == 0 and app.turnCounter != 0:
        app.enemies.add(Rat(10, 10))

def kill(app, enemy):
    if enemy.health <= 0:
        app.enemies.remove(enemy)

def fight(app, x, y, enemy):
    if (x, y) == (app.p1.x, app.p1.y):
        return enemy

def drawEnemies(app, canvas):
    for enemy in app.enemies:
        canvas.create_rectangle(enemy.x * app.size, enemy.y * app.size, (enemy.x + 1) * app.size, (enemy.y + 1) * app.size, fill = "orange")
