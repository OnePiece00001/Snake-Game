import turtle as t
import time
from snake import Snake
from food import Food
from score import Score
# pen1 = t.Turtle("square")
# pen1.color("white")
# pen2 = t.Turtle("square")
# pen2.color("white")
# pen2.goto(-20,0)
# pen3 = t.Turtle("square")
# pen3.color("white")
# pen3.goto(-40,0)
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sanke Game")
turt = []
screen.tracer(0) # used to stop the animation
# for i in range(3):
#     pen = t.Turtle("square")
#     pen.up()
#     pen.color("white")
#     pen.goto(-20*i, 0)
#     turt.append(pen)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game = True
while game:
    screen.update()
    time.sleep(0.085)

    snake.move()

    #Eating the food

    if snake.segments[0].distance(food) < 15: #to check the distance betn snake and food
        food.refresh()
        score.foodcount()
        snake.add_tail()
    #---------------------------------------------------------------------------------------------
    # Detect a wall
    # if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290 :
    #     score.game_over()
    #     game = False
    #     snake.segments[0].goto(-290, 0)
    if snake.segments[0].xcor() > 290:
        snake.segments[0].goto(-290, snake.segments[0].ycor())
    if snake.segments[0].xcor() < -290:
        snake.segments[0].goto(290, snake.segments[0].ycor())
    if snake.segments[0].ycor() > 290:
        snake.segments[0].goto(snake.segments[0].xcor(), -290)
    if snake.segments[0].ycor() < -290:
        snake.segments[0].goto(snake.segments[0].xcor(), 290)

    #------------------------------------------------------------------------------------------------ 
    
    # Detect collision with body

    for segment in snake.segments[1:]:
        # if segment == snake.segments[0]:
        #     pass
        if snake.segments[0].distance(segment) < 10:
            score.game_over()
            game = False
    # for i in range(2,0,-1):
    #     x=turt[i-1].xcor()
    #     y=turt[i-1].ycor()
    #     turt[i].goto(x,y)
    # # turt[0].right(90)
    # turt[0].fd(20)
    # turt[0].left(90)
screen.exitonclick()