tiempoLlegada = float(input("Tiempo de llegada (Digite el número de la hora de llegada de la primera persona, despúes marque un punto y digite los minutos, ej: 7.45): "))
tiempoApertura = float(input("Tiempo de llegada (Digite el número de la hora de apertura, despúes marque un punto y digite los minutos, ej: 7.45): "))
Lista = []

while tiempoLlegada < tiempoApertura:
    print("Aún no abre el negocio, son las: ", tiempoLlegada)
    print("El negocio abre a las ", tiempoApertura)
    tiempoLlegada = float(input("Tiempo de llegada (Digite el número de la hora de llegada de la siguiente persona, despúes marque un punto y digite los minutos, ej: 7.45): "))
    Lista.append(tiempoLlegada)
print(Lista)