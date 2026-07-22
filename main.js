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

        // Stage 2: Fixed Timeline Drawing
        const journeyPath = document.getElementById('journey-path');
        const timelineStage = document.getElementById('timeline-stage');
        
        if (journeyPath && timelineStage) {
            // Function to safely calculate and apply dash array
            const setupPath = () => {
                const pathLength = journeyPath.getTotalLength();
                // Set a massive dash array in CSS just in case, but overwrite it here with the exact length
                journeyPath.style.strokeDasharray = pathLength;
                journeyPath.style.strokeDashoffset = pathLength;
            };
            
            // Wait a tick for SVG to render to get true length
            setTimeout(setupPath, 100);
            window.addEventListener('resize', setupPath);

            gsap.to(journeyPath, {
                strokeDashoffset: 0,
                ease: "none",
                scrollTrigger: {
                    trigger: timelineStage,
                    start: "top 60%", // Start drawing earlier
                    end: "bottom 80%",
                    scrub: 1
                }
            });

            // Milestone Nodes and Cards
            const nodes = document.querySelectorAll('.milestone-node');
            const cards = document.querySelectorAll('.milestone-card');
            
            nodes.forEach((node, i) => {
                const card = cards[i];
                
                // Pop node
                gsap.from(node, {
                    scale: 0,
                    opacity: 0,
                    duration: 0.6,
                    ease: "back.out(2)",
                    scrollTrigger: {
                        trigger: node,
                        start: "top 60%",
                        toggleActions: "play none none reverse"
                    }
                });
                
                // Slide card
                gsap.from(card, {
                    y: 50,
                    opacity: 0,
                    duration: 0.8,
                    ease: "power3.out",
                    scrollTrigger: {
                        trigger: node, // trigger on the node so they sync
                        start: "top 60%",
                        toggleActions: "play none none reverse"
                    }
                });

                // Background Immersive Crossfade
                const bgId = `bg-milestone-${card.dataset.index}`;
                const bgImg = document.getElementById(bgId);
                if (bgImg) {
                    gsap.to(bgImg, {
                        opacity: 0.8, // Fade in the background image
                        scale: 1, // Slight zoom out effect as it appears
                        duration: 1,
                        ease: "power2.out",
                        scrollTrigger: {
                            trigger: node,
                            start: "top 70%",
                            end: "top 10%",
                            toggleActions: "play reverse play reverse"
                        }
                    });
                }

                // Popups Animation
                const popups = card.querySelectorAll('.milestone-popup');
                if (popups.length > 0) {
                    gsap.fromTo(popups, 
                        { scale: 0.5, opacity: 0, y: 40 },
                        {
                            scale: 1,
                            opacity: 1,
                            y: 0,
                            duration: 0.8,
                            stagger: 0.15,
                            ease: "back.out(1.5)",
                            scrollTrigger: {
                                trigger: node,
                                start: "top 70%", // Appear when coming into view
                                end: "top 20%", // Disappear when leaving top
                                toggleActions: "play reverse play reverse"
                            }
                        }
                    );
                }
            });
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
