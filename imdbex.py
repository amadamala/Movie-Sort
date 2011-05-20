# Code to get movie rating from imdb and sort the list of movies.
from xgoogle.search import GoogleSearch, SearchError
import imdb
import re


def imdb_url(movie_name):
	
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
	
	except SearchError, e:
		print "Search failed: %s" % e


def main():
	imdb_url('Godfather')

if __name__ == '__main__':
	main()
	