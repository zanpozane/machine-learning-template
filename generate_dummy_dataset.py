import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Generate 100 random values for jtm, jtr, and gd between 0.0 and 1.0
jtm = np.random.rand(100)
jtr = np.random.rand(100)
gd = np.random.rand(100)

# Calculate hari as a function of jtm, jtr, and gd
# The idea is the larger the jtm, jtr, and gd, the shorter the "hari" prediction
hari = np.round(10 * (1 - (0.3 * jtm + 0.3 * jtr + 0.4 * gd)) + np.random.normal(0, 0.5, 100)).astype(int)

# Ensure hari is at least 1
hari = np.clip(hari, 1, None)

# Round jtm, jtr, and gd to two decimal places
data = pd.DataFrame({
    'jtm': np.round(jtm, 2),
    'jtr': np.round(jtr, 2),
    'gd': np.round(gd, 2),
    'hari': hari
})

# Save the DataFrame to a CSV file
data.to_csv('data/training_data.csv', index=False)

# Display the first few rows of the dataset
print(data.head())
