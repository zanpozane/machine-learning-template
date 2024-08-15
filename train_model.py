import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the data from CSV
data = pd.read_csv('data/training_data.csv')

# Separate the input features (jtm, jtr, gd) and the output (hari)
X = data[['progres_pekerjaan']]
y = data['hari']

# Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Print model coefficients
print("Model coefficients:", model.coef_)

# Make predictions
y_pred = model.predict(X)

# Calculate and print the accuracy metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Save the trained model
joblib.dump(model, 'models/model.pkl')
