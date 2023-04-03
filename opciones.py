from tkinter import *
from CargarXml import *
from tkinter import ttk
from GMaquinas import Graficar

class Opciones:

    def __init__(self,posx,posy,centrado,inicial,ancho,alto,anchoV,altoV,color,nombre):
        self.Ruta = ''
        self.posx = posx
        self.posy = posy
        self.centrado = centrado
        self.inicial = inicial
        self.ancho = ancho
        self.alto = alto
        self.anchoV = anchoV
        self.color = color
        self.altoV = altoV
        self.nombre = nombre
        self.car = Cargar()
        

    def generarTablaElementos(self,ventana):
        try:
         ElementosQ = ttk.Treeview(ventana)    
         ElementosQ['columns'] = ('Numero Atómico','Símbolo','Elemento')
         #configuaracion
         ElementosQ.column("#0", width=0, stretch=NO)  # elimanmos espacio en blanco
         ElementosQ.column("Numero Atómico", width = 130)
         ElementosQ.column("Símbolo", width=100)
         ElementosQ.column("Elemento", width=100)

         ElementosQ.heading("#0", text="", anchor=CENTER) #no habrá nada en esta posición 
         ElementosQ.heading("Numero Atómico", text="Numero Atómico", anchor=CENTER)
         ElementosQ.heading("Símbolo", text="Símbolo", anchor=CENTER)
         ElementosQ.heading("Elemento", text="Elemento", anchor=CENTER)
         y= 4.2
         x= 90
         
         ejemplo = Label(ventana,text='para guardar un nuevo elemento: Numero Atómico,Símbolo,Elemento')
         ejemplo.place(x=self.centrado-x,y=self.inicial*(y-0.3))
         
         NoAtomic = Entry(ventana, width=self.ancho-15)
         NoAtomic.place(x=self.centrado-x,y=self.inicial*y)

         Símbolo = Entry(ventana, width=self.ancho-15)
         Símbolo.place(x=self.centrado-x+self.ancho+10,y=self.inicial*y)         

         nombre = Entry(ventana, width=self.ancho)
         nombre.place(x=self.centrado-x+self.ancho+40,y=self.inicial*y)

         Save = Button(ventana, text='Añadir')
         Save.config(font=("Arial",13),width=self.ancho,height=self.alto,command=lambda: self.car.AñadirElemento(NoAtomic,Símbolo,nombre))
         Save.place(x=self.centrado-x,y=self.inicial*(y+0.3))
        
         for i in range(self.car.ListaElementos.tamaño()):
          ElementosQ.insert("", "end", text="1", values=(self.car.ListaElementos.invocar(i).NoAtomico, f'{self.car.ListaElementos.invocar(i).simbolo}', f'{self.car.ListaElementos.invocar(i).NombreE}'))
         ElementosQ.pack() 
        except:
         messagebox.showinfo("Información","No Hay elementos")     

    def generarTablaCompuestos(self,ventana):
       
      try:
       CompuestosQ = ttk.Treeview(ventana)    
       CompuestosQ.column("#0", width=0, stretch=NO)
       CompuestosQ['columns'] = ('Nombre','Fórmula')
       CompuestosQ.column("Nombre", width = 100)
       CompuestosQ.column("Fórmula", width=200) 

       CompuestosQ.heading("#0", text="", anchor=CENTER) #no habrá nada en esta posición 
       CompuestosQ.heading("Nombre", text="Nombre", anchor=CENTER)
       CompuestosQ.heading("Fórmula", text="Fórmula", anchor=CENTER) 
      
       y= 4.2
       x= 90

       ejemplos = Label(ventana,text='para analizar Compuesto: Nombre del compuesto, Nombre de la máquina')
       ejemplos.place(x=self.centrado-x,y=self.inicial*(y-0.3))

       Comp = Entry(ventana, width=self.ancho)
       Comp.place(x=self.centrado-x,y=self.inicial*y)

       Maq = Entry(ventana, width=self.ancho)
       Maq.place(x=self.centrado-x+self.ancho+105,y=self.inicial*y)       

       guardar = Button(ventana, text='Analizar Compuesto')
       guardar.config(font=("Arial",13),width=self.ancho,height=self.alto)
       guardar.place(x=self.centrado-x,y=self.inicial*(y+0.3))

       for i in range(self.car.ListaCompuestos.tamaño()): 
          formula = ''
          coma = ', '
          for j in range(self.car.ListaCompuestos.invocar(i).ListaEUsados.tamaño()):
             if j == int(self.car.ListaCompuestos.invocar(i).ListaEUsados.tamaño()-1):
              coma = ''
             formula = formula+self.car.ListaCompuestos.invocar(i).ListaEUsados.invocar(j)+coma
                   
          CompuestosQ.insert('','end',text='1',values=(self.car.ListaCompuestos.invocar(i).nombre,formula))
        
       CompuestosQ.pack() 
      except:
       messagebox.showinfo("Información","No Hay Compuestos")

    def GenerarRuta(self):
        Ruta = Toplevel()

        Ruta.geometry(f"{self.anchoV}x180+{self.posx}+{self.posy}") 
        Ruta.title(f"{self.nombre}")
        Ruta.config(bg=f"{self.color}")

        Titulo = Label(Ruta, text="Guardar")
        Titulo.config(font=("Times New Roman",16))
        Titulo.pack()
        entrada = Entry(Ruta, width=self.ancho*3)
        entrada.place(x=self.centrado-60,y=self.inicial)

        Enviar = Button(Ruta, text="Enviar")
        Enviar.config(font=("Arial",13),width=self.ancho,height=self.alto,command=lambda: self.car.CargarArchivo(entrada))
        Enviar.place(x=self.centrado,y=1.5*self.inicial)

    def Elementos(self):
        Elementos = Toplevel()

        Elementos.geometry(f"{self.anchoV}x{self.altoV}+{self.posx}+{self.posy}") 
        Elementos.title(f"{self.nombre}")
        Elementos.config(bg=f"{self.color}")

        Titulo = Label(Elementos, text="Gestionar Elementos")
        Titulo.config(font=("Times New Roman",16))
        Titulo.pack()
        self.generarTablaElementos(Elementos)

    def Compuestos(self):
        Compuestos = Toplevel()

        Compuestos.geometry(f"{self.anchoV}x{self.altoV}+{self.posx}+{self.posy}") 
        Compuestos.title(f"{self.nombre}")
        Compuestos.config(bg=f"{self.color}")

        Titulo = Label(Compuestos, text="Gestionar Compuestos")
        Titulo.config(font=("Times New Roman",16))
        Titulo.pack()
        self.generarTablaCompuestos(Compuestos)  


    def GraficarMáquina(self):
     try: 
      maqs = Graficar(self.car.ListaMaquinas,self.car.ListaElementos,self.car.ListaElementos.tamaño())   
      maqs.GraficarMáquinas()
     except:
       messagebox.showinfo("Información","Faltan datos o no hay")
        

    def Eliminar(self):
       self.car.LimpiarMemoria()  
           