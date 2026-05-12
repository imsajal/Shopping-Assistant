import json


with open("data/products.json") as f:
    PRODUCTS = json.load(f)

def compare_product(product1, product2):

    p1 = None
    p2 = None

    for product in PRODUCTS:

        if product["name"].lower() == product1["name"].lower():
            p1 = product    

        if product["name"].lower() == product2["name"].lower():
            p2 = product

    if not p1 or not p2:
        return "one or both products not found"      

    comparison = {
        "product1" : p1,
        "product2" : p2
    }

    return comparison  

    
             