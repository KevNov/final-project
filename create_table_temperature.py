import pandas as pd
import psycopg2
import csv
import os
from dotenv import load_dotenv

#connection to postgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=576831")

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Droping similar table if already exists.
cursor.execute("DROP TABLE IF EXISTS temperature_lasvegas")

#Creating table as per requirement
sql ='''CREATE TABLE temperature_lasvegas(
   date DATE PRIMARY KEY,
   min DECIMAL(5, 2),
   max DECIMAL(5, 2),
   normal_min DECIMAL(5, 2),
   normal_max DECIMAL(5, 2)
)'''

cursor.execute(sql)
print("Table created successfully........")

# Specify the path and filename of the CSV file
csv_path = 'C:\\Users\\kevnov\\Documents\\Final-project DE\\output-data\\dataclean-temperature-lasvegas.csv'

# Open the CSV file and insert its contents into the database
with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    next(csv_reader)

    # Loop through each row in the CSV file and insert it into the database
    for row in csv_reader:
        date = row[0]
        min = row[1]
        max = row[2]
        normal_min = row[3]
        normal_max = row[4]

        # Define the SQL query to insert a row into the database
        sql = """
            INSERT INTO temperature_lasvegas (date, min, max, normal_min, normal_max)
            VALUES (%s, %s, %s, %s, %s)
        """

        # Execute the query
        cursor.execute(sql, (date, min, max, normal_min, normal_max))

# Commit the changes to the database
conn.commit()

# Close the database connection
cursor.close()
conn.close()

print('Database insertion success')
