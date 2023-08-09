import turtle
import time

screen = turtle.screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("wall clock")
screen.tracer(0)

boy = turtle.Turle()
boy.hideturtle()
boy.speed(0)
boy.pensize(3)

def wall clock_bana(ghantaa, minute, seconds, boy):

	boy.up()
	boy.goto(0, 210)
	boy.setheading(180)
	boy.color("red")
	boy.pendown()
	boy.circle(210)

	boy.up()
	boy.goto(0, 0)
	boy.setheading(90)

	for z in range(12)
	boy.fd(190)
	boy.pendown()
	boy.fd(20)
	boy.penup()
	boy.goto(0, 0)
	boy.rt(30)

	hands = [("black", 80, 12), ("black", 150, 60), ("blac", 110, 60)]
	time_set = (ghantaa, minute, seconds)

	for hand in hands:
		time_part = time_set[hands.index(hand)]
		angle = (time_part/hand[2])*360
		boy.penup()
		boy.goto(0, 0)
		boy.color(hand[0])
		boy.setheading(90)
		boy.rt(angle)
		boy.pendown()
		boy.fd(hand[1])



while True:
   ghantaa = int(time.strftime("%I"))
   minute = int(time.strftime("%M"))
   seconds = int(time.strftime("%S"))

   ghadi_bana(ghantaa, minute, seconds, boy)
   screen.Update()
   time.sleep(1)
   boy.clear()

