/* ==========================================================================
   SAD PORTFOLIO - INTERACTIVE JAVASCRIPT LOGIC
   University of Vavuniya | System Analysis and Design Assignment
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Sticky Navigation & Scroll Active State
    const navbar = document.getElementById('navbar');
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 40) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        let currentSectionId = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            const sectionHeight = section.offsetHeight;
            if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    });

    // 2. Theme Toggle (Dark / Light Glassmorphism)
    const themeToggleBtn = document.getElementById('themeToggle');
    const themeIcon = themeToggleBtn.querySelector('i');
    
    // Check saved theme in localStorage
    const savedTheme = localStorage.getItem('sad_portfolio_theme');
    if (savedTheme === 'light') {
        document.body.classList.add('light-theme');
        themeIcon.className = 'fa-solid fa-sun';
    }

    themeToggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('light-theme');
        const isLight = document.body.classList.contains('light-theme');
        themeIcon.className = isLight ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
        localStorage.setItem('sad_portfolio_theme', isLight ? 'light' : 'dark');
        showToast(isLight ? 'Switched to Light Theme' : 'Switched to Cinema Dark Theme', 'info');
    });

    // 3. Mobile Navigation Drawer Menu
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenuOverlay = document.getElementById('mobileMenuOverlay');
    const mobileMenuClose = document.getElementById('mobileMenuClose');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

    mobileMenuBtn.addEventListener('click', () => {
        mobileMenuOverlay.classList.add('active');
    });

    mobileMenuClose.addEventListener('click', () => {
        mobileMenuOverlay.classList.remove('active');
    });

    mobileNavLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenuOverlay.classList.remove('active');
        });
    });

    // 4. Skills Category Filter
    const filterBtns = document.querySelectorAll('.filter-btn');
    const skillCards = document.querySelectorAll('.skill-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.getAttribute('data-skill-filter');

            skillCards.forEach(card => {
                const category = card.getAttribute('data-category');
                if (filter === 'all' || filter === category) {
                    card.style.display = 'block';
                    setTimeout(() => card.style.opacity = '1', 50);
                } else {
                    card.style.opacity = '0';
                    setTimeout(() => card.style.display = 'none', 200);
                }
            });
        });
    });

    // 5. Detailed Project Modal Data & Handler
    const projectData = {
        agriconnect: {
            title: "AgriConnect – Smart Agriculture Supply Chain System",
            category: "Full-Stack Web App & SAD Case Study",
            image: "assets/agriconnect_preview.png",
            problem: "Local farmers in Northern Province faced price exploitation and distribution delays due to multi-layered intermediaries.",
            solution: "Designed and engineered a direct farmer-to-buyer platform with live market crop pricing, yield booking, and transparent logistics tracking.",
            sadArtifacts: "Authored 10 Functional Requirements (FRs), 8 Non-Functional Requirements (NFRs), Use-Case Diagram, Activity Flowchart, and Site Architecture Map.",
            techStack: ["HTML5", "CSS3", "JavaScript", "Node.js", "MySQL", "UML Specs"],
            github: "https://github.com/shehanhirusha/AgriConnect"
        },
        vavucampus: {
            title: "VavuCampus – Student Resource & Course Portal",
            category: "Departmental Resource Management",
            image: "assets/vavucampus_preview.png",
            problem: "Disorganized distribution of lecture materials and conflicting class timetable schedules across ICT academic years.",
            solution: "Built a centralized student dashboard featuring automated schedule conflict detection, note sharing repositories, and real-time announcement feeds.",
            sadArtifacts: "Designed Data Flow Diagrams (DFD Level 0 & 1), Relational ER Diagrams, and High-Fidelity Responsive Wireframes.",
            techStack: ["React.js", "Vite", "Express", "PostgreSQL", "Tailwind Tokens"],
            github: "https://github.com/shehanhirusha/VavuCampus"
        },
        medity: {
            title: "Medity – Tele-Health & Appointment System",
            category: "UI/UX & Web Application",
            image: "assets/medity_preview.png",
            problem: "Overcrowded waiting rooms and long registration delays for outpatient doctor consultations in regional clinics.",
            solution: "Developed a tele-health booking interface with real-time slot calendar picker, patient digital health card, and confirmation toast system.",
            sadArtifacts: "Conducted usability testing (8 test cases), responsiveness validation, and user interface design system formulation.",
            techStack: ["JavaScript", "HTML5", "CSS Aurora", "LocalStorage", "Wireframes"],
            github: "https://github.com/shehanhirusha/Medity"
        }
    };

    const projectModal = document.getElementById('projectModal');
    const modalClose = document.getElementById('modalClose');
    const modalBody = document.getElementById('modalBody');
    const openModalBtns = document.querySelectorAll('.open-modal-btn');

    openModalBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const key = btn.getAttribute('data-project');
            const data = projectData[key];
            if (data) {
                modalBody.innerHTML = `
                    <h2 style="font-size: 1.6rem; color: var(--accent-cyan); margin-bottom: 0.5rem;">${data.title}</h2>
                    <p style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent-indigo); margin-bottom: 1.5rem;">${data.category}</p>
                    
                    <img src="${data.image}" alt="${data.title}" style="width: 100%; max-height: 320px; object-fit: cover; border-radius: var(--radius-md); margin-bottom: 1.5rem; border: 1px solid var(--border-glass);">
                    
                    <div style="margin-bottom: 1rem;">
                        <h4 style="color: var(--text-primary); margin-bottom: 0.25rem;">Problem Statement:</h4>
                        <p style="font-size: 0.95rem;">${data.problem}</p>
                    </div>

                    <div style="margin-bottom: 1rem;">
                        <h4 style="color: var(--text-primary); margin-bottom: 0.25rem;">System Solution & Impact:</h4>
                        <p style="font-size: 0.95rem;">${data.solution}</p>
                    </div>

                    <div style="margin-bottom: 1.5rem;">
                        <h4 style="color: var(--text-primary); margin-bottom: 0.25rem;">SAD Deliverables & Modeling:</h4>
                        <p style="font-size: 0.95rem;">${data.sadArtifacts}</p>
                    </div>

                    <div style="margin-bottom: 1.5rem;">
                        <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">Technologies Used:</h4>
                        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                            ${data.techStack.map(tech => `<span class="badge" style="background: rgba(6, 182, 212, 0.1); color: var(--accent-cyan);">${tech}</span>`).join('')}
                        </div>
                    </div>

                    <a href="${data.github}" target="_blank" class="btn btn-primary"><i class="fa-brands fa-github"></i> View GitHub Repository</a>
                `;
                projectModal.classList.add('active');
            }
        });
    });

    modalClose.addEventListener('click', () => {
        projectModal.classList.remove('active');
    });

    // 6. CV Modal Viewer
    const cvModal = document.getElementById('cvModal');
    const openCvModalBtn = document.getElementById('openCvModalBtn');
    const heroCvBtn = document.getElementById('heroCvBtn');
    const cvModalClose = document.getElementById('cvModalClose');

    const openCvHandler = () => cvModal.classList.add('active');
    if (openCvModalBtn) openCvModalBtn.addEventListener('click', openCvHandler);
    if (heroCvBtn) heroCvBtn.addEventListener('click', openCvHandler);
    if (cvModalClose) cvModalClose.addEventListener('click', () => cvModal.classList.remove('active'));

    // Close modals when clicking overlay background
    window.addEventListener('click', (e) => {
        if (e.target === projectModal) projectModal.classList.remove('active');
        if (e.target === cvModal) cvModal.classList.remove('active');
    });

    // 7. Contact Form Handling with Toast Notification
    const contactForm = document.getElementById('contactForm');
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const subject = document.getElementById('subject').value.trim();
        const message = document.getElementById('message').value.trim();

        if (!name || !email || !subject || !message) {
            showToast('Please fill in all required fields.', 'error');
            return;
        }

        // Simulate successful submission
        showToast(`Thank you, ${name}! Your message has been sent successfully.`, 'success');
        contactForm.reset();
    });

    // Toast Notification System
    function showToast(msg, type = 'info') {
        const toastContainer = document.getElementById('toastContainer');
        const toast = document.createElement('div');
        toast.className = 'toast';

        let iconClass = 'fa-solid fa-circle-info';
        if (type === 'success') iconClass = 'fa-solid fa-circle-check';
        if (type === 'error') iconClass = 'fa-solid fa-triangle-exclamation';

        toast.innerHTML = `<i class="${iconClass}"></i> <span>${msg}</span>`;
        toastContainer.appendChild(toast);

        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(100%)';
            setTimeout(() => toast.remove(), 300);
        }, 4000);
    }
});
