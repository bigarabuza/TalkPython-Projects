import api

def main():
    print('******* SEARCH TALK PYTHON *******')
    keyword = input('What would you like to search for?: ')
    results = api.find_item(keyword)

    print(f'There are {len(results)} items:')
    for cnt, r in enumerate(results, start=1):
        print(cnt, r.title)


if __name__ == "__main__":
    main()