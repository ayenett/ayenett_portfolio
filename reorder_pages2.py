import re

with open('/Users/kitty/Portfolio/index.html', 'r') as f:
    html = f.read()

# Find the #flipbook content
start_marker = '<div id="flipbook" class="mx-auto">'
end_marker = '                        </div>\n                    </div>\n                </div>\n\n                <!-- STAGE 3'

start_idx = html.find(start_marker) + len(start_marker)
end_idx = html.find(end_marker)

flipbook_html = html[start_idx:end_idx]

# Split pages
pages_raw = re.split(r'(?=[\s]*<!-- (?:PAGE|COVER|BACK COVER))', flipbook_html)
pages_raw = [p for p in pages_raw if p.strip()]

pages_dict = {}
for p in pages_raw:
    match = re.search(r'<!-- (.*?) -->', p)
    if match:
        name = match.group(1).strip()
        pages_dict[name] = p

new_order_keys = [
    'COVER (FRONT)',
    'PAGE 01 / CHAPTER 1 LEFT', # Text
    'PAGE 02 / CHAPTER 1 RIGHT', # Photos
    'PAGE 03 / CHAPTER 2 LEFT',
    'PAGE 04 / CHAPTER 2 RIGHT',
    'PAGE 05 / CHAPTER 3 LEFT',
    'PAGE 06 / CHAPTER 3 RIGHT',
    'PAGE 07 / CHAPTER 4 LEFT',
    'PAGE 08 / CHAPTER 4 RIGHT',
    'PAGE 09 / CHAPTER 5 LEFT',
    'PAGE 10 / CHAPTER 5 RIGHT',
    'PAGE 11 / CHAPTER 6 LEFT',
    'PAGE 12 / CHAPTER 6 RIGHT',
    'PAGE 13 / CHAPTER 7 LEFT',
    'PAGE 14 / CHAPTER 7 RIGHT (Back Inside)',
    'BACK COVER (OUTSIDE)'
]

new_flipbook_html = ""
for i, key in enumerate(new_order_keys):
    if key in pages_dict:
        page_html = pages_dict[key]
        
        # update page number formatting 01 / 14
        content_page_num = i
        if 1 <= i <= 14:
            num_str = f"{content_page_num:02d} / 14"
            page_html = re.sub(r'\d{2} / 14', num_str, page_html)
            
        new_flipbook_html += page_html

html = html[:start_idx] + new_flipbook_html + html[end_idx:]
with open('/Users/kitty/Portfolio/index.html', 'w') as f:
    f.write(html)
