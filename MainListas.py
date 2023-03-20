from ListaSimple import *

class Elemento:
   def __init__(self, NoAtomico, simbolo, NombreE ):
      self.NoAtomico = NoAtomico
      self.simbolo = simbolo
      self.NombreE = NombreE

class Maquina:
   def __init__(self,nombre,NoPines,NoElementos,pin, listaElementos):
      self.nombre = nombre
      self.NoPines = NoPines
      self.NoElementos = NoElementos
      self.pin = pin
      self.listaElementos = listaElementos

class Compuesto:

   def __init__(self,nombre,ListaEUsados):   
      self.nombre = nombre
      self.ListaEUsados = ListaEUsados   