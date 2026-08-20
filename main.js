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

    // Global Work Section Audio Setup ("After Hours - The Weeknd")
    const workAudioEl = document.getElementById('work-audio-element');
    window.workAudio = workAudioEl || new Audio('assets/after_hours_the_weeknd.mp3');
    window.workAudio.preload = 'auto';
    window.workAudio.loop = true;
    window.workAudio.volume = 0.8;
    window.workAudio.load();

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
                        window.workAudio.muted = isMuted;
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

        // Stage 3 & 4: 3D Certificates Carousel Initialization
        initCertificatesCarousel();

        // Stage 5: Capabilities Badges Stagger
        const badges = document.querySelectorAll('.capability-badge');
        if (badges.length > 0) {
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
        }
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

        // Audio playback handlers for Selected Work section
        const playWorkAudio = () => {
            window.isWorkSectionActive = true;
            if (window.workAudio) {
                window.workAudio.volume = 0.8;
                window.workAudio.muted = false;
                if (window.workAudio.paused) {
                    window.workAudio.play().catch(err => console.log("Play waiting for motion:", err));
                }
            }
        };

        const pauseWorkAudio = () => {
            window.isWorkSectionActive = false;
            if (window.workAudio) {
                window.workAudio.pause();
                window.workAudio.currentTime = 0;
            }
        };

        // Resume playing on ANY user motion (scroll, wheel, touch, move) when active
        const triggerAudioOnMotion = () => {
            if (window.isWorkSectionActive && window.workAudio && window.workAudio.paused) {
                window.workAudio.volume = 0.8;
                window.workAudio.muted = false;
                window.workAudio.play().catch(e => {});
            }
        };

        ['scroll', 'wheel', 'touchmove', 'touchstart', 'mousemove', 'pointermove', 'keydown', 'click'].forEach(evt => {
            window.addEventListener(evt, triggerAudioOnMotion, { passive: true });
        });

        // Setup the ScrollTrigger to pin and scrub (Exact original pin parameters)
        ScrollTrigger.create({
            trigger: workSection,
            start: "top top",
            end: () => `+=${getScrollAmount() * -1}`, // The pin duration equals the scroll distance
            pin: true,
            animation: tween,
            scrub: 1, // Smooth scrubbing
            invalidateOnRefresh: true // Recalculate on resize
        });

        // Dedicated Audio Trigger (Starts instantly as section enters 90% down viewport)
        ScrollTrigger.create({
            trigger: workSection,
            start: "top 90%",
            end: () => `+=${getScrollAmount() * -1 + window.innerHeight}`,
            onEnter: playWorkAudio,
            onEnterBack: playWorkAudio,
            onLeave: pauseWorkAudio,
            onLeaveBack: pauseWorkAudio,
            onToggle: (self) => {
                if (self.isActive) {
                    playWorkAudio();
                } else {
                    pauseWorkAudio();
                }
            }
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

// ----------------------------------------------------
// 3D Certificate Carousel & Modals Implementation
// ----------------------------------------------------
function initCertificatesCarousel() {
    const track = document.getElementById('cert-carousel-track');
    const dotsContainer = document.getElementById('cert-dots-container');
    const prevBtn = document.getElementById('cert-prev-btn');
    const nextBtn = document.getElementById('cert-next-btn');
    const wrapper = document.getElementById('cert-carousel-wrapper');

    // Modals
    const viewAllBtn = document.getElementById('btn-view-all-certs');
    const galleryModal = document.getElementById('cert-gallery-modal');
    const galleryBackdrop = document.getElementById('cert-gallery-backdrop');
    const galleryClose = document.getElementById('cert-gallery-close');
    const galleryGrid = document.getElementById('cert-gallery-grid');

    const lightboxModal = document.getElementById('cert-lightbox-modal');
    const lightboxBackdrop = document.getElementById('cert-lightbox-backdrop');
    const lightboxClose = document.getElementById('cert-lightbox-close');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxTitle = document.getElementById('lightbox-title');
    const lightboxCategory = document.getElementById('lightbox-category');
    const lightboxIssuer = document.getElementById('lightbox-issuer');
    const lightboxYear = document.getElementById('lightbox-year');
    const lightboxDesc = document.getElementById('lightbox-desc');
    const lightboxPrev = document.getElementById('lightbox-prev');
    const lightboxNext = document.getElementById('lightbox-next');

    if (!track) return;

    const certificatesData = [
        {
            id: 1,
            title: "Academic Excellence & Engineering Studies",
            issuer: "Mae Fah Luang University",
            year: "2023 - Present",
            category: "Computer Engineering",
            image: "assets/Screenshot%202569-07-24%20at%2015.46.26.png",
            description: "Demonstrated academic excellence in Computer Engineering with strong GPA 3.21, focusing on software architecture, algorithms, and core engineering principles."
        },
        {
            id: 2,
            title: "Webflow Development Certification",
            issuer: "Webflow Academy",
            year: "2023",
            category: "Web Development",
            image: "assets/project_1.png",
            description: "Certification demonstrating mastery in building complex, scalable Webflow architectures, motion design, and responsive layout systems."
        },
        {
            id: 3,
            title: "Frontend Professional Development",
            issuer: "Frontend Academy",
            year: "2021",
            category: "Software Engineering",
            image: "assets/project_2.png",
            description: "Advanced certification covering modern JavaScript, React architecture, state management, and modern CSS layout frameworks."
        },
        {
            id: 4,
            title: "Interactive Media & UI/UX Design",
            issuer: "Mae Fah Luang University",
            year: "2024",
            category: "Design & UX",
            image: "assets/Designer%20(35).png",
            description: "Specialized certification in user experience research, interactive prototyping, and creative design systems for modern web applications."
        }
    ];

    let currentIndex = 0;
    let autoRotateTimer = null;
    let isHovered = false;
    let activeLightboxIndex = 0;

    // Build Cards in DOM
    track.innerHTML = '';
    if (dotsContainer) dotsContainer.innerHTML = '';

    const cardElements = [];

    certificatesData.forEach((cert, i) => {
        // Create Card Element
        const card = document.createElement('div');
        card.className = `cert-card-3d absolute cursor-pointer select-none transition-all duration-600 ease-out`;
        card.setAttribute('data-index', i);

        card.innerHTML = `
            <div class="cert-card-inner group relative w-[300px] sm:w-[380px] md:w-[440px] bg-[#FDFBF7] border border-[#5C504A]/15 rounded-[2rem] p-5 sm:p-7 shadow-2xl transition-all duration-500 ease-out flex flex-col justify-between overflow-hidden">
                <div class="absolute top-0 right-0 w-32 h-32 bg-gradient-to-bl from-[#D6BD9F]/20 via-[#E1C1B6]/10 to-transparent rounded-bl-full pointer-events-none"></div>

                <div class="relative w-full aspect-[4/3] rounded-2xl overflow-hidden bg-[#1A1715] mb-5 border border-[#5C504A]/10 shadow-inner group-hover:shadow-xl transition-all duration-500">
                    <img src="${cert.image}" alt="${cert.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-4">
                        <span class="text-xs font-bold text-white tracking-widest uppercase flex items-center gap-1.5">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                            View Certificate
                        </span>
                    </div>
                </div>

                <div>
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-3 py-1 bg-[#F5EFEB] border border-[#5C504A]/10 rounded-full text-[10px] font-bold text-[#8B6E64] uppercase tracking-widest">${cert.category}</span>
                        <span class="text-[11px] font-bold text-[#A8887F]">${cert.year}</span>
                    </div>
                    <h3 class="text-xl sm:text-2xl font-black text-[#5C504A] leading-tight mb-2 group-hover:text-[#8B6E64] transition-colors duration-300">${cert.title}</h3>
                    <p class="text-[#8E7E73] font-light text-xs sm:text-sm line-clamp-2 leading-relaxed mb-4">${cert.description}</p>
                </div>

                <div class="pt-3 border-t border-[#5C504A]/10 flex items-center justify-between text-xs">
                    <span class="font-bold text-[#5C504A] flex items-center gap-1.5">
                        <span class="text-sm">🏛</span> ${cert.issuer}
                    </span>
                    <span class="text-[10px] font-bold text-[#D6BD9F] tracking-wider uppercase group-hover:translate-x-1 transition-transform">Verify →</span>
                </div>
            </div>
        `;

        card.addEventListener('click', () => {
            if (i === currentIndex) {
                openLightbox(i);
            } else {
                goToSlide(i);
            }
        });

        track.appendChild(card);
        cardElements.push(card);

        // Build Dot Indicator
        if (dotsContainer) {
            const dot = document.createElement('button');
            dot.ariaLabel = `Go to certificate ${i + 1}`;
            dot.className = `transition-all duration-400 ease-out cursor-pointer rounded-full ${
                i === 0 ? 'w-8 h-2.5 bg-[#8B6E64]' : 'w-2.5 h-2.5 bg-[#5C504A]/25 hover:bg-[#5C504A]/50'
            }`;
            dot.addEventListener('click', () => goToSlide(i));
            dotsContainer.appendChild(dot);
        }
    });

    // Build Gallery Grid items
    if (galleryGrid) {
        galleryGrid.innerHTML = '';
        certificatesData.forEach((cert, i) => {
            const gridItem = document.createElement('div');
            gridItem.className = 'group bg-[#FDFBF7] border border-[#5C504A]/15 rounded-2xl p-5 shadow-sm hover:shadow-xl transition-all duration-300 cursor-pointer flex flex-col justify-between';
            gridItem.innerHTML = `
                <div class="relative w-full aspect-[4/3] rounded-xl overflow-hidden bg-[#1A1715] mb-4">
                    <img src="${cert.image}" alt="${cert.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                </div>
                <div>
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-2.5 py-0.5 bg-[#F5EFEB] border border-[#5C504A]/10 rounded-full text-[9px] font-bold text-[#8B6E64] uppercase tracking-widest">${cert.category}</span>
                        <span class="text-[10px] font-bold text-[#A8887F]">${cert.year}</span>
                    </div>
                    <h4 class="text-lg font-bold text-[#5C504A] mb-1 group-hover:text-[#8B6E64] transition-colors">${cert.title}</h4>
                    <p class="text-xs text-[#8E7E73] font-light line-clamp-2 mb-3">${cert.description}</p>
                </div>
                <div class="pt-2 border-t border-[#5C504A]/10 flex items-center justify-between text-[11px] text-[#5C504A] font-bold">
                    <span>${cert.issuer}</span>
                    <span class="text-[#D6BD9F]">View Full →</span>
                </div>
            `;
            gridItem.addEventListener('click', () => {
                closeGallery();
                openLightbox(i);
            });
            galleryGrid.appendChild(gridItem);
        });
    }

    // Render 3D Position
    function updateCarousel() {
        const total = certificatesData.length;
        const isMobile = window.innerWidth < 640;

        cardElements.forEach((card, i) => {
            let diff = i - currentIndex;

            // Normalize for infinite circular loop
            if (diff > total / 2) diff -= total;
            if (diff < -total / 2) diff += total;

            if (diff === 0) {
                // Active Center Card
                card.style.transform = `translateX(0px) translateZ(0px) scale(1) rotateY(0deg)`;
                card.style.opacity = `1`;
                card.style.zIndex = `30`;
                card.style.pointerEvents = `auto`;
                card.style.boxShadow = `0 25px 50px -12px rgba(92, 80, 74, 0.25)`;
            } else if (diff === -1 || (currentIndex === 0 && i === total - 1)) {
                // Left Neighbor Card
                const xOffset = isMobile ? `-45%` : `-56%`;
                const rot = isMobile ? `10deg` : `16deg`;
                card.style.transform = `translateX(${xOffset}) translateZ(-120px) scale(0.85) rotateY(${rot})`;
                card.style.opacity = `0.65`;
                card.style.zIndex = `15`;
                card.style.pointerEvents = `auto`;
                card.style.boxShadow = `0 15px 30px -10px rgba(0, 0, 0, 0.15)`;
            } else if (diff === 1 || (currentIndex === total - 1 && i === 0)) {
                // Right Neighbor Card
                const xOffset = isMobile ? `45%` : `56%`;
                const rot = isMobile ? `-10deg` : `-16deg`;
                card.style.transform = `translateX(${xOffset}) translateZ(-120px) scale(0.85) rotateY(${rot})`;
                card.style.opacity = `0.65`;
                card.style.zIndex = `15`;
                card.style.pointerEvents = `auto`;
                card.style.boxShadow = `0 15px 30px -10px rgba(0, 0, 0, 0.15)`;
            } else {
                // Hidden Back Cards
                card.style.transform = `translateX(0px) translateZ(-250px) scale(0.7) rotateY(0deg)`;
                card.style.opacity = `0`;
                card.style.zIndex = `5`;
                card.style.pointerEvents = `none`;
            }
        });

        // Update Dots
        if (dotsContainer) {
            const dots = dotsContainer.children;
            Array.from(dots).forEach((dot, idx) => {
                if (idx === currentIndex) {
                    dot.className = `w-8 h-2.5 bg-[#8B6E64] rounded-full transition-all duration-400 ease-out cursor-pointer`;
                } else {
                    dot.className = `w-2.5 h-2.5 bg-[#5C504A]/25 hover:bg-[#5C504A]/50 rounded-full transition-all duration-400 ease-out cursor-pointer`;
                }
            });
        }
    }

    function goToSlide(index) {
        currentIndex = (index + certificatesData.length) % certificatesData.length;
        updateCarousel();
        resetAutoRotate();
    }

    function nextSlide() {
        goToSlide(currentIndex + 1);
    }

    function prevSlide() {
        goToSlide(currentIndex - 1);
    }

    // Auto Rotation
    function startAutoRotate() {
        stopAutoRotate();
        autoRotateTimer = setInterval(() => {
            if (!isHovered) {
                nextSlide();
            }
        }, 3500);
    }

    function stopAutoRotate() {
        if (autoRotateTimer) {
            clearInterval(autoRotateTimer);
            autoRotateTimer = null;
        }
    }

    function resetAutoRotate() {
        startAutoRotate();
    }

    // Event Listeners for Nav Buttons
    if (prevBtn) prevBtn.addEventListener('click', prevSlide);
    if (nextBtn) nextBtn.addEventListener('click', nextSlide);

    // Hover Pause
    if (wrapper) {
        wrapper.addEventListener('mouseenter', () => { isHovered = true; });
        wrapper.addEventListener('mouseleave', () => { isHovered = false; });
        wrapper.addEventListener('touchstart', () => { isHovered = true; }, { passive: true });
        wrapper.addEventListener('touchend', () => { isHovered = false; });

        // Touch Swipe
        let startX = 0;
        wrapper.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
        }, { passive: true });

        wrapper.addEventListener('touchend', (e) => {
            const diffX = e.changedTouches[0].clientX - startX;
            if (Math.abs(diffX) > 40) {
                if (diffX < 0) nextSlide();
                else prevSlide();
            }
        });
    }

    // Keyboard Arrow Navigation
    document.addEventListener('keydown', (e) => {
        const rect = wrapper.getBoundingClientRect();
        const isInView = rect.top < window.innerHeight && rect.bottom > 0;
        if (isInView && galleryModal && !galleryModal.classList.contains('opacity-100') && lightboxModal && !lightboxModal.classList.contains('opacity-100')) {
            if (e.key === 'ArrowRight') nextSlide();
            if (e.key === 'ArrowLeft') prevSlide();
        }
        if (e.key === 'Escape') {
            closeGallery();
            closeLightbox();
        }
    });

    // Gallery Modal Functions
    function openGallery() {
        if (!galleryModal) return;
        galleryModal.classList.remove('opacity-0', 'pointer-events-none');
        galleryModal.classList.add('opacity-100');
        const contentWindow = galleryModal.querySelector('.relative');
        if (contentWindow) {
            contentWindow.classList.remove('scale-95');
            contentWindow.classList.add('scale-100');
        }
        stopAutoRotate();
    }

    function closeGallery() {
        if (!galleryModal) return;
        galleryModal.classList.add('opacity-0', 'pointer-events-none');
        galleryModal.classList.remove('opacity-100');
        const contentWindow = galleryModal.querySelector('.relative');
        if (contentWindow) {
            contentWindow.classList.add('scale-95');
            contentWindow.classList.remove('scale-100');
        }
        startAutoRotate();
    }

    if (viewAllBtn) viewAllBtn.addEventListener('click', openGallery);
    if (galleryClose) galleryClose.addEventListener('click', closeGallery);
    if (galleryBackdrop) galleryBackdrop.addEventListener('click', closeGallery);

    // Lightbox Modal Functions
    function openLightbox(index) {
        if (!lightboxModal) return;
        activeLightboxIndex = index;
        const cert = certificatesData[index];

        if (lightboxImg) lightboxImg.src = cert.image;
        if (lightboxTitle) lightboxTitle.textContent = cert.title;
        if (lightboxCategory) lightboxCategory.textContent = cert.category;
        if (lightboxIssuer) lightboxIssuer.textContent = cert.issuer;
        if (lightboxYear) lightboxYear.textContent = cert.year;
        if (lightboxDesc) lightboxDesc.textContent = cert.description;

        lightboxModal.classList.remove('opacity-0', 'pointer-events-none');
        lightboxModal.classList.add('opacity-100');
        const contentWindow = lightboxModal.querySelector('.relative');
        if (contentWindow) {
            contentWindow.classList.remove('scale-95');
            contentWindow.classList.add('scale-100');
        }
        stopAutoRotate();
    }

    function closeLightbox() {
        if (!lightboxModal) return;
        lightboxModal.classList.add('opacity-0', 'pointer-events-none');
        lightboxModal.classList.remove('opacity-100');
        const contentWindow = lightboxModal.querySelector('.relative');
        if (contentWindow) {
            contentWindow.classList.add('scale-95');
            contentWindow.classList.remove('scale-100');
        }
        startAutoRotate();
    }

    if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
    if (lightboxBackdrop) lightboxBackdrop.addEventListener('click', closeLightbox);
    if (lightboxPrev) lightboxPrev.addEventListener('click', () => {
        openLightbox((activeLightboxIndex - 1 + certificatesData.length) % certificatesData.length);
    });
    if (lightboxNext) lightboxNext.addEventListener('click', () => {
        openLightbox((activeLightboxIndex + 1) % certificatesData.length);
    });

    // Resize Handler
    window.addEventListener('resize', updateCarousel);

    // Initial setup
    updateCarousel();
    startAutoRotate();
}

