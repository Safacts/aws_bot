import json
import os

def extract_guides():
    json_path = r'c:\internship\aws_bot\legacy-web\extracted_data.json'
    target_dir = r'c:\internship\aws_bot\web\src\content\guides'
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    guides = data.get('guides', {})
    for name, content in guides.items():
        filename = name.lower().replace(' ', '_') + '.md'
        file_path = os.path.join(target_dir, filename)
        with open(file_path, 'w', encoding='utf-8') as gf:
            gf.write(content)
        print(f"Extracted {filename}")

if __name__ == "__main__":
    extract_guides()
