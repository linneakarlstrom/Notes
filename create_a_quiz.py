score = 0

print("Hello there! Welcome to my quiz!\nAre you ready? If not, then I hope so.\nGood luck!")
print("----------------------------------------")

# Question 1
print("Question 1")
answer1 = input("Imagine you're in a dark room that is empty with nothing in it. There are no windows or doors. What is the easiest way to escape? \nA. Stop imagining that you are in a dark room.\nB. Die of course.\nC. Wait.\nD. Dig a hole in the ground with your bare hands.\nAnswer:")
if answer1.upper() == "A" or answer1 == "stop imagining you're in a dark room":
    score += 1
    print("Yay! Correct answer!")
    print("Score:", score)
    print("\n")
else:
   print("Incorrect! The answer is A.Stop imagining you're in a dark room.")
   print("Score:", score )
   print("\n")

# Question 2
print("Question 2")
answer2 = input("As the Titanic headed out to sea, what did the Captain say to the first officer?\nA.'Take her to sea Mr. Murdock, lets stretch her legs'.\nB.'Get away from the wheel you jerk, I'm driving'.\nC.'Pleeeeeeeeeeease don't make me go. Somtin bad goin to happen'. \
\nD.'My boat, tee hee, my boat, tee hee, my boat, tee hee, can I ring the bell, tee hee.'\nAnswer:")
if answer2.upper() == "A" or answer2 == "'Take her to sea Mr. Murdock, lets stretch her legs'":
    score += 1
    print("Yay! Correct answer!")
    print("Score:", score)
    print("\n")
else:
   print("Incorrect! The answer is A.'Take her to sea Mr. Murdock, lets stretch her legs'")
   print("Score:", score )
   print("\n")

# Question 3
print("Question 3")
answer3 = input("If you look you cannot see me.If you can see me you cannot see anything else. I can make anything you want to happen, \
but later on everything will go back to normal. What am I?\nA. Air.\nB. Nothing,\nC. Imagination.\nD. Other.\nAnswer:")
if answer3.upper() == "C" or answer3 == "imagination":
    score += 1
    print("Yay! Correct answer!")
    print("Score:", score)
    print("\n")
else:
   print("Incorrect! The answer is C.Imagination.")
   print("Score:", score )
   print("\n")

# Question 4
print("Question 4")
answer4 = input("The titanic was powered by\nA. Thousands of hamsters' running inside little wheels. \nB. The third class passengers rowing \nC. 16 giant steam boilers \
\nD. The crew members 'hocking lugies off the sterm all at once \nAnswer:")
if answer4.upper() == "C" or answer4 == "16 giant steam boilers":
    score += 1
    print("Yay! Correct answer!")
    print("Score:", score)
    print("\n")
else:
   print("Incorrect! The answer is C.16 giant steam boilers")
   print("Score:", score )
   print("\n")

# Question 5
print("Question 5")
answer5 = input("If your car begins to hydroplane (Hydroplaning means that water separates the tires from the ground and causes it to lose traction. You feel out of control.) you should:\nA. Reduce your speed and let the car decelerate.\nB. Pump the breaks repeatedly.\nC. Immediatly slam the brakes.\
\nD. Do nothing and allow your car to turn into the plane it has always dreamed of.\nAnswer:")
if answer5.upper() == "D" or answer5 == "do nothing and allow your car to turn into the plane it has always dreamed of.":
    score += 1
    print("Yay! Correct answer!")
    print("Score:", score)
    print("\n")
else:
   print("Incorrect! The answer is D. Do nothing and allow your car to turn into the plane it has always dreamed of.")
   print("Score:", score )
   print("\n")

# Question 6
print("Question 6")
answer6 = input("When was Albert Einstein born? \nA.In Switzerland \nB.In Germany \nC.In United States \
\nD.In Israel.\nE.None of the above. \nAnswer:")
if answer6.upper() == "E" or answer6 == "none of the above":
    score += 1
    print("Yay! Correct answer!")
    print("Score:", score)
    print("\n")
else:
   print("Incorrect! The answer is E.None of the above")
   print("Score:", score )
   print("\n")

# Question 7
print("Question 7")
answer7 = input("Mental break time. This is the last question of the quiz. You deserve a easy question. What is 1 + 1?\nA. Not this one. \nB. Still not this one.\nC. 2\nD. You've gone too far, go back to C.\nAnswer:")
if answer7.upper() == "C" or answer7 == "2":
    score += 1
    print("Yay! Correct answer!")
    print("Score:", score)
    print("\n")
else:
   print("Incorrect! The answer is C. 2")
   print("Score:", score )

   # Result
print()
print("You got a total score of", str(score), "out of 7.")
print("That means you got", str(score / 7 * 100),"%", " of the answers correct!")