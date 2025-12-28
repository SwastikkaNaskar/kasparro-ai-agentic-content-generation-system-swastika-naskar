class ComparisonAgent:
    """
    Responsibility:
    - Compare GlowBoost with a fictional product
    """

    def run(self, product):
        fictional_product = {
            "name": "RadiantFix Serum",
            "ingredients": ["Niacinamide"],
            "benefits": ["Oil control"],
            "price": 599
        }

        return {
            "page_type": "Comparison Page",
            "products": {
                product["name"]: {
                    "ingredients": product["ingredients"],
                    "benefits": product["benefits"],
                    "price": product["price"]
                },
                fictional_product["name"]: fictional_product
            }
        }
