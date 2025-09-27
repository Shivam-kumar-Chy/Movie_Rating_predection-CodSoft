# Movie Rating Prediction using Linear Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample dataset (you can replace this with a real dataset like MovieLens)
data = {
    'budget': [100, 20, 150, 10, 200, 50, 120, 80, 300, 15],   # in millions
    'duration': [120, 90, 150, 85, 180, 100, 140, 110, 200, 95], # in minutes
    'votes': [5000, 800, 10000, 300, 15000, 2000, 7000, 4500, 20000, 400], # number of votes
    'rating': [7.8, 6.2, 8.5, 5.4, 9.0, 6.9, 8.0, 7.2, 9.3, 5.8] # IMDb-like ratings
}

# Create a DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[['budget', 'duration', 'votes']]
y = df['rating']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Predict for a new movie
new_movie = [[180, 150, 12000]]  # budget=180M, duration=150min, votes=12000
predicted_rating = model.predict(new_movie)
print("Predicted Rating for new movie:", predicted_rating[0])
