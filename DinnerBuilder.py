import random

def menuGenerator():
    Verduras = ["Champiñon","Cebolla","Morrón","Pepino"]
    Aderezos = ["Aceite de oliva","Mayonesa","Aceto"]
    Proteínas = ["Atun","Pechuga de pollo","Cereal","Panqueques integrales","Huevos cocido"]
    Acompañantes = ["Yogurt Griego","Vaso de agua","Jugo de limón", "Jugo de pepino con limón","Vaso de avena"]
    itemsDinner = "Condimentar y cocinar con sal u otras especias al gusto: " + random.choice(Verduras) + ", "+ random.choice(Aderezos) +", " + random.choice(Proteínas) +" y "+ random.choice(Acompañantes)
    
    for i in itemsDinner:
        finalMenu = itemsDinner
    
    return(finalMenu)