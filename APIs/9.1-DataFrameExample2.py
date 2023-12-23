import requests
import json
import pandas as pd

# Send a GET request to the API
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Parse the JSON response
data = json.loads(response.text)

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv('data.csv', index=False)

print("Data exported successfully!")