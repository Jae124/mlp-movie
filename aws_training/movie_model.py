import numpy as np
import pandas as pd

print('Read in Data')

#read in data sets
movies = pd.read_csv('ml-latest-small/movies.csv')

ratings = pd.read_csv('ml-latest-small/ratings.csv')
ratings_agg = ratings[['movieId','rating']].groupby('movieId',as_index=False).mean()

#imdb = pd.read_csv('ml-latest-small/scraped_imdb_data.csv', encoding='ISO-8859-1')
imdb = pd.read_csv('ml-latest-small/scraped_imdb_data.csv')
imdb_data = imdb[['Director','Runtime','movieId']]

print('Join Tables')

#join tables 
movies.set_index('movieId',inplace=True)
ratings_agg.set_index('movieId',inplace=True)
imdb_data.set_index('movieId',inplace=True)
join_1 = movies.join(ratings_agg,how='inner')
join_2 = join_1.join(imdb_data,how = 'inner')
mov_data_sm = join_2

print('Preprocess Descriptive Features')

#preprocess genres
genres = mov_data_sm['genres'].astype(str).apply(lambda s:s.split('|'),0)
genres_bin = pd.get_dummies(genres.apply(pd.Series).stack()).sum(level=0)
mov_data_sm.drop('genres',axis=1,inplace=True)
mov_data_sm = mov_data_sm.join(genres_bin)

#preprocess runtime
mov_data_sm['Runtime'] = mov_data_sm['Runtime'].astype(str).apply(lambda s:s.strip(' min'),0)
def time_to_int(t):
    try:
        return int(t)
    except:
        return 90
mov_data_sm['Runtime'] = mov_data_sm['Runtime'].apply(time_to_int,0).astype(int)

#preprocess directors 
mov_data_sm = pd.get_dummies(mov_data_sm,columns=['Director'])

#drop title
mov_data_sm.drop('title',axis=1,inplace=True)

print('Preprocess Posters')

#read in posters and return normalized image dim of (150,225,3)
from PIL import Image
from scipy.misc import imresize

def get_img_arr(movieid):
    try:
        img = Image.open("posters/poster_"+str(movieid)+".jpg")
        img = np.array(img)
        img = imresize(img,(225,150,3))
        assert img.shape == (225,150,3)
        return img*1.0/256
    except:
        #print movieid
        return np.zeros((150,225,3))-1

images = []
indexes_selected = []
n=0
for i in mov_data_sm.index:
    img = get_img_arr(i)
    #print img.shape
    if img[0,0,0] >=0:
        images.append(img)
        indexes_selected.append(i)
    else:
        n+=1

images = np.array(images)

print('Run Random Forest')

#preprare data for random forest 
from sklearn.model_selection import train_test_split
y = mov_data_sm['rating'].loc[indexes_selected]
x = mov_data_sm.drop('rating',axis=1).loc[indexes_selected]
assert x.shape[0] == y.shape[0]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=21)

#random forest model 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
rfg = RandomForestRegressor(200)

rfg.fit(x_train,y_train)
rfg_pred = rfg.predict(x_test)
rfg_mse = mean_squared_error(rfg_pred,y_test)
print ('Random Forest Regressor Test MSE:',rfg_mse)

from sklearn.externals import joblib
joblib.dump(rfg,'models/rfg.pkl')

print('Run CNN for Posters')

#prepare data for CNN 
x_cnn = images
assert x_cnn.shape[0] == y.shape[0]
x_cnn_train, x_cnn_test, y_cnn_train, y_cnn_test = train_test_split(x_cnn, y, test_size=0.15, random_state=21)

#import kera layers
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D

#cnn settings 
batch_size = 200
epochs = 10

#build cnn model with keras 
model = Sequential()
model.add(Conv2D(32,(3,3),input_shape = (225,150,3),data_format = 'channels_last'))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('linear'))

opt = keras.optimizers.rmsprop(lr=0.001, decay=1e-6)

model.compile(loss='mean_squared_error',optimizer=opt,metrics=['mean_squared_error'])

print ('Fitting CNN')

#fit model, run on AWS 
model.fit(x_cnn_train, y_cnn_train,batch_size=batch_size,epochs=epochs,validation_data=(x_cnn_test, y_cnn_test),shuffle=True)
scores = model.evaluate(x_cnn_test, y_cnn_test, verbose=1)
cnn_pred = model.predict(x_cnn_test)
print('CNN MSE:', scores[0])
model.save('models/cnn')

print('Show Sample Predictions from Both Models')
print(rfg_pred[:10])
print (cnn_pred[:10])

print('Ensemble both models with LR')

from sklearn.linear_model import LinearRegression
x_lr_train = np.column_stack((rfg.predict(x_train),model.predict(x_cnn_train)))
lr = LinearRegression()
lr.fit(x_lr_train,y_train)
lr_pred = lr.predict(np.column_stack((rfg_pred,cnn_pred)))
lr_mse = mean_squared_error(lr_pred,y_test)
print('Ensmble MSE:',lr_mse)
joblib.dump(lr,'models/lr.pkl')