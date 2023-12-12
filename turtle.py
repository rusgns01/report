import turtle

t = turtle.Turtle()
t.speed(0)
cnt = 0

def xyGPS():
   x = turtle.textinput("", "X 좌표")
   y = turtle.textinput("", "Y 좌표")
   t.penup()
   t.goto(int(x), int(y))
   t.pendown()

def drawColor():
   choiceColor = turtle.textinput("", "1. 선색, 2. 채우기 색")

   # Pencolor
   if(int(choiceColor) == 1):
      choicePen = turtle.textinput("", "색상 선택 : 1. 기본(검정) 2. 7 색상 고르기")

      if(int(choicePen) == 1):
         turtle.pencolor('black')
      elif(int(choicePen) == 2):
         color = turtle.textinput("","원하는 색(En)")
         turtle.pencolor(color)
         
   # Fillcolor
   elif(int(choiceColor) == 2):
      choiceFill = turtle.textinput("", "색상 선택 : 1. 기본(검정) 2. 7 색상 고르기")

      if(int(choiceFill) == 1):
         turtle.fillcolor('black')
      elif(int(choiceFill) == 2):
         color = turtle.textinput("","원하는 색(En)")
         turtle.pencolor(color)

def xyTri():
   print("삼각형 그리는 중...")
   xyGPS()
   diameter = turtle.textinput("", "길이")

   for i in range(3):
      t.fd(int(diameter))
      t.left(120)

def xySquare():
   print("사각형 그리는 중...")
   xyGPS()

   for i in range(4):
      diameter = turtle.textinput("", "길이")
      t.fd(int(diameter))
      t.left(90)

def xyParallelogram():
   print("평행사변형 그리는 중...")
   xyGPS()

   for i in range(2):
      diameter = turtle.textinput("", "길이")
      t.fd(int(diameter))
      t.left(60)
      diameter = turtle.textinput("", "길이")
      t.fd(int(diameter))
      t.left(120)

while(cnt < 1):
   choice = turtle.textinput("", "0. 끝내기, 1. 삼각형, 2. 사각형, 3. 평행사변형")

   # End
   if(int(choice) == 0):
      cnt = 2
      
   # triangle
   elif(int(choice) == 1):
      drawColor()
      xyTri()

   # Square
   elif(int(choice) == 2):
      drawColor()
      xySquare()

   # parallelogram
   elif(int(choice) == 3):
      drawColor()
      xyParallelogram()
         
print("종료")
