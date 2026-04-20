import json
import os

with open('extracted_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

json_str = json.dumps(data, indent=4)
js_injection = f"const DATA = {json_str};\n"

os.makedirs('scratch', exist_ok=True)
with open('scratch/js_injection.js', 'w', encoding='utf-8') as f:
    f.write(js_injection)
