import requests
import json
import pyperclip

# Define the API endpoint URL
api_url = "https://wsmanybuild.azurewebsites.net/Swagger/index.html"  # Replace with your actual API endpoint URL

# Define the payload (data) to send in the request
payload = {
    "userName": "cmoretti+creator9@method-automation.com",
    "password": "Bluestone1!"
}

try:
    # Make a POST request to the API endpoint with the payload
    response = requests.post(api_url, json=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON response data
        response_data = response.json()

        # Print the entire response JSON
        print("Response JSON:", json.dumps(response_data, indent=2))

        # Extract the access token from the response
        access_token = response_data.get("accessToken")
        if access_token:
            print("Access token found:", access_token)

            # Copy the access token to the clipboard (optional)
            pyperclip.copy(access_token)
            print("Access token copied to clipboard:", access_token)
        else:
            print("Access token not found in the response")

    else:
        print("Failed to retrieve access token. Status code:", response.status_code)

except requests.RequestException as e:
    print("Error making HTTP request:", e)
