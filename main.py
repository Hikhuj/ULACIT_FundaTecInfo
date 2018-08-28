#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Importe de modulos
import random
import csv
import sys

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

# Obtener el tiempo para guardar: https://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/


def opciones_de_menu_principal():
	mensaje_menu_principal()
	print("1. Registrar clientes nuevos")
	print("2. Menu de Peliculas")
	print("3. Consultar informacion")
	print("4. Salir")
	print("\n")


#  Funciones
def menu():
	
	# Variable permite que ingrese al ciclo
	opcion_menu = 1

	# Ciclo mantiene al cliente dentro del menu hasta que digite X numero y se salga
	while opcion_menu >= 1 and opcion_menu < 4:

		# Funcion imprime opciones de menu
		opciones_de_menu_principal()

		# Evaluar si dato ingresado es valido en try:Except
		try:
			
			# Capturar entrada de cliente (string)
			opcion_menu = input("Por favor ingrese una opcion (1-4): ")
			print("\n")

			# Tratar de convertir dato capturado a INT
			opcion_menu = int(opcion_menu)

			# Si opcion es valida, ingresar a submenus
			if opcion_menu == 1:
				opcion_registrar_cliente()

			elif opcion_menu == 2:
			    function_menu_peliculas_sistema()

			elif opcion_menu == 3:
				consultar_informacion_menu()
			    # Volver a llamar al menu
				menu()

			else:
				despedida()
				sys.exit(1)

		except ValueError:

			# Mostrar error: cliente no ingreso numero
			print("\n")
			print("Valor u opción no valida, intente de nuevo")
			print("\n")

			# Volver a llamar al menu
			menu()


# Menu 1: Submenu 1
def opcion_registrar_cliente():
	
	# VARIABLES
	data_saved = True

	mensaje_registrar_cliente_nuevo()

	# Se ingresa a funcion para crear datos de cliente
	# Retorna una lista
	lista_datos_cliente_nuevo = registrar_cliente_nuevo()

	# Se agregan los datos de la lista a la base de datos de usuarios
	# Retorna un booleano si logra
	data_saved = save_cliente_nuevo(lista_datos_cliente_nuevo)

	# Aviso de que se logra guardar datos o no
	if data_saved == True:
		print("\nUsuario registrado exitosamente\n")
	else:
		print("\nDatos no guardados\n")

	menu()
	

def mensaje_function_menu_peliculas_sistema():

	print("\n")
	print("* --------------------------------------- *")
	print("|                                         |")
	print("|             MENU DE PELICULAS           |")
	print("|                                         |")
	print("* --------------------------------------- *")
	print("\n")
	print("1. Buscar pelicula")
	print("2. Ingresar nueva pelicula")
	print("3. Editar informacion de pelicula")
	print("4. Volver al menu principal")
	print("\n")


# Menu 1: Submenu 2
def function_menu_peliculas_sistema():

	# INICIALIZACION
	# Variable permite que ingrese al ciclo
	opcion_menu = 1

	# Ciclo mantiene al cliente dentro del menu hasta que digite X numero y se salga
	while opcion_menu >= 1 and opcion_menu <= 3:

		# Desplegar Submenu 2
		mensaje_function_menu_peliculas_sistema()

		# Evaluar si dato ingresado es valido en try:Except
		try:
			# Capturar entrada de cliente (string)
			opcion_menu = input("Por favor ingrese una opcion (1-4): ")
			print("\n")

			# Tratar de convertir dato capturado a INT
			opcion_menu = int(opcion_menu)

			# Si opcion es validad pasar a entrar a submenus
			if opcion_menu == 1:

				# Opcion 1: Buscar una pelicula
				function_buscar_peliculas()
				# Volver a llamar al menu de peliculas
				function_menu_peliculas_sistema()

			elif opcion_menu == 2:

				# Opcion 2: Ingresar nueva pelicula
				function_agregar_nueva_pelicula()

			elif opcion_menu == 3:

				function_editar_informacion_pelicula()
			    # Volver a llamar al menu
				function_menu_peliculas_sistema()

			else:

				# Devolverse a menu principal desde Submenu 2
				menu()

		except ValueError:

			# Mostrar error: cliente no ingreso numero
			print("\n")
			print("El valor ingresado no es un numero, intente de nuevo")
			print("\n")

			# Volver a llamar al menu
			function_menu_peliculas_sistema()


