import json

from product_data import PRODUCT_DATA
from agents.parser_agent import ProductParserAgent
from agents.question_agent import QuestionGeneratorAgent
from agents.faq_agent import FAQAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent

from logic_blocks.benefits import benefits_block
from logic_blocks.usage import usage_block
from logic_blocks.safety import safety_block


def main():
    print("main() started")

    # 1. Parse product data
    parser = ProductParserAgent()
    product = parser.run(PRODUCT_DATA)

    # 2. Generate questions
    question_agent = QuestionGeneratorAgent()
    questions = question_agent.run(product)

    # 3. Run logic blocks
    logic = {
        "benefits": benefits_block(product),
        "usage": usage_block(product),
        "safety": safety_block(product)
    }

    # 4. Generate pages
    faq_page = FAQAgent().run(questions, logic)
    product_page = ProductPageAgent().run(product, logic)
    comparison_page = ComparisonAgent().run(product)

    # 5. Write outputs
    with open("outputs/faq.json", "w") as f:
        json.dump(faq_page, f, indent=2)

    with open("outputs/product_page.json", "w") as f:
        json.dump(product_page, f, indent=2)

    with open("outputs/comparison_page.json", "w") as f:
        json.dump(comparison_page, f, indent=2)

    print("All pages generated successfully in /outputs")


if __name__ == "__main__":
    main()
