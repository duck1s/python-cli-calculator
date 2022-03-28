def rekenmachine():
    som = input("Som: ")
    num01 = som.split()[0]
    num02 = som.split()[2]

    if "+" in som or "plus" in som:
        antwoord = (float(num01) + float(num02))
        print("Antwoord: " + str(antwoord))
        print(" ")
        rekenmachine()
    if "-" in som or "min" in som:
        antwoord = (float(num01) - float(num02))
        print("Antwoord: " + str(antwoord))
        print(" ")
        rekenmachine()
    if "x" in som or "*" in som or "X" in som or "keer" in som:
        antwoord = (float(num01) * float(num02))
        print("Antwoord: " + str(antwoord))
        print(" ")
        rekenmachine()
    if ":" in som or "/" in som or "delen door" in som or "gedeel" in som:
        antwoord = (float(num01) / float(num02))
        print("Antwoord: " + str(antwoord))
        print(" ")
        rekenmachine()
    else:
        print("Syntax Error")
        print(" ")
        rekenmachine()

rekenmachine()