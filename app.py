import pandas as pd

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
