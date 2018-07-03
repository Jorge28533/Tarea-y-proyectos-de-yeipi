def Adivina():
    import random
    r = random.randint(0, 9)
    while True:
            s = int(input("Escoje un numero de 0 a 9: "))
            if(s < r):
                print(str(s) + "Es mas pequeño que adivinador ")
            if(s > r):
                print(str(s) + "Es mas grande que adivinador ")
            if(s == r):
                print("Felicidades!!! Adivinaste el numero" + str(r))
                break
    continuar = int(input("Quieres usar  otra funcion !? 1.si 2.salir :  "))
    if (continuar == 1):
        main()
    if (continuar == 2):
        print("Que tenga buen dia.Usuario")

def Directorio():
	import os
	print("Escritorio\fotos jorge")
	n = input("Inserte Respositorio: ")
	print(os.listdir(n))
	continuar = int(input("Quieres usar  otra funcion !? 1.si 2.salir :  "))
	if(continuar == 1):
		main()
	if(continuar == 2):
		print("Que tenga buen dia. Usuario.")


def Absoluto():
	import os
	n = input("Inserte el nombre del archivo: ")
	print(os.path.abspath(n))
	continuar = int(input("Quieres usar  otra funcion !? 1.si 2.salir :  "))
	if(continuar == 1):
		main()
	if(continuar == 2):
		print("Que tenga buen dia. Usuario.")

def Leyenda():
    Nombre = input("Ingrese su Nombre: ")
    Texto = open('Leyend.txt', 'w')
    Texto.close() 
    Texto = open('Leyend.txt', 'a')
    Texto.write('Dice la Leyenda:\n')
    Texto.write('Hola, mi nombre es ' + str(Nombre) + '\n')
    Texto.write('Te saludo desde mi primer archivo de texto\n')
    Texto.write('\n')
    Texto.write('Saludos!!\n')
    Texto.close
    continuar = int(input("Quieres usar  otra funcion !? 1.si 2.salir :  "))
    if (continuar == 1):
        main()
    if (continuar == 2):
        print("Que tenga buen dia.Usuario")


def Felicidad():
    nani = ()

    Felices = open('felices.txt','r')
    Primos = open('primos.txt','r')
    for x in Felices.readline():
        for y in Primos.readline():
            if(x == y):
                nani.append(x)
    crear = open('coinciden.txt', 'w')
    crear.write(str(lista1))
    Felices.close()
    Primos.close()
    crear.close()

  

        




def main():
	numero = int(input("1.Directorio 2.Leyenda 3.Absoluto  4.Felicidad 5. Adivina:  "))
	if(numero == 1):
		Directorio()
	if(numero == 2):
		Leyenda()
	if(numero == 3):
		Absoluto()
	if(numero == 4):
		Felicidad()
	if(numero == 5):
		Adivina()


















if __name__ == "__main__":
    main()
