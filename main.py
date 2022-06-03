################################################
# Title: Project 6- Animation: Playing Soccer
# Programmer: Anika Sharma
# Date: 30/03/2021
# Purpose: To use python graphics to create an entertaining animated scene.
################################################

#*********************IMPORTS AND SCREEN SETUP*********************#
from tkinter import *
from time import *
from random import * 

tk = Tk()
s = Canvas(tk, width=600, height=500,background= "skyblue")
s.pack()




#*********************BACKGROUND*********************#
#the sun
s.create_oval(320,-50, 420,50, fill = "yellow", outline = '')

#the sun's rays
s.create_line(370,0, 280,40, fill = "yellow", width = 2)
x = 290
for sunline in range(6):
  s.create_line(370,0, x,75, fill = "yellow", width = 2)
  x += 30
s.create_line(370,0, 450,40, fill = "yellow", width = 2)


#clouds 
s.create_polygon(20,80, 40,65, 60,40, 80,20, 100,40, 160,60, 180,80, fill = "white", outline = "", smooth = True)
s.create_polygon(340,180, 360,176, 370,150, 440,100, 480,150, 540,155, 550,160, 560,180, fill = "white", outline = "", smooth = True)


#the ground with the soccer field line markings
s.create_rectangle(0,255, 600,500, fill = "green", outline = "")

s.create_line(0,280, 600,280, fill = "white", width = 3)
s.create_line(500,360, 460,360, 500,480, 540,480, fill = "white", width = 3)
s.create_oval(-80,340, 80,500, fill = "", outline = "white", width = 3)


#the grass
for i in range(0,300):
  grassx = randint(0,600)
  grassy = randint(255,480) 
  s.create_line(grassx,grassy, grassx,grassy+20, fill = "green3")


#the farther soccer goal front pole
s.create_polygon(500,240, 520,240, 520,360, 500,360, fill = "grey", outline = "gray43", width = 2)


#the farther side net
net1x = 540
net1y = 240
netlength = 20

for net1 in range(6):
  s.create_line(net1x,net1y, net1x-netlength,net1y+netlength, fill = "white", width = 2)

  netlength += 20
  net1x += 20

#last three lines for the farther side net
s.create_line(600,300, 540,360, fill = "white", width = 2)
s.create_line(600,320, 560,360, fill = "white", width = 2)
s.create_line(600,340, 580,360, fill = "white", width = 2)

#the overlapping lines on the farther net
overlapnetx1 = 520
overlapnety1 = 340

for overlap in range(6):
  s.create_line(overlapnetx1,overlapnety1, overlapnetx1+netlength, overlapnety1+netlength, fill = "white", width = 2)

  netlength += 20
  overlapnety1 -= 20

#remaining overlap lines
s.create_line(540,240, 600,300, fill = "white", width = 2)
s.create_line(560,240, 600,280, fill = "white", width = 2)
s.create_line(580,240, 600,260, fill = "white", width = 2)


#the lines for the farther framework of the soccer goal
s.create_line(500,240, 600,240, fill = "gray", width = 5)
s.create_line(500,358, 600,358, fill = "gray", width = 5)


#the closer front pole of the soccer goal
s.create_polygon(540,340, 560,340, 560,480, 540,480, fill = "grey", outline = "gray43", width = 2)


#the closer net
s.create_line(580,340, 560,360, fill = "white", width = 2)

nety2 = 340

for net2 in range(6):
  s.create_line(600,nety2, 560,nety2+40, fill = "white", width = 2)
  nety2 += 20

#the last line for the second net
s.create_line(600,460, 580,480, fill = "white", width = 2)

#the remaining overlap lines
s.create_line(580,340, 600,360, fill = "white", width = 2)
s.create_line(560,340, 600,380, fill = "white", width = 2)
s.create_line(560,400, 600,440, fill = "white", width = 2)
s.create_line(560,420, 600,460, fill = "white", width = 2)
s.create_line(560,440, 600,480, fill = "white", width = 2)
s.create_line(560,460, 580,480, fill = "white", width = 2)


#the lines for the closer framework of the soccer goal
s.create_line(540,340, 600,340, fill = "gray", width = 5)
s.create_line(540,478, 600,478, fill = "gray", width = 5)


#the top connecting pole of the soccer goal
s.create_polygon(520,240, 560,340, 540,340, 500,240, fill = "grey", outline = "gray43", width = 2)




