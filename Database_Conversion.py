import pandas as pd
import sqlite3

# Read Excel File w/ Pandas
excel_file = 'reactors-operating.xlsx'
df = pd.read_excel(excel_file)

# Define SQLite database file
db_file = 'OperatingReactors.db'

# Connect to database
connection = sqlite3.connect(db_file)
cursor = connection.cursor()

# Define Table Name
table_name = 'Commercial Reactors'

for index, row in df.iterrows():
    plant_name = row['Plant Name, Unit Number']
    docket = row['Docket Number']
    license_number = row['License Number']
    location = row['Location']  # Add these lines
    licensee = row['Licensee']
    reactor_type = row['Reactor and Containment Type']
    architect_engineer = row['Architect-Engineer']
    capacity_factor_2020 = row['2020 Capacity Factor (Percent)']
    capacity_factor_2019 = row['2019 Capacity Factor (Percent)']
    capacity_factor_2018 = row['2018 Capacity Factor (Percent)']
    capacity_factor_2017 = row['2017 Capacity Factor (Percent)']
    capacity_factor_2016 = row['2016 Capacity Factor (Percent)']
    capacity_factor_2015 = row['2015 Capacity Factor (Percent)']
    capacity_factor_2014 = row['2014 Capacity Factor (Percent)']
    capacity_factor_2013 = row['2013 Capacity Factor (Percent)']
    capacity_factor_2012 = row['2012 Capacity Factor (Percent)']
    capacity_factor_2011 = row['2011 Capacity Factor (Percent)']
    capacity_factor_2010 = row['2010 Capacity Factor (Percent)']
    capacity_factor_2009 = row['2009 Capacity Factor (Percent)']
    capacity_factor_2008 = row['2008 Capacity Factor (Percent)']
    capacity_factor_2005 = row['2005 Capacity Factor (Percent)']
    capacity_factor_2004 = row['2004 Capacity Factor (Percent)']
    capacity_factor_2003 = row['2003 Capacity Factor (Percent)']



    # Check if the record already exists in the table
    select_query = f'SELECT * FROM "{table_name}" WHERE "Plant Name" = ? AND "Docket Number" = ?'
    cursor.execute(select_query, (plant_name, docket))
    existing_record = cursor.fetchone()

    # Insert the record only if it doesn't already exist
    if not existing_record:
        insert_query = f'INSERT INTO "{table_name}" ("Plant Name", "Docket Number", "License Number", "Location", "Licensee", "Reactor and Containment Type", "Architect-Engineer", "2020 Capacity Factor (Percent)",  "2019 Capacity Factor (Percent)", "2018 Capacity Factor (Percent)", "2017 Capacity Factor (Percent)",  "2016 Capacity Factor (Percent)", "2015 Capacity Factor (Percent)", "2014 Capacity Factor (Percent)",  "2013 Capacity Factor (Percent)", "2012 Capacity Factor (Percent)", "2011 Capacity Factor (Percent)",  "2010 Capacity Factor (Percent)", "2009 Capacity Factor (Percent)", "2008 Capacity Factor (Percent)",   "2005 Capacity Factor (Percent)", "2004 Capacity Factor (Percent)", "2003 Capacity Factor (Percent)")   VALUES (?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?)'  # Update the query
      
        cursor.execute(insert_query, (plant_name, docket, license_number, location, licensee, reactor_type, 
        architect_engineer, capacity_factor_2020, capacity_factor_2019, capacity_factor_2018, capacity_factor_2017, 
        capacity_factor_2016, capacity_factor_2015, capacity_factor_2014, capacity_factor_2013, capacity_factor_2012,
       capacity_factor_2011,capacity_factor_2010,capacity_factor_2009,capacity_factor_2008, capacity_factor_2005, 
       capacity_factor_2004, capacity_factor_2003 ))  # Update the parameters
        connection.commit()

# Close connection
connection.close()
