import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from fileinput import filename
import pickle
from openpyxl import load_workbook

#create flask app | Flask constructor
app = Flask(__name__)

#load pickle model
#model = pickle.load(open("model.pkl", "rb"))

#Root endpoint
@app.route("/")
def Home():
    return render_template("index_upload.html")




@app.route("/predict", methods=["POST"])
def predict():
    #Read the File using Flask request
    file = request.files['file']
    #save file in local directory
    file.save(file.filename)

    #pass the data as a Pandas DataFrame type
    df = pd.read_csv(file)

    # Convert the DataFrame to HTML table
    table = df.to_html(classes='data')
    
    # Render the template with the table
    return render_template('index_upload', table=table)

if __name__ == "__main__":
    app.run(debug=True)

