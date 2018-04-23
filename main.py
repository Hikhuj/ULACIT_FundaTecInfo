# Curso: Fundamentos de Tecnologias de la Informacion
# Proyecto: Sistema de Alquiler de Video
# Profesor: Mario Segura
# Year academico: 2018_I_Quarter
# Lenguage: Python:
# Sinopsis: El proyecto se base en desarrollar un sistema usando los conocimientos adquiridos del curso con el fin 
# de aplicarlos con el idioma por lo que se planteo la conceptualizacion y desarrollo de un sistema que realice 
# diferentes funciones basicas para ser aplicado a un Club de Video y poder llevar un control sobre 
# las peliculas y los usuarios.

#!/usr/bin/env python

# Seccion de Importe de Archivos y Clases




# Clases
def main():

	# Saludo Inicial
	saludo_inicial()

	# Desplegar menu de aplicacion
	menu()


def menu():
	# mostras las opciones de menu
	opciones_de_menu()

	# obtener opcion de menu
	opcion_menu = int(input("Digite una opcion de menu"))
	
	
	if is_int(opcion_menu) == True:
		if opcion_menu >= 1 and opcion_menu <= 3

		

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
    if type(variable) == int:
        return True
    else:
        if val.is_integer():
            return True
        else:
            return False



