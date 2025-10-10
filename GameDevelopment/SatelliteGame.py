import pgzrun
from random import randint
from time import time

HEIGHT = 800
WIDTH = 600
sats = []
lines = []
next_sat = 0
start_time = 0
total_time = 0
end_time = 0
sat_total = 8

def create_sats():
    global start_time
    for count in range(0,sat_total):
        sat = Actor("satelite")
        sat.pos = randint(40, WIDTH - 40),randint(40, HEIGHT - 40) 
        sats.append(sat)
    start_time = time()

def draw():
    global total_time
    screen.blit("grass",(0,0))
    number = 1
    for sat in sats:
        screen.draw.text(str(number),(sat.pos[0],sat[1]+20))
        sat.draw()
        number += 1
    for line in lines:
        screen.draw.line(line[0],line[1],("white"))
    if next_sat < sat_total:
        total_time = time() - start_time()
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)

def update():
    pass

def mouse_down():
    global next_sat, lines
    if next_sat < sat_total:
        if sats[next_sat].collidepoint(pos):
            if next_sat:
                lines.append(
                    (sats[next_sat-1].pos, sats[next_sat].pos)
                )
            next_sat += 1
        else:
            lines = []
            next_sat = 0
    create_sats()
    pgzrun.go()
