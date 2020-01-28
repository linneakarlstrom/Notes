# 1. Skriv ett program som frågar användaren om dess namn och därefter hälsar på användaren med namnet.
# Exempel:
# Vad heter du? <Johanna>
# Hej Johanna!
    # name = input("Vad heter du?")
    # print("Hej", name, "!")

# 2. Vad skrivs ut när du kör följande kod?
# x = 0 
# y = 8
# z = 8
# print("1", x < y)  # x är 0 y är 8. x är mindre än y --> 1 True
# print("2", y < z)  # y är 8 och z är också 8. y är inte mindre än z --> 2 False
# print("3", x == 0) # x är 0 --> 3 True
# print("4", not x == 0) # det är inte sant att x inte är 0. --> 4 False
# print("5", x == "0") # x är inte lika med strängen 0 --> 5 False
# print("6", x == 0 and y == 8) # x är 0 och y är 8 --> 6 True
# print("7", x == 0 and y == 0) # x är 0 men y är inte 0 --> 7 False
# print("8", x == 0 or y == 0) # antingen är x 0 eller y 0. x är 0 --> 8 True

# 3 Skriv kod som skapar en tom lista som heter my_list och en tom dictionary som heter my_dict.
# my_list = [ ]    my_dict = { }

# 4 Skapa en lista med namn på tre personer i rummet.
# name_of_persons = ["Annika", "Linnea", "Hampus"]

for i in range(0,100,2):
    print(i)