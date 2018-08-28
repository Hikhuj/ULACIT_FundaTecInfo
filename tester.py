import random
import csv
import sys

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

### Main
def main():

	temp = get_movie_id_row_number(11111)
	print(temp)

if __name__ == "__main__":
	main()