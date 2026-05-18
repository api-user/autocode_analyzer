import os
from agents import ReaderAgent, WriterAgent, ReviewerAgent

def process_file(filepath):
    print(f"\n--- Pipeline Started: Processing {filepath} ---")
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    reader = ReaderAgent()
    writer = WriterAgent()
    reviewer = ReviewerAgent()

    # 1. Reader analyzes
    print("\n[Step 1] Reading and Understanding...")
    logic_summary = reader.analyze_code(code)
    print(f"-> Reader Output: {logic_summary}")

    # 2. Writer generates docs
    print("\n[Step 2] Generating Documentation...")
    docstring = writer.generate_docstring(logic_summary)
    print(f"-> Writer Output:\n{docstring}")

    # 3. Reviewer checks
    print("\n[Step 3] Reviewing against source...")
    is_approved = reviewer.review(code, docstring)
    if is_approved:
        print("-> Status: ✅ APPROVED. Ready to merge PR.")
    else:
        print("-> Status: ❌ REJECTED. Needs revision by WriterAgent.")

if __name__ == "__main__":
    # Create a dummy python file to analyze for the demo
    dummy_file = "sample_target.py"
    with open(dummy_file, 'w', encoding='utf-8') as f:
        f.write("def calculate_total(prices, tax_rate):\n    return sum(prices) * (1 + tax_rate)\n")
    
    print("Welcome to AutoCode-Analyzer Agent System")
    process_file(dummy_file)
