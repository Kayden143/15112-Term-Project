# Project Core Code
# Date Initialized: 11/2/21
# Author: Kayden Moreno
# AndrewID: kmoreno

import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image
from enemy import *
from player import *
from dunegon import *

def appStarted(app):
    app.wallList = set()
    app.gameOver = False
    app.turnCounter = 0
    app.playerTurn = True
    app.enemyTurn = False
    app.size = 20
    app.p1 = Player()
    app.enemies = {Rat(10, 10)}
    app.enemyLocs = set()
    app.grid = [(["grey"] * (app.width // app.size)) for i in range(app.height // app.size)]

def timerFired(app):
    createRoom(app, 5, 5, 5, 5)
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

def redrawAll(app, canvas):
    if app.gameOver:
        canvas.create_text(app.width // 2, app.height // 2, text = "GAME OVER", anchor = "center")
        return
    drawDungeon(app, canvas)
    drawPlayer(app, canvas)
    drawEnemies(app, canvas)
    drawHealthBar(app, canvas)

runApp(width = 400, height = 400)