def function_imprimir_peliculas():

	url_db_peliculas = "peliculas.csv"

	# OPERACION
	with open(url_db_peliculas, 'r', encoding='utf-8') as file:
		file = csv.reader(file, delimiter=',')
		for line in file:
			print(line)


def function_imprimir_usuarios():

	url_db_usuarios = "usuarios.csv"

	# OPERACION
	with open(url_db_usuarios, 'r', encoding='utf-8') as file:
		file = csv.reader(file, delimiter=',')
		for line in file:
			print(line)


def function_editar_informacion_pelicula():

	# Variable list
	movie_list = []
	movie_db = "peliculas.csv"
	mensaje_alerta = "\nNo se encuentra la pelicula\n"
	found_movie = False
	lista_headers_peliculas = headers_peliculas_sistema()


	# Print movie list
	print("Por favor revise la siguiente lista\n")
	function_imprimir_peliculas()
	print("\n")


	# Preguntar el id que quiere modificar
	movie_id = input("Ingrese el id de pelicula a editar (id de 5 numeros: #####): ")


	is_number = verify_if_number(movie_id)
	if is_number == True:
		


			with open(movie_db, 'w', encoding='utf-8') as csv_writable:
				writer = csv.writer(csv_writable, delimiter='|')

				with open(movie_db, 'r', encoding='utf-8') as csv_readable:
					reader = csv.reader(csv_readable, delimiter='|')

					for row in reader:
						if linea[0] == int(movie_id):
							for indice in range(len(linea)):
								if indice == 3:
									if int(linea[indice]) == 1:
										print(lista_headers_peliculas[indice] + "DVD-ROM")
									else:
										print(lista_headers_peliculas[indice] + "Blueray Disc")

								elif indice == 4:
									if int(linea[indice]) == 1:
										print(lista_headers_peliculas[indice] + "Usuario Activo")
									else:
										print(lista_headers_peliculas[indice] + "Usuario No Activo")
										
								else:
									print(lista_headers_peliculas[indice] + linea[indice])
							found_movie = True
							break

	else:
		print("Id no es un numero. Volvera al menu anterior")
		function_menu_peliculas_sistema()

	# Volver a llamar al menu de peliculas
	function_menu_peliculas_sistema()


def verify_if_number(movie_id):

	'''
		Receive data, if it is correct, will return a True.
	'''

	result = False

	try:
		number = int(movie_id)
		result = True
	except Exception as e:
		print("El valor ingresado no es un numero, intente de nuevo")
		print("\n")
		# Volver a llamar al menu de peliculas
		function_menu_peliculas_sistema()
	
	return result


def get_movie_id_row_number(movie_id):

	# VARIABLE LIST
	movies_db = "peliculas.csv"
	count = 0
	result = False

	# OPERATION
	with open(movies_db, 'r', encoding='utf-8') as csv_movies:
		readable = csv.reader(csv_movies, delimiter='|')
		for row in readable:
			if row[0] == movie_id:
				print(row[0])
				print("Pelicula encontrada")
				result = True
				break

	return result
	

def function_agregar_nueva_pelicula():

	resultado = function_buscar_peliculas_return()

	if resultado == True:
		print("")
		print("La pelicula que busca ya existe, debera buscar otra.")
		print("")
		opcion_usuario = int(input("Presione 1 para buscar de nuevo o bien 0 para salir: "))
		if opcion_usuario >= 0 and opcion_usuario <= 1:
			if opcion_usuario == 1:
				function_agregar_nueva_pelicula()
			else:
				menu()
		else:
			print("")
			print("Ingreso un valor no valido, volviendo a la opcion Ingresar nueva película")
			print("")
			function_agregar_nueva_pelicula()
	else:
		print("")
		datos_nueva_pelicula_listos = function_registrar_pelicula_nueva()
		save_pelicula_nueva(datos_nueva_pelicula_listos)
		print("")
		print("Pelicula guardada exitosamente")
		print("")


