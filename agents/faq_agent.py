from agents.base_agent import BaseAgent

class FAQAgent(BaseAgent):
    def __init__(self):
        super().__init__("FAQAgent")

    def can_handle(self, task):
        return task["type"] == "GENERATE_FAQ"

    def handle(self, task, context):
        faqs = []
        for q in context["questions"]["informational"]:
            faqs.append({
                "question": q,
                "answer": "Answer based on product benefits."
            })

        context["faq"] = faqs
        return {"faq": faqs}
