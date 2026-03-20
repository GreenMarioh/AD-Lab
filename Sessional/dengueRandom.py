import pandas as pd
import numpy as np

# Number of data points
num_samples = 100

# Set a random seed for reproducibility
np.random.seed(42)

# Generate random data for each column
fever_temperature = np.random.uniform(37.0, 41.0, num_samples) # Celsius
platelet_count = np.random.randint(50000, 450000, num_samples) # per microliter
white_blood_cell_count = np.random.randint(3000, 12000, num_samples) # per microliter

joint_pain = np.random.randint(0, 2, num_samples)
headache = np.random.randint(0, 2, num_samples)
vomiting = np.random.randint(0, 2, num_samples)
rash = np.random.randint(0, 2, num_samples)
fatigue = np.random.randint(0, 2, num_samples)
dengue = np.random.randint(0, 2, num_samples)
data = {
    'fever_temperature': fever_temperature,
    'platelet_count': platelet_count,
    'white_blood_cell_count': white_blood_cell_count,
    'joint_pain': joint_pain,
    'headache': headache,
    'vomiting': vomiting,
    'rash': rash,
    'fatigue': fatigue,
    'dengue': dengue
}

# Create a pandas DataFrame
df_dengue = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df_dengue.to_csv('dengue_data.csv', index=False)

print("Generated 'dengue_data.csv' with 100 rows.")
print(df_dengue.head())
