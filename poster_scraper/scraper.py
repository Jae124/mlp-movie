import pandas as pd
import json
import urllib2
import urllib

links = pd.read_csv('links.csv')
noposters_file = 'noposters.txt'
api_key = "2908b68"

open(noposters_file, 'w').close()

for index, row in links.iterrows():
	
	
	try:
		imdbid = str(int(row['imdbId']))
		if len(imdbid) < 7:
			diff = 7 - len(imdbid)
			for i in range(diff):
				imdbid = "0" + imdbid
		
		api_request = "http://www.omdbapi.com/?apikey=" + api_key + "&i=tt" + imdbid
			
		poster_link = json.load(urllib2.urlopen(api_request))["Poster"]

		if poster_link == "N/A":
			raise KeyError
		
		filename_temp = str(int(row['movieId']))
		extension = poster_link.split('.')[-1]
		filename = "poster_" + filename_temp + "."+ extension
		urllib.urlretrieve(poster_link, filename)
	
	except KeyError:
		with open(noposters_file,'ab') as f:
			f.write(str(int(row['movieId']))+"\n")