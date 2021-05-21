from flask import Flask, render_template, request
import pandas as pd
import pickle
from sklearn.svm import SVC

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/check_risk', methods=['POST'])
def check_risk():
    age = request.form['age']
    glucose = request.form['glucose']
    sbp = request.form['sbp']
    dbp = request.form['dbp']
    cholesterol = request.form['cholesterol']
    cigarettes = request.form['cigarettes']
    bmi = request.form['bmi']
    heart_rate = request.form['heart-rate']
    data = pd.DataFrame(columns=['age', 'glucose', 'sys_blood_pressure', 'dia_blood_pressure', 'cholesterol', 'cigarettes', 'bmi', 'heart_rate'], index=[1])
    data.loc[1] = [age, glucose, sbp, dbp, cholesterol, cigarettes, bmi, heart_rate]
    file = 'chd_model'
    loaded_model = pickle.load(open(file, 'rb'))
    data_predictions = loaded_model.predict(data)
    return render_template("check_risk.html")


if __name__ == '__main__':
    app.run(debug=True)
