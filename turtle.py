import turtle

r = 'r'
l = 'l'

turtle.ht()
turtle.speed(0)
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.color("black")
turtle.bgcolor("white")


old = r
new = old

length=20
cycle=1

iteration=int(input('Enter iteration:'))

while cycle<iteration:

    new = (old) + (r)

    old = old[::-1]

    #probegaem kazhdoe znachenije v perevernutom         
    for char in range(0,len(old)):
        if old[char] == r:
            old = (old[:char])+ (l) + (old[char+1:])
        elif old[char] == l:
            old = (old[:char]) + (r) + (old[char+1:])

    new = (new) + (old)
    old = new
    

    cycle=cycle+1


turtle.forward(length)

for char in range(0,len(new)):
    if new[char] == (r):
        turtle.right(90)
        turtle.forward(length)
    elif new[char] == (l):
        turtle.left(90)
        turtle.forward(length)
        
turtle.exitonclick()