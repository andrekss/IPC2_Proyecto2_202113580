from graphviz import *
from tkinter import messagebox
from memory.ListaSimple import *
from graphviz import *
from memory.CompuestosA import *

class Analizar:

    def __init__(self,ListaMaqs,ListaComp,color,forma):
        self.ListaMaqs = ListaMaqs
        self.ListaComp = ListaComp
        self.color = color
        self.forma = forma
        self.ListaCompuestosAnalizados = ListaSimple()

    def Analisis(self,NombreM, NombreC):
      self.dot = Digraph(comment='Analisis', format='pdf')      
      Maquina = NombreM.get()
      Compuesto = NombreC.get() 
      print('')
      print('Maquina:',Maquina)
      print('Compuesto:',Compuesto)
      Ad = 'Adelante'
      At = '  Atras '
      Es = ' Esperar'
      Fu = 'Fusionar'

      if Maquina and Compuesto:

        Maq = self.MaquinaListP(Maquina)
        Comp = self.CompuestoListE(Compuesto)
       
        CoordenadaPin =  ListaSimple()
        recorreElemento = 0

        Seguir = True
        segundo = 1 

        
        print('-----------------')
        print('Segundo',segundo)

        listaTiempos = ListaSimple()
        ListaAccions = ListaSimple() 
        for j in range(Maq.tamaño()):  
                          
         self.Guardar(j,Ad,ListaAccions)

         if j ==0:
          self.dot.node(f'pin {j}', shape=f'{self.forma}',width = '0.1', height= '0.1',fillcolor ='gray',label='Construir\n'+str(Compuesto), style="filled")   
         self.dot.node(f'pin {j+1}', shape=f'{self.forma}', width = '0.1', height='0.1',fillcolor ='red', style="filled")
         self.dot.edge(f'pin {j}',f'pin {j+1}',style = 'invis')
         if j == 0: 
          self.dot.node(f'{j},{segundo}', shape=f'{self.forma}', width = '0.1', height= '0.1',fillcolor ='gray',label='Segundo '+str(segundo), style="filled")  
         
         self.dot.node(f'{j+1},{segundo}', shape=f'{self.forma}', width = '0.1', height='0.1',fillcolor =f'{self.color}',label= str(Ad), style="filled")
         self.dot.edge(f'{j},{segundo}',f'{j+1},{segundo}',style= 'invis')
         CoordenadaPin.AgregarCabeza(0) 
         print('pin',str(j+1)+':',Ad)
        print('-----------------')
        time = tiempo(segundo,ListaAccions)
        listaTiempos.AgregarCabeza(time)        


        while Seguir:
         segundo +=1
         print('-----------------')
         print('Segundo',segundo)
         primeraVez = False
         ListaAccions = ListaSimple()
         for j in range(Maq.tamaño()): #recorremos pin por pin 
             if j == 0: 
              self.dot.node(f'{j},{segundo}', shape=f'{self.forma}', width = '0.1', height= '0.1',fillcolor ='gray',label='Segundo '+str(segundo), style="filled")                    
                    # si el primer compuesto es igual al primero del pin
             if Comp.invocar(recorreElemento) == Maq.invocar(j).invocar(CoordenadaPin.invocar(j)) and (primeraVez == False):     
               print('pin',str(j+1)+':',Fu,Comp.invocar(recorreElemento),'<--------')
               self.dot.node(f'{j+1},{segundo}', shape=f'{self.forma}', width = '0.1', height='0.1',fillcolor ='purple',label= str(Fu)+' '+str(Comp.invocar(recorreElemento)), style="filled")
               self.dot.edge(f'{j},{segundo}',f'{j+1},{segundo}',style= 'invis')
               self.Guardar(j,Fu+' '+str(Comp.invocar(recorreElemento)),ListaAccions)
               recorreElemento +=1
               primeraVez = True
                
             elif Comp.invocar(recorreElemento) == Maq.invocar(j).invocar(CoordenadaPin.invocar(j)) and primeraVez:
                where = self.Movimientos(Maq,j,Comp,recorreElemento)
                self.movs(where,CoordenadaPin,j,Ad,At,Es,Maq,Comp,recorreElemento,segundo,ListaAccions)
                #print('pin',str(j+1)+':',Es)
             elif Comp.invocar(recorreElemento) != Maq.invocar(j).invocar(CoordenadaPin.invocar(j)): 

               where= self.Movimientos(Maq,j,Comp,recorreElemento)
               self.movs(where,CoordenadaPin,j,Ad,At,Es,Maq,Comp,recorreElemento,segundo,ListaAccions)
         print('-----------------')
         time = tiempo(segundo,ListaAccions)
         listaTiempos.AgregarCabeza(time)             

         if recorreElemento == Comp.tamaño():
            comps = CompuestoAnalizado(Compuesto,Maquina,listaTiempos,segundo)
            self.ListaCompuestosAnalizados.AgregarCabeza(comps)
            Seguir= False      
            if segundo > 1:
             self.dot.node(f'Tiempo óptimo para construir {Compuesto}: {segundo} segundos', shape=f'{self.forma}',width = '0.1', height= '0.1',fillcolor ='skyblue', style="filled")
            else:
             self.dot.node(f'Tiempo óptimo para construir {Compuesto}: {segundo} segundo', shape=f'{self.forma}',width = '0.1', height= '0.1',fillcolor ='skyblue', style="filled") 
            self.dot.render('instrucciones', view=True) 
        self.imprimirCompuestosAnalizados()    
      else:
         messagebox.showinfo("Información","Faltan datos o no hay")

    def MaquinaListP(self,Maquina):
       for i in range(self.ListaMaqs.tamaño()): # recorremos la máquina
         if self.ListaMaqs.invocar(i).nombre == Maquina: #verificamos que sea la maquina <---------     
             listPin = self.ListaMaqs.invocar(i).Listapin
       return listPin   # retornamos la lista de pines de la maquina específica  
             
    def CompuestoListE(self,Compuesto): 
       listElementsC = ListaSimple()  
       for i in range(self.ListaComp.tamaño()): # recorremos compuestos
            if Compuesto == self.ListaComp.invocar(i).nombre:#verificamos el compuesto <-------- 
               for j in range(self.ListaComp.invocar(i).ListaEUsados.tamaño()):
                 listElementsC.AgregarCabeza(self.ListaComp.invocar(i).ListaEUsados.invocar(j))
       return listElementsC   # retornamos la lista de con la fórmula
                 
    def Movimientos(self,Maq,pin,Comp,ElementoAct):
       for i in range(Maq.invocar(pin).tamaño()):
          if Maq.invocar(pin).invocar(i) == Comp.invocar(ElementoAct):
             
             return i # retornamos la posición en la máquina

    def movs(self,where,CoordenadaPin,j,Ad,At,Es,Maq,Comp,ElementoAct,segundo,ListaAccions):

       try:
        if where > CoordenadaPin.invocar(j):
          CoordenadaPin.Modificar(j,CoordenadaPin.invocar(j)+1)
          print('pin',str(j+1)+':',Ad)                  
          self.Guardar(j,Ad,ListaAccions)      

          self.dot.node(f'{j+1},{segundo}', shape=f'{self.forma}', width = '0.1', height='0.1',fillcolor =f'{self.color}',label= str(Ad), style="filled")
          self.dot.edge(f'{j},{segundo}',f'{j+1},{segundo}',style= 'invis')          

        elif where < CoordenadaPin.invocar(j):
           CoordenadaPin.Modificar(j,CoordenadaPin.invocar(j)-1)
           print('pin',str(j+1)+':',At)
           self.dot.node(f'{j+1},{segundo}', shape=f'{self.forma}', width = '0.1', height='0.1',fillcolor =f'{self.color}',label= str(At), style="filled")
           self.dot.edge(f'{j},{segundo}',f'{j+1},{segundo}',style= 'invis')                          
           self.Guardar(j,At,ListaAccions)

        elif where == CoordenadaPin.invocar(j):
           self.verifcarDemás(Maq,Comp,ElementoAct,j,CoordenadaPin,Ad,At,Es,ListaAccions)   
       except:
          self.verifcarDemás(Maq,Comp,ElementoAct,j,CoordenadaPin,Ad,At,Es,segundo,ListaAccions)
          #print('pin',str(j+1)+':',Es)              

    def verifcarDemás(self,Maq,Comp,ElementoAct,j,CoordenadaPin,Ad,At,Es,segundo,ListaAccions):
        unaVez = False
        for i in range(Comp.tamaño()-ElementoAct-1): 
         where2 = self.Movimientos(Maq,j,Comp,ElementoAct+i+1)  
         if unaVez:
           #print('pin',str(j+1)+':',Es) 
           break          
         try:
          if where2 > CoordenadaPin.invocar(j):
           CoordenadaPin.Modificar(j,CoordenadaPin.invocar(j)+1)
           print('pin',str(j+1)+':',Ad)
           self.dot.node(f'{j+1},{segundo}', shape=f'{self.forma}', width = '0.1', height='0.1',fillcolor =f'{self.color}',label= str(Ad), style="filled")
           self.dot.edge(f'{j},{segundo}',f'{j+1},{segundo}',style= 'invis')           
           unaVez = True
                
           self.Guardar(j,Ad,ListaAccions)           

          elif where2 < CoordenadaPin.invocar(j):
           CoordenadaPin.Modificar(j,CoordenadaPin.invocar(j)-1)
           print('pin',str(j+1)+':',At)
           self.dot.node(f'{j+1},{segundo}', shape=f'{self.forma}', width = '0.1', height='0.1',fillcolor =f'{self.color}',label= str(At), style="filled")
           self.dot.edge(f'{j},{segundo}',f'{j+1},{segundo}',style= 'invis')
           unaVez = True

                 
           self.Guardar(j,At,ListaAccions)           
         except:
          continue  
        if unaVez == False:
           print('pin',str(j+1)+':',Es) 
           self.dot.node(f'{j+1},{segundo}', shape=f'{self.forma}', width = '0.1', height='0.1',fillcolor =f'{self.color}',label= str(Es), style="filled")
           self.dot.edge(f'{j},{segundo}',f'{j+1},{segundo}',style= 'invis')
                  
           self.Guardar(j,Es,ListaAccions)           
    
    def Guardar(self,j,A,ListaAccions):
          accion = Accion(j+1,A)
          ListaAccions.AgregarCabeza(accion)          

               
    def EscribirTiemposC(self):
     
      archivo = open("Tiempos Óptimos.xml", "x") 
      archivo.write('''
<?xml version="1.0"?>
<RESPUESTA>
 <listaCompuestos>''')
      for i in range(self.ListaCompuestosAnalizados.tamaño()):
        archivo.write(f'''
  <compuesto>
   <nombre>{self.ListaCompuestosAnalizados.invocar(i).NombreComp}</nombre>
   <maquina>{self.ListaCompuestosAnalizados.invocar(i).NombreMaq}</maquina>
    <tiempoOptimo>{self.ListaCompuestosAnalizados.invocar(i).TiempoO}</tiempoOptimo>
    <instrucciones>''')
        for j in range(self.ListaCompuestosAnalizados.invocar(i).ListaTiempos.tamaño()):
          archivo.write(f'''
     <tiempo>
      <numeroSegundo>{self.ListaCompuestosAnalizados.invocar(i).ListaTiempos.invocar(j).Segundo}</numeroSegundo>
      <acciones>''')
          for k in range(self.ListaCompuestosAnalizados.invocar(i).ListaTiempos.invocar(j).ListaAcciones.tamaño()):
            archivo.write(f'''
       <accionPin>
        <numeroPin>{self.ListaCompuestosAnalizados.invocar(i).ListaTiempos.invocar(j).ListaAcciones.invocar(k).pin}</numeroPin>
        <accion>{self.ListaCompuestosAnalizados.invocar(i).ListaTiempos.invocar(j).ListaAcciones.invocar(k).accion}</accion>
       </accionPin>
            ''')
          archivo.write('''
      </acciones>
     </tiempo>     
          ''')
                      
        archivo.write('''
    </instrucciones>
  <compuesto>
        ''')
      archivo.write('''
 </listaCompuestos>
</RESPUESTA>
      ''')
      archivo.close()

      
    def imprimirCompuestosAnalizados(self):
      print('tamaño de compuestos:',self.ListaCompuestosAnalizados.tamaño())
      print('tiempos: sas',self.ListaCompuestosAnalizados.invocar(0).ListaTiempos.tamaño())
      
      for i in range(self.ListaCompuestosAnalizados.tamaño()):
         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
         print('Nombre Compuesto:',self.ListaCompuestosAnalizados.invocar(i).NombreComp)
         print('Nombre Maquina:',self.ListaCompuestosAnalizados.invocar(i).NombreMaq)
         print('Tiempo óptimo:',self.ListaCompuestosAnalizados.invocar(i).TiempoO)
         print('-----tiempos------')
         for j in range(self.ListaCompuestosAnalizados.invocar(i).ListaTiempos.tamaño()):
           print('----------------------------------------')
           print('Segundo:',self.ListaCompuestosAnalizados.invocar(i).ListaTiempos.invocar(j).Segundo)
           print('-----lista de acciones-----')
           for k in range(self.ListaCompuestosAnalizados.invocar(i).ListaTiempos.invocar(j).ListaAcciones.tamaño()):
             print('pin:',self.ListaCompuestosAnalizados.invocar(i).ListaTiempos.invocar(j).ListaAcciones.invocar(k).pin)
             print('Accion:',self.ListaCompuestosAnalizados.invocar(i).ListaTiempos.invocar(j).ListaAcciones.invocar(k).accion)
