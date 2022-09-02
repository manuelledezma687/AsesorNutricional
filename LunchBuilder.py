import random

def menuGenerator():
    Verduras = ["Zanahoria","Tomate","Champiñon","Cebolla", "Palta","Morrón","Acelgas","Espinaca","Berenjena" ,"Pepino"]
    Aderezos = ["Aceite de oliva","Mayonesa","Aceto"]
    Proteínas = ["Milanesa al horno","Albóndigas de carne","Atún","Pechuga de pollo","Camarones o pescado","Carne magra"]
    Acompañantes = ["Arroz","Pan integral","Fajitas","Quinoa","Pasta de arroz","Pasta integral o de arroz","Papas al horno o en puré"]
    itemsLunch = "Su Almuerzo: " +"Condimentar y cocinar con sal u otras especias al gusto: " + random.choice(Verduras) + ", "+ random.choice(Aderezos) +", " + random.choice(Proteínas) +" y "+ random.choice(Acompañantes)
    
    return(itemsLunch)
