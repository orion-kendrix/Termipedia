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

    #Removing style tgs.
    for tag in soup.find_all("style"):
        tag.decompose()

    #Removing css classes
    for junk in soup.find_all(class_ = ["reference", "references", "mw-editsection", "ambox", "navbox", "reflist", "external", "infobox", "navbar", "metadata", "side-box", "sidebar", "vertical-navbox", "sistersitebox"]):
        junk.decompose() 
    list_of_req = []
    for text in soup.find_all(["p", "h2", "h3", "li", "h1", "h4", "h5", "\n"]):
        temp = text.get_text().strip()
        if temp and temp not in ["References", "External links", "Works cited", "Further reading", "Notes", "See also"]: #Returns only text content and individual elements would be on a different line
            if text.name in ["h1", "h2", "h3", "h4", "h5"]:
                list_of_req.append("\n" + temp)
            else:
                list_of_req.append(temp)
    return "\n".join(list_of_req)

print("The Termipedia has been initiated...")
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
