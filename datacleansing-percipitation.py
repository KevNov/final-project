import pandas as pd
import numpy as np
import re

# Load the CSV file into a Pandas dataframe
df = pd.read_csv('C:\\Users\\kevnov\\Documents\\Final-project DE\\sample-data\\USW00023169-LAS_VEGAS_MCCARRAN_INTL_AP-precipitation-inch.csv')

# Clean the precipitation column
df['precipitation'] = pd.to_numeric(df['precipitation'], errors='coerce')
df['precipitation'] = df['precipitation'].replace(0.0, None)
df['precipitation'] = df['precipitation'].replace('', None)

# Drop rows with empty values
df.dropna(inplace=True)

# Save the cleaned dataframe to a new CSV file
df.to_csv('output-data/dataclean-precipitation-lasvegas.csv', index=False)

print('Data cleansing success')
