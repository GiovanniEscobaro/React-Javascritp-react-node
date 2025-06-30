class Persona():
    def __init__(self,nombre,apellido):
        self.__nombre=nombre # privado para la class
        self.apellido=apellido # publico para la class
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,valor):
        self.__nombre=valor
    def nombre_completo(self):
        return f' {self.__nombre} {self.apellido}' 

class Adulto(Persona):
    def __init__(self,nombre,apellido,edad):
        super().__init__(nombre,apellido)
        self.edad=edad
    def nombre_completo(self):
        return f' {self.get_nombre()} {self.apellido} {self.edad}'
        
#persona_1=Persona(nombre='Giovanni',apellido='Escobar')
#persona_2=Persona(nombre='Pepito',apellido='Peres')
adulto_1=Adulto('Pepito', 'Perez',18)
print({adulto_1.nombre_completo()} )
#print(persona_1.nombre_completo())
#print(persona_2.nombre_completo())
#print(persona_1.apellido) 

