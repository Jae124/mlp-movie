# Movie Rating Predictor
<hr>
This machine learning program will predict movie ratings based on runtime, director, genre, and poster image.

### Set-up 
Please download the models [here](http://bit.ly/2BE1eZ4)
and place the `models` folder in the same directory as predict_rating.py. 

JavaScript package manager, npm, should be installed.

Python 2.7 should be used.

You will need the following modules installed in your local machine in order to run the script:
```
numpy
pandas
sklearn
urllib
PIL
scipy
keras
tornado
```

### Run
Everything will run in localhost 127.0.0.1

Start the Tornado back-end:
```
$ cd server
$ python hi.py
```
If a window pops up asking "Do you want the application “Python.app” to accept incoming network connections?" click "Allow."

Start the React front-end:
```
$ cd ui
$ npm start
```

Go to "localhost:3000" in your browser.

### Parameters

| Parameter        | Data type           | Notes  |
| --- |:------:| ----------------------------:|
| Runtime     | int |  |
| Director      | string      |   Only use the directors listed in `data/director_lst` |
| Genre1 | string      |     |
| Genre2 | string      |     |
| Genre3 | string      |  For all genre, only use genres listed in `data/genres_list`    |
| Poster URL | string      |  Only use IMDB image url's. Goto the IMDB page for a movie; click the poster image; right-click and select 'Copy Link Address' or equivalent   |



### Result
The prediction output will be shown as follows:
```
Predicted rating: [ x ] 
```
where x is the rating (double) that follows a 5-star rating system [0-5]. 

<hr>

## Future Sprints

* Drop-down menu for Director, Genre
* "Prettier" UI




