import numpy as np 
import pandas as pd 
from sklearn.externals import joblib
import urllib


def predict_rating(x,img):

	#director = 'Joss Whedon'
<<<<<<< HEAD
	#director = 'Director_'+director_1
=======
	director = 'Director_'+director_1

>>>>>>> origin/master
	#genres = ['Action','Adventure','Sci-Fi']
	#runtime = 143
	#img_url = 
	#filename = 'test.jpg'

<<<<<<< HEAD
	#train = pd.read_csv('data/movie_train.csv',index_col=0)
	#x = train.iloc[0]
	#x[director] = 1

	#for g in genres:
	#	if g != "":
	#		x[g] = 1
=======
	train = pd.read_csv('data/movie_train.csv',index_col=0)
	#train = pd.read_csv('data/movie_train_2.csv',index_col=0)
	x = train.iloc[0]
	x[director] = 1

	for g in genres:
		if g != "":
			x[g] = 1

	#for a in actors:
		#if a != "":
			#x['Actors_'+a] = 1	
>>>>>>> origin/master
	
	#x['Runtime']=runtime
	#x.drop('rating',axis=0,inplace=True)
	#x = x.reshape((1,3875))
	#from PIL import Image
	#from scipy.misc import imresize


	#urllib.urlretrieve(img_url, filename)

	#img = Image.open("test.jpg")
	#img = np.array(img)
	#img = imresize(img,(225,150,3))
	#img = img*1.0/256
	#img = np.array([img])

	import keras
	from keras.models import load_model

	model = load_model('models/cnn.h5')
<<<<<<< HEAD
	#rfg = joblib.load('models/rfg.pkl')
	rfg = joblib.load('models/rfg_2.pkl')
=======
	rfg = joblib.load('models/rfg.pkl')
	#rfg = joblib.load('models/rfg_2.pkl')
>>>>>>> origin/master
	lr = joblib.load('models/lr.pkl')

	x1 = rfg.predict(x)
	x2 = model.predict(img)
	return lr.predict([np.append(x1,x2.flatten())])