#*********************FIRST PERSON: STEVE (RIGHT)*********************#
#Steve's upper body variables
sAncx = 420
sAncy = 310

#creating steve on the right
def createsteveupper():
  #to use the variables outside the function
  global sHair, sFace, sEye, sPupil, sArm1, sBody, sArm2

  #Steve's head: hair, face, eye, pupil, mouth
  sHair = s.create_rectangle(sAncx,sAncy, sAncx+40,sAncy+30, fill = "black")
  sFace = s.create_oval(sAncx,sAncy+10, sAncx+40,sAncy+50, fill = "lightgoldenrod2", outline = "black")
  sEye = s.create_oval(sAncx,sAncy+20, sAncx+10,sAncy+30, fill = "white", outline = "")
  sPupil = s.create_oval(sAncx,sAncy+25, sAncx+5,sAncy+30, fill = "black")

  #Steve's upper body: arm 1, body, arm 2
  sArm1 = s.create_line(sAncx+20,sAncy+60, sAncx-5,sAncy+70, fill = "lightgoldenrod2", width = 4)
  sBody = s.create_line(sAncx+20,sAncy+50, 440,420, fill = "red", width = 6)
  sArm2 = s.create_line(sAncx+22,sAncy+60, sAncx+28,sAncy+63, sAncx+7,sAncy+75, fill = "lightgoldenrod2", width = 4)

createsteveupper()
#create a happy mouth
sHappymouth = s.create_arc(sAncx,sAncy+10, sAncx+40,sAncy+50, start = 200, extent = 20, fill = "white", outline = "black")

#Steve's lower body leg 1, shoe 1
s.create_line(440,420, 440,450, fill = "blue", width = 6)
s.create_polygon(446,440, 446,450, 430,450, 440,440, fill = "brown", outline = "", smooth = True)




#*********************SECOND PERSON: JOHN (LEFT)*********************#
#John's head: hair, face, eye, pupil, mouth
s.create_rectangle(60,310, 100,340, fill = "gold")
s.create_oval(60,320, 100,360, fill = "lightgoldenrod2", outline = "black")
s.create_oval(90,330, 100,340, fill = "white", outline = "")
s.create_oval(95,335, 100,340, fill = "black")
s.create_arc(60,320, 100,360, start = 320, extent = 20, fill = "white", outline = "black")

#John's upper body: arm 1, body, arm 2
s.create_line(80,370, 105,380, fill = "lightgoldenrod2", width = 4)
s.create_line(80,360, 80,420, fill = "turquoise", width = 6)
s.create_line(82,370, 74,373, 96,385, fill = "lightgoldenrod2", width = 4)

#John's lower body leg 1, shoe 1
s.create_line(80,420, 80,450, fill = "orange", width = 6)
s.create_polygon(74,440, 74,450, 90,450, 80,440, fill = "red", outline = "", smooth = True)



#*********************THE SOCCER BALL*********************#
#soccer ball variables
ballancx = 390
ballancy = 410
ballsize = 40

#ball lines variables
l1start = 89
l2start = 359
l3start = 305
l4start = 230
l5start = 179

#creating the ball
def createBall():
  #to use the variables outside the function
  global ballbase, ballmiddle, l1, l2, l3, l4, l5

  #the white ball
  ballbase = s.create_oval(ballancx,ballancy, ballancx+ballsize,ballancy+ballsize, fill = "white", outline = "")

  #middle black pentagon
  ballmiddle = s.create_polygon(ballancx+20,ballancy+10, ballancx+10,ballancy+20, ballancx+15,ballancy+30, ballancx+25,ballancy+30, ballancx+30,ballancy+20, fill = "black")

  #the lines on the ball
  l1 = s.create_arc(ballancx,ballancy, ballancx+ballsize,ballancy+ballsize, start = l1start, extent = 1, fill = "black")
  l2 = s.create_arc(ballancx,ballancy, ballancx+ballsize,ballancy+ballsize, start = l2start, extent = 1, fill = "black")
  l3 = s.create_arc(ballancx,ballancy, ballancx+ballsize,ballancy+ballsize, start = l3start, extent = 1, fill = "black")
  l4 = s.create_arc(ballancx,ballancy, ballancx+ballsize,ballancy+ballsize, start = l4start, extent = 1, fill = "black")
  l5 = s.create_arc(ballancx,ballancy, ballancx+ballsize,ballancy+ballsize, start = l5start, extent = 1, fill = "black")

