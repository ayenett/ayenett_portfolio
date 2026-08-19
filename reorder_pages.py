import re

with open('/Users/kitty/Portfolio/index.html', 'r') as f:
    html = f.read()

# Find the #flipbook content
start_marker = '<div id="flipbook" class="mx-auto">'
end_marker = '                        </div>\n                    </div>\n                </div>\n\n                <!-- STAGE 3'

start_idx = html.find(start_marker) + len(start_marker)
end_idx = html.find(end_marker)

flipbook_html = html[start_idx:end_idx]

# Split pages by looking for <!-- PAGE or <!-- COVER or <!-- BACK COVER
# We can use a regex to split it into a list of pages.
# We will match the comments and the div following it.
pages_raw = re.split(r'(?=[\s]*<!-- (?:PAGE|COVER|BACK COVER))', flipbook_html)
# Remove empty strings
pages_raw = [p for p in pages_raw if p.strip()]

# Let's map them by their original comment names
pages_dict = {}
for p in pages_raw:
    match = re.search(r'<!-- (.*?) -->', p)
    if match:
        name = match.group(1).strip()
        pages_dict[name] = p
    else:
        print("Could not find name for:\n", p[:100])

print("Found pages:")
for k in pages_dict.keys():
    print(k)

# We want this order:
new_order_keys = [
    'COVER (FRONT)',
    'PAGE 02 / CHAPTER 1 RIGHT',
    'PAGE 01 / CHAPTER 1 LEFT',
    'PAGE 04 / CHAPTER 2 RIGHT',
    'PAGE 03 / CHAPTER 2 LEFT',
    'PAGE 06 / CHAPTER 3 RIGHT',
    'PAGE 05 / CHAPTER 3 LEFT',
    'PAGE 08 / CHAPTER 4 RIGHT',
    'PAGE 07 / CHAPTER 4 LEFT',
    'PAGE 10 / CHAPTER 5 RIGHT',
    'PAGE 09 / CHAPTER 5 LEFT',
    'PAGE 12 / CHAPTER 6 RIGHT',
    'PAGE 11 / CHAPTER 6 LEFT',
    'PAGE 13 / CHAPTER 7 LEFT',
    'PAGE 14 / CHAPTER 7 RIGHT (Back Inside)',
    'BACK COVER (OUTSIDE)'
]

new_flipbook_html = ""
for i, key in enumerate(new_order_keys):
    if key in pages_dict:
        # Update the comment and the page number at the bottom if it exists
        page_html = pages_dict[key]
        
        # Replace the page number at the bottom (e.g. 01 / 14 -> 01 / 14)
        # Wait, the total content pages is 14. 
        # Left page is even index (1, 3, 5...), Right page is odd index (2, 4, 6...)
        # Wait, new index in the book:
        # Cover is page 0 (in PageFlip)
        # Let's just update the 01 / 14 text to reflect the content page number.
        # The content pages are index 1 to 14.
        
        content_page_num = i
        if 1 <= i <= 14:
            # Format as 01 / 14
            num_str = f"{content_page_num:02d} / 14"
            page_html = re.sub(r'\d{2} / 14', num_str, page_html)
            
        new_flipbook_html += page_html
    else:
        print(f"MISSING PAGE: {key}")

if len(new_order_keys) == 16:
    new_html = html[:start_idx] + new_flipbook_html + html[end_idx:]
    with open('/Users/kitty/Portfolio/index.html', 'w') as f:
        f.write(new_html)
    print("Successfully reordered pages and saved index.html")
else:
    print("Error in page count")

