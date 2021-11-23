import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image
from time import sleep

from items import drawItems


class Enemy():
    def __init__(self, damage):
        self.health = 10
        self.damage = damage
        self.currTile = 0
        self.currCell = 0

    def __repr__(self):
        return(f'{self.currCell, self.currTile, self.health}' + "enemy")

def findBestPath(app, enemy):
    xDist = enemy.currTile % app.maxRoomSize - app.p1.currTile % app.maxRoomSize
    yDist = enemy.currTile // app.maxRoomSize - app.p1.currTile // app.maxRoomSize
    if abs(xDist) > abs(yDist):
        if xDist < 0:
            if enemy.currTile + 1 in app.openSquares[enemy.currCell] or enemy.currTile + 1 in app.openConnections[enemy.currCell]:
                return 1, 0
            else:
                if yDist < 0:
                    return 0, 1
                else:
                    return 0, -1
        else:
            if enemy.currTile - 1 in app.openSquares[enemy.currCell] or enemy.currTile - 1 in app.openConnections[enemy.currCell]:
                return -1, 0
            else:
                if yDist < 0:
                    return 0, 1
                else:
                    return 0, -1
    else:
        if yDist < 0:
            if enemy.currTile + app.maxRoomSize in app.openSquares[enemy.currCell] or enemy.currTile + app.maxRoomSize in app.openConnections[enemy.currCell]:
                return 0, 1
            else:
                if xDist < 0:
                    return 1, 0
                else:
                    return -1, 0
        else:
            if enemy.currTile - app.maxRoomSize in app.openSquares[enemy.currCell] or enemy.currTile - app.maxRoomSize in app.openConnections[enemy.currCell]:
                return 0, -1
            else:
                if xDist < 0:
                    return 1, 0
                else:
                    return -1, 0

def moveEnemy(app):
    for enemy in app.enemies:
        if enemy.currCell != app.p1.currCell:
            pass
        else:
            newX, newY = findBestPath(app, enemy)
            print(newX, newY)
            # if abs(xDist) > abs(yDist):
            #     if xDist < 0:
            #         newX = 1
            #         enemy.currTile += 1
            #     else:
            #         newX = -1
            #         enemy.currTile -= 1
            #     pass
            # else:
            #     if yDist < 0:
            #         newY = app.maxRoomSize
            #         enemy.currTile += app.maxRoomSize
            #     else:
            #         newY = -app.maxRoomSize
            #         enemy.currTile -= app.maxRoomSize
            enemy.currTile += newX
            enemy.currTile += newY * app.maxRoomSize
            nTile = fight(app, enemy)
            if nTile != None:
                enemy.currTile -= newX
                enemy.currTile -= newY * app.maxRoomSize
                app.p1.health -= nTile.damage
                if app.p1.health <= 0:
                    app.gameOver = True

def kill(app, enemy):
    if enemy.health <= 0:
        app.enemies.remove(enemy)

def fight(app, enemy):
    if app.p1.currCell == enemy.currCell and app.p1.currTile == enemy.currTile:
        return enemy

def assignEnemy(app, enemy):
    enemy.currCell = rm.sample(sorted(app.openSquares), 1)[0]
    enemy.currTile = rm.sample(app.openSquares[enemy.currCell], 1)[0]
    print(enemy.currCell, enemy.currTile, "enemy")

def drawEnemies(app, canvas):
    for enemy in app.enemies:
        if enemy.currCell == app.p1.currCell:
            tileNumX = enemy.currTile % app.maxRoomSize
            tileNumY = enemy.currTile // app.maxRoomSize
            canvas.create_rectangle(app.size * tileNumX, 
                app.size * tileNumY, 
                app.size * (tileNumX + 1), 
                app.size * (tileNumY + 1), fill = "red")
