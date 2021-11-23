import math
import random as rm
from typing import Union
from cmu_112_graphics import *
import sys
from PIL import Image

def createRoom(app, l, w, x, y):
    for length in range(l):
        for width in range(w):
            if length == 0 or length == (l - 1) or width == 0  or width == (w - 1):
                app.wallList.add(tuple([x + length, y + width]))

def drawHealthBar(app, canvas):
    canvas.create_rectangle(app.size, app.size, 8 * app.size, app.size * 2, fill = "red")
    canvas.create_rectangle(app.size, app.size, 8 * app.size * (app.p1.health / app.p1.maxHealth), app.size * 2, fill = "yellow")

def drawDungeon(app, canvas):
    for row in range(len(app.grid)):
        for col in range(len(app.grid[0])):
            canvas.create_rectangle(row * app.size, col * app.size, (row + 1) * app.size, (col + 1) * app.size, fill = app.grid[row][col])
    for wall in app.wallList:
        canvas.create_rectangle(wall[0] * app.size, wall[1]  *app.size, (wall[0] + 1) * app.size, (wall[1] + 1) * app.size, fill = "brown")

def createDungeon(app):
    dungeon = [(["#"] * (app.maxRoomSize**2)) for i in range(app.numRooms**2)]
    roomList = dict()
    openSquares = dict()
    roomNum = 0
    for i in dungeon:
        roomStartL = rm.randint(0, app.maxRoomSize * 0.4)
        roomLen = rm.randint(app.maxRoomSize * 0.8, app.maxRoomSize)
        roomStartH = rm.randint(0, app.maxRoomSize * 0.4)
        roomHt = rm.randint(app.maxRoomSize * 0.8, app.maxRoomSize)
        for l in range(1, roomLen - roomStartL - 1):
            for h in range(1, roomHt - roomStartH - 1):
                i[roomStartL + l + app.maxRoomSize * (roomStartH + h)] = "."
                if roomNum in openSquares:
                    openSquares[roomNum].add(roomStartL + l + app.maxRoomSize * (roomStartH + h))
                else:
                    openSquares[roomNum] = {roomStartL + l + app.maxRoomSize * (roomStartH + h)}
        roomList[roomNum] = i
        roomNum += 1
    return roomList, openSquares

def connectRooms(app):
    fail = False
    for room in app.roomList:
        app.connectedCells[room] = {room}
    while len(app.connectedCells) > 1:
        breakLoop = False
        currCell = rm.sample(sorted(app.connectedCells), 1)
        currCellNum = currCell[0]
        currCell = app.connectedCells[currCell[0]]
        currRoom = rm.sample(currCell, 1)[0]
        randValues = [currRoom + 1, currRoom - 1, currRoom + app.numRooms, currRoom - app.numRooms]
        for val in randValues:
            if (val < 0 or val > app.numRooms**2 or val in currCell or tuple([currRoom, val]) in app.connections or 
            tuple([val, currRoom]) in app.connections or abs(currRoom % app.numRooms - val % app.numRooms) == app.numRooms - 1):
                randValues.remove(val)
        while len(randValues) != 0:
            cRoom = rm.randint(0, len(randValues) - 1)
            for cell in app.connectedCells:
                if randValues[cRoom] in app.connectedCells[cell] :
                    app.connections.add(tuple([currRoom, randValues[cRoom]]))
                    app.connectedCells[currCellNum] = app.connectedCells[currCellNum].union(app.connectedCells[cell])
                    app.connectedCells.pop(cell)
                    breakLoop = True
                    break
            if breakLoop:
                break
            randValues.pop(cRoom)
        app.connectCounter += 1
        if app.connectCounter >= 300:
            break
    for con in app.connections:
        if (abs(con[0] % app.numRooms - con[1] % app.numRooms) == app.numRooms - 1 or
        (con[1], con[0]) in app.connections):
            fail = True
            break
    if len(app.connections) < app.numRooms**2 - 3 or fail:
        app.connections = set()
        app.connectCounter = 0
        fail = False
        connectRooms(app)

def delRooms(app, starRoom = None):
    if starRoom == None:
        starRoom = rm.randint(0, app.numRooms**2 - 1)
    if starRoom in app.conRooms:
        return
    else:
        app.conRooms.add(starRoom)
        app.openSquaresNotToRemove[starRoom] = app.openSquares[starRoom]
        for con in app.connections:
            if starRoom == con[0]:
                app.connectionsNotToRemove.add(con)
                delRooms(app, con[1])
            elif starRoom == con[1]:
                app.connectionsNotToRemove.add(con)
                delRooms(app, con[0])

def removeConns(app):
    app.connections = copy.deepcopy(app.connectionsNotToRemove)
    app.openSquares = copy.deepcopy(app.openSquaresNotToRemove)

