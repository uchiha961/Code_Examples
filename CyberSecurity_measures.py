import matplotlib.pyplot as plt

# Sample data: security breaches before and after zero-trust implementation
before_zero_trust = [30, 28, 25, 27, 26]
after_zero_trust = [7, 6, 5, 6, 4]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

plt.figure(figsize=(10, 6))
plt.plot(months, before_zero_trust, marker='o', linestyle='--', color='red', label='Before Zero-Trust')
plt.plot(months, after_zero_trust, marker='o', color='green', label='After Zero-Trust')
plt.xlabel('Months')
plt.ylabel('Number of Security Breaches')
plt.title('Effectiveness of Zero-Trust Architecture')
plt.legend()
plt.grid(True)
plt.show()
