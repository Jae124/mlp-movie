import numpy as np
import pandas as pd

#read in data sets
movies = pd.read_csv('ml-latest-small/movies.csv')

ratings = pd.read_csv('ml-latest-small/ratings.csv')
ratings_agg = ratings[['movieId','rating']].groupby('movieId',as_index=False).mean()

#imdb = pd.read_csv('ml-latest-small/scraped_imdb_data.csv', encoding='ISO-8859-1')
imdb = pd.read_csv('ml-latest-small/scraped_imdb_data.csv')
imdb_data = imdb[['Director','Runtime','movieId']]

#join tables 
movies.set_index('movieId',inplace=True)
ratings_agg.set_index('movieId',inplace=True)
imdb_data.set_index('movieId',inplace=True)
join_1 = movies.join(ratings_agg,how='inner')
join_2 = join_1.join(imdb_data,how = 'inner')
mov_data_sm = join_2

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
director_lst = list(set(mov_data_sm['Director'].tolist()))
pd.Series(director_lst).to_csv('director_lst.csv',index=False,header=True)

mov_data_sm = pd.get_dummies(mov_data_sm,columns=['Director'])

#drop title
mov_data_sm.drop('title',axis=1,inplace=True)

mov_data_sm.head(10).to_csv('movie_train.csv',index=True)



