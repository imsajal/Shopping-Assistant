import json

from utils.llm_client import call_llm
from agent.prompts import PLANNER_PROMPT
from models.schema import PlannerOutput
from utils.helpers import format_recent_history


def create_plan(user_query, history=None, summary=None, preferences=None):
    # Sanitized, consistent formatting for prompt sections
    prompt = (
        f"{PLANNER_PROMPT}\n"
        f"Conversation Summary:\n"
        f"{summary if summary is not None else ''}\n\n"
        f"User Preferences:\n"
        f"{preferences if preferences is not None else ''}\n\n"
        f"Recent History:\n"
        f"{format_recent_history(history=history) if history is not None else ''}\n\n"
        f"User Query:\n"
        f"{user_query}\n"
    )

    response = call_llm(prompt).strip()

    # Clean out possible code fencing before parsing JSON
    if response.startswith("```json"):
        response = response.replace("```json", "", 1)
        response = response.replace("```", "")

    try:
        parsed = json.loads(response)
        validated = PlannerOutput(**parsed)
    except Exception as e:
        raise ValueError(
            f"Failed to parse or validate planner output: {e}\nRaw response: {response}"
        )

    return validated



