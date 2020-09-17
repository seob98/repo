import turtle as t

scale = 100

def move_to(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()

def draw_bieup(xs = 1):
	x, y = t.pos()
	t.pendown()
	t.setheading(270)
	t.forward(scale*0.6)
	t.left(90)
	t.forward(scale*xs)
	t.left(90)
	t.forward(scale*0.6)
	t.backward(scale*0.2)
	t.left(90)
	t.forward(scale*xs)
	move_to(x, y)

def draw_siot(xs = 1):
	x, y = t.pos()
	y2 = y - scale * 0.6
	move_to(x, y2)
	t.goto(x + scale*xs /2,y)
	t.goto(x + scale*xs,y2)
	move_to(x, y)

def draw_ieung(xs = 1):
	x, y = t.pos()
	move_to(x+ scale*xs*0.5, y - scale*0.8)
	t.setheading(0)
	t.circle(scale*0.4)
	move_to(x, y)

def draw_eo():
	x, y = t.pos()
	x2 = x + scale*1.5
	move_to(x2,y)
	t.goto(x2,y- scale)
	t.setheading(180)
	move_to(x2, y - scale*0.5)
	t.forward(scale*0.2)
	move_to(x,y)

def draw_o():
	x, y = t.pos()
	y2 = y - scale*1.15
	move_to(x,y2)
	t.setheading(0)
	t.forward(scale)
	t.backward(scale*0.5)
	t.left(90)
	t.forward(scale*0.2)
	move_to(x,y)

def draw_yo():
	x,y = t.pos()
	y2 = y- scale*1.15
	move_to(x,y2)
	t.setheading(0)
	t.forward(scale)
	t.backward(scale*0.6)
	t.left(90)
	t.forward(scale*0.2)
	move_to(x+scale*0.6,y2)
	t.forward(scale *0.2)
	move_to(x,y)

def draw_final(func = None):
	x, y = t.pos()
	if func != None:
		move_to(x,y-scale*1.4)
		func()
	move_to(x+scale*2,y)

move_to(-300,200)
t.speed(0)

draw_siot()
draw_o()
draw_final(draw_ieung)

draw_ieung()
draw_yo()
draw_final(draw_ieung)

draw_siot()
draw_eo()
draw_final(draw_bieup)


turtle.exitonlclick()
