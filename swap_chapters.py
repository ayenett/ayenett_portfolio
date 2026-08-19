import re

with open('/Users/kitty/Portfolio/index.html', 'r') as f:
    content = f.read()

# The chapters are separated by the divider:
# <div class="w-full h-[1px] bg-gradient-to-r from-transparent via-[#8A5A35]/10 to-transparent my-24"></div>
divider = '<div class="w-full h-[1px] bg-gradient-to-r from-transparent via-[#8A5A35]/10 to-transparent my-24"></div>'

# Let's split the content around the sections.
# We know they start after <!-- Chapter 03 --> ... divider
parts = content.split(divider)

# parts contains sections. Let's find the indices by checking keywords
internship_idx = -1
work_idx = -1

for i, part in enumerate(parts):
    if "<!-- Chapter 04: Internship -->" in part:
        internship_idx = i
    if "<!-- Chapter 05 -->" in part and "Work & Travel USA" in part:
        work_idx = i

if internship_idx != -1 and work_idx != -1:
    # Swap them
    parts[internship_idx], parts[work_idx] = parts[work_idx], parts[internship_idx]
    
    # Update badges and years inside them
    # Now parts[internship_idx] is Work & Travel (should be Chapter 04)
    # parts[work_idx] is Internship (should be Chapter 05)
    
    # Work and travel update
    parts[internship_idx] = parts[internship_idx].replace("<!-- Chapter 05 -->", "<!-- Chapter 04 -->")
    parts[internship_idx] = parts[internship_idx].replace("CHAPTER 05", "CHAPTER 04")
    
    # Internship update
    parts[work_idx] = parts[work_idx].replace("<!-- Chapter 04: Internship -->", "<!-- Chapter 05: Internship -->")
    parts[work_idx] = parts[work_idx].replace("CHAPTER 04", "CHAPTER 05")
    parts[work_idx] = parts[work_idx].replace("Jun – Jul 2024", "Jun – Jul 2026")
    parts[work_idx] = parts[work_idx].replace("Summer 2024", "Summer 2026")
    
    new_content = divider.join(parts)
    with open('/Users/kitty/Portfolio/index.html', 'w') as f:
        f.write(new_content)
    print("Successfully swapped and updated chapters")
else:
    print(f"Failed to find chapters. internship_idx={internship_idx}, work_idx={work_idx}")

