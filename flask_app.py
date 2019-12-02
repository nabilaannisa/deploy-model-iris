# Import libraries
import numpy as np
from flask import Flask, request, jsonify
#from sklearn.externals import joblib
import pickle
import pandas as pd


# load model
model = pickle.load(open('/home/nabilaannisa/mysite/iris_model.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/api', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': str(result[0])}

    # return data
    return jsonify(output)

# if __name__ == '__main__':
#     app.run(port = 5000, debug=True)