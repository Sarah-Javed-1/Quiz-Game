#DEFINING FUNCTIONS

#import libraries
import turtle
import random
import time

#making the picture
def picture():
  #stars
  #setup
  turtle.bgcolor("cadetblue1")
  turtle.speed(0)

  starcolors = ["red", 'blue', "green"]
  star = turtle.Turtle()
  star.pensize(10)
  star.pu()
  star.goto(-230, -180)
  star.pd()
  star.pensize(10)
  #loop
  def stars(): 
    for i in range(10):
      star.color(random.choice(starcolors))
      star.pu()
      star.setpos(random.randint(-200, 200), random.randint(-200, 200))
      star.pd()
      for i in range(5):
        star.fd(30)
        star.rt(144)
  stars()


  #BACKDROP
  turtle.tracer(False)
  #left circle of blue base
  circle1 = turtle.Turtle()
  circle1.color('darkslategray4')
  circle1.pu()
  circle1.goto(-230, -180)
  circle1.shape('circle')
  circle1.shapesize(4)

  #blue base
  rect = turtle.Turtle()
  rect.color("darkslategray4")
  rect.pu()
  rect.goto(30, -180)
  rect.shape("square")
  rect.shapesize(7, 26)

  #right circle of blue base
  circle2 = turtle.Turtle()
  circle2.pu()
  circle2.color("darkslategray4")
  circle2.goto(280, -180)
  circle2.shape('circle')
  circle2.shapesize(4)

  #1st yellow triangle on the blue base
  triangles = turtle.Turtle()
  triangles.pu()
  triangles.color("yellow")
  triangles.goto(-215, -180)
  triangles.shape("triangle")
  triangles.shapesize(0.5)

  #2nd yellow triangle on the blue base
  triangle = turtle.Turtle()
  triangle.pu()
  triangle.color("yellow")
  triangle.setheading(180)
  triangle.goto(275, -180)
  triangle.shape("triangle")
  triangle.shapesize(0.5)

  #grey handle (left vertical part)
  handle1 = turtle.Turtle()
  handle1.pu()
  handle1.color("gray")
  handle1.setheading(270)
  handle1.goto(-200, -180)
  handle1.shape("square")
  handle1.shapesize(1, 3)

  #grey handle (main/horizontal part)
  handle2 = turtle.Turtle()
  handle2.pu()
  handle2.color("gray")
  handle2.goto(25, -180)
  handle2.shape("square")
  handle2.shapesize(1, 23.5)

  #grey handle (right vertical part)
  handle3 = turtle.Turtle()
  handle3.pu()
  handle3.color("gray")
  handle3.setheading(270)
  handle3.goto(250 ,-180)
  handle3.shape("square")
  handle3.shapesize(1, 3)

  #animating the blue base
  turtle.tracer(True)
  for i in range(-100, 15, 2):
    time.sleep(0.1)
    turtle.tracer(False)
    circle1.sety(i)
    rect.sety(i)
    circle2.sety(i)
    triangles.sety (i)
    triangle.sety(i)
    handle1.sety(i+80)
    handle2.sety(i+120)
    handle3.sety(i+80)
    turtle.tracer(True)

