from nacl.signing import SigningKey, VerifyKey
from nacl.exceptions import BadSignatureError
import google.auth
from dotenv import load_dotenv
from google.adk.agents import Agent
import os

load_dotenv()

# Set the credentials environment variable BEFORE calling google.auth.default()
credentials_path = os.getenv("SERVICE_ACCOUNT_KEY_FILE")
if credentials_path:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
else:
    print("Warning: SERVICE_ACCOUNT_KEY_FILE not found in .env file.")

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")


def simulate_sensor_tool(query: str) -> str:
    """Provides realistic sensor data based on the query.

    Args:
        query: A string containing the type of sensor information to retrieve.

    Returns:
        A string with the sensor information.
    """
    import random

    if "temperature" in query.lower():
        temperature = random.uniform(
            15.0, 30.0
        )  # Simulate a realistic temperature range
        return f"The current temperature is {temperature:.1f} degrees Celsius."
    elif "humidity" in query.lower():
        humidity = random.uniform(30.0, 70.0)  # Simulate a realistic humidity range
        return f"The current humidity level is {humidity:.1f}%."
    else:
        return f"Sorry, I don't have information for query: {query}."


def digital_signature_tool(message: str) -> str:
    """Signs a message using a digital signature.

    Args:
        message: A string containing the message to be signed.

    Returns:
        A string with the digital signature.
    """
    signing_key = SigningKey.generate()
    signed_message = signing_key.sign(message.encode())
    signature_hex = signed_message.signature.hex()
    return f"Signed message: {signed_message.message.decode()} with signature: {signature_hex}"


root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    instruction="You are CipherSpace, a helpful AI assistant that simulates sensor data like Temperatures, and CO Level, and then creates a signed sensor payload.",
    tools=[simulate_sensor_tool, digital_signature_tool],
)
