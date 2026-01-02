from agents.base_agent import BaseAgent

class ProductParserAgent(BaseAgent):
    def __init__(self):
        super().__init__("ProductParserAgent")

    def can_handle(self, task):
        return task["type"] == "PARSE_PRODUCT"

    def handle(self, task, context):
        raw = task["payload"]

        product = {
            "name": raw["name"],
            "concentration": raw["concentration"],
            "skin_type": raw["skin_type"],
            "ingredients": raw["ingredients"],
            "benefits": raw["benefits"],
            "usage": raw["how_to_use"],
            "side_effects": raw["side_effects"],
            "price": raw["price"]
        }

        context["product"] = product

        return {"product": product}
