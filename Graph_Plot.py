import sqlite3
import matplotlib.pyplot as plt

# Define SQLite database file
db_file = 'OperatingReactors.db'

# Connect to database
connection = sqlite3.connect(db_file)
cursor = connection.cursor()

# Define Table Name
table_name = 'Commercial Reactors'

# Fetch data from the database
select_query = f'SELECT "Plant Name", "2020 Capacity Factor (Percent)", "2019 Capacity Factor (Percent)", "2018 Capacity Factor (Percent)", "2017 Capacity Factor (Percent)", "2016 Capacity Factor (Percent)", "2015 Capacity Factor (Percent)", "2014 Capacity Factor (Percent)", "2013 Capacity Factor (Percent)", "2012 Capacity Factor (Percent)", "2011 Capacity Factor (Percent)", "2010 Capacity Factor (Percent)", "2009 Capacity Factor (Percent)", "2008 Capacity Factor (Percent)", "2005 Capacity Factor (Percent)", "2004 Capacity Factor (Percent)", "2003 Capacity Factor (Percent)" FROM "{table_name}"'
cursor.execute(select_query)
data = cursor.fetchall()

# Close connection
connection.close()

# Extract data for plotting
plant_names = [row[0] for row in data]
capacity_factors = [row[1:] for row in data]

# Transpose the data for easier calculations
capacity_factors = list(map(list, zip(*capacity_factors)))

# Replace None values with 0 and convert to numeric
capacity_factors = [[0 if value is None else value for value in year_data] for year_data in capacity_factors]
capacity_factors = [[float(value) for value in year_data] for year_data in capacity_factors]

# Calculate average capacity factor for each year
average_capacity_factors = [sum(year_data) / len(year_data) for year_data in capacity_factors]

# Years for x-axis labels in reversed order
years = ["2003", "2004", "2005", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]

# Reverse the order of average capacity factors
average_capacity_factors.reverse()

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(years, average_capacity_factors)
plt.xlabel('Years')
plt.ylabel('Average Capacity Factor (Percent)')
plt.title('Average Capacity Factor for Different Years (Past to Present)')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the bar graph
plt.show()
