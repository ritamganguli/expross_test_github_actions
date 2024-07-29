import requests
import base64

# Replace these values with your actual credentials and file paths
username = "shubhamr"
access_key = "dl8Y8as59i1YyGZZUeLF897aCFvIDmaKkUU1e6RgBmlgMLIIhh"
app_file_path = "proverbial_android.apk"
test_suite_file_path = "proverbial_android_expressotest.apk"

# Encode credentials for the Authorization header
basic_auth_token = base64.b64encode(f"{username}:{access_key}".encode()).decode()

# Upload the application and get the app_id
app_upload_url = 'https://manual-api.lambdatest.com/app/uploadFramework'
app_upload_response = requests.post(
    app_upload_url,
    auth=(username, access_key),
    files={'appFile': open(app_file_path, 'rb')},
    data={'type': 'espresso-android'}
)

app_upload_data = app_upload_response.json()
application_id = app_upload_data.get('app_id')
print(f"Application ID: {application_id}")

# Upload the test suite and get the test_suite_id
test_suite_upload_response = requests.post(
    app_upload_url,
    auth=(username, access_key),
    files={'appFile': open(test_suite_file_path, 'rb')},
    data={'type': 'espresso-android'}
)

test_suite_data = test_suite_upload_response.json()
test_suite_id = test_suite_data.get('app_id')
print(f"Test Suite ID: {test_suite_id}")

# Start the build with the uploaded app and test suite
build_url = 'https://mobile-api.lambdatest.com/framework/v1/espresso/build'
build_headers = {
    'Authorization': f'Basic {basic_auth_token}',
    'Content-Type': 'application/json'
}

build_payload = {
    "app": application_id,
    "testSuite": test_suite_id,
    "device": ["Galaxy S21 5G-12"],
    "queueTimeout": 10800,
    "IdleTimeout": 150,
    "deviceLog": True,
    "network": False,
    "build": "Proverbial-Espresso"
}

build_response = requests.post(
    build_url,
    headers=build_headers,
    json=build_payload
)

print(f"Build Response: {build_response.json()}")
