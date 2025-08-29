import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500

def draw():
    r = 255
    g = randint(100,255)
    b = randint(0,55)
    width = WIDTH - 50
    height = HEIGHT - 50
    for i in range(20):
        rect = Rect((0,0),(width,height))
        rect.center = 250,250
        screen.draw.rect(rect,(r,g,b))
        width -= 20
        height -= 20
        r -= 10
        g -= 5
        b += 10
pgzrun.go()
