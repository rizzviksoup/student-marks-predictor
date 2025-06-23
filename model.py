import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Step 1: Load the data
data = pd.read_csv('student_scores.csv')
X = data[['Hours']]
y = data['Marks']

# Step 2: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 3: Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'model.pkl'")
