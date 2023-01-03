def miam(type:str, saison:str):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "ete":
        print("poire, fraise, cassis")
    elif type == "legumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legumes" and saison == "ete":
        print("artichaut, aubergine, navet")

miam("fruits","hiver")
miam("fruits","ete")
miam("legumes","hiver")
miam("legumes","ete")