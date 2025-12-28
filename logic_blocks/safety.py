def safety_block(product):
    """
    Logic Block:
    - Handles safety and side effect information
    """

    return {
        "side_effects": product["side_effects"],
        "recommendation": "Patch test recommended for sensitive skin"
    }
