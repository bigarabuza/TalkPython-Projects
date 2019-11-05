import requests
from bs4 import BeautifulSoup

URL = 'https://runestone.academy/runestone/books/published/thinkcspy/index.html'

def main():
    site = pull_site()
    scrape(site)

def pull_site():
    raw_site_page = requests.get(URL)
    raw_site_page.raise_for_status()
    return raw_site_page

def scrape(site):
    chapters = []
    soup = BeautifulSoup(site.text, 'html.parser')
    html_chapters_list = soup.find_all('li', 'toctree-l1')
    
    for item in html_chapters_list:
        chapters.append(item.getText())
    for chapter in chapters:
        print(chapter)  
        print('end')  
    

if __name__ == "__main__":
    main()




