import requests
import firebase_admin
from firebase_admin import auth, credentials

# NOTE: This script assumes the server is running on localhost:5000.
# It requires a valid firebase token which is hard to generate without a service account or user login.
# Instead, we will just checking if the endpoint is reachable (even if 401 Unauthorized).
# If we get 401, it means network/CORS is fine and the server is responsive.
# If we get ConnectionError, the server is down or unreachable.

try:
    print("Testing connectivity to DELETE /api/qa/history/test_course/clear...")
    response = requests.delete('http://localhost:5000/api/qa/history/test_course/clear')
    print(f"Response Status: {response.status_code}")
    print(f"Response Body: {response.text}")
except Exception as e:
    print(f"Connection Failed: {e}")
