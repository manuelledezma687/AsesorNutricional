import random

def menuGenerator():
    Frutas = ["Frutillas cortadas","Naranjas","1 o 2 Manzanas","Kiwy","1 Banana","Porción de Papaya","Porción de Pera"]
    Proteínas = ["Panqueques","Galletas con Mermelada o Queso crema","1 Arepa","Huevos revueltos","Homelet con verduras","Sandwich de Jamón y queso","Huevo cocido"]
    Bebidas = ["Café","Mate","Yogurt"]
    itemsBreakfast = random.choice(Frutas) +", " + random.choice(Proteínas) +" y "+ random.choice(Bebidas)
    
    for i in itemsBreakfast:
        finalMenu = itemsBreakfast
    
    return(finalMenu)