def format_recent_history(history):

    lines = []

    for item in history:

        role = item["role"].upper()

        content = item["content"]

        lines.append(
            f"{role}:\n{content}"
        )

    return "\n\n".join(lines)