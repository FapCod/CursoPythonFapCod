class Persona:
    def __init__(self,name):
        self.name = name
   
class Alienigena:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name       

persona= Persona('Jose')
alien= Alienigena('Terer')
print(persona)
print(alien)