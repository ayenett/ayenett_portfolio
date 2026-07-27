// Initialize Lenis for Smooth Scrolling
const lenis = new Lenis({
  duration: 1.5, // Slower, more elegant scroll
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  direction: 'vertical',
  gestureDirection: 'vertical',
  smooth: true,
  mouseMultiplier: 1,
  smoothTouch: false,
  touchMultiplier: 2,
  infinite: false,
});

lenis.on('scroll', ScrollTrigger.update);

gsap.ticker.add((time)=>{
  lenis.raf(time * 1000);
});

gsap.ticker.lagSmoothing(0);

document.addEventListener('DOMContentLoaded', () => {
    gsap.registerPlugin(ScrollTrigger);

    // 1. Reveal Animations for all sections
    const revealElements = document.querySelectorAll('.reveal-up');
    revealElements.forEach((el) => {
        gsap.to(el, {
            scrollTrigger: {
                trigger: el,
                start: "top 85%", // Trigger when top of element hits 85% down viewport
                end: "bottom top",
                toggleActions: "play none none reverse"
            },
            y: 0,
            opacity: 1,
            duration: 1,
            ease: "power3.out"
        });
    });

    // 2. Parallax Elements
    const parallaxElements = document.querySelectorAll('[data-parallax]');
    parallaxElements.forEach((el) => {
        const speed = parseFloat(el.getAttribute('data-parallax'));
        gsap.to(el, {
            scrollTrigger: {
                trigger: el,
                start: "top bottom",
                end: "bottom top",
                scrub: true
            },
            y: (i, target) => -ScrollTrigger.maxScroll(window) * speed,
            ease: "none"
        });
    });

    // --- 2. ABOUT JOURNEY (5 Stages) ---
    const aboutJourney = document.getElementById('about-journey');
    
    if (aboutJourney) {
        
        // Stage 1: Pin the giant ABOUT ME text
        const bgText = document.getElementById('about-bg-text');
        if (bgText) {
            gsap.to(bgText, {
                scrollTrigger: {
                    trigger: aboutJourney,
                    start: "top top",
                    end: "bottom top",
                    pin: bgText,
                    pinSpacing: false,
                    scrub: true
                },
                opacity: 0, // slowly fade out as you leave the section
                ease: "power1.inOut"
            });
        }

        const flipbookEl = document.getElementById('flipbook');
        const flipbookWrapper = document.getElementById('flipbook-wrapper');
        const openBtn = document.getElementById('btn-open');
        const prevBtn = document.getElementById('btn-prev');
        const nextBtn = document.getElementById('btn-next');
        const storybookSection = document.getElementById('storybook-section');
        
        console.log("Checking PageFlip:", window.St, window.PageFlip);
        
        if (flipbookEl) {
            if (!window.St || !window.St.PageFlip) {
                alert("PageFlip JS not found! window.St = " + typeof window.St);
                return;
            }
            
            try {
                const pageFlip = new St.PageFlip(flipbookEl, {
                    width: 600, // base width
                    height: 650, // base height
                    size: "stretch",
                    minWidth: 315,
                    maxWidth: 1000,
                    minHeight: 400,
                    maxHeight: 1400,
                    drawShadow: true,
                    showCover: true,
                    mobileScrollSupport: false,
                    maxShadowOpacity: 0.5,
                });

                const pages = Array.from(document.querySelectorAll('.book-page'));
                if (pages.length > 0) {
                    pageFlip.loadFromHTML(pages);
                    
                    // Initialize the closed book position (centered)
                    if (flipbookWrapper) {
                        flipbookWrapper.style.transform = "translateX(-25%)";
                    }
                }

                // Background Music Setup
                const bgMusic = new Audio('assets/santa-s-great-treasure-pecan-pie-main-version-44475-02-12.mp3');
                bgMusic.loop = true;
                bgMusic.volume = 0.5;

                // Sound Effects Setup
                const flipSound = new Audio('assets/freesound_community-small-page-103398.mp3');
                const closeSound = new Audio('assets/oxidvideos-book-closing-466850.mp3');
                flipSound.volume = 0.8;
                closeSound.volume = 1.0;

                // Mute Button Logic
                let isMuted = false;
                const muteBtn = document.getElementById('btn-mute');
                const iconSoundOn = document.getElementById('icon-sound-on');
                const iconSoundOff = document.getElementById('icon-sound-off');
                
                if (muteBtn) {
                    muteBtn.addEventListener('click', () => {
                        isMuted = !isMuted;
                        bgMusic.muted = isMuted;
                        flipSound.muted = isMuted;
                        closeSound.muted = isMuted;
                        
                        if (isMuted) {
                            iconSoundOn.classList.add('hidden');
                            iconSoundOff.classList.remove('hidden');
                        } else {
                            iconSoundOn.classList.remove('hidden');
                            iconSoundOff.classList.add('hidden');
                        }
                    });
                }

                // Open Button
                if(openBtn) {
                    openBtn.addEventListener('click', () => {
                        flipSound.currentTime = 0;
                        flipSound.play().catch(err => console.log(err));
                        bgMusic.play().catch(err => console.log("Audio play blocked by browser:", err));
                        pageFlip.flipNext();
                    });
                }

                if(prevBtn) {
                    prevBtn.addEventListener('click', () => {
                        // If flipping back to cover
                        if (pageFlip.getCurrentPageIndex() <= 2) {
                            closeSound.currentTime = 0;
                            closeSound.play().catch(err => console.log(err));
                        } else {
                            flipSound.currentTime = 0;
                            flipSound.play().catch(err => console.log(err));
                        }
                        pageFlip.flipPrev();
                    });
                }
                
                if(nextBtn) {
                    nextBtn.addEventListener('click', () => {
                        flipSound.currentTime = 0;
                        flipSound.play().catch(err => console.log(err));
                        const totalPages = pageFlip.getPageCount();
                        if (pageFlip.getCurrentPageIndex() >= totalPages - 2) {
                            pageFlip.flip(0);
                        } else {
                            pageFlip.flipNext();
                        }
                    });
                }

                // Handle dragging sound
                pageFlip.on('changeState', (e) => {
                    if (e.data === 'user_fold') {
                        flipSound.currentTime = 0;
                        flipSound.play().catch(err => console.log(err));
                    }
                });

                pageFlip.on('flip', (e) => {
                    // If flipping back to cover (page 0), center the cover and pause music
                    if(e.data === 0) {
                        bgMusic.pause();
                        openBtn.classList.remove('hidden');
                        prevBtn.classList.add('hidden');
                        nextBtn.classList.add('hidden');
                        if (muteBtn) muteBtn.classList.add('hidden');
                        if (flipbookWrapper) flipbookWrapper.style.transform = "translateX(-25%)";
                    } else {
                        // Play music if it was paused and user flips away from cover (and not muted)
                        if (bgMusic.paused && !isMuted) {
                            bgMusic.play().catch(err => console.log("Audio play blocked:", err));
                        }
                        openBtn.classList.add('hidden');
                        if (muteBtn) muteBtn.classList.remove('hidden');
                        
                        const totalPages = pageFlip.getPageCount();
                        // If it's the last page (back cover), hide next button and auto-flip to front after a delay
                        if (e.data >= totalPages - 2) {
                            nextBtn.classList.add('hidden');
                            setTimeout(() => {
                                // Only flip back if we are still on the last page
                                if (pageFlip.getCurrentPageIndex() >= totalPages - 2) {
                                    closeSound.currentTime = 0;
                                    closeSound.play().catch(err => console.log(err));
                                    pageFlip.flip(0);
                                }
                            }, 500); // Reduced delay for faster transition
                        } else {
                            nextBtn.classList.remove('hidden');
                        }
                        
                        prevBtn.classList.remove('hidden');
                        if (flipbookWrapper) flipbookWrapper.style.transform = "translateX(0)";
                    }
                });
            } catch (err) {
                console.error("PAGEFLIP ERROR:", err);
            }
        }

        // Stage 3: Achievement Cards Parallax
        const achievementCards = document.querySelectorAll('.achievement-card');
        achievementCards.forEach((card) => {
            const speed = card.getAttribute('data-speed') || 1;
            gsap.to(card, {
                y: -100 * speed,
                ease: "none",
                scrollTrigger: {
                    trigger: card.parentElement,
                    start: "top bottom",
                    end: "bottom top",
                    scrub: true
                }
            });
        });

        // Stage 4: Statistics Counters
        const counters = document.querySelectorAll('.counter');
        counters.forEach(counter => {
            const target = parseInt(counter.getAttribute('data-target'));
            gsap.to(counter, {
                innerHTML: target,
                duration: 2,
                ease: "power2.out",
                snap: { innerHTML: 1 }, // ensure it's an integer
                scrollTrigger: {
                    trigger: document.getElementById('statistics-stage'),
                    start: "top 80%",
                    toggleActions: "play none none reverse"
                }
            });
        });

        // Stage 5: Capabilities Badges Stagger
        const badges = document.querySelectorAll('.capability-badge');
        gsap.from(badges, {
            y: 30,
            opacity: 0,
            duration: 0.6,
            stagger: 0.1,
            ease: "back.out(1.5)",
            scrollTrigger: {
                trigger: badges[0],
                start: "top 85%",
                toggleActions: "play none none reverse"
            }
        });
    } // <--- Added the missing closing brace here!

    // --- 3. SELECTED WORK (Horizontal Scroll) ---
    const workSection = document.getElementById('work');
    const scrollContainer = document.getElementById('horizontal-scroll-container');
    const horizontalTrack = document.getElementById('horizontal-track');
    
    if (workSection && scrollContainer && horizontalTrack) {
        
        // Calculate the total distance to move
        // It's the full width of the track minus the viewport width
        const getScrollAmount = () => {
            let trackWidth = horizontalTrack.scrollWidth;
            return -(trackWidth - window.innerWidth + (window.innerWidth * 0.1)); // Add a little buffer padding at the end
        };

        // Create the horizontal scroll animation
        const tween = gsap.to(horizontalTrack, {
            x: getScrollAmount,
            ease: "none"
        });

        // Setup the ScrollTrigger to pin and scrub
        ScrollTrigger.create({
            trigger: workSection,
            start: "top top",
            end: () => `+=${getScrollAmount() * -1}`, // The pin duration equals the scroll distance
            pin: true,
            animation: tween,
            scrub: 1, // Smooth scrubbing
            invalidateOnRefresh: true // Recalculate on resize
        });

        // Entrance animation for cards when the section is reached
        const cards = document.querySelectorAll('.horizontal-card');
        gsap.from(cards, {
            y: 100,
            opacity: 0,
            duration: 1,
            stagger: 0.15,
            ease: "power3.out",
            scrollTrigger: {
                trigger: workSection,
                start: "top 70%",
                toggleActions: "play none none reverse"
            }
        });
    }

    // --- 4. Custom Cursor Navigation Links interaction ---
    const links = document.querySelectorAll('a, button, .project-card, .capability-badge, .horizontal-card');
    links.forEach(link => {
        link.addEventListener('mouseenter', () => {
            // Add custom cursor scale logic if needed
        });
        link.addEventListener('mouseleave', () => {
            // Remove custom cursor scale logic if needed
        });
    });
});
