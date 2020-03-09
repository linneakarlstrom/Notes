# Uppgift 1
# def h():
#     print("h") 
#     return "h" # funktionens värde och syns inte så länge du inte printar hela funktionen

# def f():
#     print("f 1")
#     h()
#     print("f 2")

# def g():
#     print("g 1")
#     f()
#     print(h())
#     print("g 2")  
# g()
# print(h())


# Uppgift 2
# Redogör så utförligt du kan för principer för att uppnå god kvalitet vid skapandet av datorprogram
# Arbeta i delar, i mindre steg
# Läsbarhet: Namngivning, struktur och kommentarer
# Refaktorisera då och då, minska upprepning
# Användartester, gör tester och se att det fungerar då och då


# Uppgift 3
# syntax fel -- du har "stavat fel" i programmet. till exempel glömt ett kolon
# runtime error -- fel som inte "syns" för än du kör programmet. Till exempel att försöka dividera med 0
# semantic error -- egentligen inte fel utan programmet fungerar men det körde inte som du ville
# Ge exempel på ett syntaxfel. Ge exempel på ett annat fel som inte är ett syntaxfel.
# for i in range(4)  # syntaxfel     def percent(x):  # semantic error
                                        #    x/10
#   print(i)



# Uppgift 4
# Skriv ett program (använd minst en for-loop) som ritar ut  följande  figur  av asterisker (OBS: ett blanksteg mellan varje asterisk)
#for i in range(4):
#    print(" * * * * * ")



# Uppfit 5
# Hur avgör du om du ska använda en while-loop eller en for-loop?	
# En while loop används när vi inte vet hur många gånger vi vill loopa, medan med en for loop så använder vi den när vi vet hur många gånger vi vill loopa



# Uppgift 6
# Vilket av följande variabelnamn är i snake case?						
#FIRST_NAME = “kalle”
#firstName = “kalle” -- camelcase
#firstname = “kalle”
#first_name = “kalle” --- snakecase
#FirstName = “kalle” -- Pascalcase


# Uppgift 7
# Skriv kod som skriver ut först och sista bokstaven i en sträng som har namnet word 	
# def g(x):
#    print(x[0])
#    print(x[-1])
#g("word")


# Uppgift 8
# Vad skrivs ut i programmet nedan?
#def f():
#  x = 4    # x is not defined
#def g():
#  print(x)
#f()
#g()

# Uppgift 9
# Vad skrivs ut i programmet nedan?							1p
# x = 4
# while x < 6: # första gången x= 4, andra gången, 5, tredje gången 6 så ut ur while och +1 = 7
#     print(x)
#     x = x + 1
# x = x + 1
# print(x) 

# Uppgift 10
#Vilken datatyp returneras av följande funktioner? 						4p
#a.  # str
#def ask_age():
#    return input(“How old are you?”)

#b. # float
#def with_interest(wealth):
#    return wealth * 1.09

#c. 
#def is_joe(person):
#    return person.first_name == “joe”   # == är equal vilket ger boolean

#d. # none då det inte har ett värde
#def happy():
#    print(“I’m so happy happy happy”)
#    print(12345)   

# Uppgift 11 #Spara det i en csv-fil
# Linn försöker skapa en digital dagbok enligt nedan. Men varje gång hon kör programmet 	
# så är det som att allting är borta och hon får börja om från början. Har du något förslag 
# på vad hon skulle kunna göra för att förbättra sitt program?
# OBS: du behöver inte koda, det räcker att förklara.


# Uppgift 12  
#Du är en grönsakshandlare som just lärt dig Python. Du vill skriva ett eget litet program för
#att hantera dina grönsaker, t.ex. hur många du har av varje sort, vad de kostar, ursprungsland 
#etc. Hur skulle en lämplig datastruktur kunna se ut för ditt grönsaksutbud?
# vegetables = [
#    {"Namn": " "
#    "Amount": " "
#    "Price": " "
#    "Country": " "
#    }
# ]

# Uppgift 13 # 7 sedan 5
# def f(a):
#     print(a - 1)
#     a = 2
# a = 5
# f(a + 3)
# print(a)

# Uppgift 14 
# def volym(side):
# return side**3

# Uppgift 15
# Vilka begrepp saknas?									5p
# a. # operatorer
# +,  -, *, % är exempel på olika  ________ som finns i Python

# b. # modulus # 3
# 15 % 12 uttalas ____________ och är lika med ________

# c. # syntax 
# ______-fel beror ofta på stav- eller skrivfel och är sällan resultatet av ett logiskt tankefel

# d.  # element
# Listans fjärde ___________ är strängen “korv med mos”.

# e.  # errors/buggar
# Har du upptäckt några ________ i ditt program? Nej, det fungerar felfritt.

# Uppgift 16
# Hur gör du för att skriva ut varje element i listan colors med stora bokstäver?
# colors = ["Red","Green","White" ,"Black", "Orange", "Purple", "Brown", "Yellow"]
# for color in colors:
#     print(color.upper())

# Uppgift 17
# def divide(number):
#     if number % 2 == 0 and number % 5 == 0:
#         return  True
#     else:
#         return False

# Uppgift 18 
# 00
# 01
# 10
# 11
# Vad skrivs ut när du kör följande kod?	
# for i in range(2):
#     for j in range(2):
#         print(i, j)
