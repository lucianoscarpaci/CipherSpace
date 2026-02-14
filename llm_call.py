import warnings
import vertexai
from vertexai.generative_models import GenerativeModel
from google.oauth2 import service_account
import os
from dotenv import load_dotenv

warnings.filterwarnings(
    "ignore", category=UserWarning, module="vertexai.generative_models"
)
load_dotenv()

SERVICE_ACCOUNT_KEY_FILE = os.getenv("SERVICE_ACCOUNT_KEY_FILE")
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
MODEL_ID = os.getenv("MODEL_ID")

credentials_path = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_KEY_FILE,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials_path)
model = GenerativeModel(MODEL_ID)
response = model.generate_content("Write a short poem about the sea.")
if response.text:
    print("Generated Content:")
    print(response.text)
    print()
