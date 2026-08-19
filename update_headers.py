import re

with open('/Users/kitty/Portfolio/index.html', 'r') as f:
    html = f.read()

# Replace ripped note text
html = html.replace('Challenges today,<br>strength tomorrow.', 'Turning obstacles into<br>opportunities.')

# Update Chapter 01
html = html.replace('<span class="text-xs font-bold text-[#A8887F] tracking-[0.15em] mb-4 uppercase">Chapter 01</span>\n                                    <h2 class="font-serif-cormorant text-4xl md:text-5xl text-[#4A3B36] font-bold mb-2">The Beginning</h2>',
'''<div class="inline-block relative mb-4 self-start">
                                        <div class="absolute inset-0 bg-[#E3A99B]/40 -rotate-2 scale-110 shadow-sm mix-blend-multiply"></div>
                                        <span class="text-xs font-bold text-[#6D544B] tracking-[0.15em] relative z-10 px-2 py-1 uppercase">Chapter 01</span>
                                    </div>
                                    <h2 class="font-serif-cormorant text-5xl md:text-6xl text-[#4A3B36] font-bold leading-tight mb-2">The Beginning</h2>''')

# Update Chapter 02
html = html.replace('<span class="text-xs font-bold text-[#A8887F] tracking-[0.15em] mb-4 uppercase">Chapter 02</span>\n                                    <h2 class="font-serif-cormorant text-4xl md:text-5xl text-[#4A3B36] font-bold mb-2">Building Foundations</h2>',
'''<div class="inline-block relative mb-4 self-start">
                                        <div class="absolute inset-0 bg-[#E3A99B]/40 -rotate-2 scale-110 shadow-sm mix-blend-multiply"></div>
                                        <span class="text-xs font-bold text-[#6D544B] tracking-[0.15em] relative z-10 px-2 py-1 uppercase">Chapter 02</span>
                                    </div>
                                    <h2 class="font-serif-cormorant text-5xl md:text-6xl text-[#4A3B36] font-bold leading-tight mb-2">Building Foundations</h2>''')

# Update Chapter 04
html = html.replace('<span class="text-xs font-bold text-[#A8887F] tracking-[0.15em] mb-4 uppercase">Chapter 04</span>\n                                    <h2 class="font-serif-cormorant text-4xl md:text-5xl text-[#4A3B36] font-bold mb-2">Work & Travel USA</h2>',
'''<div class="inline-block relative mb-4 self-start">
                                        <div class="absolute inset-0 bg-[#E3A99B]/40 -rotate-2 scale-110 shadow-sm mix-blend-multiply"></div>
                                        <span class="text-xs font-bold text-[#6D544B] tracking-[0.15em] relative z-10 px-2 py-1 uppercase">Chapter 04</span>
                                    </div>
                                    <h2 class="font-serif-cormorant text-5xl md:text-6xl text-[#4A3B36] font-bold leading-tight mb-2">Work <span class="text-[#C19586]">&</span> Travel USA</h2>''')

# Update Chapter 05
html = html.replace('<span class="text-xs font-bold text-[#A8887F] tracking-[0.15em] mb-4 uppercase">Chapter 05</span>\n                                    <h2 class="font-serif-cormorant text-4xl md:text-5xl text-[#4A3B36] font-bold mb-2">Voluntary Internship</h2>',
'''<div class="inline-block relative mb-4 self-start">
                                        <div class="absolute inset-0 bg-[#E3A99B]/40 -rotate-2 scale-110 shadow-sm mix-blend-multiply"></div>
                                        <span class="text-xs font-bold text-[#6D544B] tracking-[0.15em] relative z-10 px-2 py-1 uppercase">Chapter 05</span>
                                    </div>
                                    <h2 class="font-serif-cormorant text-5xl md:text-6xl text-[#4A3B36] font-bold leading-tight mb-2">Voluntary Internship</h2>''')


with open('/Users/kitty/Portfolio/index.html', 'w') as f:
    f.write(html)