def function_registrar_pelicula_nueva():

	# INICIALIZACION
	datos_pelicula_nueva = []

	print("Ingrese los siguientes datos de la pelicula nueva:")

	datos_pelicula_nueva.insert(0, str(pelicula_nueva_id_cleaner()))
	datos_pelicula_nueva.insert(1, pelicula_nueva_nombre_cleaner())
	datos_pelicula_nueva.insert(2, pelicula_nueva_sinopsis_cleaner())
	datos_pelicula_nueva.insert(3, str(pelicula_nueva_tipoDisco_cleaner()))
	datos_pelicula_nueva.insert(4, str(pelicula_nueva_estadoPelicula_cleaner()))

	return datos_pelicula_nueva


def save_pelicula_nueva(lista):
	
	# INICIALIZACION
	resultado = True
	url_db_peliculas = "peliculas.csv"

	# OPERACION
	with open(url_db_peliculas, 'a', encoding='utf-8') as db_peliculas:
	    db_peliculas.write("\n%s, %s, %s, %s, %s" % (lista[0],lista[1],lista[2],lista[3],lista[4]))

	return resultado


def function_buscar_peliculas():

	id_pelicula = input("Ingrese el id de pelicula (id de 5 numeros: #####): ")

	buscar_id_pelicula_en_db(id_pelicula)

	print("\n")


def buscar_id_pelicula_en_db(id_pelicula):

	'''
		Funcion recibe id de pelicula
		Busca id de pelicula en el CSV
		Si existe, retorna True
		De otro modo, si no existe, retorna False
	'''

	# INICIALIZACION
	lista_headers_peliculas = headers_peliculas_sistema()
	url_db_peliculas = "peliculas.csv"
	pelicula_encontrada = False
	mensaje_alerta = "\nNo se encuentra la pelicula\n"

	# OPERACION
	with open(url_db_peliculas, 'r', encoding='utf-8') as db_peliculas:
		archivo = csv.reader(db_peliculas, delimiter='|')
		for linea in archivo:
			if linea[0] == id_pelicula:
				for indice in range(len(linea)):
					if indice == 3:
						if int(linea[indice]) == 1:
							print(lista_headers_peliculas[indice] + "DVD-ROM")
						else:
							print(lista_headers_peliculas[indice] + "Blueray Disc")

					elif indice == 4:
						if int(linea[indice]) == 1:
							print(lista_headers_peliculas[indice] + "Usuario Activo")
						else:
							print(lista_headers_peliculas[indice] + "Usuario No Activo")
							
					else:
						print(lista_headers_peliculas[indice] + linea[indice])
				pelicula_encontrada = True
				break

		if pelicula_encontrada != True:
			print(mensaje_alerta)


def headers_peliculas_sistema():

	# Datos de cliente
	keys_db_peliculas_sistema = ["Id de Pelicula: ", "Nombre de Pelicula: ", "Sinopsis de Pelicula: ", "Tipo de disco de la pelicula: ", "Estado de pelicula: "]

	return keys_db_peliculas_sistema


def saludo_inicial():
	print("\n")
	print("* --------------------------------------- *")
	print("|                                         |")
	print("|           Inicializando Sistema         |")
	print("|                                         |")
	print("* --------------------------------------- *")
	print("\n")


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


def mensaje_menu_peliculas():
	print("\n")
	print("* --------------------------------------- *")
	print("|                                         |")
	print("|            MENU DE PELICULAS            |")
	print("|                                         |")
	print("* --------------------------------------- *")
	print("\n")


def mensaje_menu_informacion_cliente():
	print("\n")
	print("* --------------------------------------- *")
	print("|                                         |")
	print("|       INFORMACION DE LOS CLIENTES       |")
	print("|                                         |")
	print("* --------------------------------------- *")
	print("\n")


def mensaje_menu_principal():
	print("\n")
	print("* --------------------------------------- *")
	print("|                                         |")
	print("|              MENU PRINCIPAL             |")
	print("|                                         |")
	print("* --------------------------------------- *")
	print("\n")


