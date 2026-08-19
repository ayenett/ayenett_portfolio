import re

with open('/Users/kitty/Portfolio/index.html', 'r') as f:
    html = f.read()

s_comment = '<!-- PAGE 05 / CHAPTER 3 LEFT -->'
e_comment = '<!-- PAGE 07 / CHAPTER 4 LEFT -->'

s_idx = html.find(s_comment)
e_idx = html.find(e_comment)

new_content = """<!-- PAGE 05 / CHAPTER 3 LEFT -->
                            <div class="book-page bg-[#FDFBF7] relative border-l border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none z-0"></div>
                                <div class="absolute right-0 top-0 bottom-0 w-12 bg-gradient-to-l from-black/10 to-transparent z-10 pointer-events-none"></div>
                                
                                <div class="page-content p-8 md:p-10 h-full flex flex-col relative z-20">
                                    <div class="inline-block relative mb-4 self-start">
                                        <div class="absolute inset-0 bg-[#E3A99B]/40 -rotate-2 scale-110 shadow-sm mix-blend-multiply"></div>
                                        <span class="text-xs font-bold text-[#6D544B] tracking-[0.15em] relative z-10 px-2 py-1 uppercase">Chapter 03</span>
                                    </div>
                                    <h2 class="font-serif-cormorant text-5xl md:text-6xl text-[#4A3B36] font-bold leading-tight mb-2">Challenges <br> <span class="text-[#C19586]">&</span> Growth</h2>
                                    <h3 class="text-[10px] md:text-xs font-bold text-[#A8887F]/80 mb-6 tracking-widest uppercase">2023 - 2025 | CAMPUS LIFE</h3>
                                    
                                    <p class="font-sans text-sm md:text-[15px] text-[#4A3B36] leading-relaxed w-[90%] font-medium">
                                        Every challenge pushed me to grow stronger.<br>
                                        I stepped out of my comfort zone,<br>
                                        discovered my passion for teaching and leadership,<br>
                                        and learned that growth happens in action,<br>
                                        not in hesitation.
                                    </p>
                                    
                                    <div class="grid grid-cols-2 gap-3 mt-6 w-[95%] relative z-10">
                                        <div class="bg-white p-3 shadow-sm border border-black/5 relative">
                                            <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-8 h-3 bg-[#E3A99B]/30 rotate-3 mix-blend-multiply"></div>
                                            <h4 class="font-bold text-[11px] md:text-xs text-[#4A3B36] mb-1 flex items-center gap-1">📣 Cheerleader</h4>
                                            <p class="text-[#8B6E64] font-handwritten text-base leading-tight">Leading with passion & teamwork.</p>
                                            <div class="absolute bottom-1 right-2 text-[#C19586] text-[10px]">♡</div>
                                        </div>
                                        <div class="bg-white p-3 shadow-sm border border-black/5 relative">
                                            <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-8 h-3 bg-[#D4B58A]/30 -rotate-2 mix-blend-multiply"></div>
                                            <h4 class="font-bold text-[11px] md:text-xs text-[#4A3B36] mb-1 flex items-center gap-1">💻 Hackathons</h4>
                                            <p class="text-[#8B6E64] font-handwritten text-base leading-tight">Solving problems & building ideas.</p>
                                            <div class="absolute bottom-1 right-2 text-[#C19586] text-[10px]">♡</div>
                                        </div>
                                        <div class="bg-white p-3 shadow-sm border border-black/5 relative">
                                            <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-8 h-3 bg-blue-200/40 rotate-1 mix-blend-multiply"></div>
                                            <h4 class="font-bold text-[11px] md:text-xs text-[#4A3B36] mb-1 flex items-center gap-1">👥 Activities</h4>
                                            <p class="text-[#8B6E64] font-handwritten text-base leading-tight">Organizing events & memories.</p>
                                            <div class="absolute bottom-1 right-2 text-[#C19586] text-[10px]">♡</div>
                                        </div>
                                        <div class="bg-white p-3 shadow-sm border border-black/5 relative">
                                            <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-8 h-3 bg-red-200/30 -rotate-3 mix-blend-multiply"></div>
                                            <h4 class="font-bold text-[11px] md:text-xs text-[#4A3B36] mb-1 flex items-center gap-1">🤝 Volunteer</h4>
                                            <p class="text-[#8B6E64] font-handwritten text-base leading-tight">Giving back through actions.</p>
                                            <div class="absolute bottom-1 right-2 text-[#C19586] text-[10px]">♡</div>
                                        </div>
                                    </div>

                                    <div class="absolute bottom-8 left-6 bg-[#E3A99B]/40 p-4 w-[200px] -rotate-2 z-20 shadow-sm border border-[#E3A99B]/30" style="clip-path: polygon(0% 2%, 100% 0%, 98% 98%, 2% 100%);">
                                        <svg class="absolute -top-4 left-4 w-5 h-10 text-[#B38779] drop-shadow-sm -rotate-12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                          <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                                          <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                                        </svg>
                                        <p class="font-handwritten text-[13px] text-[#5C4239] leading-tight ml-2 mt-1">
                                            Growth is not about becoming someone new, but becoming a better version of myself. <span class="text-[#C19586]">♡</span>
                                        </p>
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest z-30">05 / 14</div>
                            </div><!-- PAGE 06 / CHAPTER 3 RIGHT -->
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
                                    <div class="absolute top-6 left-6 w-[150px] -rotate-2 shadow-lg bg-white p-2 pb-6 border border-gray-100 z-10">
                                        <div class="absolute -top-2 left-1/2 -translate-x-1/2 rotate-1 w-8 h-4 bg-white/70 backdrop-blur-sm z-20 mix-blend-multiply border border-black/5"></div>
                                        <img src="assets/IMG_0103.jpg" class="w-full aspect-square object-cover">
                                        <p class="absolute bottom-1 w-full text-center font-handwritten text-[10px] text-[#5C504A]">Team spirit ♡</p>
                                    </div>

                                    <!-- Top Right Polaroid (IMG_0100) -->
                                    <div class="absolute top-10 right-6 w-[140px] rotate-3 shadow-lg bg-white p-2 pb-8 border border-gray-100 z-20">
                                        <div class="absolute -top-2 left-4 -rotate-3 w-8 h-4 bg-white/70 backdrop-blur-sm z-20 mix-blend-multiply border border-black/5"></div>
                                        <img src="assets/IMG_0100.JPG" class="w-full aspect-square object-cover">
                                        <p class="absolute bottom-1 w-full text-center font-handwritten text-[10px] text-[#5C504A] leading-tight px-1">Every experience<br>shapes who I am. ♡</p>
                                    </div>

                                    <!-- Center Pink Sticky Note -->
                                    <div class="absolute top-[180px] left-14 w-[130px] p-3 bg-[#EBD8D1] shadow-md -rotate-6 z-30">
                                        <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-3 h-3 rounded-full bg-[#B38779] shadow-md border-2 border-white/50"></div>
                                        <p class="font-handwritten text-xs text-[#6D544B] text-center leading-tight">Stepping out<br>of my comfort zone<br>was the best decision<br>I ever made. <span class="text-[#C19586]">♡</span></p>
                                    </div>

                                    <!-- Bottom Left Polaroid (IMG_0086) -->
                                    <div class="absolute bottom-16 left-8 w-[140px] rotate-2 shadow-lg bg-white p-2 pb-8 border border-gray-100 z-10">
                                        <img src="assets/IMG_0086.JPG" class="w-full aspect-square object-cover">
                                        <p class="absolute bottom-1 w-full text-center font-handwritten text-[10px] text-[#5C504A] leading-tight px-1">Keep trying.<br>Keep growing. ♡</p>
                                    </div>

                                    <!-- Bottom Right Polaroid (IMG_0082) -->
                                    <div class="absolute bottom-20 right-8 w-[130px] -rotate-3 shadow-lg bg-white p-2 pb-6 border border-gray-100 z-20">
                                        <img src="assets/IMG_0082.JPG" class="w-full aspect-square object-cover">
                                        <p class="absolute bottom-1 w-full text-center font-handwritten text-[10px] text-[#5C504A]">Good memories ♡</p>
                                    </div>

                                    <!-- Bottom Right Ripped Note -->
                                    <div class="absolute bottom-6 right-6 w-[140px] p-2 bg-[#E3CBB3]/50 shadow-sm border border-[#D4B58A]/30 z-30 rotate-2" style="clip-path: polygon(2% 0%, 98% 2%, 100% 98%, 0% 100%);">
                                        <div class="absolute -top-2 left-4 rotate-12 w-8 h-4 bg-white/60 backdrop-blur-sm z-20 mix-blend-multiply"></div>
                                        <p class="font-handwritten text-[11px] text-[#5C4239] text-center leading-tight">Challenges today,<br>strength tomorrow. <span class="text-[#C19586]">♡</span></p>
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest z-30">06 / 14</div>
                            </div>"""

new_html = html[:s_idx] + new_content + html[e_idx:]
with open('/Users/kitty/Portfolio/index.html', 'w') as f:
    f.write(new_html)
