import requests
import json

# OAuth 2.0 endpoints
AUTHORIZATION_URL = "https://appcenter.intuit.com/connect/oauth2"
TOKEN_URL = "https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer"

# Client credentials
CLIENT_ID = "ABqryhQqidR5kznR69hZb1Uq8cavUlwiXzh9kKUE4zQVkNVXWF"
CLIENT_SECRET = "ET889qeyic90PNa1QW2J6UmB6Zchahf93erSgrcX"
REDIRECT_URI = "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl"

# OAuth 2.0 flow parameters
SCOPE = "com.intuit.quickbooks.accounting"

# Step 1: Get authorization code
authorization_url = f"{AUTHORIZATION_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={SCOPE}"

print(f"Open the following URL in your browser: {authorization_url}")
print("Enter the authorization code:")
authorization_code = input()

# Step 2: Get access token
headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
}

data = {
    "code": authorization_code,
    "redirect_uri": REDIRECT_URI,
    "grant_type": "authorization_code",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
}

response = requests.post(TOKEN_URL, headers=headers, data=data)

# Step 3: Handle response
if response.status_code == 200:
    # Response is successful
    response_json = response.json()
    access_token = response_json["access_token"]
    refresh_token = response_json["refresh_token"]
    realm_id = response_json["realmId"]

    # Use access token to make API calls
    print(f"Access token: {access_token}")
    print(f"Refresh token: {refresh_token}")
    print(f"Realm ID: {realm_id}")
else:
    # Response is not successful
    print(f"Error: {response.text}")
