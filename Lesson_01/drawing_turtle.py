import turtle 
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

#Draw a square with small outside squares at each corner
for i in range(4):
  t.forward(180)
  t.right(90)
  t.forward(40)
  t.right(90)
  t.forward(40)
  t.right(90)
  t.forward(40)


    
turtle.done()
