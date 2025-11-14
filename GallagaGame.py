import pgzrun
import random 

HEIGHT = 800
WIDTH = 600

WHITE = (255,255,255)
BLUE = (0,0,255)

score = 0
speed = 5
lives = 3
bullets = []
enemies = []
game_over = False


ship = Actor("ship")
ship.pos = (WIDTH//2,HEIGHT-60)

for i in range(5):
    enemy = Actor("bug")
    enemy.x = random.randint(50,WIDTH-50)
    enemy.y = random.randint(-300,-100)
    enemies.append(enemy)

def displayScore():
    screen.draw.text(str(score),(50,50),color="WHITE",fontsize=24)
def displayLives():
    screen.draw.text(("Lives Remaining: {}".format(str(lives))),(800,30),color="WHITE",fontsize=24)

def on_key_down(key):
    if keyboard.space:
        bullet = Actor("bullet")
        bullet.x = ship.x
        bullet.y = ship.y-50
        bullets.append(bullet)

def update():
    global score, lives, game_over
    if keyboard.left:
        ship.x -= speed
    if keyboard.right:
        ship.x += speed
    ship.x = max(0,(min(WIDTH,ship.x)))

    for bullet in bullets[:]:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10
     
    for enemy in enemies[:]:
        enemy.y += 4 
        if enemy.y >= HEIGHT:
            enemy.y -= 100
            enemy.x = random.randint(50,WIDTH-50)

        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                score += 10
                bullets.remove(bullet)
                enemies.remove(enemy)
                new_e = Actor("bug")
                new_e.x = random.randint(50,WIDTH-50)
                new_e.y = random.randint(-300,-100)
                enemies.append(new_e)
                break

        if enemy.colliderect(ship):
            lives -= 1
            enemies.remove(enemy)
            new_e = Actor("bug")
            new_e.x = random.randint(50,WIDTH-50)
            new_e.y = random.randint(-300,-100)
            enemies.append(new_e)

        if lives <= 0:
            game_over = True

def draw():
    screen.clear()
    screen.fill(BLUE)
    if game_over:
        screen.draw.text("Game Over.",center=(WIDTH//2,HEIGHT//2),color="WHITE",fontsize=30)
        screen.draw.text("Score: {}".format(score),center=(WIDTH//2,HEIGHT//2+100),color="WHITE",fontsize=30)
    else:
        for bullet in bullets:
            bullet.draw()
        for enemy in enemies:
            enemy.draw()
        ship.draw()
        displayScore()
        displayLives()

pgzrun.go()