#winner
  def winner():
    #w
    turtle.tracer(False)
    turtle.pu()
    turtle.pensize(20)
    turtle.setpos(-200, 50)
    turtle.pd()
    turtle.setheading(300)
    turtle.fd(50)
    turtle.lt(120)
    turtle.fd(30)
    turtle.rt(120)
    turtle.fd(30)
    turtle.setheading(-300)
    turtle.fd(50)
    #i
    turtle.pu()
    turtle.goto(-90, 50)
    turtle.pd()
    turtle.setheading(0)
    turtle.fd(30)
    turtle.fd(-15)
    turtle.rt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(15)
    turtle.fd(-30)
    #n's
    def n(x):
      turtle.pu()
      turtle.goto(x, 50)
      turtle.pd()
      turtle.rt(90)
      turtle.fd(50)
      turtle.fd(-50)
      turtle.lt(45)
      turtle.fd(70)
      turtle.rt(45)
      turtle.fd(-50)
    n(-20)
    turtle.setheading(0)
    n(60)
    #e
    turtle.pu()
    turtle.goto(150, 50)
    turtle.pd()
    turtle.setheading(0)
    turtle.fd(30)
    turtle.fd(-30)
    turtle.rt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(30)
    turtle.pu()
    turtle.lt(90)
    turtle.fd(25)
    turtle.pd()
    turtle.lt(90)
    turtle.fd(30)
    #r
    turtle.pu()
    turtle.setpos(225, 50)
    turtle.pd()
    turtle.setheading(0)
    turtle.fd(15)
    turtle.circle(-15, 180)
    turtle.fd(15)
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(20)
    turtle.fd(-45)
    turtle.pu()
    turtle.goto(225, 20)
    turtle.pd()
    turtle.lt(45)
    turtle.fd(30)

  #other part of the r
  turtle.pensize(20)
  turtle.pu()
  turtle.setpos(225, 50)
  turtle.pd()
  turtle.setheading(0)
  turtle.fd(15)
  turtle.circle(-15, 180)
  turtle.fd(15)
  turtle.fd(10)
  turtle.lt(90)
  turtle.fd(20)
  turtle.fd(-45)
  turtle.pu()
  turtle.goto(225, 20)
  turtle.pd()
  turtle.lt(45)
  turtle.fd(30)

  winner()

  #PENCIL
  #triangle part of pencil
  pencil = turtle.Turtle()
  pencil.pu()
  pencil.setheading(180)
  pencil.goto( -190, -120)
  pencil.shape("triangle")
  pencil.shapesize(3)
  pencil.stamp()
  #main, horizontal part of pencil
  pencil.shape("square")
  pencil.goto(50, -120)
  pencil.shapesize(3, 22)
  pencil.stamp()
  pencil.goto(30, -130)
  pencil.color("white")
  pencil.pensize(30)
  #prints out the name of the person who won onto the pencil
  if points1 > points2:
    pencil.write(player1, font = 50)
  elif points1 < points2:
    pencil.write(player2, font = 50)
  elif points1 == points2:
    pencil.write(player2, player1, font = 50)



#defining average variables
global average
average = 0
sciaverage = 0
sciaverage2 = 0
mathaverage = 0
mathaverage2 = 0
techaverage = 0
techaverage2 = 0
engaverage = 0
engaverage2 = 0
geoaverage = 0
geoaverage2 = 0

#tracking points
points1 = 0
points2 = 0

#course menu list
coursemenu = ["COURSE MENU", "SCIENCE", "MATH", "TECHNOLOGY", "GEOGRAPHY"]

#function to validate if the answer is right or wrong
def rightanswer(correct, turn):
    #making any necessary variables global 
    global points1
    global points2
    global average
    #asks the user to input their answer
    guess = input("What is the answer? ")
    #asks the user to try again if the answer is not valid
    while not(guess.lower() == "a" or guess.lower() == "b" or guess.lower() == "c" or guess.lower() == "d"):
      guess = input("Please choose a, b, c, or d: ")
    #if it is player 1's turn it lets them know if their answer is correct or not. If it is right then it will add to their average and points
    if turn == 1:
      if guess.lower() == correct:
        print("You are correct!")
        points1 = points1 + 1
        average = average + 1
      #lets the user know if their answer is wrong
      else:
        print("Not quite. The correct answer is:", correct)
    #if it is player 2's turn it lets them know if their answer is correct or not. If it is right then it will add to their average and points
    elif turn == 2: 
      if guess.lower() == correct:
        print("You are correct!")
        points2 = points2 + 1
        average = average + 1
    #lets the user know if their answer is wrong
    else:
      print("That's not quite right, the correct answer would be:", correct)

