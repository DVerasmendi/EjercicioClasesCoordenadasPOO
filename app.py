from punto import Punto, Rectangulo

def imprimir_pto():
    punto=list(x_y.mostrar())
    print('X','Y')
    print('(',punto[0],',',punto[1],')')

def cuadrante_x_y():
    cuadrante=x_y.cuadrante()
    print(cuadrante)

def vector(a,b):
    vectors=list(x_y.vector(a,b))
    print('VECTOR-->',vectors[0],', ',vectors[1])

def distancias(a,b):
    distancia=x_y.distancia(a,b)
    print('Distancia entre puntos X,Y y A,B: ',distancia)

def baserec(a):
    bases=rectangulo.base(a)
    print('La BASE del rectangulo es: ', str(bases))
    return bases
    
def alturarec(b):
    alturas=rectangulo.altura(b)
    print('La ALTURA del rectangulo es: ', str(alturas))
    return alturas

def arearec(base,altura):
    areass=rectangulo.area(base, altura)
    print('El AREA del rectangulo es: ', str(areass))
    
    
stop = False
while stop == False:
    print('\n')
    print('''1.-Ingresar punto X,Y \n2.-Ingresar punto A,B  \n3.-HACER OPERACIONES
        ''')
    opcioninicial=input()
    if '1' in opcioninicial:
        print('Valor X: ')
        x=int(input())
        print('Valor Y: ')
        y=int(input())
        x_y=Punto(x=x,y=y)
            
    elif '2' in opcioninicial:
        print('Valor A: ')
        a=int(input())
        print('Valor B: ')
        b=int(input())
  

    if '3' in opcioninicial:
        rectangulo=Rectangulo(x=x,y=y)
        print('PUNTOS')
        print('(X,Y) :','(',x,',',y,')')
        print('(A,B) :','(',a,',',b,')')
        
        stop = False
        while stop == False:
            
            print('''
        What would you like to do (type a number and press Enter)?
        - Type 1: IMPRIMIR ptos (X,Y).
        - Type 2: CUADRANTE al que pertenecen (X,Y)
        - Type 3: VECTOR entre (X,Y) y (A,B)
        - Type 4: DISTANCIA entre (X,Y) y (A,B)
        - Type 5: BASE del RECTANGULO formado entre (X,Y) y (A,B)
        - Type 6: ALTURA del RECTANGULO formado entre (X,Y) y (A,B)
        - Type 7: AREA del RECTANGULO formado entre (X,Y) y (A,B)
        - Type 8: To quit
            ''')
            option = int(input("Enter a number:"))
            # add your options here using conditionals (if)    
            try: 
                if option == 1:
                    imprimir_pto()
                if option == 2:
                    cuadrante_x_y()
                    
                if option==3:
                    if a and b !='':
                        vector(a,b)
                        
                if option==4:
                    if a and b !='':
                        distancias(a,b)
                
                if option==5:                
                    if a and b !='':
                        base= baserec(a)
                        
                if option==6:                
                    if a and b !='':
                        altura=alturarec(b)
                             
                if option==7:                
                    if base and altura !='':
                        arearec(base,altura)
                    
                if option==8:        
                    print("Bye bye!")
                    stop = True             
            except IndexError as e:
                print(e)