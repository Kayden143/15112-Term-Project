import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image
from player import *




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