createBall()




#*********************TITLE TEXT*********************#
titletext = s.create_text(50,160, text = """Playing Soccer
          by Anika S. """, font = "Times 20 italic", anchor = W)

s.update()
sleep(1)
s.delete(titletext)




#*********************STEVE'S LEG 2 ANIMATED*********************#
#Steve's leg variables
slx = 440
sly = 450

#making Steve's leg go back
for legmovement in range(5):
  #Steve's leg 2
  steveleg = s.create_line(440,420, slx,sly-3, fill = "blue", width = 6)
  
  #Steve's shoe 2
  steveshoe = s.create_polygon(slx+6,sly-10, slx+6,sly, slx-10,sly, slx,sly-10, fill = "brown", outline = "", smooth = True)
  
  s.update()
  sleep(0.2)
  s.delete(steveleg,steveshoe)

  slx += 4
  sly -= 2


#making Steve's leg come forward
for legmovement2 in range(5):
  #Steve's leg 2
  steveleg = s.create_line(440,420, slx,sly-3, fill = "blue", width = 6)
  
  #Steve's shoe 2
  steveshoe = s.create_polygon(slx+6,sly-10, slx+6,sly, slx-10,sly, slx,sly-10, fill = "brown", outline = "", smooth = True)

  s.update()
  sleep(0.03)
  s.delete(steveleg,steveshoe)

  slx -= 4
  sly += 2

s.delete(ballbase, ballmiddle, l1,l2,l3,l4,l5)




#*********************SOCCER BALL ANIMATION 1*********************#
#moving the ball from Steve (right) to John (left)
for movement in range(31):
  #the rolling effect by moving the lines
  l1start += 11.55
  l2start += 11.55
  l3start += 11.55
  l4start += 11.55
  l5start += 11.55

  createBall()

  s.update()
  sleep(0.0333)
  s.delete(ballbase, ballmiddle, l1, l2, l3, l4, l5)

  ballancx -= 10

ballancx += 10 #to avoid the extra push at the end of the animation

#to retain the ball after animation
createBall()




#*********************JOHN'S LEG 2 ANIMATED*********************#
#John's leg variables
jlx = 80
jly = 450

#making John's leg go back
for legmovement3 in range(8):
  #John's leg 2
  johnleg = s.create_line(80,420, jlx,jly-5, fill = "orange", width = 6)
  
  #John's shoe 2
  johnshoe = s.create_polygon(jlx-6,jly-10, jlx-6,jly, jlx+10,jly, jlx,jly-10, fill = "red", outline = "", smooth = True)

  s.update()
  sleep(0.15)
  s.delete(johnleg,johnshoe)

  jlx -= 4
  jly -= 2

#to retain the leg after the animation
#John's leg 2
johnleg = s.create_line(80,420, jlx,jly-5, fill = "orange", width = 6)

#John's shoe 2
johnshoe = s.create_polygon(jlx-6,jly-10, jlx-6,jly, jlx+10,jly, jlx,jly-10, fill = "red", outline = "", smooth = True)

sleep(0.5)




#**********CREATING THE CLOSE UP OF STEVE'S FACE SCENE**********#

########NEW TEMPORARY BACKGROUND########

#the ground and top goal pole
ground = s.create_rectangle(0,0, 600,500, fill = "green", outline = "")
toppole = s.create_rectangle(0,0, 600,40, fill = "grey", outline = "grey43")

#the white soccer field line in front of the goal
soccerline = s.create_line(0,420, 600,420, fill = "white", width = 5)

#the list for storing the grass and net lines
biglist = []

#the grass
for j in range(0,100):
  grassx = randint(0,600)
  grassy = randint(260,480)

  grassline = s.create_line(grassx,grassy, grassx,grassy+20, fill = "green3")
  biglist.append(grassline)


#the back net part 1- initial lines
startingx = 20
startingy = 40
x2 = 0
y2 = 60

for backnet in range(41):
  netline = s.create_line(startingx,startingy, x2, y2, fill = "white", width = 2)
  startingx += 20
  
  if y2 < 260:
    y2 += 20
  
  elif y2 >= 260:
    y2 = 260
    x2 += 20

  biglist.append(netline)


