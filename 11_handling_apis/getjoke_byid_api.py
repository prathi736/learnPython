import requests

def fetch_joke_api(jokeId: str):
    url = f"https://api.freeapi.app/api/v1/public/randomjokes/{jokeId}"
    response = requests.get(url)
    joke_info = response.json()

    if joke_info["success"] and "data" in joke_info:
        joke_content = joke_info["data"]["content"]
        return joke_content
    else:
        raise Exception("Not able to find joke!!")

def main():
    try:
        jokeId = input("Enter joke id: ")
        joke = fetch_joke_api(jokeId)
        print(f"Your joke is: {joke}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()