import random

class RecipeBook:

    def __init__(self):
        pass

    def breakfast(self):
        Fruits = ["Frutillas cortadas","Naranjas","1 o 2 Manzanas","Kiwi","1 Banana","Porción de Papaya","Porción de Pera"]
        Proteins = ["Panqueques","Galletas con Mermelada o Queso crema","1 Arepa","Huevos revueltos","Homelet con Vegetables","Sandwich de Jamón y queso","Huevo cocido"]
        drinks = ["Café","Mate","Yogurt"]
        return "Su Desayuno: " + random.choice(Fruits) +", " + random.choice(Proteins) +" y "+ random.choice(drinks)


    def lunch(self):
        Vegetables = ["Zanahoria","Tomate","Champiñon","Cebolla", "Palta","Morrón","Acelgas","Espinaca","Berenjena" ,"Pepino"]
        dressings = ["Aceite de oliva","Mayonesa","Aceto"]
        Proteins = ["Milanesa al horno","Albóndigas de carne","Atún","Pechuga de pollo","Camarones o pescado","Carne magra"]
        Companions = ["Arroz","Pan integral","Fajitas","Quinoa","Pasta de arroz","Pasta integral o de arroz","Papas al horno o en puré"]
        return "Su Almuerzo: " +"Condimentar y cocinar con sal u otras especias al gusto: " + random.choice(Vegetables) + ", "+ random.choice(dressings) +", " + random.choice(Proteins) +" y "+ random.choice(Companions)


    def snack(self):
        Snacks = ["Rodajas de jamón","Galletas de agua","Pan árabe","Frutos secos","Snacks celiacos","Frutos rojos","Frutos cítricos"]
        Companions = ["Yogurt Griego","Vaso de agua","Jugo de limón", "Jugo de pepino con limón","Vaso de avena"]
        return "Su Merienda: " +random.choice(Snacks) + " y "+ random.choice(Companions)


    def dinner(self):
        Vegetables = ["Champiñon","Cebolla","Morrón","Pepino"]
        dressings = ["Aceite de oliva","Mayonesa","Aceto"]
        Proteins = ["Atún","Pechuga de pollo","Cereal","Panqueques integrales","Huevos cocido"]
        Companions = ["Yogurt Griego","Vaso de agua","Jugo de limón", "Jugo de pepino con limón","Vaso de avena"]
        return "Su Cena: " +"Condimentar y cocinar con sal u otras especias al gusto: " + random.choice(Vegetables) + ", "+ random.choice(dressings) +", " + random.choice(Proteins) +" y "+ random.choice(Companions)
