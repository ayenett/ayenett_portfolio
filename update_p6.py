import re

with open('/Users/kitty/Portfolio/index.html', 'r') as f:
    html = f.read()

s_comment = '<!-- PAGE 06 / CHAPTER 3 RIGHT -->'
e_comment = '<!-- PAGE 07 / CHAPTER 4 LEFT -->'
s_idx = html.find(s_comment)
e_idx = html.find(e_comment)

new_content = """<!-- PAGE 06 / CHAPTER 3 RIGHT -->
                            <div class="book-page bg-[#FDFBF7] relative border-r border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none z-0"></div>
                                <div class="absolute left-0 top-0 bottom-0 w-12 bg-gradient-to-r from-black/10 to-transparent z-10 pointer-events-none"></div>
                                
                                <div class="page-content relative w-full h-full z-20">
                                    <!-- Decorations -->
                                    <svg class="absolute top-[35%] right-[20%] w-10 h-10 text-[#D4B58A] opacity-40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                        <path d="M12 2l3 6 6 1-4 4 1 6-6-3-6 3 1-6-4-4 6-1z"></path>
                                    </svg>
                                    <svg class="absolute top-[40%] right-[30%] w-12 h-12 text-[#C19586] opacity-30 rotate-[30deg]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M5 9c0-3 3-5 5-5s5 2 5 5-3 5-5 5-5-2-5-5z"></path>
                                        <path d="M10 14v6l3-3m-3 3l-3-3"></path>
                                    </svg>

                                    <!-- Top Left Polaroid (IMG_0103) -->
                                    <div class="absolute top-6 left-6 w-[170px] md:w-[210px] -rotate-2 shadow-lg bg-white p-2 pb-8 border border-gray-100 z-10">
                                        <div class="absolute -top-2 left-1/2 -translate-x-1/2 rotate-1 w-8 h-4 bg-white/70 backdrop-blur-sm z-20 mix-blend-multiply border border-black/5"></div>
                                        <img src="assets/IMG_0103.jpg" class="w-full aspect-square object-cover">
                                        <p class="absolute bottom-2 w-full text-center font-handwritten text-sm text-[#5C504A]">Team spirit ♡</p>
                                    </div>

                                    <!-- Top Right Polaroid (IMG_0100) -->
                                    <div class="absolute top-10 right-6 w-[160px] md:w-[200px] rotate-3 shadow-lg bg-white p-2 pb-12 border border-gray-100 z-20">
                                        <div class="absolute -top-2 left-4 -rotate-3 w-8 h-4 bg-white/70 backdrop-blur-sm z-20 mix-blend-multiply border border-black/5"></div>
                                        <img src="assets/IMG_0100.JPG" class="w-full aspect-square object-cover">
                                        <p class="absolute bottom-2 w-full text-center font-handwritten text-sm text-[#5C504A] leading-tight px-1">Every experience<br>shapes who I am. ♡</p>
                                    </div>

                                    <!-- Center Pink Sticky Note (HR Friendly text) -->
                                    <div class="absolute top-[220px] md:top-[260px] left-10 md:left-14 w-[160px] md:w-[210px] p-4 bg-[#EBD8D1] shadow-md -rotate-3 z-30">
                                        <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-3 h-3 rounded-full bg-[#B38779] shadow-md border-2 border-white/50"></div>
                                        <p class="font-handwritten text-sm md:text-lg text-[#6D544B] text-center leading-tight">Driven by passion,<br>fueled by challenges,<br>and always eager<br>to learn. <span class="text-[#C19586]">♡</span></p>
                                    </div>

                                    <!-- Bottom Right Polaroid (IMG_0082 - Uniform) -->
                                    <div class="absolute bottom-20 right-6 w-[150px] md:w-[180px] -rotate-3 shadow-lg bg-white p-2 pb-8 border border-gray-100 z-10">
                                        <img src="assets/IMG_0082.JPG" class="w-full aspect-square object-cover">
                                        <p class="absolute bottom-2 w-full text-center font-handwritten text-sm text-[#5C504A]">Good memories ♡</p>
                                    </div>

                                    <!-- Bottom Right Overlapping Polaroid (IMG_0086 - Green Shirt) -->
                                    <div class="absolute bottom-8 right-24 md:right-32 w-[160px] md:w-[190px] rotate-2 shadow-lg bg-white p-2 pb-10 border border-gray-100 z-20">
                                        <img src="assets/IMG_0086.JPG" class="w-full aspect-square object-cover">
                                        <p class="absolute bottom-2 w-full text-center font-handwritten text-sm text-[#5C504A] leading-tight px-1">Keep trying.<br>Keep growing. ♡</p>
                                    </div>

                                    <!-- Bottom Left Ripped Note -->
                                    <div class="absolute bottom-6 left-6 w-[150px] md:w-[180px] p-3 bg-[#E3CBB3]/50 shadow-sm border border-[#D4B58A]/30 z-30 -rotate-2" style="clip-path: polygon(0% 2%, 98% 0%, 100% 98%, 2% 100%);">
                                        <div class="absolute -top-2 left-4 rotate-12 w-8 h-4 bg-white/60 backdrop-blur-sm z-20 mix-blend-multiply"></div>
                                        <p class="font-handwritten text-sm md:text-base text-[#5C4239] text-center leading-tight">Challenges today,<br>strength tomorrow. <span class="text-[#C19586]">♡</span></p>
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest z-30">06 / 14</div>
                            </div>"""

new_html = html[:s_idx] + new_content + html[e_idx:]
with open('/Users/kitty/Portfolio/index.html', 'w') as f:
    f.write(new_html)
