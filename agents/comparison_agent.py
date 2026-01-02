from agents.base_agent import BaseAgent

class ComparisonAgent(BaseAgent):
    def __init__(self):
        super().__init__("ComparisonAgent")

    def can_handle(self, task):
        return task["type"] == "GENERATE_COMPARISON"

    def handle(self, task, context):
        product = context["product"]

        comparison = {
            "primary": product["name"],
            "secondary": "Fictional Serum",
            "price": {
                product["name"]: product["price"],
                "Fictional Serum": product["price"] + 200
            }
        }

        context["comparison"] = comparison
        return {"comparison": comparison}
