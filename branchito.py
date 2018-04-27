def consulta_menu():

  print ("* --------------------------------------- *")
  print ("|         Consulta de Informacion         |")
  print ("* --------------------------------------- *")
  print ('\n')
  print ("En este menu puede consultar la cantidad de usuarios o peliculas en el sistema, asi como un usuario o una pelicula en especifico.")
  print ('\n')
  print ("1. Consultar Usuarios")
  print ("2. Cantidad de Usuarios")
  print ("3. Consultar Peliculas")
  print ("4. Cantidad de Peliculas")
  print ("5. Salir")
  print ("\n")

while consulta_menu() != "5":
    choice = int(input("Introduzca un numero entre 1 y 5:\n"))
             
    if choice == 1:
      print ("* --------------------------------------- *")
      print ("|         Consulta de Usuarios            *")
      print ("* --------------------------------------- *")
      print ("\n")
      import csv
      import sys
      number = int(input("Ingrese un numero de cedula:\n"))
      archivo = open("usuarios.csv", "r")
      lineas = archivo.readlines()
      
      for line in lineas:
          attributos = line.split(".")

          print ("Cedula: "+atributos[0])
          print ("Apellido: "+atributos[1])
          print ("Nombre: "+atributos[2])
          print ("Numero de Telefono: "+atributos[3])
          print ("Tipo de Telefono: "+atributos[4])
          print ("Direccion de Correo: "+atributos[5])
          print ("Estatus de Usuario: "+atributos[6])
          print ("Tiene Peliculas Rentadas?: "+atributos[7])     

	




