# anteckningar
# en operator är + - osv. Det finns olika sorters operatorer.
# Aritmetiska (arithmetic) + - / % // * **
# Jämförelse (comparision) == (ifall de är lika) <  >  <=  =>  != (ej lika med)
# logiska (logical) and, or , not

# if, else är villkorsatser. När ett villkor ska avögra (conditional statement - villkor sats)

# Ditt quiz ska ha alternativa frågor (A,B,C, osv.). Det ska vara med if.
# ifall du vill ha resultat av quiz skriv score = 0 questions = 0
# questions = questions + 1

# print("A. Dessert topping")
# print("B. Desert topping")
# user_input = input("A cherry is a: ")

# if user_input.upper() == "A":
   # print("Correct!")
# else:
   # print("Incorrect.")

# my_list = [5]
#for i in range(5):
 #   my_list.append(i) den lägger till 0,1,2,3,4 för att for i in range(5)betyder att den ska printa ut 0,1,2,3,4
#print(my_list)

# du får ej ändra på en tuple men med en lista får du

#print("Simpson" + "College") printar ihop så simpsoncollege
#print("Simpson" + "College"[1]) printar simpsono för att den tar simpson + andra bokstaven i college
#print( ("Simpson" + "College")[1] ) printar i för att det är andra elementet i det.

#word = "Simpson"
#for i in range(3):
 #   word += "College"
#print(word) printar simpsoncollegecollegecollege för att den printar ut college 3 gånger + simpson

#my_list = []
#for i in range(5):
 #  question = input("Skriv en siffra")
  # my_list.append(question)
#print()
# tom dictonary "variabel" = {}
# ta bort värde = del
# två key_value par = {"title" : "något"}
# "variabel".keys() får man ut alla 'nycklar' i dictionary
# iterera betyder repetera
# foo = dict(first_name='Einar')
#print(foo)
# to add a key-value in python --> "variabel"[""Key""] = ""Value""

# Copy of the array to sum
#my_list = [5,76,8,5,3,3,56,5,23]
 
# Initial sum should be zero
#list_total = 0
 
# Loop from 0 up to the number of elements
# in the array:
#for i in range(len(my_list)): # len(my_list) för att annars förstår den inte hur den ska göra. listan kan inte göras till en integer. 
# Visst listan är 9 lång men då måste du isåfall lägga till saker.
    # Add element 0, next 1, then 2, etc.
 #   list_total += my_list[i]
 
# Print the result
#print(list_total)

#my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
# Initial sum should be zero
#list_total = 0
# Loop through array, copying each item in the array into
# the variable named item.
#for item in my_list:
    # Add each item
 #   list_total += item
# Print the result
#print(list_total)

#def a(x):
 #   x = x + 1 
#x = 3
#a(x)
#print(x) This will only print 3 because here we have 2 different variables. X inside the function and x outside.
#it would be the same as long as the function does not change the value


def minlista(list): 
   output = ""
   for item in list:
        output += str(item)
   return output
