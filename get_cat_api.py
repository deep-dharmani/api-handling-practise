import requests
def get_cat():
    url="https://api.freeapi.app/api/v1/public/cats/cat/random"
    data_s=requests.get(url).json()
    if data_s ["success"] and "data" in data_s:
        get_cat_info=data_s ["data"]
        name=get_cat_info["name"]
        adaptability=get_cat_info["adaptability"]
        weight_imperial=get_cat_info["weight"]["imperial"]
        weight_metric=get_cat_info["weight"]["metric"]
        description=get_cat_info["description"]
        return name,adaptability,weight_imperial,weight_metric,description
    else:
        raise Exception("failed to fetch cat")
def main():
    try:
        name,adaptability,weight_imperial,weight_metric,description=get_cat()
        print(f"Name: {name}\nadaptablity: {adaptability}%\nweight:imperial({weight_imperial}) \
        metric({weight_metric})\n{description}")
    except Exception as e:
        print(str(e))
if __name__=="__main__":
    main()