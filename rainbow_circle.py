import turtle
t = turtle.Turtle()
t.speed(10)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
turtle.bgcolor('black')
for i in range(36):
    t.color(colors[i % 7])
    t.circle(100)
    t.right(10)
turtle.done()

# This code creates a rainbow circle pattern using the turtle graphics library.
# It sets the background color to black and uses a list of colors to draw circles in a
# circular pattern, rotating slightly after each circle to create a rainbow effect.
# The turtle's speed is set to 10 for faster drawing.
# The turtle graphics library is a popular way to introduce programming concepts in Python.
# The code uses a loop to draw 36 circles, each with a different color from the
# predefined list, creating a visually appealing rainbow circle pattern.# The turtle graphics library is part of the standard Python library and is often used
# for educational purposes to teach programming concepts in a fun and interactive way.# The turtle graphics library is part of the standard Python library and is often used



