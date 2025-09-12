import pgzrun
from random import randint
#title
TITLE = "Shooting Game"
#screen setup
HEIGHT = 500
WIDTH = 500
#hit message
message = ""
#actor
alien = Actor('Alien2')
alien.pos = 250,250
#draw/update function
def draw():
    screen.clear()
    screen.fill((220,240,255))
    alien.draw()
    screen.draw.text(message, center = (250,450), color = (0,0,0), fontsize = 30)
def place_alien():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(50, HEIGHT-100)
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good Shot!"
        place_alien()
    else:
        message = "Miss!"
place_alien()
pgzrun.go()
