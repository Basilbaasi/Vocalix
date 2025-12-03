import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get API key and base URL
API_KEY = os.getenv("NVIDIA_API_KEY")
BASE_URL = os.getenv("NVIDIA_API_BASE_URL", "https://integrate.api.nvidia.com/v1")

if not API_KEY:
    raise ValueError("NVIDIA_API_KEY is not set in .env file!")
