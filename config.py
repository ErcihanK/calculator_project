import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
ENV = os.getenv('ENV')
API_KEY = os.getenv('API_KEY')

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

logger.info(f"Running in {ENV} environment")
logger.info(f"API Key: {API_KEY}")
