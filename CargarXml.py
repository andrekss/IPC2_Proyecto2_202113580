from xml.etree.ElementTree import *
from ListaSimple import *
from MainListas import *

class Cargar:
    
    def __init__(self):
        self.ListaElementos = ListaSimple()
        self.ListaMaquinas = ListaSimple()
        self.ListaCompuestos = ListaSimple()   

    def CargarArchivo (self):
      #Ruta = "/Users/gmg/Desktop/usac 2023/ipc2/release proyecto1/IPC2_Proyecto1_202113580/datos.xml"
      Ruta = input('Escriba la ruta exacta del archivo: ')
      Arbol = parse(Ruta) #cargamos el archivo en la variable Arbol
      raiz = Arbol.getroot() #entramos a la raíz de todo el archivo que sería datosMarte
      self.indicesColores = ListaSimple()
      contador = 0    
      for lista in raiz:
         if contador == 0:
          for elemento in lista:
            NoAtomico = elemento.find('numeroAtomico').text
            simbolo = elemento.find('simbolo').text
            NombreE = elemento.find('nombreElemento').text
            Element = Elemento(NoAtomico,simbolo,NombreE)
            self.ListaElementos.AgregarCabeza(Element)
         elif contador == 1:
            for maquina in lista:
              nombre = maquina.find('nombre') 
              NoPines = maquina.find('numeroPines')
              NoElementos = maquina.find('numeroElementos')
              pin =maquina.find('pin')
              Elements = maquina.find('elemento')
              #revisar
         elif contador == 2:
           for compuesto in lista:
            nombreC = compuesto.find('nombre').text
            elemetos = compuesto.find('elementos')
            self.ListaElementosC = ListaSimple()
            for elemento in elemetos:
              Eleme = elemento.find('')
              

           
      contador +=1