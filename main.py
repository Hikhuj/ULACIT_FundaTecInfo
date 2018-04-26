#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Importe de modulos
import random
import csv

# Curso: Fundamentos de Tecnologias de la Informacion
# Proyecto: Sistema de Alquiler de Video
# Profesor: Mario Segura
# Year academico: 2018_I_Quarter
# Lenguage: Python:
# Sinopsis: El proyecto se base en desarrollar un sistema usando los conocimientos adquiridos del curso con el fin 
# de aplicarlos con el idioma por lo que se planteo la conceptualizacion y desarrollo de un sistema que realice 
# diferentes funciones basicas para ser aplicado a un Club de Video y poder llevar un control sobre 
# las peliculas y los clientes.
# http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html

#  Funciones
def menu():
	
	# Variable permite que ingrese al ciclo
	opcion_menu = 1

	# Ciclo mantiene al cliente dentro del menu hasta que digite X numero y se salga
	while opcion_menu >= 1 and opcion_menu <= 3:

		# Funcion imprime opciones de menu
		opciones_de_menu()

		# Evaluar si dato ingresado es valido en try:Except
		try:
			
			# Capturar entrada de cliente (string)
			opcion_menu = input("Por favor ingrese una opcion (1-3): ")
			print("\n")

			# Tratar de convertir dato capturado a INT
			opcion_menu = int(opcion_menu)

			# Si opcion es validad pasar a entrar a submenus
			if opcion_menu == 1:
				opcion_registrar_cliente()
				# Volver a llamar al menu
				menu()
			elif opcion_menu == 2:
			    print("2. Menu de peliculas\n")
			elif opcion_menu == 3:
			    print("3. Consultar informacion\n")
			else:
				despedida()

		except ValueError:

			# Mostrar error: cliente no ingreso numero
			print("\n")
			print("El valor ingresado no es un numero, intente de nuevo")
			print("\n")

			# Volver a llamar al menu
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
	print("|           Saliendo del Sistema          |")
	print("|                                         |")
	print("|              Guardando Datos            |")
	print("|                                         |")
	print("* --------------------------------------- *")
	print("\n")

	
def mensaje_registrar_cliente_nuevo():
	print("\n")
	print("* --------------------------------------- *")
	print("|                                         |")
	print("|         REGISTRAR CLIENTE NUEVO         |")
	print("|                                         |")
	print("* --------------------------------------- *")
	print("\n")


def opciones_de_menu():
	print("Opciones de Menu")
	print("1. Registrar clientes nuevos")
	print("2. Menu de Peliculas")
	print("3. Consultar informacion")
	print("4. Salir\n")


# Menu 1: Submenu 1
def opcion_registrar_cliente():
	
	# VARIABLES
	data_saved = True

	# Mensaje de registro de cliente nuevo
	mensaje_registrar_cliente_nuevo()

	# Se ingresa a funcion para crear datos de cliente
	# Retorna una lista
	lista_datos_cliente_nuevo = registrar_cliente_nuevo()

	# Se agregan los datos de la lista a la base de datos de usuarios
	# Retorna un booleano si logra
	data_saved = save_cliente_nuevo(lista_datos_cliente_nuevo)

	# Aviso de que se logra guardar datos o no
	if data_saved == True:
		print("Datos Guardados")
	else:
		print("Datos no guardados")


def save_cliente_nuevo(lista):
	
	# INICIALIZACION
	resultado = True
	url_db_usuarios = "usuarios.csv"

	# OPERACION
	with open(url_db_usuarios, 'a', encoding='utf-8') as db_usuarios:
	    db_usuarios.write("\n%s, %s, %s, %s, %s, %s, %s, %s" % (lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]))


	''' Version 2: Da errores, agregar cosas al final, no en nueva linea
	with open(url_db_usuarios, 'a', encoding='utf-8') as db_usuarios:
	    escritura = csv.writer(db_usuarios, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    escritura.writerows(lista)
	'''


	''' Version 1: Da errores
	with open(url_db_usuarios) as archivo:
	    with open(url_db_usuarios, "a") as archivo:
	    	writer = csv.writer(archivo)
	    	writer.writerows(lista)
	'''

	return resultado


