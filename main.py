#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Importe de modulos
import random

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

		# Capturar entrada de cliente (string)
		opcion_menu = input("Por favor ingrese una opcion (1-3): ")
		print("\n")

		# Evaluar si dato ingresado es valido en try:Except
		try:
			
			# Tratar de convertir dato capturado a INT
			opcion_menu = int(opcion_menu)

			# Si opcion es validad pasar a entrar a submenus
			if opcion_menu == 1:
				opcion_registrar_cliente()
			elif opcion_menu == 2:
			    print("\n2. Menu de peliculas\n")
			elif opcion_menu == 3:
				print("\n3. Consultar informacion\n")
			else:
				# Salir del sistema
				# Mensaje de despedida agregado
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


def opcion_registrar_cliente():
	
	print("REGISTRAR CLIENTE")
	print("\n")

	registrar_cliente_nuevo()

	# Volver a llamar al menu
	menu()


def registrar_cliente_nuevo():
	
	# Valores por default
	datos_cliente_nuevo = [0, "", "", 00000000, 1, "", True, False]
	keys_datos_cliente_nuevo = keys_datos_cliente()

	print("Ingrese los siguientes datos:")
	datos_cliente_nuevo[0] = random.randrange(10000000000)
	datos_cliente_nuevo[1] = input(keys_datos_cliente_nuevo[1])
	datos_cliente_nuevo[2] = input(keys_datos_cliente_nuevo[2])
	datos_cliente_nuevo[3] = int(input(keys_datos_cliente_nuevo[3]))
	datos_cliente_nuevo[4] = int(input(keys_datos_cliente_nuevo[4]))
	datos_cliente_nuevo[5] = input(keys_datos_cliente_nuevo[5])

	return datos_cliente_nuevo


def keys_datos_cliente():

	# Datos de cliente
	keys_datos_cliente = (
							"Id de Cliente: ",
							"Apellido de Cliente: ",
							"Nombre de Cliente: ",
							"Telefono Principal de Cliente: ",
							"Tipo de telefono de Cliente: ",
							"Correo Electronico de Cliente: ",
							"Estado de Cliente (1 = Activo, 0 = No Activo): "
							)

	return keys_datos_cliente



def imprimir_listas(lista):

	for x in range(lista):
		lista[x]

### Main
def main():

	# Saludo Inicial
	saludo_inicial()

	# Desplegar menu de aplicacion
	menu()

if __name__ == "__main__":
	main()