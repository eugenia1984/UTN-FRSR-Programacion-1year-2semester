class Perros(object): # Declaramos la clase principal Perros
    def __init__(self, nombre, peso): #Definimos los parámetros 
        self.__nombre = nombre #Declaramos los atributos (privados ocultos)
        self.__peso = peso

    @property
    def nombre(self): # Definimos el método para obtener el nombre
        return self.__nombre #Aquí simplemente estamos retornando el atributo privado oculto

    @property
    def peso(self): # Definimos el método para obtener el peso
        return self.__peso # Aquí simplemente estamos retornando el atributo privado oculto

# Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.
# Ahora vamos a utilizar setter y deleter para modificarlos
    @nombre.setter #Propiedad SETTER
    def nombre(self, nuevo):
        print ("Modificando nombre..")
        self.__nombre = nuevo
        print ("El nombre se ha modificado por")
        print (self.__nombre) # Aquí vuelvo a pedir que retorne el atributo para confirmar

    @nombre.deleter # Propiedad DELETER
    def nombre(self): 
        print("Borrando nombre..")
        del self.__nombre

    """
    def __del__(self):
        print(f"Persona: {self.__nombre} {self.__peso}")
    """    
        

# Instanciamos
Tomas = Perros('Tom', 27)
# Imprimimos el nombre de Tomas. Se hace a través de getter
# Que en este caso como esta luego de property lo toma como el primer método.
print (Tomas.nombre)
"""
Tom
"""
# Cambiamos el atributo nombre que se hace a través de setter
Tomas.nombre = 'Tomasito' 
"""
Modificando nombre..
El nombre se ha modificado por
Tomasito
"""
# Borramos el nombre utilizando deleter
del Tomas.nombre 
"""
Borrando nombre..
"""

# Atributo read-only, es un atributo privado (encapsulado) que no tiene el metodo set
# la difernecia entre el GETTER y SETTER es que en el SETTER recibo un parametro para modificarlo