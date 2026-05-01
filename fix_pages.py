import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove the literal {: #id } and insert <span id="..."></span> right before the header
    def replace_header(match):
        header_text = match.group(1).strip()
        id_str = match.group(2)
        return f"<span class='anchor' id='{id_str}'></span>\n# {header_text}"
        
    content = re.sub(r'^#\s+(.+?)\s*\{\:\s*#([a-zA-Z0-9-]+)\s*\}$', replace_header, content, flags=re.MULTILINE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_file('_pages/about.md')
fix_file('_pages/about-zh.md')

# Fix head.html to remove <base target="_blank"> as it forces all links to a new page
with open('_includes/head.html', 'r', encoding='utf-8') as f:
    head_content = f.read()

head_content = head_content.replace('<head>\n  <base target="_blank">\n</head>', '')
with open('_includes/head.html', 'w', encoding='utf-8') as f:
    f.write(head_content)

print("Fixes applied successfully!")
