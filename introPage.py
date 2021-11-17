import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image


def drawBackground(app, canvas):
    canvas.create_image(app.width // 2, app.height // 2, image = app.titleImg)

def drawIntroButtons(app, canvas):
    canvas.create_rectangle(app.startX - app.buttonWidth, app.startY - app.buttonHeight, app.startX + app.buttonWidth, 
    app.startY + app.buttonHeight, fill = app.helpColor)

    canvas.create_text(app.startX, app.startY, text = "Help", anchor = "center", font = str(app.height // 40))

    canvas.create_rectangle(app.startX - app.buttonWidth, app.startY - app.buttonHeight + app.buttonMargin, 
    app.startX + app.buttonWidth, app.startY + app.buttonHeight + app.buttonMargin, fill = app.creditColor)

    canvas.create_text(app.startX, app.startY + app.buttonMargin, text = "Credits", anchor = "center", font = str(app.height // 40))

    canvas.create_rectangle(app.startX - app.buttonWidth, app.startY - app.buttonHeight - app.buttonMargin, 
    app.startX + app.buttonWidth, app.startY + app.buttonHeight - app.buttonMargin, fill = app.startColor)

    canvas.create_text(app.startX, app.startY - app.buttonMargin, text = "Start", anchor = "center", font = str(app.height // 40))




