import tkinter as tk
import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image, ImageTk
#This draws what is on the help screen


def drawInstructions(app, canvas):
    canvas.create_text(app.width//2, app.height//2 + app.menuMargin, text = "Movement is done via arrow keys. Esc pauses/exits page.", anchor = "center", font = "15")
    canvas.create_text(app.width//2, app.height//2 - app.menuMargin // 4, text = "Press w to skip a turn (enemies will move without you moving)", anchor = "center", font = "15")
    canvas.create_text(app.width//2, app.height//2 + app.menuMargin // 4, text = "Objectve is to reach the purple square.", anchor = "center", font = "15")
    canvas.create_text(app.width//2, app.height//2 + app.menuMargin // 2, text = "Doing so will increase your depth and the difficulty of the enemies.", anchor = "center", font = "15")
    canvas.create_text(app.width//2, app.height//2 - app.menuMargin // 2, text = "Red squares are enemies and black squares are item pickups.", anchor = "center", font = "15")
    canvas.create_text(app.width//2, app.height//2 - app.menuMargin, text = "To use your items press h.", anchor = "center", font = "15")