#variable to intorduce the course.
CourseIntro = "There are 5 questions for you to answer. Please answer with the letter corresponding with the correct response. If there are 2 players, both players will have to do the quiz in order to proceed."

#makes a function for the science questions
def science(turns):
    #makes any necessary variables global 
    global sciaverage
    global sciaverage2
    global average
    #prints the course intro
    print(CourseIntro)
    #Gives the user the questions and validates them using the rightanswer function
    print("1. What is the chemical formula for vinegar?\na. H2O\nb. CO3\nc. CH3COOH\nd. CH2COH")
    rightanswer("c", turns)
    print("2. Which of the following is NOT qualitative data?\na. Colour\nb. Size\nc. Texture\nd. Smell")
    rightanswer("b", turns)
    print("3. Which is NOT an example of a biotic factor?\na. tree\nb. flower\nc. fox\nd. sunlight")
    rightanswer("d", turns)
    print("4. What is the largest organ?\na. heart\nb. skin\nc. lungs\nd. liver")
    rightanswer("b", turns)
    print("5. What is Ohm's law?\na. V = IR\nb. I = RV\nc. V = R/I\nd. V = I/R")
    rightanswer("a", turns)
    #if there is only one player or if it is player one's turn, the program displays their average
    if turns == 1:
      #stores player 1's average in a variable called sciaverage
      sciaverage = average/5*100
      print("Congrats on finishing! Your science average is:", sciaverage, "%")
    #if it is player two's turn it will print player two's average
    elif turns == 2:
      #stores player 2's average in a variable called sciaverage2
      sciaverage2 = average/5*100
      print("Congrats on finishing! Your science average is:", sciaverage2, "%")
    #resets the average variable to 0 so that it can be used again for a different course.
    average = 0

#makes a function for the math questions
#same format as the science function
def math(turns):
    global mathaverage
    global mathaverage2
    global average 
    print(CourseIntro)
    print("1. What is the pythagorean theorem:\na. a²+b² = c²\nb. a+b=c\nc. a*b=c²\nd. a²*b²=c²")
    rightanswer("a", turns)
    print("2. Solve for x: 3x - 10 = -5.5\na. -1.5\nb. 3.2\nc. 2.3\nd. 1.5")
    rightanswer("d", turns)
    print("3. When Sam was 8, his brother was half his age. Now his brother is 15. How old is Sam now?\na. 16\nb. 17\nc. 18\nd. 19")
    rightanswer("c", turns)
    print("4. Which of the following is NOT a prime number\na. 3\nb. 9\nc. 11\nd. 17")
    rightanswer("b", turns)
    print("5. What is the appoximate area of a circle with a radius of 2.5?\na. 19.89\nb. 19.71\nc. 19.63\nd. 19.42")
    rightanswer("c", turns)
    if turns == 1:
      mathaverage = average/5*100
      print("Congrats on finishing! Your math average is:", mathaverage, "%")
    elif turns == 2:
      mathaverage2 = average/5*100
      print("Congrats on finishing! Your math average is:", mathaverage2, "%")
    average = 0

#makes a function for the tech questions
#same format as the science function
def tech(turns):
    global techaverage
    global techaverage2
    global average 
    print(CourseIntro)
    print("1. What does LAN stand for in networking?\na. Land Area Network\nb. Local Area Network\nc.Local Air Network\nd. Land Air Network")
    rightanswer("b", turns)
    print("2. True or False: The colours on a resistor indicate it's resistive value.\na. True\nb. False")
    rightanswer("a", turns)
    print("3. Which of the following is corect syntax\na. for i in range(10)\nb. for i in range: 0, 10\nc. for i in range(10):\nd. for i in range(0, 10):")
    rightanswer("d", turns)
    print("4. Where is the CPU in a computer?\na. on the motherboard\nb. on the monitor\nc. in the power supply\nd. in the expansion slot")
    rightanswer("a", turns)
    print("5. Embedded systems...\na. can perform many different tasks\nb. are not time specific\nc. perform one specific task\nd. are not used in cars")
    rightanswer("c", turns)
    if turns == 1:
      techaverage = average/5*100
      print("Congrats on finishing! Your technology average is:", techaverage, "%")
    elif turns == 2:
      techaverage2 = average/5*100
      print("Congrats on finishing! Your technology average is:", techaverage2, "%")
    average = 0

