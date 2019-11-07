print("**************************************")
print("Välkommen till Biografigenerator 3000!")
print("**************************************")

name = input("Hej vad heter du bish?")
if name == "Bish" or name == "bish":
    print("BRA JOBBAT MA BISH")
else:
    print("Du är ju korkad")
age = input("ÅLDER NU BISH!")
gender = input("Är du man eller kvinna? (skriv man/kvinna) ")
number_of_brothers = int(input("Hur många bröder har du? "))
number_of_sisters = int(input("Hur många systrar har du? "))

number_of_siblings = number_of_brothers + number_of_sisters

if gender == "kvinna":
    print(name + " är " + age + " år gammal"+ " och är kvinna ")
else: 
    print(name + " är " + age + " år gammal"+ " och är man ")
print(name + " har " +  str(number_of_siblings) + " syskon")