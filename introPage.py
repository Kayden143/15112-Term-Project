import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image

#This sets up the intro page UI


def drawBackground(app, canvas):
    canvas.create_image(app.width // 2, app.height // 2, image = app.titleImg)

def drawIntroButtons(app, canvas):
    canvas.create_rectangle(app.width // 2 - app.buttonWidth, app.height // 2 - app.buttonHeight, app.width // 2 + app.buttonWidth, 
    app.height // 2 + app.buttonHeight, fill = app.helpColor)

    canvas.create_text(app.width // 2, app.height // 2, text = "Help", anchor = "center", font = str(app.height // 40))

    canvas.create_rectangle(app.width // 2 - app.buttonWidth, app.height // 2 - app.buttonHeight + app.buttonMargin, 
    app.width // 2 + app.buttonWidth, app.height // 2 + app.buttonHeight + app.buttonMargin, fill = app.creditColor)

    canvas.create_text(app.width // 2, app.height // 2 + app.buttonMargin, text = "Credits", anchor = "center", font = str(app.height // 40))

    canvas.create_rectangle(app.width // 2 - app.buttonWidth, app.height // 2 - app.buttonHeight - app.buttonMargin, 
    app.width // 2 + app.buttonWidth, app.height // 2 + app.buttonHeight - app.buttonMargin, fill = app.startColor)

    canvas.create_text(app.width // 2, app.height // 2 - app.buttonMargin, text = "Start", anchor = "center", font = str(app.height // 40))




