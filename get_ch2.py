import re
with open('/Users/kitty/Portfolio/index.html', 'r') as f:
    html = f.read()

# find Chapter 2 pages
start_comment = '<!-- PAGE 03 / CHAPTER 2 LEFT -->'
end_comment = '<!-- PAGE 05 / CHAPTER 3 LEFT -->'
s = html.find(start_comment)
e = html.find(end_comment)
print(html[s:e])
