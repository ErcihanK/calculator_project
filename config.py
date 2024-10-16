import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
ENV = os.getenv('ENV')
API_KEY = os.getenv('API_KEY')

# Set up logging configuration
# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handlers: one for the console and one for a file
console_handler = logging.StreamHandler()  # Console handler
file_handler = logging.FileHandler('logs/config.log')  # File handler

# Set the format for the logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Log information
logger.info(f"Running in {ENV} environment")
logger.info(f"API Key: {API_KEY}")

# Ensure logs are output to both console and logs/config.log file
