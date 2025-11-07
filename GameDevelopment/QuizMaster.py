import pgzrun
import random

TITLE = "Quiz Master"
HEIGHT = 900
WIDTH = 650

marquee_box = Rect((0,0),(900,80))
question_box = Rect((20,100),(750,150))
timer_box = Rect((700,100),(150,150))
answer_boxes = [Rect((50,300),(300,100)),
                Rect((520,300),(300,100)),
                Rect((50,420),(300,100)),
                Rect((520,420),(300,100))]
skip_box = Rect((700,200),(150,150))
questions = []
question = []
current_question = []
score = []
time_left = 25
marquee_message = ""
is_game_over = False
question_count = 0
question_index = 0
marquee_x = WIDTH

def load_questions(filename = "Question.txt"):
    global questions
    with open(filename,"r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 6:
                questions.append(parts)
    random.shuffle(questions)

def next_question():
    global current_question,question_index,time_left,is_game_over
    if question_index < len(questions):
        current_question = questions[question_index]
        time_left = 15
    else:
        is_game_over = True

def draw():
    screen.clear()
    screen.fill("sky blue")

    screen.draw.filled_rect(marquee_box,"yellow")
    screen.draw.text(marquee_message,(marquee_x,15),color="black",fontsize=30)

    if current_question:
        screen.draw.filled_rect(question_box,"pink")
        screen.draw.textbox(current_question[0],question_box,color="black")

        for i, box in enumerate(answer_boxes):
            screen.draw.filled_Rect(box,"pink")
            screen.draw.textbox(current_question[i+1],box,color="black")

        screen.draw.filled_rect(timer_box,"purple")
        screen.draw.textbox(str(time_left),timer_box,color="white")

        screen.draw.filled_rect   (skip_box,"dark green")
        screen.draw.textbox("Skip",skip_box,color="white")
    else:
        screen.draw.text("No questions found!",center=(WIDTH/2,HEIGHT/2),color="red",fontsize=40)

def update():
    global marquee_x
    marquee_x -= 2
    if marquee_x + 600 < 0:
        marquee_x = WIDTH

def update_timer():
    global time_left,is_game_over
    if not is_game_over:
        if time_left > 0:
            time_left -= 1
        else:
            next_question()
    
def on_mouse_down(pos):
    global score
    if is_game_over:
        return
    
    for i, box in enumerate(answer_boxes):
        if box.collidepoint(pos):
            if int(current_question[5]) == i + 1:
                score += 1
            nest_question()
            return
    if skip_box.collidepoint(pos):
        next_question()
    
load_questions()
next_question()
clock.schedule_interval(update_timer,1)
pgzrun.go()
