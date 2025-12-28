# Kasparro – Multi-Agent Content Generation System

This repository contains a modular, agentic automation system designed to generate
structured, machine-readable product content pages from a single input dataset.

The system demonstrates multi-agent orchestration, reusable content logic blocks,
template-driven generation, and clean JSON outputs.


## Objective

Design and implement a production-style agentic system that:
- Parses structured product data
- Generates categorized user questions
- Applies reusable content logic
- Assembles pages using predefined templates
- Outputs fully structured JSON files


## System Overview

The system follows an orchestrator-based architecture:

- **Parser Agent** – Converts raw input into a clean internal model
- **Question Generator Agent** – Produces categorized user questions
- **Logic Blocks** – Reusable transformations for benefits, usage, and safety
- **Page Agents** – Generate FAQ, Product Page, and Comparison Page
- **Orchestrator (`main.py`)** – Coordinates the entire pipeline

All agents have single responsibilities and communicate via structured inputs/outputs.

---

## 🗂️ Project Structure
