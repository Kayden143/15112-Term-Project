import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image
from player import *

class Potion():
    def __init__(self, type, color, number):
        self.type = type
        self.color = color
        self.number = number

    def __repr__ (self):
        return f'{self.type, self.color, self.number}'

    def drink(self):
        if self.number > 0:
            self.number -= 1
            return self.type
        else:
            print("No potions remaining")
            return False

class healthPotion(Potion):

    def __init__(self):
        self.type = "health"
        self.color = "red"
        self.number = 2
    
    def drink(self, app):
        app.p1.health = app.p1.maxHealth
        return super().drink()





