class QuestionGeneratorAgent:
    """
    Responsibility:
    - Generate categorized user questions from product data
    """

    def run(self, product):
        questions = {
            "informational": [
                f"What is {product['name']}?",
                f"What does {product['concentration']} Vitamin C indicate?"
            ],
            "usage": [
                "How should this serum be applied?",
                "When is the best time to use this product?",
                "Can it be used daily?"
            ],
            "safety": [
                "Does this product cause side effects?",
                "Is it suitable for sensitive skin?",
                "Should a patch test be done?"
            ],
            "purchase": [
                "What is the price of this serum?",
                "Is this product worth its cost?",
                "Who should buy this serum?"
            ],
            "comparison": [
                "How does this serum compare to other vitamin C serums?",
                "What makes this serum different?"
            ]
        }

        return questions
   
