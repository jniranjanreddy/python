import requests

# Sending a GET request to a URL
response = requests.get('https://google.com')

# Checking the status code
if response.status_code == 200:
    print("Request was successful!")
    # print("Response body:", response.text)
else:
    print("Error:", response.status_code)