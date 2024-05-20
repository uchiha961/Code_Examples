import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Generate synthetic sensor data
np.random.seed(42)
num_samples = 1000
sensor_data = np.random.rand(num_samples, 3) * 100  # Random data for 3 sensors
time_to_failure = sensor_data[:, 0] * 0.5 + sensor_data[:, 1] * 0.3 + sensor_data[:, 2] * 0.2 + np.random.normal(0, 5, num_samples)

data = pd.DataFrame(sensor_data, columns=['sensor1', 'sensor2', 'sensor3'])
data['time_to_failure'] = time_to_failure

# Split data into training and testing sets
train_size = int(0.8 * len(data))
X_train, X_test = data[['sensor1', 'sensor2', 'sensor3']][:train_size], data[['sensor1', 'sensor2', 'sensor3']][train_size:]
y_train, y_test = data['time_to_failure'][:train_size], data['time_to_failure'][train_size:]

# Train Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Plot actual vs predicted
plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.xlabel('Sample')
plt.ylabel('Time to Failure')
plt.legend()
plt.title('Predictive Maintenance: Actual vs Predicted')
plt.show()
