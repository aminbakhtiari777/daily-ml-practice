import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Simple dataset
x = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)
y = np.array([25, 45, 65, 85, 105])

# Train model
model = LinearRegression()
model.fit(x, y)

# Predict
x_new = np.array([[60]])
prediction = model.predict(x_new)

print("Prediction for x = 60:", prediction[0])

# Plot
plt.scatter(x, y)
plt.plot(x, model.predict(x))
plt.title("Simple Linear Regression Practice")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