def createConnCoords(app):
    for con in app.connections:
        if con[0] not in app.openConnections:
            app.openConnections[con[0]] = set()
        if con[1] not in app.openConnections:
            app.openConnections[con[1]] = set()
        conDir = abs(con[1] - con[0])
        while True:
            conTile = rm.sample(app.openSquares[con[0]], 1)[0]
            if conTile in app.openSquares[con[1]]:
                break
        if conDir == 1:
            tileX = conTile % app.maxRoomSize
            tileY = conTile // app.maxRoomSize
            for i in range(app.maxRoomSize):
                if conTile + i < app.maxRoomSize ** 2 and (conTile + i) // app.maxRoomSize == tileY:
                    app.openConnections[min(con[0], con[1])].add(conTile + i)
                if conTile - i > 0 and (conTile - i) // app.maxRoomSize == tileY:
                    app.openConnections[max(con[0], con[1])].add(conTile - i)
            for i in range(conTile % app.maxRoomSize + app.maxRoomSize - conTile % app.maxRoomSize):
                app.connectionsToDraw.append(tuple([app.size * (tileX + i + app.maxRoomSize * (min(con[0], con[1]) % app.numRooms)), 
                app.size * (tileY + app.maxRoomSize * (min(con[0], con[1]) // app.numRooms)), 
                app.size * (tileX + 1 + i + app.maxRoomSize * (min(con[0], con[1]) % app.numRooms)), 
                app.size * (tileY + 1 + app.maxRoomSize * (min(con[0], con[1]) // app.numRooms))]))
        else:
            tileX = conTile % app.maxRoomSize
            tileY = conTile // app.maxRoomSize
            for i in range(conTile % app.maxRoomSize + app.maxRoomSize):
                if conTile + i * app.maxRoomSize < app.maxRoomSize ** 2:
                    app.openConnections[min(con[0], con[1])].add(conTile + i * app.maxRoomSize)
                if conTile - i * app.maxRoomSize > 0:
                    app.openConnections[max(con[0], con[1])].add(conTile - i * app.maxRoomSize)
            for i in range(conTile % app.maxRoomSize + app.maxRoomSize - conTile % app.maxRoomSize):
                app.connectionsToDraw.append(tuple([app.size * (tileX + app.maxRoomSize * (min(con[0], con[1]) % app.numRooms)), 
                app.size * (tileY + i + app.maxRoomSize * (min(con[0], con[1]) // app.numRooms)), 
                app.size * (tileX + 1 + app.maxRoomSize * (min(con[0], con[1]) % app.numRooms)), 
                app.size * (tileY + 1 + i + app.maxRoomSize * (min(con[0], con[1]) // app.numRooms))]))

# def drawConnections(app, canvas):
#     for tile in app.connectionsToDraw:
#         canvas.create_rectangle(tile[0], tile[1], tile[2], tile[3], fill = "orange")

def drawConnections(app, canvas):
    for tile in app.openConnections[app.p1.currCell]:
        tileNumX = tile % app.maxRoomSize
        tileNumY = tile // app.maxRoomSize
        canvas.create_rectangle(app.size * tileNumX, 
        app.size * tileNumY, 
        app.size * (tileNumX + 1), 
        app.size * (tileNumY + 1), fill = "orange")

# def drawRooms(app, canvas):
#     tileNumX = 0
#     tileNumY = 0
#     for open in app.openSquares:
#         for tile in app.openSquares[open]:
#             tileNumX = tile % app.maxRoomSize
#             tileNumY = tile // app.maxRoomSize
#             canvas.create_rectangle(app.size * (tileNumX + app.maxRoomSize * (open % app.numRooms)), 
#             app.size * (tileNumY + app.maxRoomSize * (open // app.numRooms)), 
#             app.size * (tileNumX + 1 + app.maxRoomSize * (open % app.numRooms)), 
#             app.size * (tileNumY + 1 + app.maxRoomSize * (open // app.numRooms)), fill = "orange")
#             if open == app.p1.currCell:
#                 canvas.create_rectangle(app.size * (tileNumX + app.maxRoomSize * (open % app.numRooms)), 
#                 app.size * (tileNumY + app.maxRoomSize * (open // app.numRooms)), 
#                 app.size * (tileNumX + 1 + app.maxRoomSize * (open % app.numRooms)), 
#                 app.size * (tileNumY + 1 + app.maxRoomSize * (open // app.numRooms)), fill = "blue")

def drawCurrentCell(app, canvas):
    tileNumX = 0
    tileNumY = 0
    for tile in app.openSquares[app.p1.currCell]:
        tileNumX = tile % app.maxRoomSize
        tileNumY = tile // app.maxRoomSize
        canvas.create_rectangle(app.size * tileNumX, 
        app.size * tileNumY, 
        app.size * (tileNumX + 1), 
        app.size * (tileNumY + 1), fill = "orange")

