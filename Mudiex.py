
'''funcion: un bloque de codigo el cual tiene un propocito especifico. esta puede tener parametros de entrada(inputs) y valores de retorno(output) [resultado]. se puede ejecutar (llamar) desde otras partes del programa'''

#funcion de saludo
def Saludar():
	print("hola a mi funcion de calculadora basica ")

#funcion de suma
def Suma(numx, numy):
	if(type(numx)) != int or (type(numy)) != int:
		print("Error de dato")
	result = numx + numy
	print(result)

#funcion de Resta
def Resta(numx, numy):
	if(type(numx)) != int or (type(numy)) != int:
		print("Error de dato")
	result = numx - numy
	print(result)


#funcion de Multoplicacion
def Multi(numx, numy):
	if(type(numx)) != int or (type(numy)) != int:
		print("Error de dato")
	result = numx * numy
	print(result)

#funcion de Division
def Divi(numx, numy):
	if(type(numx)) != int or (type(numy)) != int:
		print("Error de dato")
	result = numx / numy
	print(result)

#funcion de Potencia
def Potencia(numx, numy):
	if(type(numx)) != int or (type(numy)) != int:
		print("Error de dato")
	result = numx ** numy
	print(result)

def main():
	Saludar()

if __name__ == '__main__':
	main()

print("1.Suma, 2.Resta, 3.Multiplicacion, 4.Division, 5.Exponente ")

numero = int(input("Escoje una Funcion:  "))

if(numero == 1):
	numx = int(input("Escoje un numero:  "))
	numy = int(input("Escoje otro numero:  "))
	Suma(numx,numy)	
	
if(numero == 2):
	numx = int(input("Escoje un numero:  "))
	numy = int(input("Escoje otro numero:  "))
	Resta(numx,numy )

if(numero == 3):
	numx = int(input("Escoje un numero:  "))
	numy = int(input("Escoje otro numero:  "))
	Multi(numx, numy)

if(numero == 4):
	numx = int(input("Escoje un numero:  "))
	numy = int(input("Escoje otro numero:  "))
	Divi(numx, numy)

if(numero == 5):
	numx = int(input("Escoje un numero:  "))
	numy = int(input("Escoje otro numero:  "))
	Potencia(numx, numy)
