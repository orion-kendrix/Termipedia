import requests
import json
def fetch_wiki_payload(query_string):
    #Request creation
    base_url = "https://en.wikipedia.org/w/api.php" #Request address
    params = {                      #Request data
    "action" : "parse",
    "page" : query_string,
    "format" : "json",
    "prop" : "text",
    "redirects" : "true"
    }
    #What the request looks like to the client
    headers = {
        "User-Agent": "Termipedia/1.0 (academic project)" #Who is making the request
    }
    #Sending the request
    response = requests.get(base_url, params=params, headers=headers, timeout=10)

    #Check and return 
    if response.status_code == 200:
        return response.json()
    else:
        raise ConnectionError(f"Failed: {response.status_code}")

print("The termipedia has been intiated...")
while True:
    data_req = input("Welcome User!, what article do you want from wiki? ")

    if data_req == "":
        print("Try again!")
    else:
        break

data = fetch_wiki_payload(data_req)
print(json.dumps(data, indent=2))
