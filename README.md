# 🧠 Student Marks Predictor

This is a simple machine learning web app built with **Flask** and **Python** that predicts student marks based on the number of hours they studied.

---

## 🚀 How it works

The model is trained using **Linear Regression** on sample data of hours studied vs scores.

- `model.py` → trains and saves the model as `model.pkl`
- `app.py` → runs a Flask server to take user input and return predictions
- `templates/index.html` → basic front-end form

---

## 📁 Files

- `student_scores.csv` — the dataset used
- `model.py` — ML training script
- `model.pkl` — saved regression model
- `app.py` — Flask backend
- `templates/index.html` — HTML frontend

---

## 🧪 How to Run It

1. Install the requirements:

```bash
pip install flask pandas scikit-learn
python model.py
python app.py
http://127.0.0.1:5000
