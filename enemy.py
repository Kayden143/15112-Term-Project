import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image
from time import sleep

from items import drawItems

#This deals with enemy stats and movement/tracking towards the player

class Enemy():
    def __init__(self, damage):
        self.health = 10
        self.maxHealth = 10
        self.damage = damage
        self.currTile = 0
        self.currCell = 0
        self.targetTile = 0
        self.targetCell = 0
        self.path = None

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

def findCellPathToPlayer(app, enemy, startCell = None, path = None, usedConns = None):
    if startCell == None:
        startCell = enemy.currCell
        path = [enemy.currCell]
        usedConns = set()
    if startCell == app.p1.currCell:
        return path
    else:
        if app.p1.currCell < app.numRooms**2 // 2:
            for con in sorted(list(app.connections)):
                if con in usedConns:
                    continue
                elif startCell == con[0]:
                    path.append(con[1])
                    usedConns.add(con)
                    sol = findCellPathToPlayer(app, enemy, con[1], path, usedConns)
                    if sol != None:
                        return sol
                    path.pop()
                elif startCell == con[1]:
                    path.append(con[0])
                    usedConns.add(con)
                    sol = findCellPathToPlayer(app, enemy, con[0], path, usedConns)
                    if sol != None:
                        return sol
                    path.pop()
        else:
            for con in reversed(sorted(list(app.connections))):
                if con in usedConns:
                    continue
                elif startCell == con[0]:
                    path.append(con[1])
                    usedConns.add(con)
                    sol = findCellPathToPlayer(app, enemy, con[1], path, usedConns)
                    if sol != None:
                        return sol
                    path.pop()
                elif startCell == con[1]:
                    path.append(con[0])
                    usedConns.add(con)
                    sol = findCellPathToPlayer(app, enemy, con[0], path, usedConns)
                    if sol != None:
                        return sol
                    path.pop()
        return None

def moveEnemyOffScreen(app, enemy, target):
    print(enemy.currCell, enemy.currTile, target, enemy.targetCell, enemy.targetTile)
    if target == enemy.currCell - 1:
        dir = "left"
        for tile in app.openConnections[enemy.currCell]:
            if tile % app.maxRoomSize == 0:
                targetTile = tile
                break
    elif target == enemy.currCell + 1:
        dir = "right"
        for tile in app.openConnections[enemy.currCell]:
            if tile % app.maxRoomSize == app.maxRoomSize - 1:
                targetTile = tile
                break
    elif target == enemy.currCell + app.numRooms:
        dir = "down"
        for tile in app.openConnections[enemy.currCell]:
            if tile // app.maxRoomSize == app.maxRoomSize - 1:
                targetTile = tile
                break
    elif target == enemy.currCell - app.numRooms:
        dir = "up"
        for tile in app.openConnections[enemy.currCell]:
            if tile // app.maxRoomSize == 0:
                targetTile = tile
                break
    xDist = enemy.currTile % app.maxRoomSize - targetTile % app.maxRoomSize
    yDist = enemy.currTile // app.maxRoomSize - targetTile // app.maxRoomSize
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
    elif abs(yDist) > abs(xDist) or (abs(yDist) == abs(xDist) and yDist != 0):
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
    else:
        if dir == "left":
            enemy.currCell -= 1
            enemy.currTile += (app.maxRoomSize - 1)
        elif dir == "right":
            enemy.currCell += 1
            enemy.currTile -= (app.maxRoomSize - 1)
        elif dir == "down":
            enemy.currCell += app.numRooms
            enemy.currTile -= app.maxRoomSize * (app.maxRoomSize - 1)
        elif dir == "up":
            enemy.currCell -= app.numRooms
            enemy.currTile += app.maxRoomSize * (app.maxRoomSize - 1)
        return None, None


def moveEnemy(app):
    for enemy in app.enemies:
        if enemy.currCell != app.p1.currCell:
            if (enemy.currCell == enemy.targetCell and enemy.currTile == enemy.targetTile) or enemy.path == None or enemy.targetCell != app.p1.currCell:
                enemy.path = list()
                enemy.targetCell = app.p1.currCell
                enemy.targetTile = app.p1.currTile
                enemy.path = findCellPathToPlayer(app, enemy)
            nextCell = enemy.path[enemy.path.index(enemy.currCell) + 1]
            newX, newY = moveEnemyOffScreen(app, enemy, nextCell)
            if newX != None:
                enemy.currTile += newX
                enemy.currTile += newY * app.maxRoomSize
        else:
            newX, newY = findBestPath(app, enemy)
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

def drawEnemyHealth(app, canvas):
    canvas.create_rectangle(app.width * 0.75 + app.size // 4, app.size // 4, app.width * 0.75 + 2 * app.size, app.size // 2, fill = "red")
    canvas.create_text(app.width * 0.75 - app.size // 4, app.size // 4, text = str(app.inFight.health) + "/" + str(app.inFight.maxHealth), anchor = "ne")
    canvas.create_rectangle(app.width * 0.75, app.size // 4, app.width * 0.75 + 2 * app.size * (app.inFight.health / app.inFight.maxHealth), app.size // 2, fill = "yellow")