def save_cliente_nuevo(lista):
	
	# INICIALIZACION
	resultado = True
	url_db_usuarios = "usuarios.csv"

	# OPERACION
	with open(url_db_usuarios, 'a', encoding='utf-8') as db_usuarios:
	    db_usuarios.write("\n%s, %s, %s, %s, %s, %s, %s, %s" % (lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]))

	return resultado


def registrar_cliente_nuevo():
	
	# INICIALIZACION
	# Valores por default
	datos_cliente_nuevo = []
	keys_datos_cliente_nuevo = keys_datos_cliente()

	print("Ingrese los siguientes datos del nuevo cliente:")

	datos_cliente_nuevo.insert(0, str(cliente_nuevo_id_cleaner()))
	datos_cliente_nuevo.insert(1, cliente_nuevo_apellido_cleaner())
	datos_cliente_nuevo.insert(2, cliente_nuevo_nombre_cleaner())
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
							"Estado de Cliente (1 = Activo, 0 = No Activo): ",
							"El cliente tiene peliculas rentadas"
							)

	return keys_datos_cliente


def keys_datos_pelicula():

	# Datos de pelicula
	keys_datos_pelicula = (
							"Numero de identificación de película: ",
							"Nombre de película: ",
							"Descripción de película: ",
							"Tipo de disco (Ingrese 1 para DVD-ROM o bien 2 para Blueray Disc): ",
							"La película está rentada? (1 para si, 0 para no): "
							)

	return keys_datos_pelicula


def cliente_nuevo_id_cleaner():

	resultado = random.randrange(10000000000)
	return resultado


def pelicula_nueva_id_cleaner():

	# INICIALIZACION
	keys_datos_pelicula_nueva = keys_datos_pelicula()
	resultado = 0

	# OPERACIONES
	try:
		id_de_pelicula = input(keys_datos_pelicula_nueva[0])
		if len(id_de_pelicula) == 5:
			resultado = int(id_de_pelicula)
	except Exception as e:
		print("")
		print("El id no tiene 5 digitos o bien ingreso una letra")
		print("")
		pelicula_nueva_id_cleaner()

	# RESULTADO
	return resultado


def pelicula_nueva_nombre_cleaner():

	# INICIALIZACION
	keys_datos_pelicula_nueva = keys_datos_pelicula()
	resultado = ""

	# OPERACIONES
	resultado = input(keys_datos_pelicula_nueva[1])

	# RESULTADO
	return resultado


def pelicula_nueva_sinopsis_cleaner():

	# INICIALIZACION
	keys_datos_pelicula_nueva = keys_datos_pelicula()
	resultado = ""

	# OPERACIONES
	resultado = input(keys_datos_pelicula_nueva[2])

	# RESULTADO
	return resultado


def pelicula_nueva_tipoDisco_cleaner():

	# INICIALIZACION
	keys_datos_pelicula_nueva = keys_datos_pelicula()
	resultado = 0

	# OPERACIONES
	tipo_disco = input(keys_datos_pelicula_nueva[3])
	if len(tipo_disco) == 1:
		try:
			resultado = int(tipo_disco)
			if resultado >= 1 and resultado <= 2:
				resultado = resultado
			else:
				print("\n")
				print("La opcion no existe, ingrese una opcion valida\n")
				pelicula_nueva_tipoDisco_cleaner()
		except ValueError:
			print("\n")
			print("El valor ingresado no es un numero, intente de nuevo\n")
			print("\n")
			pelicula_nueva_tipoDisco_cleaner()
	else:
		print("\n")
		print("Solo puede ser un valor numerico, intente de nuevo.\n")
		pelicula_nueva_tipoDisco_cleaner()
												
	# RESULTADO
	return resultado


