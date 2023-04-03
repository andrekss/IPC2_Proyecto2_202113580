from tkinter import *
import sys
from opciones import *
from GMaquinas import *

op = Opciones(440,30,150,70,20,2,500,650,'red','Proyecto 2')

selector = Tk()

Opciones = Label(selector, text="Opciones")
Opciones.config(font=("Times New Roman",16))
Opciones.pack()

selector.geometry(f"{op.anchoV}x{op.altoV}+{op.posx}+{op.posy}") 
selector.title(f"{op.nombre}")
selector.config(bg=f"{op.color}")

Inicio = Button(selector, text="Inicialización")
Inicio.config(font=("Arial",13),width=op.ancho,height=op.alto,command=op.Eliminar)

archivo = Button(selector, text="Cargar Archivo XML",command=op.GenerarRuta)
archivo.config(font=("Arial",13),width=op.ancho,height=op.alto)

archivoG = Button(selector, text="Generar Archivo XML")
archivoG.config(font=("Arial",13),width=op.ancho,height=op.alto)

GElementos = Button(selector, text="Gestión de Elementos")
GElementos.config(font=("Arial",13),width=op.ancho,height=op.alto,command=op.Elementos)

GCompuestos = Button(selector, text="Gestión de Compuestos")
GCompuestos.config(font=("Arial",13),width=op.ancho,height=op.alto,command=op.Compuestos)

GMaquinas = Button(selector, text="Gestión de Maquinas")
GMaquinas.config(font=("Arial",13),width=op.ancho,height=op.alto,command=op.GraficarMáquina)

Ayuda = Button(selector, text="Ayuda")
Ayuda.config(font=("Arial",13),width=op.ancho,height=op.alto)

salir = Button(selector, text="Salir")
salir.config(font=("Arial",13),width=op.ancho,height=op.alto,command=sys.exit) 

Inicio.place(x=op.centrado,y=op.inicial)
archivo.place(x=op.centrado,y=2*op.inicial)
archivoG.place(x=op.centrado,y=3*op.inicial)
GElementos.place(x=op.centrado,y=4*op.inicial)
GCompuestos.place(x=op.centrado,y=5*op.inicial)
GMaquinas.place(x=op.centrado,y=6*op.inicial)
Ayuda.place(x=op.centrado,y=7*op.inicial)
salir.place(x=op.centrado,y=8*op.inicial)

selector.mainloop()