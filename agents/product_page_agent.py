from agents.base_agent import BaseAgent

class ProductPageAgent(BaseAgent):
    def __init__(self):
        super().__init__("ProductPageAgent")

    def can_handle(self, task):
        return task["type"] == "GENERATE_PRODUCT_PAGE"

    def handle(self, task, context):
        product = context["product"]

        page = {
            "name": product["name"],
            "ingredients": product["ingredients"],
            "benefits": product["benefits"],
            "usage": product["usage"],
            "price": product["price"]
        }

        context["product_page"] = page
        return {"product_page": page}
