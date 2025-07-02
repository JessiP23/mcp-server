import requests
import json
import time
import subprocess
import sys
from pathlib import Path

def test_server():
    """Simple test to verify the MCP server is running"""
    server_process = subprocess.Popen([sys.executable, "src/server.py"])

    try:
        # Wait for the server to start
        time.sleep(3)

        # Test the server using the MCP client
        # in prod use MCP client sdk
        # for dev simulate a client http request

        base_url = "http://localhost:8000"

        response = requests.get(f"{base_url}/resources/user_profiles")
        assert response.status_code == 200

        data = response.json()

        print("Resource response:", json.dumps(data, indent=2))

        tool_data = {
            "name": "Test User",
            "role": "Tester",
            "department": "QA"
        }

        response = requests.post(
            f"{base_url}/tools/create_user_profile",
            json=tool_data
        )

        assert response.status_code == 200
        data = response.json()
        print("Tool response:", json.dumps(data, indent=2))

        print("All tests passed!")

    finally:
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    test_server()
    