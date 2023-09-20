from gasp import *

begin_graphics()

Circle((300, 250),100) #head
Circle((350, 270),20) #eye
Circle((250, 270), 20) #eye
Arc((300, 200), 30, 225, 315)

update_when("key_pressed")
end_graphics()
