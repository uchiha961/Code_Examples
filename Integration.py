import matplotlib.pyplot as plt

# Sample data: interoperability scores before and after middleware implementation
before_middleware = [60, 62, 61, 63, 64]
after_middleware = [85, 87, 86, 88, 90]
devices = ['Device1', 'Device2', 'Device3', 'Device4', 'Device5']

plt.figure(figsize=(10, 6))
plt.bar(devices, before_middleware, color='blue', alpha=0.6, label='Before Middleware')
plt.bar(devices, after_middleware, color='green', alpha=0.6, label='After Middleware')
plt.xlabel('IoT Devices')
plt.ylabel('Interoperability Score')
plt.title('Interoperability Improvement with Middleware Implementation')
plt.legend()
plt.show()
