#!/usr/bin/env python
# Curso: Fundamentos de Tecnologias de la Informacion
# Proyecto: Sistema de Alquiler de Video
# Profesor: Mario Segura
# Year academico: 2018_I_Quarter
# Lenguage: Python:
# Sinopsis: El proyecto se base en desarrollar un sistema usando los conocimientos adquiridos del curso con el fin 
# de aplicarlos con el idioma por lo que se planteo la conceptualizacion y desarrollo de un sistema que realice 
# diferentes funciones basicas para ser aplicado a un Club de Video y poder llevar un control sobre 
# las peliculas y los usuarios.
# http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html

#  Funciones
def menu():
	
	# Variable permite que ingrese al ciclo
	opcion_menu = 1

	# Ciclo mantiene al usuario dentro del menu hasta que digite X numero y se salga
	while opcion_menu >= 1 and opcion_menu <= 3:

		# Funcion imprime opciones de menu
		opciones_de_menu()

		opcion_menu = input("Por favor ingrese una opcion (1-3): ")

		try:
			
			opcion_menu = int(opcion_menu)
			if opcion_menu == 1:
				print("\n1. Registrar clientes nuevos\n")
			elif opcion_menu == 2:
			    print("\n2. Menu de peliculas\n")
			elif opcion_menu == 3:
				print("\n3. Consultar informacion\n")
			else:
				despedida()

		except ValueError:
			# No es un numero
			print("\n")
			print("El valor ingresado no es un numero, intente de nuevo")
			print("\n")
			menu()
	

def saludo_inicial():
	print("\n")
	print("* --------------------------------------- *")
	print("|                                         |")
	print("|           Inicializando Sistema         |")
	print("|                                         |")
	print("|              Cargando Datos             |")
	print("|                                         |")
	print("* --------------------------------------- *")
	print("Inicializando sistema, por favor espere...\n")


def despedida():
	print("\n")
	print("* --------------------------------------- *")
	print("|                                         |")
	print("|          Saliendo del  Sistema          |")
	print("|                                         |")
	print("|             Guardando Datos             |")
	print("|                                         |")
	print("* --------------------------------------- *")
	print("\n")


def opciones_de_menu():
	print("Opciones de Menu")
	print("1. Registrar clientes nuevos")
	print("2. Menu de Peliculas")
	print("3. Consultar informacion")
	print("4. Salir\n")


def es_un_numero(variable):

	resultado = False
	es_digito = variable.isdigit()

	if es_digito != False:
		resultado = True

	return resultado

### Main
def main():

	# Saludo Inicial
	saludo_inicial()

	# Desplegar menu de aplicacion
	menu()

if __name__ == "__main__":
	main()