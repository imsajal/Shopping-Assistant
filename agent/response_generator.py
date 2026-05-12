def generate_response(result, memory):
    workflow = memory.session.get("active_workflow")

    # SEARCH / RANK RESPONSE
    if workflow in ["search_product", "rank_products"]:
        if not result:
            return "No matching products found."

        lines = ["Here are some recommended products:\n"]
        for index, product in enumerate(result):
            line = (
                f"{index + 1}. {product['name']}\n"
                f"   - Price: ₹{product['price']}\n"
                f"   - Battery: {product['battery']} hours\n"
                f"   - Brand: {product.get('brand', 'N/A')}\n"
                f"   - Category: {product.get('category', 'N/A')}\n"
            )
            lines.append(line)
        return "\n".join(lines)
   

    # COMPARE RESPONSE
    if workflow == "compare_products":
        if isinstance(result, str):
            return result
        if not isinstance(result, dict):
            return str(result)
        p1 = result.get("product1")
        p2 = result.get("product2")
        if not p1 or not p2:
            return str(result)

        def _battery_line(p):
            b = p.get("battery", p.get("battery"))
            if b is None:
                return "N/A"
            return f"{b} hours"

        def _product_section(p):
            return (
                f"{p['name']}\n"
                f"  Price:    ₹{p['price']:,}\n"
                f"  Battery:  {_battery_line(p)}\n"
                f"  Brand:    {p.get('brand', 'N/A')}\n"
                f"  Category: {p.get('category', 'N/A')}\n"
            )

        return (
            "Here's a clear comparison of the two products:\n\n"
            + _product_section(p1)
            + "\n"
            + _product_section(p2)
        )

    return str(result)