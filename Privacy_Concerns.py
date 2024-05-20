import matplotlib.pyplot as plt

# Sample data: utility of data with different levels of noise added for differential privacy
noise_levels = [0.1, 0.2, 0.3, 0.4, 0.5]
data_utility = [0.95, 0.93, 0.90, 0.87, 0.85]

plt.figure(figsize=(10, 6))
plt.plot(noise_levels, data_utility, marker='o')
plt.xlabel('Noise Level')
plt.ylabel('Data Utility (Accuracy)')
plt.title('Impact of Differential Privacy on Data Utility')
plt.grid(True)
plt.show()
