import requests

try:
    # Send a GET request to the API
    # response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response = requests.get('https://httpbin.org/status/404')
    
    # Check the response status code
    if response.status_code == 200:
        # Request was successful, proceed with parsing the response
        data = response.json()
        # Process the data further
        print(data)
    else:
        # Request failed, handle the error
        print(f"Request failed with status code {response.status_code}")
except requests.exceptions.RequestException as e:
    # Handle connection errors
    print("Connection error occurred:", e)