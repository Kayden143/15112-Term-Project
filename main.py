# Project Core Code
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
from pauseMenu import *
from player import *
from dungeon import *
from items import *
from introPage import *
from controllers import *

def appStarted(app):
    app.newCon = True
    app.connectCounter = 0
    app.connectedCells = dict()
    app.connections = set()
    app.maxRoomSize = 10
    app.numRooms = 6
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
    print(app.potionList)
    app.wallList = set()
    app.gameOver = False
    app.turnCounter = 0
    app.playerTurn = True
    app.enemyTurn = False
    app.size = 20
    app.p1 = Player()
    app.enemies = {Enemy(25, 25)}
    app.enemyLocs = set()
    app.grid = [(["grey"] * (app.width // app.size)) for i in range(app.height // app.size)]
    app.roomList, app.openSquares = createDungeon(app)
    connectRooms(app)
    print("running")

def timerFired(app):
    if app.currPage == "credit":
        app.newCon = False
    if app.currPage != "game" or app.pause:
        return
    createRoom(app, 8, 6, 13, 5)
    createRoom(app, 10, 10, 12, 12)
    if app.gameOver:
        return
    if app.enemyTurn:
        print(app.p1.health)
        app.enemyLocs = set()
        for enemy in app.enemies:
            app.enemyLocs.add(tuple([enemy.x, enemy.y]))
        moveEnemy(app)
        app.playerTurn, app.enemyTurn = True, False
        app.turnCounter += 1
        createEnemy(app)

def displayCurrentPage(app, canvas):
    if app.currPage == "intro":
        drawBackground(app, canvas)
        drawIntroButtons(app, canvas)
    elif app.currPage == "game":
        if app.gameOver:
            canvas.create_text(app.width // 2, app.height // 2, text = "GAME OVER", anchor = "center")
            if app.pause:
                drawPauseMenu(app, canvas)
                drawPauseButtons(app, canvas)
            return
        drawDungeon(app, canvas)
        drawPlayer(app, canvas)
        drawEnemies(app, canvas)
        drawHealthBar(app, canvas)
        if app.pause:
            drawPauseMenu(app, canvas)
            drawPauseButtons(app, canvas)
    elif app.currPage == "credit":
        drawRooms(app, canvas)
        drawConnections(app, canvas)

def redrawAll(app, canvas):
    displayCurrentPage(app, canvas)


runApp(width = 600, height = 600)