def registrar_cliente_nuevo():
	
	# INICIALIZACION
	# Valores por default
	datos_cliente_nuevo = []
	keys_datos_cliente_nuevo = keys_datos_cliente()

	print("Ingrese los siguientes datos:")

	datos_cliente_nuevo.insert(0, str(cliente_nuevo_id_cleaner()))
	datos_cliente_nuevo.insert(1, input(keys_datos_cliente_nuevo[1]))
	datos_cliente_nuevo.insert(2, input(keys_datos_cliente_nuevo[2]))
	datos_cliente_nuevo.insert(3, str(cliente_nuevo_telefono_cleaner()))
	datos_cliente_nuevo.insert(4, str(cliente_nuevo_tipo_telefono_cleaner()))
	datos_cliente_nuevo.insert(5, input(keys_datos_cliente_nuevo[5]))
	datos_cliente_nuevo.insert(6, "True")
	datos_cliente_nuevo.insert(7, "False")

	return datos_cliente_nuevo


def keys_datos_cliente():

	# Datos de cliente
	keys_datos_cliente = (
							"Id de Cliente: ",
							"Apellido de Cliente: ",
							"Nombre de Cliente: ",
							"Telefono Principal de Cliente: ",
							"Tipo de telefono de Cliente (1 = Movil, 2 = Hogar, 3 = Trabajo): ",
							"Correo Electronico de Cliente: ",
							"Estado de Cliente (1 = Activo, 0 = No Activo): "
							"El cliente tiene peliculas rentadas"
							)

	return keys_datos_cliente


def cliente_nuevo_id_cleaner():

	resultado = random.randrange(10000000000)

	return resultado


def cliente_nuevo_telefono_cleaner():

	# INICIALIZACION
	keys_datos_cliente_nuevo = keys_datos_cliente()
	resultado = 00000000

	# OPERACIONES
	telefono = input(keys_datos_cliente_nuevo[3])
	if len(telefono) == 8:
		try:
			resultado = int(telefono)
		except ValueError:
			print("\n")
			print("El valor ingresado no es un numero, intente de nuevo\n")
			print("\n")
			cliente_nuevo_telefono_cleaner()
	else:
		print("\n")
		print("El telefono no tiene 8 digitos y/o contiene letras o simbolos, intente de nuevo.\n")
		cliente_nuevo_telefono_cleaner()
												
	# RESULTADO
	return resultado


def cliente_nuevo_tipo_telefono_cleaner():

	# INICIALIZACION
	keys_datos_cliente_nuevo = keys_datos_cliente()
	resultado = 0

	# OPERACIONES
	tipo_telefono = input(keys_datos_cliente_nuevo[4])
	if len(tipo_telefono) == 1:
		try:
			resultado = int(tipo_telefono)
			if resultado >= 1 and resultado <= 3:
				resultado = resultado
			else:
				print("\n")
				print("El tipo de telefono no es valido y/o contiene letras o simbolos, intente de nuevo.\n")
				cliente_nuevo_telefono_cleaner()
		except ValueError:
			print("\n")
			print("El valor ingresado no es un numero, intente de nuevo\n")
			print("\n")
			cliente_nuevo_telefono_cleaner()
	else:
		print("\n")
		print("Solo puede ser un valor numerico, intente de nuevo.\n")
		cliente_nuevo_telefono_cleaner()
												
	# RESULTADO
	return resultado


def imprimir_listas(lista):

	for x in lista:
		print(x, end="")
		print(", ")


### Main
def main():

	# Saludo Inicial
	saludo_inicial()

	# Desplegar menu de aplicacion
	menu()

if __name__ == "__main__":
	main()