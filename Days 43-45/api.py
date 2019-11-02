import requests
from collections import namedtuple
from typing import List

SearchItem = namedtuple('SearchItem', 'category, id, url, title, description')

def find_item(search_term: str) -> List[SearchItem]:
    url = f'https://search.talkpython.fm/api/search?q={search_term}'

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()
    search_items = []
    
    for r in results.get('results'):
        search_items.append(SearchItem(**r))

    return search_items