#the backnet part 2- overlapping lines
startingx = 0
startingy = 240
x2 = 20

for backnet2 in range(41):
  netline2 = s.create_line(startingx,startingy, x2, 260, fill = "white", width = 2)
  x2 += 20

  if startingy > 40:
    startingy -= 20
  
  elif startingy <= 40:
    startingy = 40
    startingx += 20

  biglist.append(netline2)


#the bottom frame of the soccer goal
frame = s.create_rectangle(0,260, 600,280, fill = "grey", outline = "grey43")


#######CREATING STEVE'S CLOSEUP FACE#######
#hair
hair = s.create_rectangle(160,140, 440,320, fill = "black")

#face
face = s.create_oval(160,180, 440,440, fill = "lightgoldenrod2", outline = "black")

#eyes
eye1 = s.create_oval(210,260, 270,320, fill = "white", outline = "")
pupil1 = s.create_oval(230,290, 250,310, fill = "black")

eye2 = s.create_oval(330,260, 390,320, fill = "white", outline = "")
pupil2 = s.create_oval(350,290, 370,310, fill = "black")

#mouth
mouth = s.create_oval(240,360, 360,400, fill = "white", outline = "black")

#the small body
body = s.create_rectangle(280,440, 320,500, fill = "red", outline = "")

#the arms- currently down
arm1 = s.create_line(280,460, 240,520, fill = "lightgoldenrod2", width = 10)
arm2 = s.create_line(320,460, 360,520, fill = "lightgoldenrod2", width = 10)




#**************ANIMATING THE SWEAT DROP**************#
#drop y variables
dy = 250
dy2 = 280

for drop in range(30):
  sweatdrop = s.create_polygon(390,dy, 380,dy2, 400,dy2, fill = "light blue", outline = "blue", smooth = True)

  s.update()
  sleep(0.033)
  s.delete(sweatdrop)

  dy += 10
  dy2 += 10

sleep(0.5)




#**************DELETING EVERYTHING OF TEMPORARY SCREEN**************#
s.delete(ground, toppole, soccerline, frame, hair, face, eye1, pupil1, eye2, pupil2, mouth, body, arm1, arm2)

#deleting the grass and net lines
for items in biglist:
  s.delete(items)

#changing steve's happy mouth to open nervous mouth
s.delete(sHappymouth)
sScaredmouth = s.create_oval(sAncx+4,sAncy+35, sAncx+20,sAncy+45, fill = "white")

s.delete(johnleg, johnshoe)




#**************JOHN KICKING THE BALL**************#
#making John's leg go back
for legmovement4 in range(11):
  #John's leg 2
  johnleg = s.create_line(80,420, jlx,jly-5, fill = "orange", width = 6)
  
  #John's shoe 2
  johnshoe = s.create_polygon(jlx-6,jly-10, jlx-6,jly, jlx+10,jly, jlx,jly-10, fill = "red", outline = "", smooth = True)

  s.update()
  sleep(0.03333)
  s.delete(johnleg,johnshoe)

  if jly >= 450:
    jly -= 2

  else:
    jly += 2

  jlx += 5




#*****************ANIMATION: SOCCER BALL AND STEVE BENDING*****************#
s.delete(ballbase,ballmiddle,l1,l2,l3,l4,l5) #to delete previous copy

