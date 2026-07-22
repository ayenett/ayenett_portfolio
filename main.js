// Initialize Lenis
const lenis = new Lenis({
  duration: 1.5,
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

    // 1. Custom Cursor Logic
    const cursorDot = document.querySelector('.cursor-dot');
    const cursorOutline = document.querySelector('.cursor-outline');
    const cursorText = document.querySelector('.cursor-text');
    
    // Track mouse position
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let outlineX = mouseX;
    let outlineY = mouseY;
    
    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        
        // Immediate update for dot
        gsap.to(cursorDot, {
            x: mouseX,
            y: mouseY,
            duration: 0.1,
            ease: "power2.out"
        });
    });

    // Lerp animation for outline
    gsap.ticker.add(() => {
        const dt = 1.0 - Math.pow(1.0 - 0.15, gsap.ticker.deltaRatio());
        outlineX += (mouseX - outlineX) * dt;
        outlineY += (mouseY - outlineY) * dt;
        
        gsap.set(cursorOutline, {
            x: outlineX,
            y: outlineY
        });
    });

    // Cursor Hover States
    const magnetics = document.querySelectorAll('.magnetic');
    const projects = document.querySelectorAll('[data-cursor="-project"]');

    magnetics.forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursorOutline.classList.add('hover-magnetic');
            cursorDot.classList.add('hover-magnetic');
        });
        el.addEventListener('mouseleave', () => {
            cursorOutline.classList.remove('hover-magnetic');
            cursorDot.classList.remove('hover-magnetic');
            gsap.to(el, { x: 0, y: 0, duration: 0.5, ease: "power3.out" });
        });
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const relX = e.clientX - rect.left - (rect.width/2);
            const relY = e.clientY - rect.top - (rect.height/2);
            gsap.to(el, {
                x: relX * 0.3,
                y: relY * 0.3,
                duration: 0.3,
                ease: "power2.out"
            });
        });
    });

    projects.forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursorOutline.classList.add('hover-project');
            cursorDot.classList.add('hover-project');
        });
        el.addEventListener('mouseleave', () => {
            cursorOutline.classList.remove('hover-project');
            cursorDot.classList.remove('hover-project');
        });
    });

    // Hide cursor when leaving window
    document.addEventListener('mouseleave', () => {
        cursorOutline.classList.add('cursor-hidden');
        cursorDot.classList.add('cursor-hidden');
    });
    document.addEventListener('mouseenter', () => {
        cursorOutline.classList.remove('cursor-hidden');
        cursorDot.classList.remove('cursor-hidden');
    });

    // 2. Loading Sequence
    // Prevent scrolling during load
    lenis.stop();
    
    const tlLoader = gsap.timeline({
        onComplete: () => {
            lenis.start();
        }
    });

    // Sequence
    tlLoader.to('.loader-logo .char', {
        y: 0,
        stagger: 0.1,
        duration: 1.2,
        ease: "power4.out",
        delay: 0.2
    })
    .to('.loader-logo', {
        scale: 1.1,
        duration: 1.5,
        ease: "power2.inOut"
    }, "-=0.5")
    .to('.loader-overlay', {
        yPercent: -100,
        duration: 1.2,
        ease: "power4.inOut"
    }, "+=0.5")
    // Reveal Hero
    .from('.hero-headline-line', {
        y: "110%",
        stagger: 0.15,
        duration: 1.5,
        ease: "power4.out"
    }, "-=0.6")
    .to('.hero-intro.reveal-text, .hero-support.reveal-text', {
        opacity: 1,
        duration: 1
    }, "-=1")
    .to('nav.nav-hidden', {
        opacity: 1,
        duration: 1
    }, "-=0.8")
    .to('.scroll-indicator', {
        opacity: 1,
        duration: 1
    }, "-=0.5");


    // 3. Cinematic Scroll Interactions

    // Blur Reveals for elements
    gsap.utils.toArray('.blur-reveal').forEach(el => {
        gsap.fromTo(el, 
            { opacity: 0, filter: "blur(10px)", y: 50 },
            {
                opacity: 1,
                filter: "blur(0px)",
                y: 0,
                duration: 1.2,
                ease: "power3.out",
                scrollTrigger: {
                    trigger: el,
                    start: "top 85%",
                    toggleActions: "play none none reverse"
                }
            }
        );
    });

    // Timeline Growth
    const timelineLine = document.querySelector('.timeline-progress');
    if (timelineLine) {
        gsap.to(timelineLine, {
            height: "100%",
            ease: "none",
            scrollTrigger: {
                trigger: ".timeline-track",
                start: "top center",
                end: "bottom center",
                scrub: 0.5
            }
        });
    }

    // Parallax Project Backgrounds
    gsap.utils.toArray('.project-fullscreen').forEach(section => {
        const bg = section.querySelector('.project-bg');
        
        gsap.fromTo(bg,
            { yPercent: -15 },
            {
                yPercent: 15,
                ease: "none",
                scrollTrigger: {
                    trigger: section,
                    start: "top bottom",
                    end: "bottom top",
                    scrub: true
                }
            }
        );
    });
});
