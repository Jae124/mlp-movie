import pandas as pd
import json
import urllib2
import urllib

links = pd.read_csv('links.csv')

i = 0

for index, row in links.iterrows():

	if i < 5:


		api_request = "http://www.omdbapi.com/?apikey=ef9d844d&i=tt0" + str(int(row['imdbId']))
		poster_link = json.load(urllib2.urlopen(api_request))["Poster"]
		filename_temp = str(int(row['movieId']))
		filename = "poster_" + filename_temp + ".jpg"
		urllib.urlretrieve(poster_link, filename)


		i = i + 1
