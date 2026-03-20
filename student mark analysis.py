import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Name": ["Arun", "Bala", "Cathy", "Divya", "Elan"],
    "Maths": [85, 78, 92, 88, 76],
    "Science": [90, 82, 88, 91, 79],
    "English": [75, 80, 85, 87, 72]
}
# Convert to DataFrame
df = pd.DataFrame(data)
# Display dataset
print("Student Data:\n", df)
# Calculate average marks
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)
print("\nWith Average:\n", df)
# Find topper
topper = df.loc[df["Average"].idxmax()]
print("\nTopper:\n", topper)
# Basic statistics
print("\nStatistics:\n", df.describe())
# Plot average marks
plt.bar(df["Name"], df["Average"])
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()
