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
        self.damage = 5
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
    if tile in app.openSquares[app.p1.currCell]:
        return True
    elif (tile in app.openConnections[app.p1.currCell] or tile % app.maxRoomSize == app.maxRoomSize - 1 or 
    tile % app.maxRoomSize == 0 or tile + app.maxRoomSize > app.maxRoomSize ** 2 or tile - app.maxRoomSize < 0):
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

def updatePlayerLocation(app, left, right, down, up):
    print(app.p1.currCell)
    app.playerTurn, app.enemyTurn = False, True
    oldTile = app.p1.currTile
    oldCell = app.p1.currCell
    newTile = 0
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
    legal = isLegalMove(app, newTile, dir)
    if legal == False:
        app.playerTurn, app.enemyTurn = True, False
    elif legal == None:
        pass
    else:
        app.p1.currTile = newTile
        app.playerTurn, app.enemyTurn = False, True
    nTile = fight(app)
    if nTile != None:
        nTile.health -= 5
        if nTile.health <= 0:
            app.enemies.remove(nTile)
            app.playerTurn, app.enemyTurn = False, True
        app.p1.currCell, app.p1.currTile = oldCell, oldTile
    if app.p1.currCell == app.goalCell and app.p1.currTile == app.goalTile:
        print("Won!!!!!")
        app.depth += 1
        app.goalCell = 0
        app.goalTile = 0
        app.newCon = True
        app.connectCounter = 0
        app.connectedCells = dict()
        app.connections = set()
        app.conRooms = set()
        app.connectionsNotToRemove = set()
        app.openSquaresNotToRemove = dict()
        app.openConnections = dict()
        app.connectionsToDraw = []
        app.tilesToDraw = set()
        app.roomList, app.openSquares = createDungeon(app)
        connectRooms(app)
        app.oldConns = copy.deepcopy(app.connections)
        app.oldOpenSquares = copy.deepcopy(app.openSquares)
        delRooms(app)
        removeConns(app)
        #Change values in loop to specify number of rooms there will be
        while len(app.connections) != 20 + app.depth:
            app.conRooms = set()
            app.connectionsNotToRemove = set()
            app.openSquaresNotToRemove = dict()
            app.connections = set()
            app.connectCounter = 0
            app.openSquares = copy.deepcopy(app.oldOpenSquares)
            connectRooms(app)
            delRooms(app)
            removeConns(app)
        createConnCoords(app)
        playerStart(app)
        assignGoal(app)
        createItems(app)
        app.enemies = set()
        app.enemies = {Enemy(app.depth + 5), Enemy(app.depth + 5), Enemy(app.depth + 5)}
        for enemy in app.enemies:
            assignEnemy(app, enemy)
            print(enemy.currCell, enemy.currTile)
    pickupItems(app)

def fight(app):
    for enemy in app.enemies:
        if app.p1.currCell == enemy.currCell and app.p1.currTile == enemy.currTile:
            return enemy

def playerStart(app):
    app.p1.currCell = rm.sample(sorted(app.openSquares), 1)[0]
    app.p1.currTile = rm.sample(app.openSquares[app.p1.currCell], 1)[0]

def drawPlayer(app, canvas):
    tileNumX = app.p1.currTile % app.maxRoomSize
    tileNumY = app.p1.currTile // app.maxRoomSize
    canvas.create_rectangle(app.size * tileNumX, 
        app.size * tileNumY, 
        app.size * (tileNumX + 1), 
        app.size * (tileNumY + 1), fill = "green")