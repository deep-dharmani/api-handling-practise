import requests
def random_quotes():
    url="https://api.freeapi.app/api/v1/public/quotes/quote/random"
    data_s=requests.get(url).json()
    if data_s["success"] and "data" in data_s:
        quotes_info=data_s["data"]
        quote=quotes_info["content"]
        author=quotes_info["author"]
        type=quotes_info["tags"][0]
        return quote,author,type
    else:
        raise Exception("failed to fetch qoute")
def main():
    try:
        quote,author,type=random_quotes()
        print(f"{type}:\n{" "*len(type)}{quote}\nby {author}")
    except Exception as e:
        print(str(e))
if __name__=="__main__":
    main()