# You can use this code in any way you want. Like, really.

import math
import turtle

vectors = []
turtle.hideturtle()
turtle.colormode(255)
turtle.speed(0)
print("\n\nVectoboi by Boutaib Ghali Omar\nUse this code in any way you want.\n\nPlease wait while the screen updates...\n\n")

def update():
	print("------------------------")
	print("Screen Update")
	turtle.pencolor(0, 0, 0)
	turtle.clear()
	turtle.penup()
	turtle.setheading(0)
	turtle.goto(-500,500)
	turtle.pendown()
	print("Painting grid...")
	for x in range(50):
		turtle.pencolor(200, 200, 200)
		turtle.forward(1000)
		turtle.right(90)
		turtle.forward(10)
		turtle.right(90)
		turtle.forward(1000)
		turtle.left(90)
		turtle.forward(10)
		turtle.left(90)
	turtle.goto(-500,-500)
	turtle.setheading(90)
	for x in range(50):
		turtle.pencolor(200, 200, 200)
		turtle.forward(1000)
		turtle.right(90)
		turtle.forward(10)
		turtle.right(90)
		turtle.forward(1000)
		turtle.left(90)
		turtle.forward(10)
		turtle.left(90)
	turtle.pencolor(0,0,0)
	turtle.penup()
	print("Painting axis'...")
	turtle.setheading(0)
	turtle.goto(-500,0)
	turtle.pendown()
	turtle.forward(1000)
	turtle.forward(-500)
	turtle.left(90)
	turtle.forward(500)
	turtle.forward(-1000)
	turtle.penup()
	turtle.goto(0,0)
	print("Tracing vectors...")
	for vec in vectors:
		turtle.pencolor(255, 0, 0)
		turtle.penup()
		turtle.goto(vec[0][0],vec[0][1])
		turtle.pendown()
		turtle.goto(vec[1][0],vec[1][1])
		turtle.penup()
		turtle.left(180)
		turtle.forward(2.5)
		turtle.left(90)
		turtle.forward(2.5)
		turtle.left(90)
		turtle.pendown()
		for x in range(4):
			turtle.forward(5)
			turtle.left(90)
	print("Screen update completed!")
	print("------------------------")

def norm(vecx):
	return math.sqrt(((vecx[1][0]-vecx[0][0])**2)+((vecx[1][1]-vecx[0][1])**2))

def menu():
	print("Vectoboi by Boutaib Ghali Omar\nMenu\n(0) Exit\n(1) Draw new vector\n(2) Delete vector")
	ch = int(input(">"))
	if ch == 0:
		print("\n\nGoodbye!\n\n")
		exit()
	if ch == 1:
		print("What method?\n(0) Give origin and target coordinates\n(1) Give origin coordinates and vector coordinates\n(2) Give vector coordinates and target coordinates")
		chx = int(input(">"))
		if chx == 0:
			ox = float(input("Origin x : "))
			oy = float(input("Origin y : "))
			tx = float(input("Target x : "))
			ty = float(input("Target y : "))
			vectors.append([[ox,oy],[tx,ty]])
		if chx == 1:
			ox = float(input("Origin x : "))
			oy = float(input("Origin y : "))
			vx = float(input("Vector x : "))
			vy = float(input("Vector y : "))
			vectors.append([[ox,oy],[ox+vx,oy+vy]])
		if chx == 2:
			vx = float(input("Vector x : "))
			vy = float(input("Vector y : "))
			tx = float(input("Target x : "))
			ty = float(input("Target y : "))
			vectors.append([[tx-vx,ty-vy],[tx,ty]])
	if ch == 2:
		i = 0
		for vec in vectors:
			print("[",i,"]")
			print("		",vec)
			print("		Norm =",norm(vec))
			i = i + 1
		print("Type the id of the vector that you want to delete")
		idx = int(input(">"))
		vectors.pop(idx)
	update()

update()
while True:
	menu()
