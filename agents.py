import os
import time

class BaseAgent:
    def __init__(self, name, model="gemini-1.5-pro"):
        self.name = name
        self.model = model
        print(f"[{self.name}] Initialized with model {self.model}")

    def prompt(self, text):
        # Mocking LLM call for demonstration
        print(f"[{self.name}] Thinking...")
        time.sleep(1)
        return f"[{self.name}] Processed: {text[:20]}..."

class ReaderAgent(BaseAgent):
    def __init__(self):
        super().__init__("ReaderAgent")

    def analyze_code(self, code_snippet):
        print(f"[{self.name}] Analyzing AST and logic flow...")
        return f"Logic summary of {len(code_snippet)} bytes of code."

class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__("WriterAgent")

    def generate_docstring(self, logic_summary):
        print(f"[{self.name}] Generating markdown docs and docstrings...")
        return '"""\nThis function calculates the total price including tax.\nArgs:\n    prices: List of item prices.\n    tax_rate: The applicable tax rate.\nReturns:\n    Total cost.\n"""'

class ReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__("ReviewerAgent")

    def review(self, code, docstring):
        print(f"[{self.name}] Cross-checking code against generated docs for hallucinations...")
        time.sleep(1)
        return True # Approved
