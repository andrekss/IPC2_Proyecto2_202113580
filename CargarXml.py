from xml.etree.ElementTree import *
from memory.ListaSimple import *
from memory.MainListas import *
from tkinter import messagebox
import subprocess
import sys


class Cargar:
    
   def __init__(self):
        self.ListaElementos = ListaSimple()
        self.ListaMaquinas = ListaSimple()
        self.ListaCompuestos = ListaSimple()
        self.Ruta = ''

   def LimpiarMemoria(self):
     #terminamos el primer proceso
     subprocess.Popen(['python','main.py'])
     
     #iniciamos el otro
     sys.exit()
    

   def CargarArchivo (self,entrada):
      #Ruta = "/Users/gmg/Desktop/usac 2023/ipc2/release proyecto1/IPC2_Proyecto1_202113580/datos.xml"
    self.Ruta= str(entrada.get())           
    if self.Ruta != '':
     try: 
      Arbol = parse(self.Ruta) #cargamos el archivo en la variable Arbol
      raiz = Arbol.getroot() #entramos a la raíz de todo el archivo que sería config
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
              nombre = maquina.find('nombre').text 
              NoPines = maquina.find('numeroPines').text
              NoElementos = maquina.find('numeroElementos').text
              self.listaPines = ListaSimple()
              #recorremos la maquina
              for pin in maquina:
                  #aceptará los iterales
                  self.ListaElementosPin = ListaSimple()
                  for elementos in pin:
                    for elemento in elementos:
                      element = elemento.text
                      self.ListaElementosPin.AgregarCabeza(element)
                    self.listaPines.AgregarCabeza(self.ListaElementosPin)
              maq = Maquina(nombre,NoPines,NoElementos,self.listaPines)     
              self.ListaMaquinas.AgregarCabeza(maq)   
         elif contador == 2:
          for compuesto in lista:
            nombreC = compuesto.find('nombre').text
            elemetos = compuesto.find('elementos')
            self.ListaElementosC = ListaSimple()
            for elemento in elemetos:
              Eleme = elemento.text
              self.ListaElementosC.AgregarCabeza(Eleme)
            comp = Compuesto(nombreC,self.ListaElementosC)
            self.ListaCompuestos.AgregarCabeza(comp)  
         contador +=1       
        
      #ordenar elementos por numero atómico
      self.Imprimir(True,True,True)    
     except: # si ocurre algún error lo avisará
      messagebox.showerror("Error", "El archivo XML no tiene la estructura deseada\n o no es el archivo correcto") 
   
   def AñadirElemento(self,numero,simbolo, nombre):
    paso = True
    numeroInt = str(numero.get())
    simboloString = str(simbolo.get())
    nombreString = str(nombre.get())
    print('Numero:',numeroInt)
    print('simbolo:',simboloString)
    print('nombre:',nombreString)

    if numeroInt and simboloString and nombreString: # tienen que estar llenos 
     for i in range(self.ListaElementos.tamaño()): # verificamos que no este en la lista
      if str(self.ListaElementos.invocar(i).NoAtomico) == numeroInt or str(self.ListaElementos.invocar(i).simbolo) == simboloString or str(self.ListaElementos.invocar(i).NombreE) == nombreString:
       paso = False
     if paso: 
      numeroInt = int(numeroInt) 
      elementoExtra = Elemento(numeroInt,simboloString,nombreString)
      self.ListaElementos.AgregarCabeza(elementoExtra)
      self.Imprimir(True,False,False)
     else:
      messagebox.showwarning("Advertencia","Estos datos ya estan en memoria")  
    else:
      messagebox.showinfo("Información","Faltan datos o no hay") 
   
   
   def Imprimir(self,elm,Maqs,comps):
     if elm : 
      print('--------Lista de Elementos--------')
      for i in range(self.ListaElementos.tamaño()):
        print('Número atómico:',self.ListaElementos.invocar(i).NoAtomico)
        print('Símbolo:',self.ListaElementos.invocar(i).simbolo)
        print('Número del elemento:',self.ListaElementos.invocar(i).NombreE)
        print('*************************************')
     if Maqs:
      print('--------Lista de Máquinas--------')  
      for i in range(self.ListaMaquinas.tamaño()):
        print('Nombre:',self.ListaMaquinas.invocar(i).nombre)
        print('Número de pines:',self.ListaMaquinas.invocar(i).NoPines)
        print('Número de Elementos:',self.ListaMaquinas.invocar(i).NoElementos)
        print('--->Lista de pines<---')
        for j in range(self.ListaMaquinas.invocar(i).Listapin.tamaño()):
         print('--->lista de elementos del pin',str(j+1)+'<---')
         for k in range(self.ListaMaquinas.invocar(i).Listapin.invocar(j).tamaño()): 
          print('Elemento:',self.ListaMaquinas.invocar(i).Listapin.invocar(j).invocar(k))
        print('*************************************')  
     if comps:
      print('--------Lista de Compuestos--------')    
      for i in range(self.ListaCompuestos.tamaño()):
        print('Nombre del compuesto:',self.ListaCompuestos.invocar(i).nombre)
        print('--->lista de elementos<---')
        for j in range(self.ListaCompuestos.invocar(i).ListaEUsados.tamaño()):
          print('Elemento:',self.ListaCompuestos.invocar(i).ListaEUsados.invocar(j))
        print('*************************************')       

