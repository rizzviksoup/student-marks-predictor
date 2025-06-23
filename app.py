from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        hours = float(request.form['hours'])
        prediction = model.predict(np.array([[hours]]))
        predicted_marks = round(prediction[0], 2)
        return render_template('index.html', prediction=predicted_marks, hours=hours)
    except:
        return render_template('index.html', prediction="Invalid input", hours="")

if __name__ == '__main__':
    app.run(debug=True)
