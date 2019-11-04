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
    sections = []
    sub_sections = []
    soup = BeautifulSoup(site.text, 'html.parser')
    html_chapters_list = soup.find_all('li', 'toctree-l1')
    html_sections_list = soup.find_all('li', 'toctree-l2')
    html_subsections_list = soup.find_all('li', 'toctree-l3')

    for item in html_chapters_list:
        chapters.append(item.getText())
    for chapter in chapters:
        print(chapter)
    
    

if __name__ == "__main__":
    main()