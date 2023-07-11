import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#create flask app
app = Flask(__name__)

#load pickle model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    #converting into numpy array
    features = [np.array(float_features)]
    #make prediction using the model
    prediction = model.predict(features)

    return render_template("index.html", prediction_value = "The portability value is {}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)

