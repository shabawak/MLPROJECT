from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import numpy as np
import pickle

#create flask app
app = Flask(__name__)


#connecting to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRETE_KEY'] = 'thisisasecretekey'
#initializing the database
db = SQLAlchemy(app)

#Creating the database table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Add the application context to perform database operations
with app.app_context():
    # Perform database operations within the application context
    db.create_all()
 

#load pickle model
model = pickle.load(open("model.pkl", "rb"))

#Route to homepage
@app.route("/")
def home():
    return render_template("home.html")

#Route to the login page
@app.route('/login')
def login():
    return render_template("login.html")

#Route to the register page
@app.route('/register')
def register():
    return render_template("register.html")

#Route to the ML page
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