#makes a function for the geography questions
#same format as the science function
def geography(turns):
    global geoaverage
    global geoaverage2
    global average
    print(CourseIntro)
    print("1. How many countries are in the world?\na. 193\nb. 195\nc.203\nd.198")
    rightanswer("b", turns)
    print("2. What is the capital city of Ontario?\na. Ottawa\nb. Toronto\nc. Milton\nd. Barrie")
    rightanswer("b", turns)
    print("3. How many provinces are in Canada?\na. 10\nb. 11\nc. 12\nd. 13")
    rightanswer("a", turns)
    print("4. Which continent is Singapore in?\na. North America\nb. Africa\nc. Europe\nd. Asia")
    rightanswer("d", turns)
    print("5. Which of the following is a line of longitude?\na. Tropic of Cancer\nb. Tropic of Capricorn\nc. Arctic Circle\nd. Prime Meridian")
    rightanswer("d", turns)
    if turns == 1:
      geoaverage = average/5*100
      print("Congrats on finishing! Your geography average is:", geoaverage, "%")
    elif turns == 2:
      geoaverage2 = average/5*100
      print("Congrats on finishing! Your geography average is:", geoaverage2, "%")
    average = 0

#makes a function for the english questions
#same format as the science function
def english(turns):
    global engaverage
    global engaverage2
    global average
    print(CourseIntro)
    print("1. Add a suffix to art to turn it into a person who does art.\na. arter\nb. artist\nc. archer\nd. archist")
    rightanswer("b", turns)
    print("2. What should be hyphenated in the book title: Through the looking glass\na.Through-the looking glass\nb. Through the-looking glass\nc. Through the looking-glass\nd. Through the-looking-glass")
    rightanswer("c", turns)
    print("3. Which word should be placed in the blank?'I enjoyed _______ the kids to the mall.'\na. to take\nb. take\nc. takeing\nd. taking")
    rightanswer("d", turns)
    print("4. What does the word monosemy mean?\na. a word having a single meaning\nb. a word having multiple meanings\nc. a word that sounds like another word but is spelt differently\nd. a word that has a single letter in it")
    rightanswer("a", turns)
    print("5. What is a verb?\na. a word that refers to a person, place, or object.\nb. a word that is used to describe a noun\nc. a word that expresses an act, occurrence, or mode of being\n d. a word that can be used in place of a noun")
    rightanswer("c", turns)
    engaverage = average/5*100
    if turns == 1:
      engaverage = average/5*100
      print("Congrats on finishing! Your english average is:", engaverage, "%")
    elif turns == 2:
      engaverage2 = average/5*100
      print("Congrats on finishing! Your english average is:", engaverage2, "%")
    average = 0

