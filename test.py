import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Emma', 'Emma', 'John', 'Alex', 'Sophia', 'James'],
    'Age': [25, 30, 22, 28, 35, 30, 25]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Displaying the initial DataFrame
print("Initial DataFrame:")
print(df)

# Getting distinct values in the 'Name' column
distinct_values = df.groupby('Name')['Age'].first().reset_index()

# Displaying the distinct values
print("\nUnique Names:")
print(distinct_values[distinct_values['Age'] == 25])



