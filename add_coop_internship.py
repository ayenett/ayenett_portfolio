import re

with open('/Users/kitty/Portfolio/index.html', 'r') as f:
    content = f.read()

divider = '<div class="w-full h-[1px] bg-gradient-to-r from-transparent via-[#8A5A35]/10 to-transparent my-24"></div>'
parts = content.split(divider)

internship_idx = -1
future_idx = -1

for i, part in enumerate(parts):
    if "<!-- Chapter 05: Internship -->" in part:
        internship_idx = i
    if "<!-- Chapter 06 -->" in part and "The Future" in part:
        future_idx = i

if internship_idx != -1 and future_idx != -1:
    # 1. Update Chapter 05 (Voluntary Internship)
    parts[internship_idx] = parts[internship_idx].replace('<h3 class="font-serif-cormorant italic text-3xl text-[#6F5A4B] mb-8">Internship</h3>',
        '<h3 class="font-serif-cormorant italic text-3xl text-[#6F5A4B] mb-8">Voluntary Internship</h3>')
    
    parts[internship_idx] = parts[internship_idx].replace('<span class="text-[#8A5A35] mt-0.5">✔</span> Gained hands-on industry experience', 
        '<span class="text-[#8A5A35] mt-0.5">✔</span> Self-driven internship to gain real-world experience')

    # 2. Create Chapter 06 (Co-op Internship)
    new_chapter = parts[internship_idx].replace("<!-- Chapter 05: Internship -->", "<!-- Chapter 06: Co-op Internship -->")
    new_chapter = new_chapter.replace("CHAPTER 05", "CHAPTER 06")
    new_chapter = new_chapter.replace("Jun – Jul 2026", "Jan – Apr 2027")
    new_chapter = new_chapter.replace("Voluntary Internship", "Cooperative Education")
    new_chapter = new_chapter.replace("Summer 2026", "Spring 2027")
    new_chapter = new_chapter.replace("Self-driven internship to gain real-world experience", "University co-op program to apply academic knowledge in a professional environment")
    
    # Let's change the images for Chapter 06 so it doesn't look identical
    # Currently it uses project_1.png and project_2.png
    new_chapter = new_chapter.replace('assets/project_1.png', 'assets/classroom-photo.jpg')
    new_chapter = new_chapter.replace('assets/project_2.png', 'assets/high-school-group-photo.jpg')
    
    # 3. Update The Future to Chapter 07
    parts[future_idx] = parts[future_idx].replace("<!-- Chapter 06 -->", "<!-- Chapter 07 -->")
    parts[future_idx] = parts[future_idx].replace("CHAPTER 06", "CHAPTER 07")
    
    # Insert new chapter before future_idx
    parts.insert(future_idx, new_chapter)
    
    new_content = divider.join(parts)
    with open('/Users/kitty/Portfolio/index.html', 'w') as f:
        f.write(new_content)
    print("Successfully added Co-op internship and updated chapters")
else:
    print(f"Failed to find chapters. internship_idx={internship_idx}, future_idx={future_idx}")

