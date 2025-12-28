def benefits_block(product):
    """
    Logic Block:
    -Converts product benefits into structured form
    """

    return {
        "summary":"Helps brighten the skin and fade dark spots.",
        "ingredients_to_benefits": dict(
           zip(product["ingredients"], product["benefits"])
         )
    }
