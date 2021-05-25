from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/check_risk', methods=['POST'])
def check_risk():
    # Get the input data
    age = request.form['age']
    glucose = request.form['glucose']
    sbp = request.form['sbp']
    dbp = request.form['dbp']
    cholesterol = request.form['cholesterol']
    cigarettes = request.form['cigarettes']
    bmi = request.form['bmi']
    heart_rate = request.form['heart-rate']
    # Put the data into a dataframe
    data = pd.DataFrame(columns=['age', 'cigarettes', 'cholesterol', 'sbp', 'dbp', 'bmi','heart_rate', 'glucose'], index=[1])
    data.loc[1] = [age, cigarettes, cholesterol, sbp, dbp, bmi, heart_rate, glucose]

    file = 'static/misc/chd_model'
    loaded_model = pickle.load(open(file, 'rb'))
    data_predictions = loaded_model.predict(data)
    print(data_predictions)
    if data_predictions == 1:
        return risk()
    elif data_predictions == 0:
        return no_risk()
    else:
        return error()


@app.route('/risk', methods=['POST'])
def risk():
    return render_template('risk.html')


@app.route('/no-risk', methods=['POST'])
def no_risk():
    return render_template('no-risk.html')


@app.route('/error', methods=['POST'])
def error():
    return render_template('error.html')


@app.route('/statistics', methods=['GET'])
def statistics():
    return render_template('statistics.html')


@app.route('/risk-factors', methods=['GET'])
def risk_factors():
    return render_template('risk-factors.html')


@app.route('/trends', methods=['GET'])
def trends():
    return render_template('trends.html')


@app.route('/accuracy', methods=['GET'])
def accuracy():
    return render_template('accuracy.html')


if __name__ == '__main__':
    app.run(debug=True)
