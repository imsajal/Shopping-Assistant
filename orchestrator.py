from agent.planner import create_plan
from agent.executor import execute_plan
from agent.memory import ConversationMemory
from agent.validator import ClarificationRequired, validate_business_rules
from utils.logger import log_event

from agent.summarizer import summarize_conversation
from agent.preferences import update_preferences
from agent.response_generator import generate_response

memory = ConversationMemory()

print("\nShopping Assistant Started")
print("Type 'exit' to quit\n")

while True:

    user_query = input("User: ")
    if user_query.lower() == "exit":
        break

    memory.add("user", user_query)
    log_event("USER_QUERY",str(user_query))

    plan = None
    try:
        plan = create_plan(
            user_query,
            history=memory.get_recent_history(),
            summary=memory.session["conversation_summary"],
            preferences=memory.session["preferences"]
        )
   
        log_event("PLANNER_OUTPUT",str(plan))
    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nI could not understand the request properly. "
            "Please rephrase your query.")
    if plan:
        try:
            validate_business_rules(plan, memory)
        except ClarificationRequired as e:
            print(str(e))
        try:
            result = execute_plan(plan, memory)
            log_event("ASSISTANT_RESPONSE", str(result))
            final_response = generate_response(result, memory)
            print("\nAssistant Response:")
            print(final_response)
            memory.add("assistant", final_response)
            update_preferences(plan, memory)
            summarize_conversation(memory)
        except Exception as e:
            print(str(e))





   

