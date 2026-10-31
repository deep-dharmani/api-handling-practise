import requests
def get_dummy_produts():
        url=("https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches")
        data_s=requests.get(url).json()
        if data_s["success"] and "data" in data_s :
                products_data= data_s["data"]["data"]
                product1_name=products_data[0]["category"]
                product1_price=products_data[0]["price"]
                product2_name=products_data[7]["category"]
                product2_price=products_data[7]["price"]
                product3_name=products_data[8]["category"]
                product3_price=products_data[8]["price"]
                product4_name=products_data[3]["category"]
                product4_price=products_data[3]["price"]
                product5_name=products_data[9]["category"]
                product5_price=products_data[9]["price"]
                product6_name=products_data[5]["category"]
                product6_price=products_data[5]["price"]
                return product1_name,product1_price,product2_name,product2_price,product3_name,product3_price,product4_name,product4_price,product5_name,product5_price,product6_name,product6_price
        else:
            raise Exception ("Failed to fetch products")
def main():
    try:
        product1_name,product1_price,product2_name,product2_price,product3_name,product3_price,product4_name,product4_price,product5_name,product5_price,product6_name,product6_price=get_dummy_produts()
        print(f"{product1_name} : {product1_price}\n{product2_name} : {product2_price}\n{product3_name}: {product3_price}\n{product4_name}:{product4_price}\n{product5_name}:{product5_price}\n{product6_name}:{product6_price}")
    except Exception as e:
        print(str(e))
if __name__=="__main__":
    main()      
