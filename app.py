from flask import Flask, render_template, request, url_for
import pickle

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__) 

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        age = request.form['age']
        location = request.form['location']
        monthly_bill = request.form['monthly_bill']

        loc_map = {'Chicago': 0, 'Houston': 1, 'Los Angeles': 2, 'Miami': 3, 'New York': 4}
        location = loc_map[location]

        sample = np.array([age, location, monthly_bill])
        result = model.predict(sample.reshape(1, -1))[0]

        result = {'prediction' : result}
        return render_template('home.html', result=result)
    else:
        return render_template('home.html')
    
if __name__ == '__main__':
    app.run(debug=True)