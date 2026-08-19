import sys

with open('/Users/kitty/Portfolio/main.js', 'r') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if "// Stage 2: Scrapbook Timeline Storytelling" in line:
        start_idx = i
    if start_idx != -1 and i > start_idx and "}" in line and i == 199: # Line 200 is index 199
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_js = """        // Stage 2: Interactive Storybook
        const flipbookEl = document.getElementById('flipbook');
        const openBtn = document.getElementById('btn-open');
        const prevBtn = document.getElementById('btn-prev');
        const nextBtn = document.getElementById('btn-next');
        const storybookSection = document.getElementById('storybook-section');
        
        if (flipbookEl && window.St && window.St.PageFlip) {
            
            // Set up scroll trigger to fade in the book when scrolling to the section
            gsap.to(flipbookEl, {
                opacity: 1,
                scrollTrigger: {
                    trigger: storybookSection,
                    start: "top 60%",
                    once: true
                }
            });

            const pageFlip = new St.PageFlip(flipbookEl, {
                width: 500, // base width
                height: 700, // base height
                size: "stretch",
                minWidth: 315,
                maxWidth: 1000,
                minHeight: 420,
                maxHeight: 1350,
                drawShadow: true,
                showCover: true,
                mobileScrollSupport: false,
                maxShadowOpacity: 0.5,
            });

            // Initialize it
            pageFlip.loadFromHTML(document.querySelectorAll('.page'));

            // Open Button
            if(openBtn) {
                openBtn.addEventListener('click', () => {
                    pageFlip.flipNext();
                    openBtn.classList.add('hidden');
                    prevBtn.classList.remove('hidden');
                    nextBtn.classList.remove('hidden');
                });
            }

            if(prevBtn) {
                prevBtn.addEventListener('click', () => {
                    pageFlip.flipPrev();
                });
            }

            if(nextBtn) {
                nextBtn.addEventListener('click', () => {
                    pageFlip.flipNext();
                });
            }

            pageFlip.on('flip', (e) => {
                // If flipping back to cover (page 0), show open button again
                if(e.data === 0) {
                    openBtn.classList.remove('hidden');
                    prevBtn.classList.add('hidden');
                    nextBtn.classList.add('hidden');
                } else {
                    openBtn.classList.add('hidden');
                    prevBtn.classList.remove('hidden');
                    nextBtn.classList.remove('hidden');
                }
            });
        }
"""
    # Create the new content
    lines = lines[:start_idx] + [new_js] + lines[end_idx+1:]
    
    with open('/Users/kitty/Portfolio/main.js', 'w') as f:
        f.writelines(lines)
    print("Successfully replaced JS logic.")
else:
    print(f"Could not find JS block. start={start_idx}, end={end_idx}")
