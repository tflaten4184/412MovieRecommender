import csv

with open('netflix_titles_nov_2019.csv',encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)

    movies = {}

    for row in csv_reader:
        movies[row[1]] = row[10]

    #for each in movies:
        #print(movies)