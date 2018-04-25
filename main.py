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
	
	# Opciones de menu
	opciones_de_menu()

	## Recibir opcion acorde a funcion anterior
	opcion_menu = input('Por favor ingrese una opcion (1-4): ')

	es_numero = es_un_numero(opcion_menu)

	while es_numero == True:
		
		# Desplegar si opcion de menu es valido
		if type(int(opcion_menu)) == int:

			if int(opcion_menu) == 1:
				print ("1. Registrar clientes nuevos")
			elif int(opcion_menu) == 2:
			    print ("2. Menu de peliculas")
			elif int(opcion_menu) == 3:
				print ("3. Consultar informacion")
			else:
				print ("4. Salir de sistema")
				break

		else:
			# No es un numero
			print("Ingreso un valor no valido")
			menu()
	

def saludo_inicial():
	print("* --------------------------------------- *")
	print("|                                         |")
	print("|           Inicializando Sistema         |")
	print("|                                         |")
	print("|              Cargando Datos             |")
	print("|                                         |")
	print("* --------------------------------------- *")
	print("Inicializando sistema, por favor espere...")


def opciones_de_menu():
	print("Opciones de Menu")
	print("1. Registrar clientes nuevos")
	print("2. Menu de Peliculas")
	print("3. Consultar informacion")
	print("4. Salir")


def es_un_numero(variable):

	resultado = False

    if type(variable) != int:
    	return resultado


### Main
def main():

	# Saludo Inicial
	saludo_inicial()

	# Desplegar menu de aplicacion
	menu()

if __name__ == "__main__":
	main()