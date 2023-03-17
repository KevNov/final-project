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
cursor.execute("DROP TABLE IF EXISTS PRECIPITATION_lasvegas")

#Creating table as per requirement
sql ='''CREATE TABLE PRECIPITATION_lasvegas(
   date DATE PRIMARY KEY,
   precipitation DECIMAL(5, 2),
   precipitation_normal DECIMAL(5, 2)
)'''

cursor.execute(sql)
print("Table created successfully........")

# Specify the path and filename of the CSV file
csv_path = 'C:\\Users\\kevnov\\Documents\\Final-project DE\\output-data\\dataclean-precipitation-lasvegas.csv'

# Open the CSV file and insert its contents into the database
with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    next(csv_reader)

    # Loop through each row in the CSV file and insert it into the database
    for row in csv_reader:
        date = row[0]
        precipitation = row[1]
        precipitation_normal = row[2]

        # Define the SQL query to insert a row into the database
        sql = """
            INSERT INTO precipitation_lasvegas (date, precipitation, precipitation_normal)
            VALUES (%s, %s, %s)
        """

        # Execute the query
        cursor.execute(sql, (date, precipitation, precipitation_normal))

# Commit the changes to the database
conn.commit()

# Close the database connection
cursor.close()
conn.close()

print('Database insertion success')