temperature = int(input("Hur många grader är det ute?"))
sunny = True

if temperature < 20:
    print("Det börjar bli lite höstkänsla")
    if sunny:
        print("Men det är i alla fall lite sol.")
    else:
        print("Vart i hela friden är solen?")
else:
    print("Det är fortfarande sommar i luften")