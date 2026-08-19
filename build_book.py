import re

with open('/Users/kitty/Portfolio/index.html', 'r') as f:
    html = f.read()

book_html = """
                <!-- STAGE 2: Interactive Storybook -->
                <div id="storybook-section" class="relative w-full min-h-[100vh] bg-[#FDFBF7] flex flex-col items-center justify-center py-24 overflow-hidden font-sans-jakarta">
                    
                    <!-- Background Typography -->
                    <div class="absolute inset-0 z-0 pointer-events-none flex items-center justify-center opacity-5 overflow-hidden">
                        <h1 class="text-[30vw] font-black text-[#5C504A] leading-none tracking-tighter whitespace-nowrap">AYENETT</h1>
                    </div>

                    <!-- Book Container -->
                    <div class="relative z-10 w-full max-w-[1000px] h-[600px] mx-auto md:px-4">
                        
                        <!-- Open Book Button & Controls -->
                        <div id="book-controls" class="absolute -right-8 bottom-4 md:-bottom-12 z-50 flex gap-4 transition-all duration-500">
                            <button id="btn-prev" class="hidden w-12 h-12 bg-white/80 rounded-full shadow-lg flex items-center justify-center text-[#8F7469] hover:bg-white transition-colors">
                                &larr;
                            </button>
                            <button id="btn-open" class="bg-[#E8D7C4] text-[#5C504A] px-8 py-3 rounded-full font-bold shadow-lg border border-[#5C504A]/10 hover:bg-[#DBC3AC] transition-colors flex items-center gap-2 group">
                                Open the Book <span class="group-hover:translate-x-1 transition-transform">&rarr;</span>
                            </button>
                            <button id="btn-next" class="hidden w-12 h-12 bg-white/80 rounded-full shadow-lg flex items-center justify-center text-[#8F7469] hover:bg-white transition-colors">
                                &rarr;
                            </button>
                        </div>

                        <!-- PageFlip Wrapper -->
                        <div id="flipbook" class="w-full h-full shadow-2xl mx-auto opacity-0 transition-opacity duration-1000">
                            
                            <!-- COVER (FRONT) -->
                            <div class="page page-cover bg-[#C5ADA2] rounded-r-xl overflow-hidden relative border-l border-[#A3897C]">
                                <div class="absolute inset-0 opacity-40 bg-[url('https://www.transparenttextures.com/patterns/leather.png')] pointer-events-none"></div>
                                <div class="absolute inset-0 shadow-[inset_-10px_0_20px_rgba(0,0,0,0.1)] pointer-events-none"></div>
                                
                                <div class="relative h-full flex flex-col items-center justify-center p-8">
                                    <div class="border border-[#8F7469]/40 w-full h-full flex flex-col items-center justify-center p-6 text-center">
                                        <h3 class="text-[#6D544B] font-bold tracking-[0.2em] text-xs mb-4">THE STORY OF</h3>
                                        <h1 class="font-sans text-5xl md:text-7xl font-black text-[#5C4239] tracking-tighter mb-8 leading-none">AYENETT</h1>
                                        <span class="text-[#8B6E64] text-2xl mb-8">♥</span>
                                        <div class="w-24 h-[1px] bg-[#8B6E64]/40 mb-8"></div>
                                        <p class="font-handwritten text-2xl text-[#4A3B36] leading-relaxed">A journey of curiosity,<br>growth, and ambition.</p>
                                    </div>
                                </div>
                                <div class="absolute right-0 top-1/2 -translate-y-1/2 w-10 h-16 bg-[#8F7469] rounded-l-lg shadow-lg border border-[#5C4239]/20 flex items-center justify-start pl-2">
                                    <div class="w-4 h-4 rounded-full bg-[#C5ADA2] shadow-inner"></div>
                                </div>
                                <!-- Binder Ring Graphic Overlay (Right Side) -->
                                <div class="absolute -left-1 top-4 bottom-4 w-6 bg-gradient-to-r from-black/20 to-transparent"></div>
                            </div>

                            <!-- INSIDE COVER (LEFT) -->
                            <div class="page bg-[#F0EBE1] border-r border-black/10 relative">
                                <div class="absolute inset-0 opacity-50 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute inset-0 shadow-[inset_-20px_0_30px_rgba(0,0,0,0.05)] pointer-events-none"></div>
                            </div>

                            <!-- PAGE 01 / CHAPTER 1 LEFT -->
                            <div class="page bg-[#FDFBF7] relative border-l border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute right-0 top-0 bottom-0 w-12 bg-gradient-to-l from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content p-8 md:p-12 h-full flex flex-col justify-center relative z-10">
                                    <span class="text-xs font-bold text-[#A8887F] tracking-[0.15em] mb-4 uppercase">Chapter 01</span>
                                    <h2 class="font-serif-cormorant text-4xl md:text-5xl text-[#4A3B36] font-bold mb-2">The Beginning</h2>
                                    <h3 class="text-[10px] md:text-xs font-bold text-[#A8887F]/80 mb-8 tracking-widest uppercase">2017 - 2023 | High School</h3>
                                    
                                    <p class="font-handwritten text-xl md:text-2xl text-[#6F5A4B] leading-relaxed mt-4 pr-4">
                                        I walked into high school with a heart full of curiosity and a mind full of questions. I didn't know where this journey would lead me, but I was ready to embrace every moment.
                                    </p>
                                    <div class="mt-8 text-[#A8887F] text-2xl font-handwritten">♡</div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">01 / 14</div>
                            </div>

                            <!-- PAGE 02 / CHAPTER 1 RIGHT -->
                            <div class="page bg-[#FDFBF7] relative border-r border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute left-0 top-0 bottom-0 w-12 bg-gradient-to-r from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content relative w-full h-full p-8 z-10 overflow-hidden">
                                    <!-- Portrait Photo -->
                                    <div class="absolute top-6 left-4 md:left-8 z-10 rotate-2 shadow-lg">
                                        <div class="absolute -top-3 left-1/2 -translate-x-1/2 -rotate-2 w-16 h-5 bg-white/70 backdrop-blur-sm shadow-sm z-20 mix-blend-multiply"></div>
                                        <img src="assets/IMG_0081.JPG" class="w-[160px] md:w-[220px] h-[220px] md:h-[300px] object-cover p-2 md:p-3 pb-8 md:pb-12 bg-white border border-gray-100">
                                    </div>
                                    
                                    <!-- Highlights Note -->
                                    <div class="absolute top-4 md:top-8 right-2 md:right-6 w-40 md:w-56 p-4 md:p-5 bg-[#F5EEDC] shadow-md -rotate-2 z-20">
                                        <div class="absolute -top-2 right-4 rotate-6 w-12 h-4 bg-white/60 backdrop-blur-sm mix-blend-multiply z-20"></div>
                                        <h4 class="font-handwritten text-xl md:text-2xl text-[#8A5A35] mb-2 border-b border-[#8A5A35]/20 pb-1">Highlights</h4>
                                        <ul class="list-none text-[#5C504A] space-y-2 font-handwritten text-base md:text-xl leading-tight mt-3">
                                            <li class="flex gap-2"><span class="text-[#8A5A35]">*</span> Gifted Program (Science-Math)</li>
                                            <li class="flex gap-2"><span class="text-[#8A5A35]">*</span> Strong foundation in Math & Logic</li>
                                            <li class="flex gap-2"><span class="text-[#8A5A35]">*</span> Active in academic activities</li>
                                        </ul>
                                    </div>
                                    
                                    <!-- Group Photo -->
                                    <div class="absolute bottom-6 md:bottom-10 right-6 md:right-10 z-30 -rotate-3 shadow-lg">
                                        <div class="absolute -top-2 left-4 rotate-12 w-10 md:w-12 h-4 bg-white/60 backdrop-blur-sm mix-blend-multiply z-20"></div>
                                        <img src="assets/IMG_0095.JPG" class="w-[140px] md:w-[180px] h-[90px] md:h-[120px] object-cover p-2 pb-6 md:pb-8 bg-white border border-gray-100">
                                        <p class="absolute bottom-1 w-full text-center font-handwritten text-[10px] md:text-xs text-[#5C504A]">The place where it all began ~ ♡</p>
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">02 / 14</div>
                            </div>

                            <!-- PAGE 03 / CHAPTER 2 LEFT -->
                            <div class="page bg-[#FDFBF7] relative border-l border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute right-0 top-0 bottom-0 w-12 bg-gradient-to-l from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
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
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">03 / 14</div>
                            </div>

                            <!-- PAGE 04 / CHAPTER 2 RIGHT -->
                            <div class="page bg-[#FDFBF7] relative border-r border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute left-0 top-0 bottom-0 w-12 bg-gradient-to-r from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content relative w-full h-full p-8 z-10 overflow-hidden">
                                    <div class="absolute top-8 right-6 md:right-8 z-10 -rotate-2 shadow-lg">
                                        <div class="absolute -top-2 left-1/2 -translate-x-1/2 -rotate-2 w-12 h-4 bg-white/60 backdrop-blur-sm shadow-sm z-20 mix-blend-multiply"></div>
                                        <img src="assets/university-campus.jpg" class="w-[160px] md:w-[220px] h-[110px] md:h-[150px] object-cover p-2 md:p-3 pb-8 md:pb-10 bg-white">
                                    </div>

                                    <div class="absolute top-[160px] md:top-[180px] left-4 md:left-8 w-44 md:w-56 p-4 md:p-5 bg-[#E8F0F5] shadow-md rotate-2 z-20">
                                        <div class="absolute -top-2 left-1/2 -translate-x-1/2 rotate-1 w-10 h-4 bg-white/60 backdrop-blur-sm z-20 mix-blend-multiply"></div>
                                        <h4 class="font-handwritten text-xl md:text-2xl text-[#4A6478] mb-3">What I'm learning</h4>
                                        <ul class="text-[#4A6478] space-y-1 font-handwritten text-base md:text-lg leading-tight">
                                            <li>☑ Data Structures</li>
                                            <li>☑ Database Systems</li>
                                            <li>☑ Software Engineering</li>
                                            <li>☑ HCI & UI/UX</li>
                                        </ul>
                                    </div>

                                    <div class="absolute bottom-8 right-10 md:right-16 z-30 rotate-4 shadow-lg">
                                        <div class="absolute -top-2 left-4 rotate-12 w-12 h-4 bg-white/60 backdrop-blur-sm mix-blend-multiply z-20"></div>
                                        <img src="assets/classroom-photo.jpg" class="w-[140px] md:w-[180px] h-[140px] md:h-[180px] object-cover p-2 md:p-3 pb-6 md:pb-8 bg-white">
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">04 / 14</div>
                            </div>

                            <!-- PAGE 05 / CHAPTER 3 LEFT -->
                            <div class="page bg-[#FDFBF7] relative border-l border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute right-0 top-0 bottom-0 w-12 bg-gradient-to-l from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content p-8 md:p-12 h-full flex flex-col justify-center relative z-10">
                                    <span class="text-xs font-bold text-[#A8887F] tracking-[0.15em] mb-4 uppercase">Chapter 03</span>
                                    <h2 class="font-serif-cormorant text-4xl md:text-5xl text-[#4A3B36] font-bold mb-2">Challenges & Growth</h2>
                                    <h3 class="text-[10px] md:text-xs font-bold text-[#A8887F]/80 mb-8 tracking-widest uppercase">2023 - 2025 | Campus Life</h3>
                                    
                                    <div class="grid grid-cols-2 gap-3 md:gap-4 mt-4 pr-4">
                                        <div class="p-3 bg-white/50 border border-[#A8887F]/20 shadow-sm rounded-sm hover:-translate-y-1 transition-transform">
                                            <h4 class="font-bold text-xs md:text-sm text-[#4A3B36]">📣 Cheerleader</h4>
                                            <p class="text-[#8B6E64] mt-1 font-handwritten text-base md:text-lg leading-tight">Leading with passion & teamwork.</p>
                                        </div>
                                        <div class="p-3 bg-white/50 border border-[#A8887F]/20 shadow-sm rounded-sm hover:-translate-y-1 transition-transform">
                                            <h4 class="font-bold text-xs md:text-sm text-[#4A3B36]">💻 Hackathons</h4>
                                            <p class="text-[#8B6E64] mt-1 font-handwritten text-base md:text-lg leading-tight">Solving problems & building ideas.</p>
                                        </div>
                                        <div class="p-3 bg-white/50 border border-[#A8887F]/20 shadow-sm rounded-sm hover:-translate-y-1 transition-transform">
                                            <h4 class="font-bold text-xs md:text-sm text-[#4A3B36]">👥 Activities</h4>
                                            <p class="text-[#8B6E64] mt-1 font-handwritten text-base md:text-lg leading-tight">Organizing events & memories.</p>
                                        </div>
                                        <div class="p-3 bg-white/50 border border-[#A8887F]/20 shadow-sm rounded-sm hover:-translate-y-1 transition-transform">
                                            <h4 class="font-bold text-xs md:text-sm text-[#4A3B36]">🤝 Volunteer</h4>
                                            <p class="text-[#8B6E64] mt-1 font-handwritten text-base md:text-lg leading-tight">Giving back through actions.</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">05 / 14</div>
                            </div>

                            <!-- PAGE 06 / CHAPTER 3 RIGHT -->
                            <div class="page bg-[#FDFBF7] relative border-r border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute left-0 top-0 bottom-0 w-12 bg-gradient-to-r from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content relative w-full h-full p-8 z-10 flex flex-col items-center justify-center gap-4 md:gap-6">
                                    <div class="relative w-[150px] md:w-[180px] h-[150px] md:h-[180px] -rotate-3 shadow-lg self-start ml-2 md:ml-4">
                                        <div class="absolute -top-2 left-1/2 -translate-x-1/2 rotate-2 w-10 h-4 bg-white/60 backdrop-blur-sm z-20 mix-blend-multiply"></div>
                                        <img src="assets/cheerleader-activity.jpg" class="w-full h-full object-cover p-2 pb-8 bg-white border border-gray-100">
                                    </div>
                                    <div class="relative w-[170px] md:w-[220px] h-[120px] md:h-[150px] rotate-4 shadow-lg self-end mr-2 md:mr-4 -mt-4 md:-mt-8">
                                        <div class="absolute -top-2 left-4 rotate-12 w-12 h-4 bg-white/60 backdrop-blur-sm mix-blend-multiply z-20"></div>
                                        <img src="assets/hackathon.jpg" class="w-full h-full object-cover p-2 pb-8 bg-white border border-gray-100">
                                    </div>
                                    <div class="relative w-[140px] md:w-[170px] h-[140px] md:h-[170px] -rotate-2 shadow-lg self-start ml-8 md:ml-12 -mt-4 md:-mt-6">
                                        <div class="absolute -top-2 right-4 -rotate-6 w-12 h-4 bg-white/60 backdrop-blur-sm mix-blend-multiply z-20"></div>
                                        <img src="assets/volunteer.jpg" class="w-full h-full object-cover p-2 pb-8 bg-white border border-gray-100">
                                        <p class="absolute bottom-1 w-full text-center font-handwritten text-[10px] md:text-xs text-[#5C504A]">Good people & great memories ♡</p>
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">06 / 14</div>
                            </div>

                            <!-- PAGE 07 / CHAPTER 4 LEFT -->
                            <div class="page bg-[#FDFBF7] relative border-l border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute right-0 top-0 bottom-0 w-12 bg-gradient-to-l from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content p-8 md:p-12 h-full flex flex-col justify-center relative z-10">
                                    <span class="text-xs font-bold text-[#A8887F] tracking-[0.15em] mb-4 uppercase">Chapter 04</span>
                                    <h2 class="font-serif-cormorant text-4xl md:text-5xl text-[#4A3B36] font-bold mb-2">Work & Travel USA</h2>
                                    <h3 class="text-[10px] md:text-xs font-bold text-[#A8887F]/80 mb-8 tracking-widest uppercase">May - Aug 2025 | Real World Experience</h3>
                                    
                                    <div class="p-6 bg-[#FDF8F5] shadow-sm border border-[#A8887F]/20 relative">
                                        <div class="absolute -top-3 left-1/2 -translate-x-1/2 w-16 h-4 bg-white/80 rotate-2 z-10 shadow-sm mix-blend-multiply border border-[#A8887F]/10"></div>
                                        <h4 class="font-bold text-[#4A3B36] mb-1">🇺🇸 Sales Associate</h4>
                                        <p class="font-handwritten text-xl text-[#A8887F] mb-4">Summer 2025</p>
                                        <ul class="text-[#5C504A] space-y-2 text-sm font-medium">
                                            <li class="flex items-start gap-2"><span class="text-[#8B6E64] font-bold">»</span> Assisted customers and provided recommendations</li>
                                            <li class="flex items-start gap-2"><span class="text-[#8B6E64] font-bold">»</span> Developed communication & problem-solving skills</li>
                                            <li class="flex items-start gap-2"><span class="text-[#8B6E64] font-bold">»</span> Thrived in a fast-paced, diverse environment</li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">07 / 14</div>
                            </div>

                            <!-- PAGE 08 / CHAPTER 4 RIGHT -->
                            <div class="page bg-[#FDFBF7] relative border-r border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute left-0 top-0 bottom-0 w-12 bg-gradient-to-r from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content relative w-full h-full p-8 z-10 overflow-hidden">
                                    <div class="absolute top-8 left-6 md:left-8 z-10 rotate-3 shadow-lg">
                                        <div class="absolute -top-2 left-4 rotate-12 w-10 md:w-12 h-4 bg-white/60 backdrop-blur-sm mix-blend-multiply z-20"></div>
                                        <img src="assets/usa-city.jpg" class="w-[160px] md:w-[220px] h-[110px] md:h-[150px] object-cover p-2 md:p-3 pb-6 md:pb-8 bg-white border border-gray-100">
                                    </div>
                                    <div class="absolute top-[140px] md:top-[170px] right-6 md:right-8 z-20 -rotate-4 shadow-lg">
                                        <img src="assets/usa-flag.jpg" class="w-[100px] md:w-[130px] h-[80px] md:h-[110px] object-cover p-2 md:p-3 bg-white border border-gray-100">
                                    </div>
                                    <div class="absolute bottom-8 md:bottom-12 left-10 md:left-16 z-30 rotate-2 shadow-lg">
                                        <div class="absolute -top-2 left-1/2 -translate-x-1/2 -rotate-2 w-12 h-4 bg-white/60 backdrop-blur-sm shadow-sm z-20 mix-blend-multiply"></div>
                                        <img src="assets/work-photo.jpg" class="w-[140px] md:w-[170px] h-[140px] md:h-[170px] object-cover p-2 md:p-3 pb-6 md:pb-8 bg-white border border-gray-100">
                                        <p class="absolute bottom-1 w-full text-center font-handwritten text-[10px] md:text-xs text-[#5C504A]">New place, new lessons ✈️</p>
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">08 / 14</div>
                            </div>

                            <!-- PAGE 09 / CHAPTER 5 LEFT -->
                            <div class="page bg-[#FDFBF7] relative border-l border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute right-0 top-0 bottom-0 w-12 bg-gradient-to-l from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content p-8 md:p-12 h-full flex flex-col justify-center relative z-10">
                                    <span class="text-xs font-bold text-[#A8887F] tracking-[0.15em] mb-4 uppercase">Chapter 05</span>
                                    <h2 class="font-serif-cormorant text-4xl md:text-5xl text-[#4A3B36] font-bold mb-2">Voluntary Internship</h2>
                                    <h3 class="text-[10px] md:text-xs font-bold text-[#A8887F]/80 mb-8 tracking-widest uppercase">Jun - Jul 2026 | Self-Driven Growth</h3>
                                    
                                    <div class="p-6 bg-[#F5F8F6] shadow-sm border border-[#A8887F]/20 relative">
                                        <div class="absolute -top-3 left-1/2 -translate-x-1/2 w-16 h-4 bg-[#A8887F]/30 -rotate-2 z-10 mix-blend-multiply"></div>
                                        <h4 class="font-bold text-[#4A3B36] mb-1">💼 Fusion Solution</h4>
                                        <p class="font-handwritten text-xl text-[#A8887F] mb-4">Summer 2026</p>
                                        <ul class="text-[#5C504A] space-y-2 text-sm font-medium">
                                            <li class="flex items-start gap-2"><span class="text-[#8B6E64] font-bold">»</span> Self-driven internship to gain real-world experience</li>
                                            <li class="flex items-start gap-2"><span class="text-[#8B6E64] font-bold">»</span> Collaborated with professional development teams</li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">09 / 14</div>
                            </div>

                            <!-- PAGE 10 / CHAPTER 5 RIGHT -->
                            <div class="page bg-[#FDFBF7] relative border-r border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute left-0 top-0 bottom-0 w-12 bg-gradient-to-r from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content relative w-full h-full p-8 z-10 overflow-hidden">
                                    <div class="absolute top-12 md:top-16 left-8 md:left-10 z-10 -rotate-2 shadow-lg">
                                        <div class="absolute -top-2 left-1/2 -translate-x-1/2 -rotate-2 w-12 h-4 bg-white/60 backdrop-blur-sm shadow-sm z-20 mix-blend-multiply"></div>
                                        <img src="assets/project_1.png" class="w-[180px] md:w-[240px] h-[130px] md:h-[180px] object-cover p-2 md:p-3 pb-6 md:pb-8 bg-white filter sepia border border-gray-100">
                                    </div>
                                    <div class="absolute bottom-12 md:bottom-20 right-8 md:right-10 z-20 rotate-3 shadow-lg">
                                        <div class="absolute -top-2 right-4 -rotate-6 w-12 h-4 bg-white/60 backdrop-blur-sm mix-blend-multiply z-20"></div>
                                        <img src="assets/project_2.png" class="w-[170px] md:w-[220px] h-[120px] md:h-[160px] object-cover p-2 md:p-3 pb-6 md:pb-8 bg-white grayscale border border-gray-100">
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">10 / 14</div>
                            </div>

                            <!-- PAGE 11 / CHAPTER 6 LEFT -->
                            <div class="page bg-[#FDFBF7] relative border-l border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute right-0 top-0 bottom-0 w-12 bg-gradient-to-l from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content p-8 md:p-12 h-full flex flex-col justify-center relative z-10">
                                    <span class="text-xs font-bold text-[#A8887F] tracking-[0.15em] mb-4 uppercase">Chapter 06</span>
                                    <h2 class="font-serif-cormorant text-4xl md:text-5xl text-[#4A3B36] font-bold mb-2">Cooperative Education</h2>
                                    <h3 class="text-[10px] md:text-xs font-bold text-[#A8887F]/80 mb-8 tracking-widest uppercase">Jan - Apr 2027 | University Co-op</h3>
                                    
                                    <div class="p-6 bg-[#FDF8F5] shadow-sm border border-[#A8887F]/20 relative">
                                        <div class="absolute -top-3 right-6 w-16 h-4 bg-white/80 rotate-6 z-10 shadow-sm mix-blend-multiply border border-[#A8887F]/10"></div>
                                        <h4 class="font-bold text-[#4A3B36] mb-1">💼 Fusion Solution</h4>
                                        <p class="font-handwritten text-xl text-[#A8887F] mb-4">Spring 2027</p>
                                        <ul class="text-[#5C504A] space-y-2 text-sm font-medium">
                                            <li class="flex items-start gap-2"><span class="text-[#8B6E64] font-bold">»</span> University co-op program in a professional environment</li>
                                            <li class="flex items-start gap-2"><span class="text-[#8B6E64] font-bold">»</span> Advanced collaboration with development teams</li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">11 / 14</div>
                            </div>

                            <!-- PAGE 12 / CHAPTER 6 RIGHT -->
                            <div class="page bg-[#FDFBF7] relative border-r border-black/5">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute left-0 top-0 bottom-0 w-12 bg-gradient-to-r from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content relative w-full h-full p-8 z-10 overflow-hidden">
                                    <div class="absolute top-10 md:top-16 right-8 md:right-12 z-10 rotate-2 shadow-lg">
                                        <div class="absolute -top-2 left-1/2 -translate-x-1/2 rotate-1 w-10 h-4 bg-white/60 backdrop-blur-sm z-20 mix-blend-multiply"></div>
                                        <img src="assets/classroom-photo.jpg" class="w-[180px] md:w-[230px] h-[130px] md:h-[160px] object-cover p-2 md:p-3 pb-6 md:pb-8 bg-white filter sepia border border-gray-100">
                                    </div>
                                    <div class="absolute bottom-12 md:bottom-16 left-6 md:left-10 z-20 -rotate-3 shadow-lg">
                                        <div class="absolute -top-2 left-4 rotate-12 w-12 h-4 bg-white/60 backdrop-blur-sm mix-blend-multiply z-20"></div>
                                        <img src="assets/high-school-group-photo.jpg" class="w-[180px] md:w-[230px] h-[130px] md:h-[170px] object-cover p-2 md:p-3 pb-6 md:pb-8 bg-white grayscale border border-gray-100">
                                        <p class="absolute bottom-1 w-full text-center font-handwritten text-[10px] md:text-xs text-[#5C504A]">Putting skills to work!</p>
                                    </div>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">12 / 14</div>
                            </div>

                            <!-- PAGE 13 / CHAPTER 7 LEFT -->
                            <div class="page bg-[#FDFBF7] relative border-l border-black/5 flex flex-col items-center justify-center">
                                <div class="absolute inset-0 opacity-30 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute right-0 top-0 bottom-0 w-12 bg-gradient-to-l from-black/10 to-transparent z-0 pointer-events-none"></div>
                                
                                <div class="page-content p-8 md:p-12 h-full flex flex-col justify-center items-center relative z-10 text-center">
                                    <span class="text-xs font-bold text-[#A8887F] tracking-[0.15em] mb-4 uppercase">Chapter 07</span>
                                    <h2 class="font-serif-cormorant text-5xl md:text-6xl text-[#4A3B36] font-bold mb-4">The Future</h2>
                                    <h3 class="font-handwritten text-3xl md:text-4xl text-[#8B6E64] mb-12">Keep Learning.<br>Keep Building.</h3>
                                    
                                    <div class="w-16 h-[1px] bg-[#A8887F]/30 mx-auto mb-10"></div>
                                    
                                    <h2 class="font-serif-cormorant text-xl md:text-2xl text-[#2B211B] leading-relaxed italic text-center px-4 md:px-8">
                                        “I’m still learning.<br>I’m still building.<br>And this is only the beginning.”
                                    </h2>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">13 / 14</div>
                            </div>

                            <!-- PAGE 14 / CHAPTER 7 RIGHT (Back Inside) -->
                            <div class="page bg-[#F0EBE1] border-r border-black/10 relative">
                                <div class="absolute inset-0 opacity-50 bg-[url('https://www.transparenttextures.com/patterns/cream-paper.png')] pointer-events-none"></div>
                                <div class="absolute inset-0 shadow-[inset_20px_0_30px_rgba(0,0,0,0.05)] pointer-events-none"></div>
                                
                                <div class="relative w-full h-full flex items-center justify-center z-10">
                                    <a href="#contact" class="px-8 py-4 border-2 border-[#8B6E64] text-[#8B6E64] font-bold hover:bg-[#8B6E64] hover:text-[#F0EBE1] transition-colors duration-300 rounded-sm uppercase tracking-widest text-sm shadow-sm">
                                        Let's Connect &rarr;
                                    </a>
                                </div>
                                <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold text-[#A8887F]/50 tracking-widest">14 / 14</div>
                            </div>
                            
                            <!-- BACK COVER (OUTSIDE) -->
                            <div class="page page-cover bg-[#C5ADA2] rounded-l-xl overflow-hidden relative border-r border-[#A3897C]">
                                <div class="absolute inset-0 opacity-40 bg-[url('https://www.transparenttextures.com/patterns/leather.png')] pointer-events-none"></div>
                                <div class="absolute inset-0 shadow-[inset_10px_0_20px_rgba(0,0,0,0.1)] pointer-events-none"></div>
                                <div class="absolute left-0 top-1/2 -translate-y-1/2 w-8 h-16 bg-[#8F7469] rounded-r-lg shadow-lg border border-[#5C4239]/20"></div>
                            </div>

                        </div>
                    </div>
                </div>
"""

start_marker = "<!-- STAGE 2: The Scrapbook Storytelling Journey -->"
end_marker = "<!-- STAGE 3: Floating Certifications -->"

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + book_html + "\n                " + html[end_idx:]
    with open('/Users/kitty/Portfolio/index.html', 'w') as f:
        f.write(new_html)
    print("Successfully replaced timeline with book HTML structure.")
else:
    print(f"Could not find markers. start_idx={start_idx}, end_idx={end_idx}")

