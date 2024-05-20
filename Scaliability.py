import matplotlib.pyplot as plt

# Sample data: performance under different data loads
data_loads = [100, 500, 1000, 5000, 10000]
performance = [0.95, 0.94, 0.92, 0.90, 0.88]

plt.figure(figsize=(10, 6))
plt.plot(data_loads, performance, marker='o')
plt.xlabel('Data Load (in thousands)')
plt.ylabel('Performance (Accuracy)')
plt.title('Scalability Performance with Distributed Architectures')
plt.grid(True)
plt.show()
