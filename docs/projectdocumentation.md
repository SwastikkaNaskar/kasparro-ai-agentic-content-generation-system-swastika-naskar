Kasparro – Multi-Agent Content Generation System

1. Problem Statement
The objective of this assignment is to design and implement a modular, agentic automation
system that converts structured product data into machine-readable content pages.
The system must demonstrate agent orchestration, reusable logic blocks, template-driven
generation, and clean JSON outputs without relying on external data or monolithic scripts.


2. Solution Overview
The solution is implemented as a multi-agent pipeline where each agent has a single,
well-defined responsibility. The system parses product data, generates categorized user
questions, applies reusable content logic, and assembles structured pages using predefined
templates. An orchestrator coordinates the entire flow and produces final JSON outputs.


3. Scope & Assumptions
- Only the provided product dataset is used as input.
- No external APIs or additional product facts are introduced.
- A fictional Product B is used strictly for comparison purposes.
- The system focuses on backend automation and content generation, not UI or frontend.


4. System Design (Core Section)

4.1 Architecture Overview
The system follows an orchestrator-based agentic architecture. A central orchestrator
coordinates multiple independent agents, each responsible for a single task.

Pipeline flow:
1. Product Parser Agent parses raw product data.
2. Question Generator Agent generates categorized user questions.
3. Logic Blocks transform raw data into reusable content structures.
4. Page Agents assemble final pages using templates and logic blocks.
5. Orchestrator writes machine-readable JSON outputs.


 4.2 Agent Responsibilities

1.ProductParserAgent**
- Converts raw product input into a clean internal model.

2.QuestionGeneratorAgent**
- Generates categorized user questions (informational, usage, safety, purchase, comparison).

3.FAQAgent**
- Produces FAQ page JSON using questions and logic blocks.

4.ProductPageAgent**
- Generates structured product detail page JSON.

5.ComparisonAgent**
- Compares the primary product with a fictional secondary product.

Each agent has:
- a single responsibility
- explicit inputs and outputs
- no shared global state


4.3 Reusable Logic BlocksLogic blocks are implemented as pure functions and reused across multiple agents:
- benefits_block
- usage_block
- safety_block

This ensures composability, maintainability and separation of concerns.


4.4 Template System
Templates define the structure and required fields for each page type:
- FAQ Template
- Product Page Template
- Comparison Page Template

Agents generate content strictly according to these templates, ensuring consistency and
machine-readability.


4.5 Automation & Orchestration
The entire system is executed via a single orchestrator (`main.py`). Running the pipeline
automatically generates all required pages as JSON files in the output directory, proving
end-to-end automation.


5. Output Format
All generated pages are clean, structured JSON:
- faq.json
- product_page.json
- comparison_page.json

These outputs can be directly consumed by downstream systems or services.


6. Conclusion
This project demonstrates a production-style agentic content generation system with clear
agent boundaries, reusable logic, template-driven generation, and full automation. The design
emphasizes scalability, clarity, and maintainability, aligning with real-world AI system
engineering practices.
