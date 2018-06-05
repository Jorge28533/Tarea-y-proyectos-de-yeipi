
x = 1
y = 0
#saca los numeros Fibonashi del 5 al 15
Fibo = int(input("Escoje un numero:  "))

if(Fibo <= 5):
		Fibo = 5

if(Fibo >=15):
	Fibo = 15

for Fibo in range(Fibo):
	x = x + y
	y = x - y

	

	print(x)
'''
	Soy un Tensai(Genio) de la programacion jajaja
	me costo hacerlo pero salio jajajaja
	'''