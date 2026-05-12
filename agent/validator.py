class ClarificationRequired(Exception):

    pass


def validate_business_rules(plan, memory):
    for step in plan.steps:
        if step.tool == "compare_products":
            if step.indexes:
                total_products = len(memory.tools["search_product"].get("search_results", []))

                for index in step.indexes:
                    if abs(index) >= total_products:
                        raise ClarificationRequired(
                            f"Only {total_products} products available to compare."
                        )

            if not step.indexes and not (step.product1 and step.product2):
                raise ClarificationRequired(
                    "Please specify which products to compare."
                )