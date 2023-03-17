# ejercicio 6
class Persona():
    def __init__(self, nombre, apellido, dni, edad):
      self.__nombre = nombre
      self.__apellido = apellido
      self.__dni = dni
      self.edad = edad
    @property
    def nombre(self):
      return "valido".format(self.__nombre)
    @nombre.setter
    def nombre(self, nombre):
      self.__nombre = nombre
      
    def mostrar(self):
      for Persona in Persona:
        print (Persona)
    def es_mayor_de_edad(edad):
      if edad >= 18:
        print ("es MAYOR")
      else:
        print ("Es menor")
# ejercicio 7      
class Cuenta(Persona):
  def __init__(self,nombre, edad, titular, cantidad):
    self.__titular = Persona
    self.__cantidad = cantidad
  @property
  def titular(self):
    return "este es el titular {}".format(self.__titular)
  def cantidad(self):
    return "su monto es{}".format(self.__cantidad) 
  @cantidad.setter
  def cantidad(self, cantidad):
    self.__cantidad = cantidad
  

def mostrar(self):
    for Cuenta in Cuenta:
      print (Cuenta)
ingreso = ingreso
def ingresar (cantidad, ingreso):
  if ingreso >= 0:
    cantidad = cantidad + ingreso
    return cantidad
  else:
    print (cantidad)
retiro = retiro
def retirar(cantidad, retiro):
  cantidad = cantidad - retiro
  return cantidad
  
# ejercicio 8
class CuentaJoven(Cuenta):
  def __init__(self, nombre, edad, titular, cantidad, bonificacion):
    self.__bonificacion = bonificacion
  @property
  def bonificacion(self):
      return "bonificado".format(self.__bonificacion)
  @bonificacion.setter
  def bonificacion(self, bonificacion):
    self.__bonificacion = bonificacion
  
  def es_titular_valido(edad):
    if edad >= 18 < 25 :
      return True
    else: 
      return False
  def mostrar(self):
      for CuentaJoven in CuentaJoven:
        return ("Cuenta Joven").format(self.__bonificacion)
def retirar(cantidad, retiro, es_titular_valido):
  if es_titular_valido == True:
    cantidad = cantidad - retiro
    return cantidad
  else:
    print("No es valido")
    
