class Cuenta:
    def __init__(self, titular="Carolina", cantidad=0):
        self.titular = titular
        self.cantidad = cantidad
        
    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad: $", self.cantidad)
        
    def ingresar(self, cantidad):
        self.cantidad += cantidad
        print("Se ingresaron $", cantidad, "en total tenés $",self.cantidad, "pesos")
        
    def retirar(self, cantidad):
        self.cantidad -= cantidad
        print("Se retiraron $", cantidad, "el saldo total es $",self.cantidad, "pesos")
        

cuenta1=Cuenta("Maria", 15000)
cuenta1.mostrar()
cuenta1.ingresar(1500)
cuenta1.retirar(2000)