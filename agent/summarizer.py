def summarize_conversation(memory):

    history = memory.history

    summary_parts = []

    for item in history[-20:]:

        role = item["role"]

        content = item["content"]

        summary_parts.append(
            f"{role}: {content}"
        )

    summary = "\n".join(summary_parts)

    # simple compressed memory

    memory.session[
        "conversation_summary"
    ] = summary[:1000]