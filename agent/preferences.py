def update_preferences(plan, memory):

    preferences = memory.session[
        "preferences"
    ]

    for step in plan.steps:

        if getattr(step, "category", None):

            preferences[
                "category"
            ] = step.category

        if getattr(step, "brand", None):

            preferences[
                "brand"
            ] = step.brand

        if getattr(step, "max_price", None):

            preferences[
                "max_price"
            ] = step.max_price

        if getattr(step, "sort_by", None):

            preferences[
                "sort_by"
            ] = step.sort_by