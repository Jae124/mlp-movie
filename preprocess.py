import numpy as np 
import pandas as pd 
from sklearn.externals import joblib
import urllib
def preprocess(director_1, genres, runtime, img_url, actors):

	
	
	filename = 'test.jpg'

	#train = pd.read_csv('data/movie_train.csv',index_col=0)
	train = pd.read_csv('data/movie_train_2.csv',index_col=0)
	x = train.iloc[0]
	
	if director_1 != "":
		director = 'Director_'+director_1
		x[director] = 1

	for g in genres:
		if g != "":
			x[g] = 1
	
	for a in actors:
 		if a != "":
 			x['Actor_'+a] = 1
	
	try:
		runtime = int(runtime)
		if runtime <= 0:
			return None, " runtime "
		x['Runtime']=runtime
	except:
		return None, " runtime "
	x.drop('rating',axis=0,inplace=True)
	x = x.reshape((1,len(x)))
	from PIL import Image
	from scipy.misc import imresize

	try:
		urllib.urlretrieve(img_url, filename)
		img = Image.open("test.jpg")
		img = np.array(img)
		img = imresize(img,(225,150,3))
		img = img*1.0/256
		img = np.array([img])
	except:
		return None, " url "


	return x,img
