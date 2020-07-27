import pickle
import numpy as np

from app import app
from app.forms import ModelInputForm

from flask.json import jsonify
from flask import request, render_template, redirect, url_for



@app.route('/')
def index():
    return render_template('base.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    with open('models/simple_model_v1.pkl', 'rb') as fp:
        model = pickle.load(fp)

    scores = [
        data['score_3'], 
        data['score_4'], 
        data['score_5'], 
        data['score_6']
        ]

    input_data = np.array(scores).reshape(1, -1)
    predicted = model.predict_proba(input_data)

    return jsonify(id=data["id"], output=predicted[0][1])



