import pandas as pd

# Sample data
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'date': ["2021-09-01", "2021-09-02", "2021-09-03", "2021-09-04", "2021-09-05",
             "2022-09-01", "2022-09-02", "2022-09-03", "2022-09-04", "2022-09-05"],
    'value': [5, 10, 15, 20, 25, 30, 35, 40, 5, 10]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('input_data.csv', index=False)

print("Sample input_data.csv created!")

# Load the data from CSV file
df = pd.read_csv('input_data.csv')

# Filter records where value is less than 10
df = df[df['value'] >= 10]

# Extract year from the date column and create a new column 'year'
df['year'] = pd.to_datetime(df['date']).dt.year

# Calculate average value and create a new column 'average_value'
average_value = df['value'].mean()
df['average_value'] = average_value

# Save the transformed data to a new CSV file
df.to_csv('output_data.csv', index=False)

print("Transformed data saved to output_data.csv")

yearly_total = df.groupby(df['date'].astype('datetime64').dt.year)['value'].sum()
yearly_total.to_csv('yearly_total.csv', index=False)
print(yearly_total)
