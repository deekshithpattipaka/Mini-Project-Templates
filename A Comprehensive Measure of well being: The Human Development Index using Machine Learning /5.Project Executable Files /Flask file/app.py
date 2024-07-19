from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)

# Load the model
with open('HDI.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/Prediction')
def prediction():
    return render_template('indexnew.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve form data
        life_expectancy = float(request.form['lifeExpectancy'])
        mean_years_of_schooling = float(request.form['meanYearsOfSchooling'])
        gni_per_capita = float(request.form['gniPerCapita'])
        country = request.form['Country']

        # Assuming the model requires these inputs in a specific order
        features = [life_expectancy, mean_years_of_schooling, gni_per_capita,country]

        # Make prediction
        prediction = model.predict([features])[0]
        prediction_text = f'The predicted HDI for {country} is {prediction:.2f}.'

        return render_template('resultsnew.html', prediction_text=prediction_text)
    except Exception as e:
        error_text = str(e)
        return render_template('error.html', error_text=error_text)

if __name__ == '__main__':
    app.run(debug=True)
