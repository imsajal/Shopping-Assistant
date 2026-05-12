from tools.search_product import search_product
from tools.compare_product import compare_product
from tools.rank_products import rank_products   # UPDATED


def update_filters(plan, memory):

    if getattr(plan, "category", None):
        memory.tools["search_product"]["filters"]["category"] = plan.category

    if getattr(plan, "brand", None):
        memory.tools["search_product"]["filters"]["brand"] = plan.brand

    if getattr(plan, "max_price", None):
        memory.tools["search_product"]["filters"]["max_price"] = plan.max_price


def execute_plan(plan, memory):

    # UPDATED
    # Multi-step workflow support

    final_result = None

    # UPDATED
    # Iterate through workflow steps

    for step in plan.steps:

        # SEARCH PRODUCT

        if step.tool == "search_product":

            # Update session filters
            update_filters(step, memory)
            memory.session["active_workflow"] = "search_product"

            # Execute grounded retrieval
            results = search_product(
                category=memory.tools["search_product"]["filters"].get("category"),
                max_price=memory.tools["search_product"]["filters"].get("max_price"),
                brand=memory.tools["search_product"]["filters"].get("brand")
            )

            # Save grounded tool output
            memory.tools["search_product"]["search_results"] = results

            # UPDATED
            final_result = results


        # RANK PRODUCTS

        elif step.tool == "rank_products":

            # UPDATED
            # Ranking relies on grounded memory state
            # instead of hallucinated LLM output

            memory.session["active_workflow"] = "rank_products"

            ranked_results = rank_products(
                products=memory.tools["search_product"]["search_results"],
                sort_by=step.sort_by
            )

            # UPDATED
            # Save ranked results in memory

            memory.tools["rank_products"]["ranked_results"] = ranked_results

            final_result = ranked_results


        # COMPARE PRODUCTS

        elif step.tool == "compare_products":
            memory.session["active_workflow"] = "compare_products"
            products_to_compare = []

            # CASE 1:
            # Explicit product comparison
            # Example:
            # compare ASUS and Lenovo

            if step.product1 and step.product2:

                product1 = step.product1.lower()
                product2 = step.product2.lower()

                for product in memory.tools["search_product"]["search_results"]:

                    name = product["name"].lower()

                    if product1 in name or product2 in name:
                        products_to_compare.append(product)

            # CASE 2:
            # Positional comparison
            # Example:
            # compare first two

            elif step.indexes:

                for index in step.indexes:

                    if abs(index) < len(memory.tools["search_product"]["search_results"]):

                        products_to_compare.append(
                            memory.tools["search_product"]["search_results"][index]
                        )

            # Validation
            if len(products_to_compare) < 2:
                return "Unable to find enough products to compare"

            # Save selected comparison products
            memory.tools["compare_products"]["comparison_products"] = products_to_compare

            # Grounded comparison
            comparison = compare_product(
                products_to_compare[0],
                products_to_compare[1]
            )

            # Save comparison output
            memory.tools["compare_products"]["last_comparison"] = comparison

            final_result = comparison

    # UPDATED
    return final_result