from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import sys
import os
os.chdir("..")
sys.path.insert(0,os.path.abspath(os.curdir))
from predict_rating import predict_rating
from preprocess import preprocess

from model import ModelHandler

class WelcomeHandler(RequestHandler):
    def get(self):
        self.write("Welcome to our project page")

class PredictHandler(RequestHandler):
    def set_default_headers(self):
        super(PredictHandler, self).set_default_headers()
        self.set_header('Access-Control-Allow-Origin', 'http://localhost:3000')
        self.set_header('Access-Control-Allow-Credentials', 'true')
    def get(self):
        
        runtime = self.get_argument('runtime')
        
        director = str(self.get_argument('director'))
        genres = self.get_argument('genres')
        actors = self.get_argument('actors')

        g = genres.split(",")   
        a = actors.split(",")

        ######### process in the modeling script?
        poster = str(self.get_argument('image_url'))

        ########### switch 'model.predict()' w/method call name equivalent to our model
        x,img = preprocess(director, g, runtime, poster, a)

        if x is None:
            self.write('{}'.format(img))
        else:
            rating = predict_rating(x,img)
            self.write('{}'.format(rating))

class ModelApplication(Application):
    def __init__(self, handler_mapping):
        super(ModelApplication, self).__init__(handler_mapping)



if __name__ == "__main__":
    handler_mapping = [
                       (r'/welcome', WelcomeHandler),
                       (r'/predict$', PredictHandler)                       
                      ]
    application = ModelApplication(handler_mapping)
    # application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()