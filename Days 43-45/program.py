import api
import webbrowser

def main():
    print('******* SEARCH TALK PYTHON *******')
    keyword = input('What would you like to search for?: ')
    results = api.find_item(keyword)

    print(f'There are {len(results)} items:')
    for cnt, r in enumerate(results, start=1):
        print(cnt, r.title)

    episode_ref = int(input(f'Enter episode index to view episode page: '))
    selected_url = f'talkpython.fm{results[episode_ref - 1].url}'
    webbrowser.open(selected_url, new=2)
    
if __name__ == "__main__":
    main()