import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    radius = 125
    r = randint(0,100)
    g = 0
    b = randint(155,255)
    width = WIDTH
    height = HEIGHT - 200
    for i in range(20):
        screen.draw.circle((150,150),radius,(r,g,b))
        r += 5
        g += 10
        b -= 5
        radius -= 5
      
