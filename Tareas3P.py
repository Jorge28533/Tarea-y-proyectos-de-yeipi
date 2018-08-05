
def Factorial(n):
	if(n == 1):
		return 1

	else:
		return n * Factorial(n-1)


def Fibonashi(s):
	if(s == 1 ):
		return 0
	if(s == 2):
		return 1
	else:
		return Fibonashi(s-1) + Fibonashi(s-2)


def Multiplo3(n, k):
	if(n == 1):
		return k
	else:
		return k +  Multiplo3(n-1, k)

	def NioH(n):
		if(n == 1):
			return 1
		else:
			return n + 2*(NioH(n-1))+1


def main():
	numero = int(input("1.Factorial: 2.Fibonashi: 3.Multi3: 4.Nioh "))
	if(numero == 1):
		n = int(input("De que numero quieres saber su factorial: "))
		print(Factorial(n))
	if(numero == 2):
		lista = []
		s = int(input("Hasta que numero quieres Fibonachi: "))
		print(Fibonashi(s))
	if(numero == 3):
		n = 3
		k = int(input("De que numero quieres Multiplo de 3: "))
		print(Multiplo3(n, k))
	if(numero == 4):
		NioH(n)
if __name__ == "__main__":
	main()