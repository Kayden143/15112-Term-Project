import tkinter as tk
import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image, ImageTk
#This is the code for the pause menu/buttons

def drawPauseMenu(app, canvas):
    canvas.create_rectangle(app.width // 2 - app.menuMargin, app.height // 2 - app.menuMargin, app.width // 2 + app.menuMargin, 
    app.height // 2 + app.menuMargin, fill = "green")

def drawPauseButtons(app, canvas):
    canvas.create_rectangle(app.width // 2 - app.buttonWidth, app.height // 2 - app.buttonHeight, 
    app.width // 2 + app.buttonWidth, app.height // 2 + app.buttonHeight, fill = app.pauseHelpColor)

    canvas.create_text(app.width // 2, app.height // 2, text = "Help", anchor = "center", font = str(app.height // 40))

    canvas.create_rectangle(app.width // 2 - app.buttonWidth, app.height // 2 - app.buttonHeight + app.buttonMargin, 
    app.width // 2 + app.buttonWidth, app.height // 2 + app.buttonHeight + app.buttonMargin, fill = app.pauseQuitColor)

    canvas.create_text(app.width // 2, app.height // 2 + app.buttonMargin, text = "Quit", anchor = "center", font = str(app.height // 40))

    canvas.create_rectangle(app.width // 2 - app.buttonWidth, app.height // 2 - app.buttonHeight - app.buttonMargin, 
    app.width // 2 + app.buttonWidth, app.height // 2 + app.buttonHeight - app.buttonMargin, fill = app.pauseBackColor)

    canvas.create_text(app.width // 2, app.height // 2 - app.buttonMargin, text = "Back", anchor = "center", font = str(app.height // 40))