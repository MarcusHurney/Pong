# Implementation of classic arcade game Pong

# Left paddle uses W & S, Right paddle uses UP & DOWN arrows

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles

WIDTH = 1000
HEIGHT = 700
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
score_left = 0
score_right = 0
color = "white"



# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos
    global ball_vel

    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0,0]


    if direction == RIGHT:
        ball_vel[0] += ((random.randrange(120, 240)) / 60.0)
        ball_vel[1] += ((-(random.randrange(60, 180))) / 60.0)

    elif direction == LEFT:
        ball_vel[0] += ((-(random.randrange(120, 240)) / 60.0))
        ball_vel[1] += ((-(random.randrange(60, 180))) / 60.0)


# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score_left, score_right

    score_left = 0
    score_right = 0

    spawn_ball(RIGHT)


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel


    # draw mid line and gutters

    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "white")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "white")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "white")


    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= ((HEIGHT -1) - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0] + 0.5
        else:
            spawn_ball(RIGHT)
    elif ball_pos[0] >= ((WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH)):
        if (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0] - 0.5
        else:
            spawn_ball(LEFT)

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]


    # draw ball

    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, color, color)

    # update paddle's vertical position, keep paddle on the screen

    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel

    if (paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos = (HEIGHT - HALF_PAD_HEIGHT)

    if (paddle1_pos <= HALF_PAD_HEIGHT):
        paddle1_pos = HALF_PAD_HEIGHT

    if (paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos = (HEIGHT - HALF_PAD_HEIGHT)

    if (paddle2_pos <= HALF_PAD_HEIGHT):
        paddle2_pos = HALF_PAD_HEIGHT

    # draw paddles

    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, color)
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, color)

    # determine whether paddle and ball collide


    # draw scores

    global score_left, score_right

    canvas.draw_text(str(score_left), [150, 100], 28, "white")
    canvas.draw_text(str(score_right), [450, 100], 28, "white")

    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH):
        if (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):
            pass
        else:
            score_right += 1

    if (ball_pos[0] >= ((WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH))):
        if (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):
            pass
        else:
            score_left += 1



def keydown(key):

    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -6

    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 6

    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -6

    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 6



def keyup(key):

    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0

    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

def restart():
    new_game()

def color_tick():
    global color

    number = random.randrange(0,7)

    if number == 1:
        color = "yellow"
    elif number == 2:
        color = "red"
    elif number == 3:
        color = "blue"
    elif number == 4:
        color = "green"
    elif number == 0:
        color = "pink"
    elif number == 5:
        color = "orange"
    elif number == 6:
        color = "purple"



# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)
timer = simplegui.create_timer(225, color_tick)


# start frame
new_game()
frame.start()
timer.start()
