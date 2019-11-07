print("Welcome to Oregon Trail!")
 
print("A. Banker")
print("B. Carpenter")
print("C. Farmer")
 
user_input = input("What is your occupation? ")
 
if user_input == "A":
    money = 100
elif user_input == "B":
    money = 70
elif user_input == "C":
    money = 50
 
print("Great! you will start the game with", money, "dollars.")