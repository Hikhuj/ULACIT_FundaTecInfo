import random
import csv
import sys

def get_movie_id_row_number(movie_id):

	'''
		Recibe un movie_id (numero entero) y retorna un numero entero(row number donde este el id)
	'''

	# INICIALIZACION
	movies_db = "peliculas.csv"
	count = 0
	results = ['','']

	# OPERACION
	with open(movies_db, 'r', encoding='utf-8') as csv_movies:
		readable = csv.reader(csv_movies, delimiter='|')
		for row in readable:
			if row[0] == movie_id:
				results.insert(0, True)
				if results[0] == True:
					results.insert(1,count)
					break
				else:
					results.remove(1)
					results.insert(1, False)
			else:
				count += 1

	return results

### Main
def main():

	# Saludo Inicial
	temp = get_movie_id_row_number(11111)

	for x in temp:
		print(x)

if __name__ == "__main__":
	main()