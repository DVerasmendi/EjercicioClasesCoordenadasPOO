import math

class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def mostrar(self):
        return self.x,self.y
    
    def cuadrante(self):
        if self.x==0 and self.y!=0:
            return 'Situado en el eje Y'
        if self.x!=0 and self.y==0:
            return 'Situado en el eje X'
        if self.x==0 and self.y==0:
            return 'Situado en el ORIGEN'
     
    def vector(self,a, b):
        puntoA=self.x, self.y
        puntoB=a,b
        vectorAB=(a-self.x,b-self.y)
        return vectorAB
    
    def distancia(self,a, b):
        puntoA=self.x, self.y
        puntoB=a,b
        op1=(a-self.x)**2
        op2=(b-self.y)**2
        suma=op1+op2
        raiz=math.sqrt(suma) 
        return raiz
        
class Rectangulo(Punto):
    def __init__(self, x,y):
       Punto.__init__(self, x, y)
       
    def base(self,a):
        bases=abs(a-self.x)
        return bases
    
    def altura(self,b):
        alturas=abs(b-self.y)
        return alturas
    
    def area(self,base,altura):
        areas=base*altura
        return areas
    
    