import os

with open('scratch/js_injection.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find the target location
target = "const DATA = null; // We will replace this with the real data in the next step"
if target in html_content:
    new_html = html_content.replace(target, js_content)
    
    # Also add the Study Center logic
    study_logic = """
        // ─── STUDY CENTER ───────────────────────────────────────────────────────────
        function initStudyCenter() {
            const tabs = document.getElementById('study-tabs');
            const content = document.getElementById('study-content');
            
            tabs.innerHTML = '';
            DATA.study_guides.forEach((guide, i) => {
                const btn = document.createElement('button');
                btn.className = 'notes-tab' + (i === 0 ? ' active' : '');
                btn.textContent = guide.title.replace('AWS_CCP_Complete_Guide_', '').replace('.md', '').replace('_', ' ');
                btn.onclick = () => {
                    document.querySelectorAll('#study-tabs .notes-tab').forEach(t => t.classList.remove('active'));
                    btn.classList.add('active');
                    renderGuide(guide.content);
                };
                tabs.appendChild(btn);
            });
            
            if (DATA.study_guides.length > 0) {
                renderGuide(DATA.study_guides[0].content);
            }
        }

        function renderGuide(md) {
            document.getElementById('study-content').innerHTML = marked.parse(md);
            window.scrollTo(0,0);
        }

        // Update AWS_Q initialization
        const AWS_Q = DATA.questions;
    """
    
    # Insert logic before AWS Practice logic or similar
    logic_target = "const AWS_Q = []; // We will populate this from DATA"
    if logic_target in new_html:
        new_html = new_html.replace(logic_target, study_logic)
        
    # Final step: ensure renderAWSQ is called after data is ready
    init_target = "awsFiltered = shuffleArray([...AWS_Q]);"
    new_init = "initStudyCenter();\n        awsFiltered = shuffleArray([...AWS_Q]);"
    if init_target in new_html:
        new_html = new_html.replace(init_target, new_init)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully updated index.html")
else:
    print("Target not found in index.html")
