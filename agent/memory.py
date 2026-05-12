class ConversationMemory:

    def __init__(self):
        self.history = []

        self.session = {

            "preferences": {},

            "active_workflow": None,
            "conversation_summary": ""

        }

        self.tools = {

            "search_product": {

                "filters": {
                    "category": None,
                    "brand": None,
                    "max_price": None
                },
           

                "search_results": [],
            },

            "rank_products": {

                "ranked_results": []

            },

            "compare_products": {

                "comparison_products": [],

                "last_comparison": None

            }

        }

    def add(self, role, content):

        self.history.append({
            "role" : role, 
            "content" : content
        }) 

    def get_recent_history(self):
        return self.history[-5:]       