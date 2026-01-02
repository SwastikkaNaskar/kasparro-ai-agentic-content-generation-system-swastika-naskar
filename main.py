from product_data import PRODUCT_DATA

from agents.parser_agent import ProductParserAgent
from agents.question_agent import QuestionGeneratorAgent
from agents.faq_agent import FAQAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent


class Orchestrator:
    def __init__(self, agents):
        self.agents = agents
        self.context = {}

    def dispatch(self, task):
        for agent in self.agents:
            if agent.can_handle(task):
                print(f"{agent.name} handling {task['type']}")
                agent.handle(task, self.context)
                return
        raise Exception("No agent found")


def main():
    agents = [
        ProductParserAgent(),
        QuestionGeneratorAgent(),
        FAQAgent(),
        ProductPageAgent(),
        ComparisonAgent()
    ]

    orchestrator = Orchestrator(agents)

    orchestrator.dispatch({"type": "PARSE_PRODUCT", "payload": PRODUCT_DATA})
    orchestrator.dispatch({"type": "GENERATE_QUESTIONS"})
    orchestrator.dispatch({"type": "GENERATE_FAQ"})
    orchestrator.dispatch({"type": "GENERATE_PRODUCT_PAGE"})
    orchestrator.dispatch({"type": "GENERATE_COMPARISON"})

    print("\nFINAL CONTEXT:")
    print(orchestrator.context)


if __name__ == "__main__":
    main()
