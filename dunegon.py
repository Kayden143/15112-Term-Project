import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image
from player import *


def drawDungeon(app, canvas):
    for row in range(len(app.grid)):
        for col in range(len(app.grid[0])):
            canvas.create_rectangle(row * app.size, col * app.size, (row + 1) * app.size, (col + 1) * app.size, fill = app.grid[row][col])