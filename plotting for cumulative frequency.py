
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Given data
runs = [45, 34, 50, 75, 22, 56, 63, 70, 49, 33,
        0, 8, 14, 39, 86, 92, 88, 70, 56, 50,
        57, 45, 42, 12, 39]

# Sort the data
runs.sort()

# Define class intervals
min_score = min(runs)
max_score = max(runs)
interval_size = 10
classes = list(range(0, ((max_score // 10) + 2) * 10, interval_size))

# Create frequency distribution
frequency = []
for i in range(len(classes)-1):
    count = sum(classes[i] <= run < classes[i+1] for run in runs)
    frequency.append(count)

#Compute cumulative frequency
cumulative_frequency = np.cumsum(frequency)

# DataFrame for display
df = pd.DataFrame({
    'Class Interval': [f"Less than {classes[i+1]}" for i in range(len(frequency))],
    'Cumulative Frequency': cumulative_frequency
})
print(df)

# cumulative frequency curve
plt.figure(figsize=(10,6))
plt.plot(classes[1:], cumulative_frequency, marker='o', linestyle='-', color='blue')
plt.title('Less Than Type Cumulative Frequency Curve')
plt.xlabel('Runs (Less than)')
plt.ylabel('Cumulative Frequency')
plt.grid(True)
plt.show()