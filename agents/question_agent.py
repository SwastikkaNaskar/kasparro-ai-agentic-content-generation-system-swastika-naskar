from agents.base_agent import BaseAgent

class QuestionGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("QuestionGeneratorAgent")

    def can_handle(self, task):
        return task["type"] == "GENERATE_QUESTIONS"

    def handle(self, task, context):
        product = context["product"]

        questions = {
            "informational": [
                f"What are the benefits of {product['name']}?"
            ],
            "usage": [
                f"How do I use {product['name']}?"
            ],
            "safety": [
                f"Are there side effects of {product['name']}?"
            ]
        }

        context["questions"] = questions
        return {"questions": questions}
   
