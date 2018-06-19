
def Asterisco(myList):
    print(myList)
    for i in (myList): 
        n = i * "*"
        print(n)
    continuar = int(input("Quieres usar  otra funcion !? 1.si 2.salir :  "))
    if (continuar == 1):
        main()
    if (continuar == 2):
        print("Que tenga buen dia.Usuario")
    
def BaseTri(b, a):
    mul = b*a
    Div = mul/2
    print("La Area del Triangulo es: " + str(Div))
    continuar = int(input("Quieres usar  otra funcion !? 1.si 2.salir :  "))
    if (continuar == 1):
        main()
    if (continuar == 2):
        print("Que tenga buen dia.Usuario")

def Volumen(v):
    c = v**3
    m = 4%3*c
    pi = 3.1416*m
    print(pi)
    continuar = int(input("Quieres usar  otra funcion !? 1.si 2.salir :  "))
    if (continuar == 1):
        main()
    if (continuar == 2):
        print("Que tenga buen dia.Usuario")

def Archivo():
    myLista = (input("Nombre del  archivo. E:Archivo.exe  "))
    hola = myLista.split(".")
    x = hola.pop()
    print(x)
    continuar = int(input("Quieres usar  otra funcion !? 1.si 2.salir :  "))
    if (continuar == 1):
        main()
    if (continuar == 2):
        print("Que tenga buen dia.Usuario")
  
def Fechas():
    from  datetime import date
    w = int(input("Dia de hoy: "))
    q = int(input("Mes de aurita:  "))
    Inicio = date(2018, q, w)
    l = int(input("Dia de cita: "))
    o = int(input("Mes de cita:  "))
    cita = date(2018, o, l) 
    n = cita - Inicio
    print(n)
    continuar = int(input("Quieres usar  otra funcion !? 1.si 2.salir :  "))
    if (continuar == 1):
        main()
    if (continuar == 2):
        print("Que tenga buen dia.Usuario")


def Version():
    import sys
    n = sys.version
    print(n)
    continuar = int(input("Quieres usar  otra funcion !? 1.si 2.salir :  "))
    if (continuar == 1):
        main()
    if (continuar == 2):
        print("Que tenga buen dia.Usuario")
    


        
def main():

    print("1.Archivo, 2.Fechas, 3.Volumen, 4.Asterisco, 5.BaseTri, 6.VersionPython ")

    numero = int(input("Escoje una Funcion:  "))

    if(numero == 1): 
         Archivo()
       
       
    if(numero == 2):
	    Fechas()

    if(numero == 3):
	    v = int(input("Radio del circulo: "))
	    Volumen(v)

    if(numero == 4):
        conti = "si"
        myList = []
        while (conti!="no"):
            n = int(input("Que nuemro quieres agragar: "))
            myList.append(n)
            print("quieres agragar otro nnumero: si/no")
            conti= input()
        Asterisco(myList)


	  
    if(numero == 5):
        b = int(input("Base del triangulo:  "))
        a = int(input("altura del triangulo:  "))
        BaseTri(b, a)



    if(numero == 6):
	    Version()



if __name__ == "__main__":
    main()