def pelicula_nueva_estadoPelicula_cleaner():

	# INICIALIZACION
	keys_datos_pelicula_nueva = keys_datos_pelicula()
	resultado = 0

	# OPERACIONES
	estado_pelicula = input(keys_datos_pelicula_nueva[4])
	if len(estado_pelicula) == 1:
		try:
			resultado = int(estado_pelicula)
			if resultado >= 0 and resultado <= 1:
				resultado = resultado
			else:
				print("\n")
				print("La opcion no existe, ingrese una opcion valida\n")
				pelicula_nueva_estadoPelicula_cleaner()
		except ValueError:
			print("\n")
			print("El valor ingresado no es un numero, intente de nuevo\n")
			print("\n")
			pelicula_nueva_estadoPelicula_cleaner()
	else:
		print("\n")
		print("Solo puede ser un digito, intente de nuevo.\n")
		pelicula_nueva_estadoPelicula_cleaner()
												
	# RESULTADO
	return resultado


def cliente_nuevo_apellido_cleaner():

	# INICIALIZACION
	keys_datos_cliente_nuevo = keys_datos_cliente()
	resultado = ""

	# OPERACIONES
	apellido = input(keys_datos_cliente_nuevo[1])
	apellido = apellido.lower()
	inicial_apellido = apellido[0].upper()
	resto_apellido = apellido[1:]
	resultado = inicial_apellido + resto_apellido
												
	# RESULTADO
	return resultado


def cliente_nuevo_nombre_cleaner():

	# INICIALIZACION
	keys_datos_cliente_nuevo = keys_datos_cliente()
	resultado = ""

	# OPERACIONES
	nombre = input(keys_datos_cliente_nuevo[2])
	nombre = nombre.lower()
	inicial_nombre = nombre[0].upper()
	resto_nombre = nombre[1:]
	resultado = inicial_nombre + resto_nombre
												
	# RESULTADO
	return resultado


def cliente_nuevo_telefono_cleaner():

	# INICIALIZACION
	keys_datos_cliente_nuevo = keys_datos_cliente()
	resultado = ""

	# OPERACIONES
	try:
		telefono = int(input(keys_datos_cliente_nuevo[3]))
		resultado = telefono
	except Exception as e:
		print("El valor ingresado no es un numero, intente de nuevo\n")
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
				print("La opcion no existe, ingrese una opcion valida\n")
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



######## DANIEL MORA ############

def consulta_menu():
	
	print("\n")
	print("* --------------------------------------- *")
	print("|                                         |")
	print("|         CONSULTA DE INFORMACION         |")
	print("|                                         |")
	print("* --------------------------------------- *")
	print("\n")
	print ("En este menu puede consultar la cantidad de usuarios o peliculas en el sistema,\tasi como un usuario o una pelicula en especifico.")
	print ('\n')
	print ("1. Consultar Usuarios")
	print ("2. Cantidad de Usuarios")
	print ("3. Consultar Peliculas")
	print ("4. Cantidad de Peliculas")
	print ("5. Salir")
	print ("\n")


def revisarUsuario(lista, busqueda):
	resultado = [] #devolverá false por defecto si no encuentra un dato
	header = [
				"Numero de Cedula: ",
				"Apellido: ",
			 	"Nombre: ",
			 	"Telefono: ",
				"Tipo de Telefono: ",
				"Correo Electronico: ",
				"Estado: ",
				"Tiene peliculas: "
				]
	usuario_encontrado = False
	mensaje_alerta = "\nNo se encuentro usuario.\n"

	for row in lista:
		if row[0] == busqueda:
			#si encuentra el dato en alguna linea de esa lista, se cambia el resultado a esa linea
			lista_usuario = row
			print("")
			print("Usuario encontrado!: ")
			print(" ")

			'''
			for indice in range(len(linea)):
				if indice == 3:
					if int(linea[indice]) == 1:
						print(lista_headers_peliculas[indice] + "DVD-ROM")
					else:
						print(lista_headers_peliculas[indice] + "Blueray Disc")
			'''

			for indice in range(len(lista_usuario)):
				if indice == 3:
					if int(lista_usuario[indice]) == 1:
						print(header[indice] + "DVD-ROM")
					else:
						print(header[indice] + "Blueray Disc")

				elif indice == 4:
					if int(lista_usuario[indice]) == 1:
						print(header[indice] + "Usuario Activo")
					else:
						print(header[indice] + "Usuario No Activo")
				else:
					print(header[indice] + lista_usuario[indice])
			usuario_encontrado = True
			'''
				elif indice == 4:
					if int(linea[indice]) == 1:
						print(lista_headers_peliculas[indice] + "Usuario Activo")
					else:
						print(lista_headers_peliculas[indice] + "Usuario No Activo")
				else:
					print(lista_headers_peliculas[indice] + linea[indice])
			pelicula_encontrada = True
			break
			'''
			break

	if usuario_encontrado != True:
		print(mensaje_alerta)


