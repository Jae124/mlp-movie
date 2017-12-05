

class ModelHandler(object):
    def __init__(self):
        self.model = self.get_model()

    def get_model(self):
        # training_data = get_data(self.N)
        # X = training_data[self.x_columns]
        # y = training_data[self.y_column]

        ################ basically need to insert our model here (instead of LR)
        self.model = LinearRegression().fit(X, y) 
        print(self.model.coef_)
        return self.model