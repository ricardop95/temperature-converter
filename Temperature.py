from ast import Return


class conversor:
    def __int__(self):
        self.conversor=conversor
        
    def cel_a_fah(self,):
        c=input('ingrese los grados que desea transformar \n')
        print(c,'grados celsius son \n')
        print(float(c)-32*(5.0/9.0),'grados farenheit')
    
    def fah_a_cel(self,):
        c=input('ingrese los grados que desea transformar \n')
        print(c,'grados farenheit son \n')
        print(float(c)*(9.0/5.0)+32,'grados celsius')
temperatura= conversor()      
x=0

while x!=8:
    print('!HOLA¡ soy un convertidor de temperatura \n')
    print("a,si deseas convertir de celsius a faranheit \n")
    print("b,si deseas convertir de faranheit a celsius \n")
    print("c,si desea salir del sistema de conversor\n")
    
    Operacion=input('')
    if Operacion == "a" or Operacion== "si deseas convertir de celsius a farenheit":
        temperatura.cel_a_fah()
    elif Operacion== "b" or Operacion == "si deseas convertir de faranheit a celsius":
        temperatura.fah_a_cel()
    elif Operacion== "c" or Operacion== "si desea salir del sistema de conversor":
        print("Fue un placer hasta luego")
    Operacion_2= input('¿Desea utilizar nuevamente el conversor?')
    if Operacion_2== 'si' or 'SI' or 's':
        x=9
    elif Operacion_2== 'no' or 'NO' or 'n':
        print('Gracias por usar el conversor')       
            
            
