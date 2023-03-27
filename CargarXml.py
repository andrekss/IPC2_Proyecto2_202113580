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
              pins =maquina.find('pin')
              self.listaPines = ListaSimple()
              for pin in pins:
               Elements = pin.find('elementos')
               ListaElementosPin = ListaSimple()
               for elemento in Elements:
                 element = elemento.find('elemento').text
                 ListaElementosPin.AgregarCabeza(element)
               self.listaPines.AgregarCabeza(ListaElementosPin)  
              maq = Maquina(nombre,NoPines,NoElementos,self.listaPines)
              self.ListaMaquinas.AgregarCabeza(maq) 
         elif contador == 2:
           for compuesto in lista:
            nombreC = compuesto.find('nombre').text
            elemetos = compuesto.find('elementos')
            self.ListaElementosC = ListaSimple()
            for elemento in elemetos:
              Eleme = elemento.find('elemento').text
              self.ListaElementosC.AgregarCabeza(Eleme)
            comp = Compuesto(nombreC,self.ListaElementosC)
            self.ListaCompuestos.AgregarCabeza(comp)  
         contador +=1

      print('--------Lista de Elementos--------')
      for i in range(self.ListaElementos.tamaño()):
        print('Número atómico:',self.ListaElementos.invocar(i).NoAtomico)
        print('Símbolo:',self.ListaElementos.invocar(i).simbolo)
        print('Número del elemento:',self.ListaElementos.invocar(i).NombreE)
      
      print('--------Lista de Máquinas--------')  
      for i in range(self.ListaMaquinas.tamaño()):
        print('Nomre:',self.ListaMaquinas.invocar(i).nombre)
        print('Número de pines:',self.ListaMaquinas.invocar(i).NoPines)
        print('Número de Elementos:',self.ListaMaquinas.invocar(i).NoElementos)
        print('Lista de pines')
        for j in range(self.ListaMaquinas.invocar(i).Listapin.tamaño()):
         print('lista de elementos del pin',str(j+1))
         for k in range(self.ListaMaquinas.invocar(i).Listapin.invocar(j).tamaño()): 
          print('Elemento:',self.ListaMaquinas.invocar(i).Listapin.invocar(j).invocar(k))

      print('--------Lista de Compuestos--------')    
      for i in range(self.ListaCompuestos.tamaño()):
        print('Nombre del compuesto:',self.ListaCompuestos.invocar(i).nombre)
        print('lista de elementos')
        for j in range(self.ListaCompuestos.invocar(i).ListaEUsados.tamaño()):
          print('Elemento:',self.ListaCompuestos.invocar(i).ListaEUsados.invocar(j))