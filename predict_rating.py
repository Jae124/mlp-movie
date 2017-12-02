import numpy as np 
import pandas as pd 

from sklearn.externals import joblib

train = pd.read_csv('data/movie_train.csv',index_col=0)

x_len = train.shape[1]-1
#hard coidng x for now

x = np.zeros((1,x_len))
x[0,0]=120
x[0,10]=1
x[0,20]=1
x[0,100]=1

from PIL import Image
from scipy.misc import imresize
img = Image.open("data/sample.jpg")
img = np.array(img)
img = imresize(img,(225,150,3))
img = img*1.0/256

import keras
from keras.models import load_model

model = load_model('models/cnn')
rfg = joblib.load('models/rfg.pkl')
lr = joblib.load('models/lr.pkl')

x1 = rfg.predict(x)
x2 = mopdel.predict(img)
print(x1)
print(lr.predict(np.array([[x1,4.5]])))