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

def mousePressed(app, event):
    if app.currPage == "intro":
        if event.x >= app.width // 2 - app.buttonWidth and event.x <= app.width // 2 + app.buttonWidth:
            if event.y >= app.height // 2 - app.buttonHeight and event.y <= app.height // 2 + app.buttonHeight:
                pass
            elif event.y >= app.height // 2 - app.buttonHeight + app.buttonMargin and event.y <= app.height // 2 + app.buttonHeight + app.buttonMargin:
                app.currPage = "game"
            elif event.y >= app.height // 2 - app.buttonHeight - app.buttonMargin and event.y <= app.height // 2 + app.buttonHeight - app.buttonMargin:
                app.currPage = "credit"
                app.pause = False
    elif app.currPage == "game" and app.pause:
        if event.x >= app.width // 2 - app.buttonWidth and event.x <= app.width // 2 + app.buttonWidth:
            if event.y >= app.height // 2 - app.buttonHeight and event.y <= app.height // 2 + app.buttonHeight:
                pass
            elif event.y >= app.height // 2 - app.buttonHeight + app.buttonMargin and event.y <= app.height // 2 + app.buttonHeight + app.buttonMargin:
                app.pause = False
                app.currPage = "intro"
            elif event.y >= app.height // 2 - app.buttonHeight - app.buttonMargin and event.y <= app.height // 2 + app.buttonHeight - app.buttonMargin:
                app.pause = False

def mouseMoved(app, event):
    if app.currPage == "intro":
        if event.x >= app.width // 2 - app.buttonWidth and event.x <= app.width // 2 + app.buttonWidth:
            if event.y >= app.height // 2 - app.buttonHeight and event.y <= app.height // 2 + app.buttonHeight:
                app.helpColor = "red"
            elif event.y >= app.height // 2 - app.buttonHeight + app.buttonMargin and event.y <= app.height // 2 + app.buttonHeight + app.buttonMargin:
                app.creditColor = "red"
            elif event.y >= app.height // 2 - app.buttonHeight - app.buttonMargin and event.y <= app.height // 2 + app.buttonHeight - app.buttonMargin:
                app.startColor = "red"
            else:
                app.helpColor, app.startColor, app.creditColor = "gray", "gray", "gray"
        else:
            app.helpColor, app.startColor, app.creditColor = "gray", "gray", "gray"
    elif app.currPage == "game" and app.pause:
        if event.x >= app.width // 2 - app.buttonWidth and event.x <= app.width // 2 + app.buttonWidth:
            if event.y >= app.height // 2 - app.buttonHeight and event.y <= app.height // 2 + app.buttonHeight:
                app.pauseHelpColor = "red"
            elif event.y >= app.height // 2 - app.buttonHeight + app.buttonMargin and event.y <= app.height // 2 + app.buttonHeight + app.buttonMargin:
                app.pauseQuitColor = "red"
            elif event.y >= app.height // 2 - app.buttonHeight - app.buttonMargin and event.y <= app.height // 2 + app.buttonHeight - app.buttonMargin:
                app.pauseBackColor = "red"
            else:
                app.pauseHelpColor, app.pauseQuitColor, app.pauseBackColor = "gray", "gray", "gray"
        else:
            app.pauseHelpColor, app.pauseQuitColor, app.pauseBackColor = "gray", "gray", "gray"

def keyPressed(app, event):
    # if event.key == "Escape" and app.currPage == "game" and not app.pause:
    #     app.pause = True
    # elif event.key == "Escape" and app.currPage == "game" and app.pause:
    #     app.pause = False
    # elif event.key == "Escape":
    #     app.currPage = "intro"
    # if app.gameOver or not app.playerTurn:
    #     return
    # if event.key in {"h", "w", "Right", "Left", "Up", "Down"}:
    #     app.playerTurn = False
    if event.key == "h":
        app.playerTurn = True
        if "health" in app.potionList:
            app.potionList["health"].drink(app)
    if event.key == "w":
        updatePlayerLocation(app, False, False, False, False)
    if event.key == "Right":
        updatePlayerLocation(app, False, True, False, False)
    if event.key == "Left":
        updatePlayerLocation(app, True, False, False, False)
    if event.key == "Up":
        updatePlayerLocation(app, False, False, False, True)
    if event.key == "Down":
        updatePlayerLocation(app, False, False, True, False)