import csv

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

def revisarUsuario(lista, busqueda):
  resultado = False #devolverá false por defecto si no encuentra un dato

  for row in lista:
    if row[0] == busqueda:
      resultado = row #si encuentra el dato en alguna linea de esa lista, se cambia el resultado a esa linea
      break #se sale del ciclo para no seguir corriendo innecesariamente
    
  return resultado    

def revisarPelicula(listapeli, code):
  resultado = False #devolverá false por defecto si no encuentra un dato

  for row in listapeli:
    if row[0] == code:
      resultado = row #si encuentra el dato en alguna linea de esa lista, se cambia el resultado a esa linea
      break #se sale del ciclo para no seguir corriendo innecesariamente
    
  return resultado

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

      linea = revisarUsuario(lista, number) #dato será lo que retorne la funcion de revisar dato con la lista de usuarios y lo que se ingreso como argumento

      if linea: #si linea no es False, se printea lo que es (si no es false, significa que se encontró una linea con el dato revisado)
        print("Usuario encontrado! :\n")
        print(linea)
      else:
        print("El usuario no existe")

    elif choice == 2:
      print ("* --------------------------------------- *")
      print ("|         Cantidad de Usuarios            *")
      print ("* --------------------------------------- *")
      print ("\n")

      f = open ("usuarios.csv", "r")
      reader = csv.reader(f,delimiter = ",")
      value = len(list(reader))
      
      print ("El sistema contiene actualmente " + str(value) + " usuarios")

    elif choice == 3:
      print ("* --------------------------------------- *")
      print ("|         Consulta de Peliculas           *")
      print ("* --------------------------------------- *")
      print ("\n")

      code = input("Ingrese un numero de identificacion de pelicula (5 digitos):\n")

      csvfile2 = open("peliculas_sistema.csv") #se lee el archivo en texto
      listapeli = csv.reader(csvfile2, delimiter=",", quotechar= "|") #se pasa a una lista de listas

      linea2 = revisarPelicula(listapeli, code) #dato será lo que retorne la funcion de revisar dato con la lista de usuarios y lo que se ingreso como argumento

      if linea2: #si linea no es False, se printea lo que es (si no es false, significa que se encontró una linea con el dato revisado)
        print("Pelicula encontrada!: \n")
        print(linea2)
      else:
        print("La pelicula no esta en el sistema")

    elif choice == 4:
      print ("* --------------------------------------- *")
      print ("|         Cantidad de Peliculas           *")
      print ("* --------------------------------------- *")
      print ("\n")

      f = open ("peliculas_sistema.csv", "r")
      reader = csv.reader(f,delimiter = ",")
      value = len(list(reader))
      
      print ("El sistema contiene actualmente " + str(value) + " peliculas")
        
    elif choice == 5:
        print ("Menu Principal")

    else:
        print ("Por favor introduzca una opcion valida")
