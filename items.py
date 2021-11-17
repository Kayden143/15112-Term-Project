import math
import random as rm
from cmu_112_graphics import *
import sys
from PIL import Image

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

    def throw(self):
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
        if super().drink() != False:
            app.p1.health = app.p1.maxHealth


    def throw(self, app, x, y):
        if app.p1.x == x and app.p1.y == y:
            app.p1.health = app.p1.maxHealth
        elif (x, y) in app.enemyLocations:
            pass
            







