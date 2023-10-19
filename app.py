from flask import Flask, render_template, request, url_for
import pickle
import numpy as np

chicago_model = pickle.load(open('Chicago_model.pkl', 'rb'))
houston_model = pickle.load(open('Houston_model.pkl', 'rb'))
losangeles_model = pickle.load(open('Los Angeles_model.pkl', 'rb'))
miami_model = pickle.load(open('Miami_model.pkl', 'rb'))
newyork_model = pickle.load(open('New York_model.pkl', 'rb'))

models_dict = {0: chicago_model, 1: houston_model, 2: losangeles_model, 3: miami_model, 4: newyork_model}

app = Flask(__name__) 

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        location = request.form['location']
        subscription_length_months = request.form['subscription_length_months']
        monthly_bill = request.form['monthly_bill']
        total_usage_gb = request.form['total_usage_gb']

        gender = 0 if gender == 'Male' else 1

        loc_map = {'Chicago': 0, 'Houston': 1, 'Los Angeles': 2, 'Miami': 3, 'New York': 4}
        location = loc_map[location]

        sample = np.array([age, gender, subscription_length_months, monthly_bill, total_usage_gb])
        result = models_dict[location].predict(sample)

        result = {'prediction' : result}
        return render_template('home.html', result=result)
    else:
        return render_template('home.html')
    
if __name__ == '__main__':
    app.run(debug=True)