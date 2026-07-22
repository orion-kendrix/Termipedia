from bs4 import BeautifulSoup
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
    #What the request looks like to the client, metadata of the request
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
    
def clean_article_html(article_html):
    #HTML string --> Navigable Object(soup object)
    soup = BeautifulSoup(article_html, "html.parser")
    for tag in soup.find_all("style"):
        tag.decompose()

    #Removing css classes
    for junk in soup.find_all(class_ = ["reference", "references", "mw-editsection", "ambox", "navbox", "reflist", "external"]):
        junk.decompose() 

    #Returns only text content
    raw_text = soup.get_text(separator="\n") 
    lines = []
    for line in raw_text.splitlines():
        stripped = line.strip()
        if stripped:
            lines.append(stripped)

    clean_text = "\n".join(lines)
    return clean_text

print("The Termipedia has been intiated...")
while True:
    data_req = input("Welcome User!, what article do you want from wiki? ")
    if data_req == "":
        print("Try again!")
    else:
        break

data = fetch_wiki_payload(data_req)
article_html = data["parse"]["text"]["*"] #Getting only the html part
readable = clean_article_html(article_html)
print(readable)
