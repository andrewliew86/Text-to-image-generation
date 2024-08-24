# Code for deploying model on RunPod: https://blog.dreamrunnerlabs.com/deploying-your-preferred-model-on-runpod-serverless-490981fc5b6f
# Note that I used DockerHub instead of GitHub Container Registry

import base64
import runpod
import io
from PIL import Image
import os
from dotenv import load_dotenv

# Load env file
load_dotenv()

# Add RunPod API key
runpod.api_key = os.environ.get("RUNPOD_API_KEY")

# Change this to your unique RunPod serverless endpoint ID 
endpoint = runpod.Endpoint("wogtprlnbnmng5")

prompt = "Photograph taken in 1883, old west, cowboys"

input = {"input": {"prompt": prompt}}

try:
    run_request = endpoint.run_sync(request_input=input, timeout=120)
    image_bytes = run_request["bytes"]
    bytes = base64.b64decode((image_bytes.encode("utf-8")))
    image = Image.open(io.BytesIO(bytes))
    image.save(f"output.png")
    print("Image generated!")

except TimeoutError:
    print("Job timed out.")