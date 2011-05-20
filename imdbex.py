# Code to get movie rating from imdb and sort the list of movies.

import imdb
import re

from xgoogle.search import GoogleSearch, SearchError
from xgoogle.googlesets import GoogleSets


def get_imdb_url(movie_name):
	
	try:
	# Use xgoogle api to parse google. Following is the url to the api
	# http://www.catonmat.net/blog/python-library-for-google-search/
		search_str = movie_name + ' site:imdb.com'
		gs = GoogleSearch(search_str)
		gs.results_per_page = 1
		results = gs.get_results()
		url = results[0].url.encode('utf8')
		# url_title = results[0].title.encode('utf8')
		# print url, url_title
		return url
	
	except SearchError, e:
		print "Search failed: %s" % e

def imdb_rating(url):
	tt = url.split('/')[-2]
	
	if(tt[0:2] == 'tt'):
		movie_id = tt[2:]
	else:
		movie_id = None
		print 'Note: \"%s\"  is\'t listed in imdb as movie name' %movie_name

	#  print movie name and movie rating using imdbpy api
	if movie_id != None:
		im = imdb.IMDb(accessSystem='http')
		movie = im.get_movie(movie_id)
		title = movie['title']
		year = movie['year']
		rating = movie['rating']
		print "Movie name:: %s (%d) \nRating:: %0.2f" %(title, year, rating)
		print

def main():
	url = get_imdb_url('Godfather')
	imdb_rating(url)
	
	# url = get_imdb_url('Scarface')
	# imdb_rating(url)
	# 
	# url = get_imdb_url('Gladiator')
	# imdb_rating(url)

    
	gs = GoogleSets(['Godfather', 'Scarface'])	
	results = gs.get_results()
	print 'Some movies you might like: '
	
	i = 0
	while i < 5:
		print "    ", (i + 1), ".", results[i].encode('utf8')
		i = i + 1 

				
if __name__ == '__main__':
	main()
	