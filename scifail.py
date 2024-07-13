import random
import math

# Generate sample data
random.seed(0)
X = [random.uniform(0, 1) for _ in range(100)]
y = [2 + 3 * x + random.gauss(0, 0.1) for x in X]

# Split the data into training and testing sets
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Calculate mean of X and y
mean_X = sum(X_train) / len(X_train)
mean_y = sum(y_train) / len(y_train)

# Calculate coefficients
numerator = sum((x - mean_X) * (y - mean_y) for x, y in zip(X_train, y_train))
denominator = sum((x - mean_X) ** 2 for x in X_train)
slope = numerator / denominator
intercept = mean_y - slope * mean_X

# Make predictions on the test set
y_pred = [slope * x + intercept for x in X_test]

# Calculate Mean Squared Error 
mse = sum((pred - actual) ** 2 for pred, actual in zip(y_pred, y_test)) / len(y_test)

# Calculate R-squared
ss_tot = sum((y - mean_y) ** 2 for y in y_test)
ss_res = sum((pred - actual) ** 2 for pred, actual in zip(y_pred, y_test))
r2 = 1 - (ss_res / ss_tot)

print("Model Performance:")
print(f"Mean Squared Error: {mse:.4f}")
print(f"R-squared Score: {r2:.4f}")

print("\nModel Coefficients:")
print(f"Intercept: {intercept:.4f}")
print(f"Slope: {slope:.4f}")

# Make a sample prediction
sample_x = 0.5
prediction = slope * sample_x + intercept
print(f"\nSample Prediction:")
print(f"For X = 0.5, Predicted Y: {prediction:.4f}")
