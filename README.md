# Termipedia

A terminal-based Wikipedia reader written in Python.

## The origin story

I started this wanting to build a terminal *browser*; a full web browser running inside the terminal. A bit of research later, reality gently informed me that was a wildly ambitious first project. So I climbed down the hopes-ladder a few rungs and landed on something I could actually build *and* learn from: a Wikipedia article reader that lives in your terminal.

No regrets about the climbdown. The point was never to beat Google, it was to learn Python by building something real, by hand, understanding every line instead of pasting code I didn't write. Termipedia is that: my main learning project, scars and all.

## What it does

You type a search term. Termipedia fetches that article from Wikipedia, strips the raw HTML down to clean readable text, prints it in your terminal, and saves a local copy so the next time you ask for it, it loads instantly instead of hitting the network again.

## How it works

Three layers, each doing one job:

- **Fetching** (`fetch_wiki_payload`) — calls the Wikipedia API with the search term, using a custom `User-Agent` header (without it, Wikipedia returns a 403 and refuses the request). Returns the article as JSON.
- **Cleaning** (`clean_article_html`) — parses the HTML with BeautifulSoup, removes the junk (references, infoboxes, navigation boxes, sidebars), then extracts text block by block so sentences stay intact. The order matters: remove junk first, extract text second.
- **Caching** (`get_article`) — before fetching, checks whether the article is already saved locally. If yes, reads from disk. If no, fetches, cleans, saves, and returns it.

## Built with

- Python
- [`requests`](https://pypi.org/project/requests/) — HTTP requests to the Wikipedia API
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) — HTML parsing and cleaning
- `pathlib` — file handling for the cache

## How to run it
- git clone https://github.com/orion-kendrix/Termipedia
- cd Termipedia
- cd "C:\Users\BUDDY\Documents\GARBAGE\test\Termipedia"
- .\venv\Scripts\Activate.ps1
- python -m pip install -r requirements.txt
- python scraper.py

## Current status

- ✅ CLI version working — fetch, clean, and local caching all functional
- 🚧 Textual TUI (interactive terminal interface) — in progress
- 📋 Planned — ArXiv support, global launch command

## What I learned
I learned how the actual API requests work behind the browser environment, how the request is created and sent. I also came across a error 403 access denied bug while doing this because I did not include a header
of the request which includes the "User-Agent", which is considered as a rookie mistake. I also learned how to use beautiful soup to filter out html files and gather important information from a an article using a "html.parser". 
I also learned that it is important to remove the junk HTML before extracting the text instead of cleaning the text after because then it will include unecessary html part which would end up in cleaning the text.
There were several bugs that I encounterd in the way like the list-mutation-during-loop crash, which basically means that you cannot update a list while traversing the same list in a loop, again a rookie mistake. 
I also learned little bit of the Path python library and used it to save all the outputs from the user, so in case if the user asks for the same result again, the program can return the existing result stored as a markdown file.

*A learning project, deliberately built by hand. Still growing(slowly but surely!*
