import re
with open('/Users/kitty/Portfolio/index.html', 'r') as f:
    html = f.read()

start_marker = '<div id="flipbook" class="mx-auto">'
end_marker = '                        </div>\n                    </div>\n                </div>\n\n                <!-- STAGE 3'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)
flipbook_html = html[start_idx:end_idx]

pages_raw = re.split(r'(?=[\s]*<!-- (?:PAGE|COVER|BACK COVER))', flipbook_html)
pages_raw = [p for p in pages_raw if p.strip()]

for i, p in enumerate(pages_raw):
    match = re.search(r'<!-- (.*?) -->', p)
    if match:
        print(f"Index {i}: {match.group(1).strip()}")
