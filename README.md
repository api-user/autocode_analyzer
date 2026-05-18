# AutoCode-Analyzer

AutoCode-Analyzer is an AI-driven, multi-agent system designed to automatically analyze legacy codebases, generate comprehensive documentation, and identify potential refactoring opportunities.

## 🌟 Core Pain Point Solved
Legacy codebases often lack sufficient documentation, making onboarding new developers extremely costly. Manually reading, understanding, and documenting old code is tedious and error-prone. This project automates the process using Large Language Models (LLMs) and a multi-agent architecture.

## 🚀 Core Logic Flow (Multi-Agent Collaboration)
1. **Extraction**: Automatically parses Python files and extracts AST (Abstract Syntax Tree) nodes (functions, classes).
2. **Reader Agent (Long-chain reasoning)**: Analyzes the code structure, understands business logic, and infers dependencies.
3. **Writer Agent**: Based on the Reader's insights, generates standard PEP-257 compliant docstrings and Markdown documentation.
4. **Reviewer Agent**: Critiques the generated documentation against the original code to ensure accuracy and prevents hallucinations.

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/autocode-analyzer.git
cd autocode-analyzer
pip install -r requirements.txt
```

## 💻 Quick Start

Run the main agent pipeline on a sample file:
```bash
python main.py
```
