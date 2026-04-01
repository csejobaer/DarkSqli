import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url):
    found = set()

    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href")
            if href:
                full = urljoin(url, href)
                if "?" in full:
                    found.add(full)

    except:
        pass

    return list(found)
