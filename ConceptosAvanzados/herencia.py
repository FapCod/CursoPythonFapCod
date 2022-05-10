class Animal:
    def patas(self,number):
        self.numero = number
    def mostrarPatitas(self):
        print("{} patitas".format(self.numero))
    


class Mascota:
    def comer(self):
        print("Comiendo")
    def dormir(self):
        print("Duermiendo")
    
    

class Perro(Animal,Mascota):
    def __init__(self,nombre):
        self.nombre = nombre
    def ladra(self):
        print("{} esta Ladrando".format(self.nombre))
        
    def dormir(self):
        print("{} esta durmiendo".format(self.nombre))
   

class Loro(Mascota):
    def __init__(self,nombre):
        self.nombre = nombre
    def habla(self):
        print("{} esta hablando".format(self.nombre))

class Gato(Mascota):
    def __init__(self,nombre):
        self.nombre = nombre
    def maullido(self):
        print("{} esta maullando".format(self.nombre))

perro = Perro('Firulais')
perro.dormir()
perro.comer()
perro.ladra()
perro.patas(4)
perro.mostrarPatitas()

""" print("Loro details")
loro = Loro('Repetin')
loro.dormir()
loro.comer()
loro.habla()
print("Gato details")

gatito= Gato('Miua')
gatito.dormir()
gatito.comer()
gatito.maullido() """