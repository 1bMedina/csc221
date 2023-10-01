from gasp import *

begin_graphics()

Circle((300, 250),100) #head
Circle((350, 270),20) #eye
Circle((250, 270), 20) #eye
Arc((300, 200), 30, 225, 315)
Arc((350,290),30, 150, 10)
Arc((350,290),30, 150,60)

update_when("key_pressed")
end_graphics()
