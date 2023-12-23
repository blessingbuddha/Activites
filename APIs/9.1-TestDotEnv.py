from dotenv import load_dotenv
import os

load_dotenv()

print("Testing environment!")
print("API Key (don't look):")
print(os.getenv('MY_API_KEY'))