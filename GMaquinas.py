from graphviz import *
from opciones import *
import random
from memory.Colas import *

class Graficar:

    def __init__(self,listaMaqs,listaElement,Elementos):
         self.dot = Digraph(comment='Maquinas', format='pdf')
         self.listaMaqs = listaMaqs
         self.listaElement = listaElement
         self.colores = ListaSimple()
         self.Elementos = Elementos
         self.Colores = cola()

    def CrearColores(self):
      #tupla rgb
      tupla = ListaSimple()
      for i in range(self.Elementos):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        #Emepezamos a Apilar
        tupla.AgregarCabeza((red,green,blue))

      #tupla a codigo rgb y lo agregamos a la pila
      for i in range(tupla.tamaño()):
        self.Colores.push('#{0:02X}{1:02X}{2:02X}'.format(*tupla.invocar(i))) 

    def GraficarMáquinas(self):
        self.CrearColores()
        espacio = '                                  '

        for i in range(self.listaMaqs.tamaño()): # maquinas
          self.dot.node(f'{i}',shape='box', width = '0.1', height= '0.1',label='Nombre: '+str(self.listaMaqs.invocar(i).nombre)+'\n'+'Número de pines: '+str(self.listaMaqs.invocar(i).NoPines)+'\n'+'Número de elementos: '+str(self.listaMaqs.invocar(i).NoElementos),fillcolor='skyblue', style="filled")
          for j in range(self.listaMaqs.invocar(i).Listapin.tamaño()): # pin por pin
           a= 0
           for k in range(self.listaMaqs.invocar(i).Listapin.invocar(j).tamaño()): # elemento por elemento
            a+=1
            if k == 0:
             self.dot.node(f'{i},{j}', shape='circle', width = '0.1', height= '0.1',label='-',fillcolor='gray', style="filled") 
           
            for l in range(self.listaElement.tamaño()):
              if self.listaElement.invocar(l).simbolo == self.listaMaqs.invocar(i).Listapin.invocar(j).invocar(k):
               NoAtomic = str(self.listaElement.invocar(l).NoAtomico)
               Nombre = str(self.listaElement.invocar(l).NombreE)
               color = str(self.Colores.invoke(l)) #asignamos un color de la pila

            self.dot.node(f'{i},{j},{k}', shape='square', width = '0.1', height= '0.1',label=NoAtomic+espacio+'\n\n\n\n'+str(self.listaMaqs.invocar(i).Listapin.invocar(j).invocar(k))+'\n\n\n\n'+Nombre,fillcolor=color, style="filled")
            if 0<j <(self.listaMaqs.invocar(i).Listapin.tamaño()):
               self.dot.edge(f'{i},{j-1},{k}',f'{i},{j},{k}', style='invis')
               if a==1:
                self.dot.edge(f'{i},{j-1}',f'{i},{j}', style='invis')
               
        self.dot.render('maquinas', view=True)          