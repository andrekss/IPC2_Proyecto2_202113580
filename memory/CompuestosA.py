class CompuestoAnalizado:

    def __init__(self,  NombreComp,NombreMaq, ListaTiempos,TiempoO):
      self.NombreComp = NombreComp      
      self.NombreMaq = NombreMaq
      self.TiempoO = TiempoO
      self.ListaTiempos = ListaTiempos

class tiempo:

    def __init__(self, Segundo,ListaAcciones):
      self.Segundo = Segundo      
      self.ListaAcciones = ListaAcciones

class Accion:
   
   def __init__(self,pin,accion):
      self.pin = pin
      self.accion = accion
