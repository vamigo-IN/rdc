from duckduckgo_search import DDGS
import requests

queries = {
    'assets/img/cases/whitening-1.jpg': 'teeth whitening before after',
    'assets/img/cases/root-canal-1.jpg': 'root canal before after xray',
    'assets/img/cases/cleaning-1.jpg': 'teeth scaling cleaning before after'
}

with DDGS() as ddgs:
    for path, query in queries.items():
        results = ddgs.images(query, max_results=1)
        if results:
            url = results[0]['image']
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(r.content)
                print(f"Downloaded {path}")
            else:
                print(f"Failed {path}")
        else:
            print(f"No results for {query}")
