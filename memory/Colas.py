class cola:
    def __init__(self):
        self.cola = []
        self.tamaño = 0

    def Empty(self):
        return len(self.cola) == 0
    
    def push(self,dato):
     self.cola +=[dato]
     self.tamaño += 1

    def pop(self):
       if self.Empty()== True:
          print("La cola esta vacía")
       else:
          self.cola =[self.cola[i] for i in range(1, self.tamaño)]    
          self.tamaño -=1
    def invoke(self,indice):
       i = self.tamaño-1
       while i >-1:
         if indice == i: 
          return self.cola[i]
         i-=1

    def PrimerDato(self):
       if self.Empty():
          print("cola esta vacía")
       else:
          print("Primer Dato:", self.cola[0])   
          
