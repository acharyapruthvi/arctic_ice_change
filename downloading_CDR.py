import re
import requests
import earthaccess
from bs4 import BeautifulSoup

earthaccess.login(strategy="netrc")

INDEX_URL = "https://noaadata.apps.nsidc.org/NOAA/G02202_V6/south/monthly/"

# Step 1: get the directory listing
resp = requests.get(INDEX_URL)
resp.raise_for_status()
soup = BeautifulSoup(resp.text, "html.parser")

# Step 2: pull out all links that look like actual data files (.nc)
urls = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href and href.endswith(".nc"):
        urls.append(INDEX_URL + href)

print(f"Found {len(urls)} monthly files")

# Step 3: download everything via earthaccess (handles Earthdata auth)
earthaccess.download(urls, "./data/south")