#makes a function for the display results screen
def display():
  #makign all necessary variables global 
  global sciaverage
  global sciaverage2
  global mathaverage
  global mathaverage2
  global techaverage
  global techaverage2
  global geoaverage
  global geoaverage2
  global engaverage
  global engaverage2

  #displays player 1's averages
  print(player1, "RESULTS: ")
  print("Science Average:", sciaverage)
  print("Math Average:", mathaverage)
  print("Technology Average:", techaverage)
  print("Geography Average:", geoaverage)
  #only displays english average the advanced level is being played
  if level.lower() == "advanced":
    print("English Average:", engaverage)
    print("OVERALL AVERAGE:", (sciaverage+mathaverage+techaverage+geoaverage+engaverage)/5)
  if level.lower() == "basic":
    print("OVERALL AVERAGE:", (sciaverage+mathaverage+geoaverage+techaverage)/4)
    print("TOTAL POINTS:", points1)
  #lets the player know that they need to work on a specific course if they failed that course.
  if sciaverage < 50:
    print("Looks like you need to work on science")
  if mathaverage < 50:
    print("Looks like you need to work on math")
  if techaverage < 50:
    print("Looks like you need to work on tech")
  if geoaverage < 50:
    print("Looks like you need to work on geography")
  if engaverage < 50 and level.lower() == "advanced":
    print("Looks like you need to work on english.")

  #same format as player 1 results except for player 2
  if players == 2:
    print(player2, "RESULTS: ")
    print("Science Average:", sciaverage2)
    print("Math Average:", mathaverage2)
    print("Technology Average:", techaverage2)
    print("Geography Average:", geoaverage2)
    if level.lower() == "advanced":
      print("English Average:", engaverage2)
      print("OVERALL AVERAGE:", (sciaverage2+mathaverage2+techaverage2+geoaverage2+engaverage2)/5)
    if level.lower() == "basic":
      print("OVERALL AVERAGE:", (sciaverage2+mathaverage2+geoaverage2+techaverage2)/4)
    print("TOTAL POINTS:", points2)
    if sciaverage2 < 50:
      print("Looks like you need to work on science.")
    if mathaverage2 < 50:
      print("Looks like you need to work on math.")
    if techaverage2 < 50:
      print("Looks like you need to work on tech.")
    if geoaverage2 < 50:
      print("Looks like you need to work on geography.")
    if engaverage2 < 50 and level.lower() == "advanced":
      print("Looks like you need to work on english.")


#QUIZZEZ

#introduces QUIZZEZ
print("*********\n QUIZZEZ \n*********")
print("Welcome to Quizzez, the world's best online learning tool!")

#asks how many players there are
players = int(input("How many users will be using Quizzez today? "))
#ensures that the user only inputs 1 or 2 players
while not(players == 1 or players == 2):
  players = input("Quizzez only supports 1 or 2 players! Please enter a number, 1 or 2: ")
#if there is one player: asks for the player's username and greets them
if players == 1:
  player1 = input("Player 1 username: ")
  print("Hello,", player1)
#if there are 2 players: asks for both player usernames and greets them
if players == 2:
  player1 = input("Player 1 username: ")
  player2 = input("Player 2 username: ")
  print("Hello,", player1, "and", player2)

#asks what level they would like to play
level = input("Would you like to play the advanced or basic level? ")
#makes sure they enter basic or advanced for the level option and not anything else
while not(level == "basic" or level == "advanced"):
  level = input("Would you like to play the advanced or basic level? ")

#adds english to the list of courses if the advanced level is chosen
if level.lower() == "advanced":
  coursemenu.append("ENGLISH")

#1 PLAYER GAME
if players == 1:
  #loops the code so the user can choose more than one course
  while True:
    #prints out all the course options
    for i in coursemenu:
      print(i)
    print("If you would like to exit please type EXIT. If you would like to display your results, please type DISPLAY. It is recomended that you only see results AFTER you have completed all the courses")

    #asks the usr what course they would like to study
    courseChoice = input("Which course would you like to study? ")

    #asks the user to enter a valid course until they enter a valid option
    while not(courseChoice.lower() == "science" or courseChoice.lower() == "math" or courseChoice.lower() == "technology" or courseChoice.lower() == "geography" or courseChoice.lower() == "english" or courseChoice.lower() == "display" or courseChoice == "EXIT"):
      courseChoice = input("That is not a valid course option, try again: ")
    #exits the app if the user would like to leave
    if courseChoice.lower() == "exit":
        exit()
    #displays the science questions if the player chooses science. Then displays the total points the player has.
    elif courseChoice.lower() == "science":
        science(1)
        print(player1, "points:", points1)
    #displays the math questions if the player chooses math. Then displays the total points the player has.
    elif courseChoice.lower() == "math":
        math(1)
        print(player1, "points:", points1)
    #displays the technology questions if the player chooses technology. Then displays the total points the player has.
    elif courseChoice.lower() == "technology":
        tech(1)
        print(player1, "points:", points1)
    #displays the geography questions if the player chooses geography. Then displays the total points the player has.
    elif courseChoice.lower() == "geography":
        geography(1)
        print(player1, "points:", points1)
    #displays the english questions if the player chooses english and if their level is advanced. Then displays the total points the player has.
    elif courseChoice.lower() == "english" and level.lower() == "advanced":
        english(1)
        print(player1, "points:", points1)
    #displays the display screen if display is chosen.
    elif courseChoice.lower() == "display":
      #plays the animation
      picture()
      display()
      #puts a wait time in between
      time.sleep(10)
      #thanks the user and exits the app
      print("Thank you for using Quizzez. See you next time!")
      exit()

