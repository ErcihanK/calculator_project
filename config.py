import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
ENV = os.getenv('ENV')
API_KEY = os.getenv('API_KEY')
print(API_KEY,ENV)

