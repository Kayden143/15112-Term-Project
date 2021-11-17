import tkinter as tk
import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image, ImageTk

def drawPauseMenu(app, canvas):
    canvas.create_rectangle(app.startX - app.menuMargin, app.startY - app.menuMargin, app.startX + app.menuMargin, 
    app.startY + app.menuMargin, fill = "green")

def drawPauseButtons(app, canvas):
    canvas.create_rectangle(app.startX - app.buttonWidth, app.startY - app.buttonHeight, 
    app.startX + app.buttonWidth, app.startY + app.buttonHeight, fill = app.pauseHelpColor)

    canvas.create_text(app.startX, app.startY, text = "Help", anchor = "center", font = str(app.height // 40))

    canvas.create_rectangle(app.startX - app.buttonWidth, app.startY - app.buttonHeight + app.buttonMargin, 
    app.startX + app.buttonWidth, app.startY + app.buttonHeight + app.buttonMargin, fill = app.pauseQuitColor)

    canvas.create_text(app.startX, app.startY + app.buttonMargin, text = "Quit", anchor = "center", font = str(app.height // 40))

    canvas.create_rectangle(app.startX - app.buttonWidth, app.startY - app.buttonHeight - app.buttonMargin, 
    app.startX + app.buttonWidth, app.startY + app.buttonHeight - app.buttonMargin, fill = app.pauseBackColor)

    canvas.create_text(app.startX, app.startY - app.buttonMargin, text = "Back", anchor = "center", font = str(app.height // 40))