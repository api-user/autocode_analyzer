import os
import argparse
from agents import ReaderAgent, WriterAgent, ReviewerAgent

def process_file(filepath, reader, writer, reviewer):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
    except Exception as e:
        return f"Failed to read {filepath}: {e}\n\n---\n\n"

    result_md = f"## File: `{filepath}`\n\n"
    
    # 1. Reader analyzes
    logic_summary = reader.analyze_code(code)
    result_md += f"### 1. Logic Summary (Reader Agent)\n{logic_summary}\n\n"

    # 2. Writer generates docs
    docstring = writer.generate_docstring(logic_summary, code)
    result_md += f"### 2. Generated Documentation (Writer Agent)\n```python\n{docstring}\n```\n\n"

    # 3. Reviewer checks
    is_approved = reviewer.review(code, docstring)
    status = "✅ APPROVED" if is_approved else "❌ REJECTED"
    result_md += f"### 3. Review Status (Reviewer Agent)\n**{status}**\n\n---\n\n"
    
    return result_md

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
    
    reader = ReaderAgent()
    writer = WriterAgent()
    reviewer = ReviewerAgent()
    
    all_results = "# AutoCode-Analyzer Report\n\n"
    
    for file_path in python_files:
        print(f"Processing: {file_path}...")
        report = process_file(file_path, reader, writer, reviewer)
        all_results += report
        
    output_file = "analysis_report.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(all_results)
    
    print(f"\n[Success] All results have been aggregated into {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AutoCode-Analyzer: Code automated analysis and documentation agent.")
    parser.add_argument("path", nargs="?", default=".", help="File or directory path to scan (default: current directory)")
    
    args = parser.parse_args()
    
    print("=============================================")
    print(" Welcome to AutoCode-Analyzer Agent System")
    print("=============================================")
    
    target_path = args.path
    if os.path.isfile(target_path) and target_path.endswith('.py'):
        reader = ReaderAgent()
        writer = WriterAgent()
        reviewer = ReviewerAgent()
        print(f"Processing single file: {target_path}...")
        report = process_file(target_path, reader, writer, reviewer)
        
        output_file = "analysis_report.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# AutoCode-Analyzer Report\n\n{report}")
        print(f"\n[Success] Result saved to {output_file}")
    elif os.path.isdir(target_path):
        scan_and_process(target_path)
    else:
        print(f"Error: Invalid path or not a python file: {target_path}")
