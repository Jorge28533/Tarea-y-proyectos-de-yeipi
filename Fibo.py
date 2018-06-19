
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
	

	def Asterisco(List):
    for i in [List]:
        for e in (i):
            print("*")

def BaseTri(b, a):
    mul = b*a
    Div = mul/2
    print("La Area del Triangulo es: " + str(Div))

def Volumen(v):
    c = v**3
    m = 4%3*c
    pi = 3.1416*m
    print(pi)
if(numero == 3):
    v = int(input("Base del triangulo:  "))
	Volumen(v)
	
if(numero == 4):

if(numero == 5):
        b = int(input("Base del triangulo:  "))
        a = int(input("altura del triangulo:  "))
        BaseTri(b, a)
