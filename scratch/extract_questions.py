import json
import os

def extract_questions():
    json_path = r'c:\internship\aws_bot\legacy-web\extracted_data.json'
    target_path = r'c:\internship\aws_bot\web\src\data\questions.json'
    
    target_dir = os.path.dirname(target_path)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    questions = data.get('questions', [])
    with open(target_path, 'w', encoding='utf-8') as qf:
        json.dump(questions, qf, indent=4)
        
    print(f"Extracted {len(questions)} questions")

if __name__ == "__main__":
    extract_questions()
