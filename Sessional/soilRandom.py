import pandas as pd
import numpy as np

# Number of data points
num_samples = 1000

# Generate random data for each column
np.random.seed(42) # for reproducibility
nitrogen = np.random.randint(0, 200, num_samples)  # mg/kg (ppm)
phosphorus = np.random.randint(0, 150, num_samples) # mg/kg (ppm)
potassium = np.random.randint(0, 300, num_samples)  # mg/kg (ppm)
ph = np.random.uniform(5.0, 8.5, num_samples)     # pH scale
moisture = np.random.uniform(10.0, 60.0, num_samples) # percentage
temperature = np.random.uniform(5.0, 35.0, num_samples) # Celsius

# Create a dictionary from the data
data = {
    'nitrogen': nitrogen,
    'phosphorus': phosphorus,
    'potassium': potassium,
    'ph': ph,
    'moisture': moisture,
    'temperature': temperature
}
df_soil = pd.DataFrame(data)

df_soil.to_csv('soil_data.csv', index=False)

print("Generated 'soil_data.csv' with 1000 rows.")
print(df_soil.head())
