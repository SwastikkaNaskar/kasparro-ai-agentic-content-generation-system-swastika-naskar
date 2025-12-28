class FAQAgent:
    """
    Responsibility:
    - Generate FAQ page JSON using questions + logic blocks
    """

    def run(self, questions, logic):
        faq_items = []

        for question in questions["informational"][:5]:
            faq_items.append({
                "question": question,
                "answer": logic["benefits"]["summary"]
            })

        return {
            "page_type": "FAQ",
            "items": faq_items
        }
