# Code to get movie rating from imdb and sort the list of movies.
import imdb

imdb = imdb.IMDb(accessSystem='http')
movie = imdb.get_movie('0114369')

name = movie['title']
rating = movie['rating']
print "Movie name:: %s \nRating:: %0.2f" %(name, rating)

request = self.request()
item_id = request.uri().split('/')[-1]
self.data = self.app.get_movie(item_id)
