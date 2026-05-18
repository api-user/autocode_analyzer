import os
import time
import google.generativeai as genai

# Try to configure Gemini API if key is present
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Use modern models that are widely supported and permitted.
# User can override this by setting the GEMINI_MODEL environment variable.
DEFAULT_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.1-flash")

class BaseAgent:
    def __init__(self, name, model=None):
        self.name = name
        self.model = model if model is not None else DEFAULT_MODEL
        self.use_real_llm = bool(GEMINI_API_KEY)
        if self.use_real_llm:
            self.llm = genai.GenerativeModel(self.model)
            print(f"[{self.name}] Initialized REAL model {self.model}")
        else:
            print(f"[{self.name}] Initialized MOCK model (Set GEMINI_API_KEY to activate)")

    def prompt(self, text):
        print(f"[{self.name}] Thinking...")
        if self.use_real_llm:
            try:
                response = self.llm.generate_content(text)
                return response.text
            except Exception as e:
                return f"Error calling Gemini: {e}"
        else:
            # Mocking LLM call for demonstration
            time.sleep(1)
            return f"Mock response for: {text[:30]}..."

class ReaderAgent(BaseAgent):
    def __init__(self):
        super().__init__("ReaderAgent")

    def analyze_code(self, code_snippet):
        print(f"[{self.name}] Analyzing AST and logic flow...")
        prompt = f"Please analyze the following Python code and provide a brief logic summary:\n\n{code_snippet}"
        if self.use_real_llm:
            return self.prompt(prompt)
        return f"Logic summary of {len(code_snippet)} bytes of code."

class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__("WriterAgent")

    def generate_docstring(self, logic_summary, code):
        print(f"[{self.name}] Generating markdown docs and docstrings...")
        prompt = f"Based on this logic summary: {logic_summary}\n\nGenerate PEP-257 docstrings for the functions in this code:\n\n{code}"
        if self.use_real_llm:
            return self.prompt(prompt)
        return '"""\nMock Docstring generated.\n"""'

class ReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__("ReviewerAgent")

    def review(self, code, docstring):
        print(f"[{self.name}] Cross-checking code against generated docs...")
        prompt = f"Does this docstring accurately describe the code without hallucinations?\nCode:\n{code}\n\nDocstring:\n{docstring}\n\nAnswer only YES or NO."
        if self.use_real_llm:
            ans = self.prompt(prompt)
            return "YES" in ans.upper()
        time.sleep(1)
        return True # Approved
