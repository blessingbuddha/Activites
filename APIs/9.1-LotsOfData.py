import sys
import requests
import json

print ()
print("DAP 9.1: Working With APIs")

# Send a GET request to the API
response = requests.get('https://jsonplaceholder.typicode.com/comments')

plaintext = response.text

print("What's the first comment?")
print(plaintext[0])

print("How big is the plaintext JSON infortmation?")
print(sys.getsizeof(plaintext))

decoded_object = json.loads(plaintext)

print("How big is the decoded Python object?")
print(sys.getsizeof(decoded_object))

print("What is the very first comment?")
print(decoded_object[0])

print("What is the very first comment's email?")
print(decoded_object[0]["email"])