def revisarPelicula(listapeli, code):
	resultado = [] #devolverá false por defecto si no encuentra un dato
	header2 = [
				"Codigo de Pelicula: ",
				"Nombre: ",
				"Director: ",
				"Tipo de Disco: ",
				"Descripcion: ",
				"Estado de Disco: "
				]
	pelicula_encontrada = False
	mensaje_alerta = "\nNo se encuentra la pelicula.\n"

	for row in listapeli:
		if row[0] == code:
			#si encuentra el dato en alguna linea de esa lista, se cambia el resultado a esa linea
			lista_pelicula = row
			print("")
			print("Pelicula encontrada!: ")
			print(" ")

			for indice in range(len(lista_pelicula)):
				print(header2[indice], ": ", lista_pelicula[indice])
				pelicula_encontrada = True
			break
	
		else:
			pelicula_encontrada


	if pelicula_encontrada != True:
		print(mensaje_alerta)


def consultar_informacion_menu():

	header = [
				"Numero de Cedula",
				"Apellido",
			 	"Nombre",
			 	"Telefono",
				"Tipo de Telefono",
				"Correo Electronico",
				"Estado",
				"Tiene peliculas"
				]

	header2 = [
				"Codigo de Pelicula",
				"Nombre",
				"Director",
				"Tipo de Disco",
				"Descripcion",
				"Estado de Disco"
				]

	while consulta_menu() != "5":
		choice = int(input("Introduzca un numero entre 1 y 5:\n"))

		if choice == 1:
			print ("* --------------------------------------- *")
			print ("|         Consulta de Usuarios            *")
			print ("* --------------------------------------- *")
			print ("\n")

			number = input("Ingrese un numero de cedula:\n")

			csvfile = open("usuarios.csv") #se lee el archivo en texto
			lista = csv.reader(csvfile, delimiter=",", quotechar= "|") #se pasa a una lista de listas

			revisarUsuario(lista, number) #dato será lo que retorne la funcion de revisar dato con la lista de usuarios y lo que se ingreso como argumento

		elif choice == 2:
			print ("* --------------------------------------- *")
			print ("|         Cantidad de Usuarios            *")
			print ("* --------------------------------------- *")
			print ("\n")

			f = open ("usuarios.csv", "r")
			reader = csv.reader(f,delimiter = ",")
			value = len(list(reader))

			print ("\nEl sistema contiene actualmente con " + str(value) + " usuarios\n")

		elif choice == 3:
			print ("* --------------------------------------- *")
			print ("|         Consulta de Peliculas           *")
			print ("* --------------------------------------- *")
			print ("\n")

			code = input("Ingrese un numero de identificacion de pelicula (5 digitos):\n")

			csvfile2 = open("peliculas.csv") #se lee el archivo en texto
			listapeli = csv.reader(csvfile2, delimiter=",", quotechar= "|") #se pasa a una lista de listas

			revisarPelicula(listapeli, code) #dato será lo que retorne la funcion de revisar dato con la lista de usuarios y lo que se ingreso como argumento

		elif choice == 4:
			print ("* --------------------------------------- *")
			print ("|         Cantidad de Peliculas           *")
			print ("* --------------------------------------- *")
			print ("\n")

			f = open ("peliculas.csv", "r")
			reader = csv.reader(f,delimiter = ",")
			value = len(list(reader))

			print ("El sistema contiene actualmente con " + str(value) + " peliculas")

		elif choice == 5:
			menu()

		else:
			print ("\nPor favor introduzca una opcion valida")


### Main
def main():

	# Saludo Inicial
	saludo_inicial()

	# Desplegar menu de aplicacion
	menu()

if __name__ == "__main__":
	main()