# Movie Rating Predictor
<hr>
This machine learning program will predict movie ratings based on runtime, director, genre, and poster image.

### Set-up 
Please download the models [here](http://bit.ly/2BE1eZ4) and place the `models` folder in the same directory as predict_rating.py. Please also download an updated model [here](https://drive.google.com/file/d/1nEWisBLDowAiW9yl1VPXiAPt6NQTssz_/view) and place it in the `models` folder.

JavaScript package manager, npm, and react (can be done through npm) should be installed.

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
$ npm install
$ npm start
```

Go to "localhost:3000" in your browser.

### Parameters

| Parameter  | Data type  |  Required? | Notes                                      |
| ---------  | ---------- | ---------- | :----------------------------------------- |
| Runtime    | int        | Yes        |                                            |
| Director   | string     | No         | Only choose director from the drop-down options|
| Genre      | string     | No         | For all genre, only choose genre from the drop-down options|
| Actor      | string     | No         | *IMPORTANT:* Currently Unstable. Some options may not work. Also, search is currently very slow; it is advisable to just scroll through the options and click |
| Poster URL | string     | Yes        | Only use IMDB image url's: goto the IMDB page for a movie; click the poster image; right-click and select 'Copy Link Address' or equivalent  |




### Result
Please wait for around 5 seconds for the prediction output.
The output will be shown as follows:
```
Predicted rating: 
	x  
```
where x is the rating (double) that follows a 5-star rating system [0-5]. 

<hr>

## Minimum Viable Product (MVP)

#### Screenshots
Starting Screen            |  Results Screen
:-------------------------:|:-------------------------:
![image](./mvp_screen.png) |![image](./mvp_result.png)

The best way to see the MVP is to checkout the commit with message "MVP Done": `$ git checkout 50760f0`. You should restart the back-end server. After you are done looking around, you can go back to the most current branch by`$ git checkout master`.


## 1st Iteration

#### Rebekah
* Drop-down menu for Director, Genre, Actor
* "Prettier" UI 
	- Display poster passed
	- Slide show of posters

#### Richard
* Improve model by adding more features (actors)
* Try different model storage to improve prediction speed, if possible

#### Valmik
* Error Handling
* Decouple preprocessing and predictor

#### Screenshot
Starting Screen            |  Results Screen
:-------------------------:|:-------------------------:
![image](./first_iter_screen.png) |![image](./first_iter_result.png)


### Requirements Met
1. REST API
2. Train (and use) a Model
3. More than one service

Our JIRA subscription ended; however, we followed the agile workflow, doing sprints, stand-ups, and retros.

## Future Iterations
* Stabilize Actor parameters
* Faster indexing for Actor options
* Director and Actor name encoding problem (quotes and Unicode)
* Add wait-time
* Star Rating display 




