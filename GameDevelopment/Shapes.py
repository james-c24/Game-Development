import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    r = 255
    g = randint(100,255)
    b = randint(0,55)
    width = WIDTH
    height = HEIGHT - 200
    for i in range(20):
        rect = Rect((0,0),(width,height))
        rect.center = 150,150
        screen.draw.rect(rect,(r,g,b))
        width -= 5
        height += 5
        r -= 10
        g -= 5
        b += 10
pgzrun.go()
