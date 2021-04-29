from ClaseConjunto import conjunto
from ManejadorConjunto import manejador
import os

def opcion0():
    print("Saliendo")

def opcion1():
    ListaCompleta=conjunto1+conjunto2
    print(ListaCompleta)

def opcion2():
    ListaCompleta=conjunto1-conjunto2
    print(ListaCompleta)

def opcion3():
    ListaCompleta=conjunto1==conjunto2
    if ListaCompleta==True:
        print("Las listas son iguales")
    else:
        print("no son iguales")

switcher ={
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opcion incorrecta"))
    func()
      


if __name__=='__main__':
    bucle=True
    casilla=1
    variable=str
    numero=int
    bucle2=1
    CantList=2
    conjunto1=conjunto()
    conjunto2=conjunto()
    while bucle2<=CantList:
        print(f"------------------------------------------{bucle2}------------------------------------------")
        while bucle==True:
            variable=input(f"Ingrese el numero de la casilla {casilla} de la lista {bucle2} (Fin para terminar con esta lista):")
            if variable.isdigit():
                print(f"El numero {variable} fue ingresado a la lista")
                casilla+=1
                numero=int(variable)
                if bucle2==1:
                    conjunto1.agregarElemento(numero)
                else:
                    conjunto2.agregarElemento(numero)
            else:
                variable=variable.lower()
                if variable=="fin":
                    bucle=False
                else:
                    print("Valor incorrecto, por favor ingrese un numero entero")
        bucle=True
        bucle2+=1
        casilla=1
    ListaCompleta=conjunto()
    #ListaCompleta=conjunto1+conjunto2
    #print(ListaCompleta)
    #ListaCompleta=conjunto1-conjunto2
    #print(ListaCompleta)
    #ListaCompleta=conjunto1==conjunto2
    bandera = False
    while not bandera:
        os.system ("cls") 
        print("MENU DE OPCIONES")
        print("0 para salir")
        print("1 Unir los dos conjuntos")
        print("2 La diferencia entre dos conjuntos")
        print("3 Consultar si son iguales")
        opcion = int(input("Ingrese valor: "))
        switch(opcion)
        bandera = int(opcion) == 0
        os.system("pause")