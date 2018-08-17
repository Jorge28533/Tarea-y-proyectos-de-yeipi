
class Alumno:
	def __init__(self, Nombre, Calificaion, Grupo):
		self.Nombre = Nombre
		self.Calificaion = Calificaion
		self.Grupo = Grupo
	
	def Clasificacion(self):
		if(self.Grupo == ' 2018A\n'):
			Texto = open('Grupo2018A.txt', 'a+')
			Texto.write(self.Nombre + ',')
			Texto.write(self.Calificaion + ',')
			Texto.write(self.Grupo)
			Texto.close
		if(self.Grupo == " 2018B\n"):
			Texto = open('Grupo2018B.txt', 'a+')
			Texto.write(self.Nombre + ',')
			Texto.write(self.Calificaion + ',')
			Texto.write(self.Grupo)
			Texto.close
		if(self.Grupo == " 2017A\n"):
			Texto = open('Grupo2017A.txt', 'a+')
			Texto.write(self.Nombre + ',')
			Texto.write(self.Calificaion + ',')
			Texto.write(self.Grupo)
			Texto.close
		if(self.Grupo == " 2017B\n"):
			Texto = open('Grupo2017B.txt', 'a+')
			Texto.write(self.Nombre + ',')
			Texto.write(self.Calificaion + ',')
			Texto.write(self.Grupo)
			Texto.close
		if(self.Grupo == " 2016A\n"):
			Texto = open('Grupo2016A.txt', 'a+')
			Texto.write(self.Nombre + ',')
			Texto.write(self.Calificaion + ',')
			Texto.write(self.Grupo)
			Texto.close
		if(self.Grupo == " 2016B\n"):
			Texto = open('Grupo2016B.txt', 'a+')
			Texto.write(self.Nombre + ',')
			Texto.write(self.Calificaion + ',')
			Texto.write(self.Grupo)
			Texto.close
	
		


def Agregar():
	print("Ejemplo de como agregar al nuevo Alumno")
	print("Jorge, 9.5, 2018B")
	Alum = input("Ingrese al Alumno: ")
	f = open("Estudiantes.txt", "a")
	f.write('\n' + (Alum))
	f.close
	otro = int(input("1.Agregar otro Alumno: 2.Menu: 3.Salir: "))
	if(otro == 1):
		Agregar()
	if(otro == 2):
		main()
	if(otro == 3):
		print("Que tenga buen dia.")


def Promedio():
	with open("Estudiantes.txt", "r") as file:
		lines = file.readlines()
		for i in lines:
			list = i.split(",")	
			x = Alumno(list[0], list[1], list[2])
			x.Clasificacion()
	



def main():
	usuario = input("Por favor ingrese su nombre: ")
	print("Buenas Tardes," + str(usuario) + ". Que deceas hacer!?")
	intro = int(input("1.Agregar un Alumno 2.Ordenar Alumnos: "))
	if(intro == 1):
		Agregar()
	if(intro == 2):
		Ordenado = int(input("Quieres ordenar: 1.Alfabeticaemente 2.Promedio: "))
		if(Ordenado == 1):
			Alfabeticaemente()
		if(Ordenado == 2):
			Promedio()
		else:
			print("No existe esa opcion en el sistema")
			main()
	



if __name__ == "__main__":
	main()	