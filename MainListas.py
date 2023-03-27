from ListaSimple import *

class Elemento:
   def __init__(self, NoAtomico, simbolo, NombreE ):
      self.NoAtomico = NoAtomico
      self.simbolo = simbolo
      self.NombreE = NombreE

class Maquina:
   def __init__(self,nombre,NoPines,NoElementos,Listapin, listaElementos):
      self.nombre = nombre
      self.NoPines = NoPines
      self.NoElementos = NoElementos
      self.Listapin = Listapin

class Compuesto:

   def __init__(self,nombre,ListaEUsados):   
      self.nombre = nombre
      self.ListaEUsados = ListaEUsados   