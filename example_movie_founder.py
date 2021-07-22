import imdb

ib = imdb.IMDb()

top250m = ib.get_top250_movies()
top10m = top250m[:10]

for movie in top10m:
    movie_title = movie["title"]

    found_movie = ib.search_movie(movie_title)

    year = found_movie[0]['year']
    print(found_movie[0]['title'] + " : " + str(year))






