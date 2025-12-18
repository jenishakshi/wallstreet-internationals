import re

# Fix services.html
with open('d:/Anitha/github/website/services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove lone emoji lines that are outside divs
content = re.sub(r'\s+[🏢🌿🧹🛡️🐛🌳⚡🔧❄️🎨🚪🔨]\s*\n', '\n', content)

# Write back
with open('d:/Anitha/github/website/services.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Fix index.html  
with open('d:/Anitha/github/website/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove lone emoji lines
content = re.sub(r'\s+[🏢🌿🧹🛡️🐛🔧]\s*</div>', '</div>', content)

# Write back
with open('d:/Anitha/github/website/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully removed all emoji icons!")