#2 PLAYER GAME
if players == 2:
  #loops the code so the user can choose more than one course
  while True:
    #prints out all the course options
    for i in coursemenu:
      print(i)
    print("If you would like to exit please type EXIT. If you would like to display your results, please type DISPLAY. It is recomended that you only see results AFTER you have completed all the courses")

    #asks the usr what course they would like to study
    courseChoice = input("Which course would you like to study? ")

    #asks the user to enter a valid course until they enter a valid option
    while not(courseChoice.lower() == "science" or courseChoice.lower() == "math" or courseChoice.lower() == "technology" or courseChoice.lower() == "geography" or courseChoice.lower() == "english" or courseChoice.lower() == "display" or courseChoice == "EXIT"):
      courseChoice = input("That is not a valid course option, try again: ")
    #exits the app if the user would like to leave
    if courseChoice.lower() == "exit":
        exit()
    #displays the science questions if the player chooses science. Then displays the total points the player has.
    elif courseChoice.lower() == "science":
        science(1)
        print(player1, "points:", points1)
        #Let's the user know that it is player 2's turn
        print(player2)
        #displays the science questions. Then displays the total points the player has.
        science(2)
        print(player2, "points: ", points2)
    #displays the math questions if the player chooses math. Then displays the total points the player has.
    elif courseChoice.lower() == "math":
        math(1)
        print(player1, "points:", points1)
        #Let's the user know that it is player 2's turn
        print(player2)
        #displays the math questions. Then displays the total points the player has.
        math(2)
        print(player2, "points: ", points2)
    #displays the technology questions if the player chooses technology. Then displays the total points the player has.
    elif courseChoice.lower() == "technology":
        tech(1)
        print(player1, "points:", points1)
        #Let's the user know that it is player 2's turn
        print(player2)
        #displays the technology questions. Then displays the total points the player has.
        tech(2)
        print(player2, "points:", points2)
    #displays the geography questions if the player chooses geography. Then displays the total points the player has.
    elif courseChoice.lower() == "geography":
        geography(1)
        print(player1, "points:", points1)
        #Let's the user know that it is player 2's turn
        print(player2)
        #displays the geography questions. Then displays the total points the player has.
        geography(2)
        print(player2, "points:", points2)
    #displays the english questions if the player chooses english and if the level is advanced. Then displays the total points the player has.
    elif courseChoice.lower() == "english" and  level.lower() == "advanced":
        english(1)
        print(player1, "points:", points1)
        #Lets the user know that it is player 2's turn
        print(player2)
        #displays the english questions. Then displays the total points the player has.
        english(2)
        print(player2, "points: ", points2)
    #displays the display screen if display is chosen.
    elif courseChoice.lower() == "display":
      #plays the animation
      picture()
      display()
      #thanks the user
      print("Thank you for using Quizzez. See you next time!")
      #puts a wait time in between
      time.sleep(10)
      #exits the app
      exit()