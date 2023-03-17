import pandas as pd
import numpy as np
import re

# Load the CSV file into a Pandas dataframe
df = pd.read_csv('C:\\Users\\kevnov\\Documents\\Final-project DE\\sample-data\\USW00023169-temperature-degreeF.csv')

# Clean the min column
df['min'] = pd.to_numeric(df['min'], errors='coerce')
df['min'] = df['min'].replace('', None)

# Clean the max column
df['max'] = pd.to_numeric(df['max'], errors='coerce')
df['max'] = df['max'].replace('', None)

# Clean the normal_min column
df['normal_min'] = pd.to_numeric(df['normal_min'], errors='coerce')
df['normal_min'] = df['normal_min'].replace('', None)

# Clean the normal_max column
df['normal_max'] = pd.to_numeric(df['normal_max'], errors='coerce')
df['normal_max'] = df['normal_max'].replace('', None)

# Drop rows with empty values
df.dropna(inplace=True)

# Save the cleaned dataframe to a new CSV file
df.to_csv('output-data/dataclean-temperature-lasvegas.csv', index=False)

print('Data cleansing success')