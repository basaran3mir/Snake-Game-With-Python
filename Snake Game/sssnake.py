import turtle
import time
import random

score_list = [0]

def game(window_name, window_color, food_color, head_color, tail_color):

    my_window.title(window_name)
    my_window.cv._rootwindow.resizable(False, False)
    my_window.setup(width=610, height=610)
    my_window.bgcolor(window_color)
    my_window.tracer(0)

    up_border = turtle.Turtle()
    up_border.penup()
    up_border.speed(0)
    up_border.shape("square")
    up_border.shapesize(0.5, 60)
    up_border.color("black")
    up_border.goto(-15*20, 15*20)

    down_border = turtle.Turtle()
    down_border.penup()
    down_border.speed(0)
    down_border.shape("square")
    down_border.shapesize(0.5, 60)
    down_border.color("black")
    down_border.goto(15*20, -15*20)

    left_border = turtle.Turtle()
    left_border.penup()
    left_border.speed(0)
    left_border.shape("square")
    left_border.shapesize(60, 0.5)
    left_border.color("black")
    left_border.goto(-15*20, 15*20)

    right_border = turtle.Turtle()
    right_border.penup()
    right_border.speed(0)
    right_border.shape("square")
    right_border.shapesize(60, 0.5)
    right_border.color("black")
    right_border.goto(15*20, -15*20)

    head = turtle.Turtle()
    head.penup()
    head.speed(0)
    head.shape("square")
    head.shapesize(0.5, 0.5)
    head.color(head_color)
    head.goto(0, 100)
    head.direction = "stop"

    food_1 = turtle.Turtle()
    food_1.penup()
    food_1.speed(0)
    food_1.shape("square")
    food_1.shapesize(0.5, 0.5)
    food_1.color(food_color)
    food_1.goto(random.randint(-14,14)*20, random.randint(-14,14)*20)
    food_1.direction = "stop"

    food_2 = turtle.Turtle()
    food_2.penup()
    food_2.speed(0)
    food_2.shape("square")
    food_2.shapesize(0.5, 0.5)
    food_2.color(food_color)
    food_2.goto(random.randint(-14,14)*20, random.randint(-14,14)*20)
    food_2.direction = "stop"

    print_score = turtle.Turtle()
    print_score.penup()
    print_score.speed(0)
    print_score.shape("square")
    print_score.color("black")
    print_score.goto(0, 225)
    print_score.hideturtle()

    print_high_score = turtle.Turtle()
    print_high_score.penup()
    print_high_score.speed(0)
    print_high_score.shape("square")
    print_high_score.color("black")
    print_high_score.goto(0, 250)
    print_high_score.hideturtle()

    print_game_over = turtle.Turtle()
    print_game_over.penup()
    print_game_over.speed(0)
    print_game_over.shape("square")
    print_game_over.color("black")
    print_game_over.goto(0, 0)
    print_game_over.hideturtle()

    score = 0
    speed = 0.1
    tails = []

    def move():
        if head.direction == "up":
            head.sety(head.ycor() + 10)
        if head.direction == "down":
            head.sety(head.ycor() - 10)
        if head.direction == "right":
            head.setx(head.xcor() + 10)
        if head.direction == "left":
            head.setx(head.xcor() - 10)

    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def write_score():
        print_score.clear()
        print_score.write("Score: {}".format(score), align="center", font=("Courier", 12, "normal"))
    
    def write_high_score():
        print_high_score.clear()
        print_high_score.write("High Score: {}".format(max(score_list)), align="center", font=("Courier", 12, "normal"))

    def game_over():
        print_game_over.write("Game Over.", align="center", font=("Courier", 12, "normal"))
        time.sleep(2)
        my_window.clear()
        if theme == "blue":
            game("Yılan Dobby", "light blue", "light yellow", "black", "purple2")
        if theme == "white":
            game("Snake Game", "white", "red", "black", "green")

    my_window.listen()
    my_window.onkeypress(go_up, "w")
    my_window.onkeypress(go_down, "s")
    my_window.onkeypress(go_right, "d")
    my_window.onkeypress(go_left, "a")

    while True:

        my_window.update()
        write_score()
        write_high_score()

        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290: #Finish and restart the game
            score_list.append(score)
            game_over()

        if head.distance(food_1) == 0: #Eat food_1
            food_1_x = random.randint(-14,14)*20 
            food_1_y = random.randint(-14,14)*20
            food_1.goto(food_1_x, food_1_y)

            new_tail = turtle.Turtle()
            new_tail.speed(0)
            new_tail.shape("square")
            new_tail.shapesize(0.5, 0.5)
            new_tail.color(tail_color)
            new_tail.penup()
            tails.append(new_tail)

            score = score + 10
            speed = speed - 0.0001

        if head.distance(food_2) == 0: #Eat food_2
            food_2_x = random.randint(-14,14)*20 
            food_2_y = random.randint(-14,14)*20
            food_2.goto(food_2_x, food_2_y)

            new_tail = turtle.Turtle()
            new_tail.speed(0)
            new_tail.shape("square")
            new_tail.shapesize(0.5, 0.5)
            new_tail.color(tail_color)
            new_tail.penup()
            tails.append(new_tail)

            score = score + 10
            speed = speed - 0.0001

        for i in range(len(tails) - 1, 0, -1):
            x = tails[i - 1].xcor()
            y = tails[i - 1].ycor()
            tails[i].goto(x, y)

        if len(tails) > 0:
            x = head.xcor()
            y = head.ycor()
            tails[0].goto(x, y)

        move()
        time.sleep(speed)

        if len(tails) > 1:
            for i in range(len(tails)):
                if head.xcor() == tails[i].xcor() and head.ycor() == tails[i].ycor():
                    game_over()
    
my_window = turtle.Screen()
theme = my_window.textinput("Snake Game", "Please choose theme (blue or white):")

while theme != "blue" or theme != "white": #Start game

    if theme == None:
        my_window.clear()
        my_window.bye()

    if theme == "blue":
        game("Yılan Dobby", "light blue", "light yellow", "black", "purple2")
    if theme == "white":
        game("Snake Game", "white", "red", "black", "green")
    else:
        theme = my_window.textinput("Snake Game", "Please choose theme (blue or white):")