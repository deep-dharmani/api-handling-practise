import requests

def fetch_random_jokes_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response=requests.get(url)
    data_s=response.json()
    if data_s["success"] and "data" in data_s:
        joke_data=data_s["data"]["data"]
        joke1=joke_data[0]["content"]
        joke2=joke_data[1]["content"]
        joke3=joke_data[2]["content"]
        joke4=joke_data[3]["content"]
        return joke1,joke2,joke3,joke4
    else:
        raise Exception ("failed to fetch joke")
def main():
    try:
        joke1,joke2,joke3,joke4=fetch_random_jokes_freeapi()
        print(f"joke1:{joke1}\n    \njoke2:{joke2}\n     \njoke3:{joke3}\n        \njoke4:{joke4}")
    except Exception as e:
        print(str(e))
if __name__=="__main__":
    main()
    
    