from flask import jsonify, Flask, request
from flask_restful import Resource, Api, reqparse
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)
api = Api(app)

class RawFeats:
    def __init__(self, feats):
        self.feats = feats
    
    def fit(self,X,y=None):
        pass

    def transform(self,X,y=None):
        return X[self.feats]

    def fit_transform(self,X,y=None):
        self.fit(X)
        return self.transform(X)


with open('model.pkl','rb') as f:
    model = pickle.load(f)


class Predict(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        prediction = list(model.predict(df))
        return jsonify({'prediction': prediction})

api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
