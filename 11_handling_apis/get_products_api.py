import requests

def fetch_product_api(page:str="1", limit:str="10", query:str="mens-watches"):
    url = "https://api.freeapi.app/api/v1/public/randomproducts"
    product_data = {"page":str(page), "limit":str(limit),"inc":"category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid", "query":str(query)}
    response = requests.get(url, params = product_data)
    product_info = response.json()

    if product_info["success"] and "data" in product_info:
        return product_info["data"]["data"]
    else:
        raise Exception("Product Not Found Error!!")

def main():
    try:
        page = input("Enter page: ")
        limit = input("Enter limit: ")
        query = input("Enter query: ")

        products = fetch_product_api(page, limit, query)

        for product in products:
            print(f"\nID: {product['id']}")
            print(f"Category: {product['category']}")
            print(f"Price: {product['price']}")
            print(f"Thumbnail: {product['thumbnail']}")
            print(f"Title: {product['title']}")
            print("Images:")
            for img in product['images']:
                print(f" - {img}")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()