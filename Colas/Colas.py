from time import time

class Cola:

    def __init__(self):
        self.cola = []

    def insertar(self,valor):
        self.cola.append(valor)

    def atender(self):
        if len(self.cola)<1:
            print("cola no tiene elementos: ")
            return None
        return self.cola.pop(0)

venta = Cola()
abierto=0
personas=0
precio=0
ventas=[]

for i in range(10):
    nuevo=int(input("Digite 1 si tiene una venta: "))
    precio =int(input("¿Cuál es el precio de la venta?: "))
    if nuevo==1:
        x=time()
        venta.insertar(x)
        personas=personas+1
        ventas.append(precio)
        precio=precio+1
    
    if personas>10:
        print("Se cerró el negocio")

venta.atender()#1
venta.atender()#2
venta.atender()#3
print(ventas)
promedio = ventas[0]+ventas[1]+ventas[2]/3
print(promedio)

    
