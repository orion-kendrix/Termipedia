import requests
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
        "User-Agent": "SentriWiki/1.0 (academic project)" #Who is making the request
    }
    #Sending the request
    response = requests.get(base_url, params=params, headers=headers, timeout=10)

    #Check and return 
    if response.status_code == 200:
        return response.json()
    else:
        raise ConnectionError(f"Failed: {response.status_code}")

data = fetch_wiki_payload("Linux")
print(data)
