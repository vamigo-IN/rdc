import requests
import json
import os

def download_ddg(query, filename):
    print(f"Downloading for {query}...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    # A simple approach: use duckduckgo html search to find image urls
    url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}+before+after+dental"
    res = requests.get(url, headers=headers)
    
    # Very rudimentary extraction of the first image link
    # Actually, we can use a free image API or just search Wikimedia
    # Since it's just for a website mockup, we'll try to find a real image URL
    pass

# We will just use some static placeholder images from a known dental clinic or wikimedia for safety
urls = {
    'assets/img/cases/whitening-1.jpg': 'https://upload.wikimedia.org/wikipedia/commons/d/dd/Teeth_whitening_before_and_after.jpg',
    'assets/img/cases/root-canal-1.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Root_canal_treatment_before_and_after_X-ray.jpg/640px-Root_canal_treatment_before_and_after_X-ray.jpg',
    'assets/img/cases/cleaning-1.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Dental_calculus_before_and_after.jpg/640px-Dental_calculus_before_and_after.jpg'
}

for path, url in urls.items():
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)
            print(f"Downloaded {path}")
        else:
            print(f"Failed {path}")
    except Exception as e:
        print(f"Error {path}: {e}")

