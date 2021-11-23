import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image
from enemy import *
from items import *
from dungeon import *



class Player():
    def __init__ (self):
        self.maxHealth = 40
        self.health = 40
        self.x = 0
        self.y = 0
        self.currCell = 0
        self.currTile = 0
    
    def __repr__ (self):
        return f'{self.x, self.y}' + "health" + f'self.health'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def __hash__(self):
        return id(self)

def isLegalMove(app, tile, dir):
    print(app.openConnections[app.p1.currCell])
    #  and ((app.p1.currCell % app.maxRoomSize
    #  != app.maxRoomSize - 1 and nextCell % app.maxRoomSize != 0 ) and (app.p1.currCell % app.maxRoomSize
    #  != 0 and nextCell % app.maxRoomSize != app.maxRoomSize - 1)))
    if tile in app.openSquares[app.p1.currCell]:
        return True
    elif (tile in app.openConnections[app.p1.currCell] or tile % app.maxRoomSize == app.maxRoomSize - 1 or 
    tile % app.maxRoomSize == 0 or tile + app.maxRoomSize > app.maxRoomSize ** 2 or tile - app.maxRoomSize < 0):
        print("entered")
        if (dir == "left" and tile % app.maxRoomSize == app.maxRoomSize - 1 and 
        (app.p1.currCell - 1) in app.openConnections and (app.p1.currTile + app.maxRoomSize - 1) in 
        app.openConnections[app.p1.currCell - 1]):
            app.p1.currCell -= 1
            app.p1.currTile += (app.maxRoomSize - 1)
        elif (dir == "left" and 
        (((app.p1.currCell - 1) in app.openConnections and (app.p1.currTile + app.maxRoomSize - 1) in 
        app.openConnections[app.p1.currCell - 1]) or (app.p1.currTile - 1) in app.openConnections[app.p1.currCell])):
            app.p1.currTile -= 1
        elif (dir == "right" and tile % app.maxRoomSize == 0 and 
        (app.p1.currCell + 1) in app.openConnections and (app.p1.currTile - app.p1.currTile % app.maxRoomSize) in 
        app.openConnections[app.p1.currCell + 1]):
            app.p1.currCell += 1
            app.p1.currTile -= app.p1.currTile % app.maxRoomSize
        elif (dir == "right" and 
        (((app.p1.currCell + 1) in app.openConnections and (app.p1.currTile - app.p1.currTile % app.maxRoomSize) in 
        app.openConnections[app.p1.currCell + 1]) or (app.p1.currTile + 1) in app.openConnections[app.p1.currCell])):
            app.p1.currTile += 1
        elif (dir == "down" and tile + app.maxRoomSize > app.maxRoomSize ** 2 + app.maxRoomSize and 
        (app.p1.currCell + app.numRooms) in app.openConnections and (app.p1.currTile % app.maxRoomSize) in 
        app.openConnections[app.p1.currCell + app.numRooms]):
            app.p1.currCell += app.numRooms
            app.p1.currTile -= app.maxRoomSize * (app.maxRoomSize - 1)
        elif (dir == "down" and 
        (((app.p1.currCell + app.numRooms) in app.openConnections and (app.p1.currTile % app.maxRoomSize) in 
        app.openConnections[app.p1.currCell + app.numRooms]) or (app.p1.currTile + app.maxRoomSize) in app.openConnections[app.p1.currCell])):
            app.p1.currTile += app.maxRoomSize
        elif (dir == "up" and tile - app.maxRoomSize < 0 and 
        (app.p1.currCell - app.numRooms) in app.openConnections and (app.p1.currTile + app.maxRoomSize**2 - app.maxRoomSize) in 
        app.openConnections[app.p1.currCell - app.numRooms]):
            app.p1.currCell -= app.numRooms
            app.p1.currTile += app.maxRoomSize * (app.maxRoomSize - 1)
        elif (dir == "up" and 
        (((app.p1.currCell - app.numRooms) in app.openConnections and (app.p1.currTile + app.maxRoomSize**2 - app.maxRoomSize) in 
        app.openConnections[app.p1.currCell - app.numRooms]) or (app.p1.currTile - app.maxRoomSize) in app.openConnections[app.p1.currCell])):
            app.p1.currTile -= app.maxRoomSize
        return None
        # elif dir == "down" and tile > app.maxRoomSize ** 2:
        #     app.p1.currCell += app.numRooms
        #     app.p1.currTile -= app.maxRoomSize - 1
        # elif dir == "up" and tile < 0:
        #     app.p1.currCell -= app.numRooms
        #     app.p1.currTile -= app.maxRoomSize - 1
    print("failed")

def updatePlayerLocation(app, left, right, down, up):
    oldTile = app.p1.currTile
    dir = ""
    if left:
        newTile = app.p1.currTile - 1
        dir = "left"
    if right:
        newTile = app.p1.currTile + 1
        dir = "right"
    if down:
        newTile = app.p1.currTile + app.maxRoomSize
        dir = "down"
    if up:
        newTile = app.p1.currTile - app.maxRoomSize
        dir = "up"
    # nTile = fight(app, newTile)
    # if nTile != None:
    #     nTile.health -= 5
    #     if nTile.health <= 0:
    #         app.enemies.remove(nTile)
    #         app.playerTurn, app.enemyTurn = False, True
    legal = isLegalMove(app, newTile, dir)
    print(legal)
    if legal == False:
        app.playerTurn = True
    elif legal == None:
        pass
    else:
        app.p1.currTile = newTile
        # app.playerTurn, app.enemyTurn = False, True
    print(app.openConnections[app.p1.currCell])
    print(app.p1.currCell, app.p1.currTile)

def fight(app, x, y):
    for enemy in app.enemies:
        if (x, y) == (enemy.x, enemy.y):
            return enemy

def playerStart(app):
    app.p1.currCell = rm.sample(sorted(app.openSquares), 1)[0]
    app.p1.currTile = rm.sample(app.openSquares[app.p1.currCell], 1)[0]
    print(app.p1.currCell, app.p1.currTile)

# def drawPlayer(app, canvas):
#     tileNumX = app.p1.currTile % app.maxRoomSize
#     tileNumY = app.p1.currTile // app.maxRoomSize
#     canvas.create_rectangle(app.size * (tileNumX + app.maxRoomSize * (app.p1.currCell % app.numRooms)), 
#     app.size * (tileNumY + app.maxRoomSize * (app.p1.currCell // app.numRooms)), 
#     app.size * (tileNumX + 1 + app.maxRoomSize * (app.p1.currCell % app.numRooms)), 
#     app.size * (tileNumY + 1 + app.maxRoomSize * (app.p1.currCell // app.numRooms)), fill = "green")

def drawPlayer(app, canvas):
    tileNumX = app.p1.currTile % app.maxRoomSize
    tileNumY = app.p1.currTile // app.maxRoomSize
    canvas.create_rectangle(app.size * tileNumX, 
        app.size * tileNumY, 
        app.size * (tileNumX + 1), 
        app.size * (tileNumY + 1), fill = "green")