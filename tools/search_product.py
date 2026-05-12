import json

with open("data/products.json") as f:
    PRODUCTS = json.load(f)


 # if required to read data from inventory data file also read it here ,
 # do the logic inside function by loading inventory also   


def search_product(category = None, max_price = None, brand = None):

    results = []

    for product in PRODUCTS:

        if category:
            if category.lower() != product["category"].lower():
                continue;

        if brand:
            if brand.lower() != product["brand"].lower():
                continue;        

        if max_price:

            if max_price < product["price"]:
                continue; 

        results.append(product)
    return results                  

