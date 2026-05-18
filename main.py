import os
import argparse
from agents import ReaderAgent, WriterAgent, ReviewerAgent

def process_file(filepath):
    print(f"\n--- Pipeline Started: Processing {filepath} ---")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
    except Exception as e:
        print(f"Failed to read {filepath}: {e}")
        return

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

def scan_and_process(target_dir):
    print(f"\n[Scanner] Starting scan in directory: {os.path.abspath(target_dir)}")
    ignore_dirs = {'.git', '.venv', 'venv', '__pycache__', 'env', '.idea', '.vscode'}
    
    python_files = []
    for root, dirs, files in os.walk(target_dir):
        # Exclude hidden and environment directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs and not d.startswith('.')]
        
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
                
    if not python_files:
        print(f"[Scanner] No Python files found in {target_dir}.")
        return

    print(f"[Scanner] Found {len(python_files)} Python files to process.")
    for file_path in python_files:
        process_file(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AutoCode-Analyzer: Code automated analysis and documentation agent.")
    parser.add_argument("path", nargs="?", default=".", help="File or directory path to scan (default: current directory)")
    
    args = parser.parse_args()
    
    print("=============================================")
    print(" Welcome to AutoCode-Analyzer Agent System")
    print("=============================================")
    
    target_path = args.path
    if os.path.isfile(target_path) and target_path.endswith('.py'):
        process_file(target_path)
    elif os.path.isdir(target_path):
        scan_and_process(target_path)
    else:
        print(f"Error: Invalid path or not a python file: {target_path}")
