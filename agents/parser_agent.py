class ProductParserAgent:
    """
    Responsibility:
    - Take raw product data
    - Convert it into a clean internal product model
    """

    def run(self, raw_data):
        product = {
            "name": raw_data["name"],
            "concentration": raw_data["concentration"],
            "skin_type": raw_data["skin_type"],
            "ingredients": raw_data["ingredients"],
            "benefits": raw_data["benefits"],
            "usage": raw_data["how_to_use"],
            "side_effects": raw_data["side_effects"],
            "price": raw_data["price"]
        }
        return product