import requests

def random_username_fetch_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    info = response.json()

    if info["success"] and "data" in info:
        user_data = info["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        street_name = user_data["location"]["street"]["name"]
        return username, country, street_name
    else:
        # raise -> used to raise errors
        raise Exception("Failed to fetch data from api!!")

def main():
    # to protect main() we need try catch block
    try:
        username, country, street_name = random_username_fetch_api()
        print(f"Username: {username}, \nCountry: {country}, \nStreet Name: {street_name}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()