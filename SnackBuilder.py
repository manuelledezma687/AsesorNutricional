import random

def menuGenerator():
    Snacks = ["Rodajas de jamón","Galletas de agua","Pan árabe","Frutos secos","Snacks celiacos","Frutos rojos","Frutos cítricos"]
    Acompañantes = ["Yogurt Griego","Vaso de agua","Jugo de limón", "Jugo de pepino con limón","Vaso de avena"]
    itemsSnack = "Su Merienda: " +random.choice(Snacks) + " y "+ random.choice(Acompañantes)
    
    return(itemsSnack)
