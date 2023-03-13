from nodo import *

class ListaSimple:
    IdIncrementable = -1
    validación = True
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def AgregarCabeza(self, valor):
       self.IdIncrementable +=1
       if self.validación==True:
            self.cabeza = Nodo(valor,self.IdIncrementable)
            self.cola=self.cabeza
       else: 
           newNodo = Nodo(valor,self.IdIncrementable) 
           self.cabeza.setDirection(newNodo)
           self.cabeza = newNodo 
       self.validación = False
    """
    def EliminarCabeza(self):
        newNodo = self.cola
        while newNodo.getDirection() != self.cabeza: #irá cambiando entre nodos hasta que newNodo sea igual a cabeza
            newNodo=newNodo.getDirection()
      #  print(newNodo.getDato())   necesario para testear, será el dato anterior a la cabeza
        newNodo.setDirection(None)
        self.cabeza  = newNodo 
        self.IdIncrementable-=1"""
    """
    def recorrido (self):    
        newNod = self.cola
        while newNod != None:
            print(str(newNod.getId()),")",newNod.getDato())
            newNod = newNod.getDirection()"""

    def invocar(self, idBuscar):
     newNodo = self.cola
     while newNodo != None:
        if newNodo.getId() == idBuscar:
            return newNodo.getDato()
        newNodo = newNodo.getDirection()
     return None # si se cumple el cliclo y no encontró nada, entonces no retornará nada
    """
    def Modificar(self, idBuscar,newDato):
     newNodo = self.cola
     while newNodo != None:
        if newNodo.getId() == idBuscar:
            return newNodo.setDato(newDato)
        newNodo = newNodo.getDirection()
     return None # si se cumple el cliclo y no encontró nada, entonces no retornará nada"""

    def tamaño(self):
        return self.cabeza.getId()+1
        