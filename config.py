import os
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# Access environment variables
ENV = os.getenv('ENV')
API_KEY = os.getenv('API_KEY')

# Log the environment variables (instead of printing)
logging.info(f"Running in {ENV} environment")
logging.info(f"API Key: {API_KEY}")
