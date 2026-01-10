import turtle
import time

# 1. Setup Screen
sc = turtle.Screen()
sc.setup(1000, 1000)
sc.bgcolor('black')
sc.tracer(0) 

# 2. Setup Turtles
t = turtle.Turtle()      # Text turtle
t.hideturtle()
t.penup()
t.color('white')

bar_outline = turtle.Turtle() # Outline turtle
bar_outline.hideturtle()
bar_outline.speed(0)
bar_outline.color('white')

filler = turtle.Turtle()      # The actual moving bar
filler.hideturtle()
filler.penup()
filler.color('lime')
filler.shape("square")        # Using a square shape to fill smoothly
filler.shapesize(stretch_wid=1.5, stretch_len=0.1) 

player = turtle.Turtle() 
player.hideturtle()
player.shape("turtle")

# 3. The Loading Animation
def draw_loading_bar():
    # 1. Use 't' for the static title (will not be deleted)
    t.goto(0, 80)
    t.write("Turtle game by MRMojangguy", align="center", font=("Arial", 20, "bold"))
    
    # 2. Draw the empty rectangle outline
    bar_outline.penup()
    bar_outline.goto(-202, -22) 
    bar_outline.pendown()
    for _ in range(2):
        bar_outline.forward(404)
        bar_outline.left(90)
        bar_outline.forward(44)
        bar_outline.left(90)
    
    # 3. Create a temporary turtle just for the % text so it doesn't delete the title
    percent_writer = turtle.Turtle()
    percent_writer.hideturtle()
    percent_writer.penup()
    percent_writer.color("white")

    # 4. Fill the bar
    start_x = -200
    for i in range(1, 101):
        # Move filler and stamp
        filler.goto(start_x + (i * 4), 0) 
        filler.stamp()
        
        # Update percentage text
        percent_writer.clear()
        percent_writer.goto(0, -60)
        percent_writer.write(f"Loading... {i}%", align="center", font=("Arial", 14, "normal"))
        
        sc.update()
        time.sleep(0.02)
        
    # 5. Final Message
    percent_writer.goto(0, -100)
    percent_writer.write("PRESS 'ENTER' TO START", align="center", font=("Arial", 16, "bold"))
    sc.update()

# 4. Game Functions
def start_game():
    sc.onkeypress(None, "Return")
    sc.bgcolor("white")
    t.clear()
    bar_outline.clear()
    filler.clear()
    
    player.color("black")
    player.goto(0,0)
    player.showturtle()
    player.pendown()
    sc.tracer(1) 
    sc.update()

# 5. Movements (Now moving 'player')
def forward(): player.setheading(90); player.forward(30)
def backward(): player.setheading(270); player.forward(30)
def left(): player.setheading(180); player.forward(30)
def right(): player.setheading(0); player.forward(30)
def clear(): player.clear()
# 6. Listeners
sc.listen()
sc.onkeypress(start_game, "Return")
sc.onkeypress(forward, "w")
sc.onkeypress(backward, "s")
sc.onkeypress(left, "a")
sc.onkeypress(right, "d")
sc.onkeypress(sc.bye, "Escape")
sc.onkeypress(clear, "space")

# START
draw_loading_bar()
sc.mainloop()
