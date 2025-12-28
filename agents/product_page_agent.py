class ProductPageAgent:
    """
    Responsibility:
    - Generate product detail page JSON
    """

    def run(self, product, logic):
        return {
            "page_type": "Product Page",
            "name": product["name"],
            "overview": f"{product['concentration']} Vitamin C serum for {', '.join(product['skin_type'])} skin.",
            "ingredients": product["ingredients"],
            "benefits": logic["benefits"],
            "usage": logic["usage"],
            "price": product["price"]
        }
