import pandas as pd

# Assume we have some JSON data
data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "Chicago"},
    {"name": "Mike", "age": 35, "city": "San Francisco"}
]

# Convert the JSON data to a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)