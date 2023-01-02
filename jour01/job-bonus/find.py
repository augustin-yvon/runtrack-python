str = "constitution"
nbr = 1
for i in (str):
    if i == "e":
        print("Cette chaîne contient un e")
        nbr = 0
    else:
        nbr+=1
        if nbr == len(str):
            print("Cette chaîne ne contient pas de e")

        
    