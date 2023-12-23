import requests
import json

print ()
print("DAP 9.1: Working With APIs")

# Send a GET request to the API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print("Full plaintext response:")
print(response.text)

# Parse the JSON response
data = json.loads(response.text)

print("Full plaintext response:")
print(data)

# Print the title of the post
print(data['title'])

print ("All done!")
print()