for ballcurve in range(55):
  #curving the soccer ball into the net

  #the rolling effect by moving the lines
  l1start += 22.552
  l2start += 22.552
  l3start += 22.552
  l4start += 22.552
  l5start += 22.552

  #the curve motion calculations 
  ballancx = 8*ballcurve + 90
  ballancy = 0.25 * ballcurve**2 -14 * ballcurve +410
  
  createBall()


  #bringing back John's leg

  #John's leg 2
  johnleg = s.create_line(80,420, jlx,jly-5, fill = "orange", width = 6)
  #John's shoe 2
  johnshoe = s.create_polygon(jlx-6,jly-10, jlx-6,jly, jlx+10,jly, jlx,jly-10, fill = "red", outline = "", smooth = True)

  if jly >= 450:
    jly = 450
    jlx = 80
  else:
    jlx -=5 
    jly += 2
  

  #creating the poles again so that the ball goes INTO the goal

  #the top connecting pole
  pole1 = s.create_polygon(520,240, 560,340, 540,340, 500,240, fill = "grey", outline = "gray43", width = 2)
  #the closer front pole
  pole2 = s.create_polygon(540,340, 560,340, 560,480, 540,480, fill = "grey", outline = "gray43", width = 2)


  #making Steve bend to avoid the ball
  if ballancx >= 340:
    s.delete(sHair, sFace, sEye, sPupil, sScaredmouth, sArm1, sBody, sArm2)
    createsteveupper()
    sScaredmouth = s.create_oval(sAncx+4,sAncy+35, sAncx+20,sAncy+45, fill = "white")

    sAncx -= 1
    sAncy += 1


  s.update()
  sleep(0.0333)  

  #deleting items when Steve is bending
  if ballancx >= 340:
    s.delete(ballbase, ballmiddle, l1,l2,l3,l4,l5, pole1,pole2, johnleg, johnshoe, sHair, sFace, sEye, sPupil, sScaredmouth, sArm1, sBody, sArm2)
  
  #deleting items when Steve is not bending
  else:
    s.delete(ballbase, ballmiddle, l1,l2,l3,l4,l5, pole1,pole2, johnleg, johnshoe) 




#*********************RETAINING THE BALL AND POLES*********************#
createBall()

#the top connecting pole
s.create_polygon(520,240, 560,340, 540,340, 500,240, fill = "grey", outline = "gray43", width = 2)

#the closer front pole
s.create_polygon(540,340, 560,340, 560,480, 540,480, fill = "grey", outline = "gray43", width = 2)




#*********************ANIMATION TO BRING STEVE BACK*********************#
#to bring Steve back to standing
while sAncx <= 420:
  createsteveupper()
  sScaredmouth = s.create_oval(sAncx+4,sAncy+35, sAncx+20,sAncy+45, fill = "white")

  s.update()
  sleep(0.012)
  s.delete(sHair, sFace, sEye, sPupil, sScaredmouth, sArm1, sBody, sArm2)

  sAncx += 1
  sAncy -= 1

#to avoid the extra push after animation
sAncx -= 1
sAncy += 1

#to retain steve
createsteveupper()
sScaredmouth = s.create_oval(sAncx+4,sAncy+35, sAncx+20,sAncy+45, fill = "white")

sleep(1)




#*********************ENDING DIALOGUE*********************#

########JOHN DIALOGUE########

#John's talking bubble
def johnbubble():
  global jb1, jb2
  jb1 = s.create_polygon(140,300, 120,320, 180,320, fill = "white", outline = "")
  jb2 = s.create_oval(130,260, 300,330, fill = "white", outline = "")

johnbubble()

#John's text
johntext = s.create_text(210,295, text = """    Yay! I scored! 
  Sorry I almost hit you.""", font = "Arial 10")

s.update()
sleep(2)
s.delete(jb1, jb2, johntext)



########STEVE DIALOGUE########

#Steve's talking bubble
def stevebubble():
  global sb1, sb2
  sb1 = s.create_polygon(380,300, 400,320, 360,320, fill = "white", outline = "")
  sb2 = s.create_oval(390,260, 220,330, fill = "white", outline = "")

stevebubble()

#Steve's text
stevetext = s.create_text(300,295, text = """    Yeah no problem.
    I should not have 
    been goalie haha.""", font = "Arial 9")

s.update()
sleep(2)
s.delete(sb1, sb2, stevetext)



########JOHN TALKING########

johnbubble()
johntext = s.create_text(210,295, text = """         Nah, it's fine.
   You just need practice.
      Let's try again!""", font = "Arial 10")

s.update()
sleep(2)
s.delete(jb1, jb2, johntext)



########STEVE TALKING########

#bringing back the happy face
s.delete(sScaredmouth)
sHappymouth = s.create_arc(sAncx,sAncy+10, sAncx+40,sAncy+50, start = 200, extent = 20, fill = "white", outline = "black")

stevebubble()
stevetext = s.create_text(300,295, text = """ Yeah sure let's do it.""", font = "Arial 10")

s.update()
sleep(2)
s.delete(sb1, sb2, stevetext)




#*********************END TEXT SHOW*********************#
s.create_text(60,160, text = """And they played 
happily ever after.

The End""", font = "Times 20 italic", anchor = W)


#########################* END OF PROGRAM *#########################