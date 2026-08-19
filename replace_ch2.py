import re
with open('/Users/kitty/Portfolio/index.html', 'r') as f:
    html = f.read()

start_comment = '<!-- PAGE 03 / CHAPTER 2 LEFT -->'
end_comment = '<!-- PAGE 05 / CHAPTER 3 LEFT -->'
s = html.find(start_comment)
e = html.find(end_comment)

old_content = html[s:e]

new_content = """<!-- PAGE 03 / CHAPTER 2 LEFT -->
                            <div class="book-page bg-[#FDFBF7] relative border-l border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none z-10"></div>
                                <div class="absolute right-0 top-0 bottom-0 w-12 bg-gradient-to-l from-black/10 to-transparent z-20 pointer-events-none"></div>
                                
                                <div class="absolute inset-0 w-full h-full p-0 m-0 z-0">
                                    <img src="assets/Screenshot%202569-07-24%20at%2015.46.26.png" class="w-full h-full object-cover">
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#5C504A] bg-white/80 px-2 py-1 rounded-md tracking-widest z-30 shadow-sm backdrop-blur-sm">03 / 14</div>
                            </div><!-- PAGE 04 / CHAPTER 2 RIGHT -->
                            <div class="book-page bg-[#FDFBF7] relative border-r border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute left-0 top-0 bottom-0 w-12 bg-gradient-to-r from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content p-8 md:p-12 h-full flex flex-col justify-center relative z-10">
                                    <span class="text-xs font-bold text-[#A8887F] tracking-[0.15em] mb-4 uppercase">Chapter 02</span>
                                    <h2 class="font-serif-cormorant text-4xl md:text-5xl text-[#4A3B36] font-bold mb-2">Building Foundations</h2>
                                    <h3 class="text-[10px] md:text-xs font-bold text-[#A8887F]/80 mb-8 tracking-widest uppercase">2023 - Present | University Life</h3>
                                    
                                    <p class="font-handwritten text-xl md:text-2xl text-[#6F5A4B] leading-relaxed mt-4 pr-4">
                                        Stepping into Mae Fah Luang University (Computer Engineering) opened a new world. Coding, problem-solving, and late-night debugging sessions.
                                    </p>
                                    
                                    <div class="mt-10 p-4 border border-[#A8887F]/20 rounded-md bg-white/50 w-[80%] shadow-sm">
                                        <p class="font-sans text-sm md:text-base font-bold text-[#4A3B36] mb-1">GPA 3.21</p>
                                        <p class="font-sans text-xs md:text-sm text-[#A8887F]">Bachelor of Engineering</p>
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">04 / 14</div>
                            </div>"""

new_html = html[:s] + new_content + html[e:]

with open('/Users/kitty/Portfolio/index.html', 'w') as f:
    f.write(new_html)
