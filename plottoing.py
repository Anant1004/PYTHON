import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV file into a pandas DataFrame
df = pd.read_csv('data.csv')

# Assuming your CSV file has columns named 'x' and 'y'
x = df.iloc[0,1:]
y = df.iloc[1,1:]

# Plotting the data
plt.bar(x, y)  # You can customize marker and linestyle as per your requirement
plt.title('Plot of Data from CSV')
plt.show()
