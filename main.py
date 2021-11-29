# Project Main Code
# Date Initialized: 11/2/21
# Author: Kayden Moreno
# AndrewID: kmoreno

import tkinter as tk
import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image, ImageTk
from enemy import *
from help import drawInstructions
from pauseMenu import *
from player import *
from dungeon import *
from items import *
from introPage import *
from controllers import *

def appStarted(app):
    app.inFight = None
    app.expLevel = 1
    app.expToNextLevel = 10 * app.expLevel
    app.goalCell = 0
    app.goalTile = 0
    app.depth = 1
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
    app.maxRoomSize = 10
    app.numRooms = 7
    app.menuMargin = app.width // 4
    app.pauseMargin = app.menuMargin // 3
    app.pause = False
    app.helpColor, app.startColor, app.creditColor, app.pauseHelpColor, app.pauseQuitColor, app.pauseBackColor = ("gray" for i in range(6))
    app.buttonMargin = app.height // 6
    app.currPage = "intro"
    app.buttonWidth = app.width // 12
    app.buttonHeight = app.height // 40
    app.titleImg = Image.open("Images\TP Title Image.jfif")
    app.titleImg = app.titleImg.resize((app.width, app.height))
    app.titleImg = ImageTk.PhotoImage(app.titleImg)
    app.potionList = dict()
    health = healthPotion()
    app.potionList["health"] = health
    app.wallList = set()
    app.gameOver = False
    app.turnCounter = 0
    app.playerTurn = True
    app.enemyTurn = False
    app.size = app.width // app.maxRoomSize
    app.p1 = Player()
    app.enemies = [Enemy(5), Enemy(5), Enemy(5)]
    app.turnCounter = 0
    app.grid = [(["grey"] * (app.width // app.size)) for i in range(app.height // app.size)]
    #Intial Dungeon Generation
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
    app.itemLocs = dict()
    createItems(app)
    for enemy in app.enemies:
        assignEnemy(app, enemy)

def timerFired(app):
    if app.currPage == "credit":
        app.newCon = False
    if app.currPage != "credit" or app.pause:
        return
    if app.gameOver:
        return
    if app.enemyTurn:
        app.turnCounter += 1
        if app.turnCounter % 35 == 0:
            app.enemies.append(Enemy(app.depth + 5))
            assignEnemy(app, app.enemies[-1])
        moveEnemy(app)
        app.playerTurn, app.enemyTurn = True, False

def displayCurrentPage(app, canvas):
    if app.currPage == "intro":
        drawBackground(app, canvas)
        drawIntroButtons(app, canvas)
    elif app.currPage == "credit":
        if app.gameOver:
            canvas.create_text(app.width // 2, app.height // 2, text = "GAME OVER", anchor = "center")
            if app.pause:
                drawPauseMenu(app, canvas)
                drawPauseButtons(app, canvas)
            return
        canvas.create_rectangle(0, 0, app.width, app.height, fill = "gray")
        drawCurrentCell(app, canvas)
        drawConnections(app, canvas)
        drawPlayer(app, canvas)
        drawStats(app, canvas)
        drawEnemies(app, canvas)
        drawGoal(app, canvas)
        drawItems(app, canvas)
        if app.inFight != None: 
            drawEnemyHealth(app, canvas)
        if app.pause:
            drawPauseMenu(app, canvas)
            drawPauseButtons(app, canvas)
    elif app.currPage == "help":
        drawInstructions(app, canvas)

def redrawAll(app, canvas):
    displayCurrentPage(app, canvas)


runApp(width = 600, height = 600)
