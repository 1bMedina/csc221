from gasp import *
from time import sleep

begin_graphics()
ball_x = 5
ball_y = 5
c = Circle((ball_x, ball_y),5)

while ball_x < 630 and ball_y < 470:
    ball_x = ball_x + 4
    ball_y = ball_y + 3
    move_to(c, (ball_x, ball_y))
    time.sleep(0.02)


end_graphics()
