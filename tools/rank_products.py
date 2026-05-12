def rank_products(products, sort_by):

    if sort_by == "price":
        ranked = sorted(
            products,
            key=lambda x: x["price"]
        )
        return ranked
    elif sort_by == "battery":
        ranked = sorted(
            products,
            key=lambda x: x["battery"],
            reverse=True
        )
        return ranked

    return products