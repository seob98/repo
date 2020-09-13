import turtle as t

t.speed(0)

t.penup()
t.goto(-200,-200)
t.pendown()

size = 100
count = 5
length = count * size


def draw_line(s,e):
	t.penup()
	t.goto(*s)
	t.pendown()
	t.goto(*e)

x1, y1 = t.pos()
x2, y2 = x1+length, y1+length

for i in range(count + 1):
	n = i*size
	draw_line((x1, y1+n), (x2, y1+n))
	draw_line((x1+n, y1), (x1+n, y2))


t.exitonclick()
