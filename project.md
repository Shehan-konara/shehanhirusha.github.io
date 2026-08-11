<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shehan Hirusha | Android Application Developer</title>
    <meta name="description"
        content="Professional System Analysis and Design (SAD) portfolio website of Shehan Hirusha, ICT Undergraduate at University of Vavuniya. Software Developer & System Analyst.">
    <meta name="keywords"
        content="Shehan Hirusha, SAD Portfolio, University of Vavuniya, System Analysis and Design, Full Stack Developer, Web Development">

    <!-- Design System CSS -->
    <link rel="stylesheet" href="styles.css">

    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>

<body>

    <!-- Header & Navigation Bar -->
    <header class="navbar" id="navbar">
        <div class="container nav-container">
            <a href="#home" class="nav-logo">
                <i class="fa-solid fa-code" style="color: var(--accent-primary);"></i> Shehan<span>H. Konara</span>
            </a>

            <ul class="nav-links">
                <li><a href="#home" class="nav-link active">Home</a></li>
                <li><a href="#about" class="nav-link">About Me</a></li>
                <li><a href="#education" class="nav-link">Education</a></li>
                <li><a href="#skills" class="nav-link">Skills</a></li>
                <li><a href="#projects" class="nav-link">Projects</a></li>
                <li><a href="#experience" class="nav-link">Experience</a></li>
                <li><a href="#cv" class="nav-link">CV</a></li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>

            <div class="nav-actions">
                <button class="theme-toggle-btn" id="themeToggle" title="Toggle Light/Dark Theme">
                    <i class="fa-solid fa-moon"></i>
                </button>
                <a href="#contact" class="btn btn-primary btn-sm">Hire Me</a>
                <button class="mobile-menu-btn" id="mobileMenuBtn">
                    <i class="fa-solid fa-bars"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- Mobile Navigation Drawer -->
    <div class="mobile-menu-overlay" id="mobileMenuOverlay">
        <button class="modal-close" id="mobileMenuClose"><i class="fa-solid fa-xmark"></i></button>
        <ul class="mobile-nav-links">
            <li><a href="#home" class="mobile-nav-link">Home</a></li>
            <li><a href="#about" class="mobile-nav-link">About Me</a></li>
            <li><a href="#education" class="mobile-nav-link">Education</a></li>
            <li><a href="#skills" class="mobile-nav-link">Skills</a></li>
            <li><a href="#projects" class="mobile-nav-link">Projects</a></li>
            <li><a href="#experience" class="mobile-nav-link">Experience</a></li>
            <li><a href="#cv" class="mobile-nav-link">CV</a></li>
            <li><a href="#contact" class="mobile-nav-link">Contact</a></li>
        </ul>
    </div>

    <main>
        <!-- 1. HOME SECTION (HERO) -->
        <section id="home" class="hero">
            <div class="container hero-grid">
                <div class="hero-text-content">
                    <div class="hero-badge">
                        <i class="fa-solid fa-code-commit"></i> Shehan Hirusha — Android Application Developer
                    </div>
                    <h1 class="hero-title">
                        Crafting High-Performance <span class="highlight-text">Android Apps</span> with Flutter, Java &
                        Kotlin
                    </h1>
                    <p class="hero-subtitle">
                        Hello! I'm <strong>Shehan Hirusha</strong>, an ICT Undergraduate at the
                        <strong>University of Vavuniya</strong>. I specialize in building cross-platform and native
                        Android applications with clean architecture, responsive UIs, and seamless user experiences.
                    </p>

                    <div class="hero-actions">
                        <a href="#projects" class="btn btn-primary"><i class="fa-solid fa-layer-group"></i> View Case
                            Studies</a>
                        <button class="btn btn-secondary" id="heroCvBtn"><i class="fa-solid fa-file-pdf"></i> View /
                            Download CV</button>
                    </div>

                    <div class="hero-stats">
                        <div class="stat-item">
                            <h4>3.82</h4>
                            <p>Current GPA</p>
                        </div>
                        <div class="stat-item">
                            <h4>5+</h4>
                            <p>Android Apps Built</p>
                        </div>
                        <div class="stat-item">
                            <h4>100%</h4>
                            <p>Hand-Crafted Quality</p>
                        </div>
                    </div>
                </div>

                <div class="hero-avatar-wrapper">
                    <div class="glass-card hero-avatar-card">
                        <img src="assets/myphoto-clean.png  " alt="Shehan Hirusha Profile" class="hero-avatar-img">
                        <div class="floating-tag floating-tag-1">
                            <i class="fa-solid fa-diagram-project" style="color: var(--accent-primary);"></i> Flutter &
                            Kotlin
                        </div>
                        <div class="floating-tag floating-tag-2">
                            <i class="fa-solid fa-graduation-cap" style="color: var(--accent-secondary);"></i> ICT
                            Vavuniya
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 2. ABOUT ME SECTION -->
        <section id="about" class="section">
            <div class="container">
                <div class="section-header">
                    <span class="section-tag"><i class="fa-solid fa-user"></i> Biography</span>
                    <h2 class="section-title">About Me</h2>
                    <p class="section-subtitle">Bridging theoretical System Analysis & Design principles with modern web
                        engineering.</p>
                </div>

                <div class="about-grid">
                    <div class="glass-card about-card">
                        <h3><i class="fa-solid fa-user-gear"></i> Professional Profile</h3>
                        <p>
                            I am a dedicated 2nd-year ICT undergraduate student at the Faculty of Technological Studies,
                            University of Vavuniya. My primary academic and technical focus centers on <strong>System
                                Analysis and Design (SAD)</strong>, modern frontend frameworks, and cloud-ready database
                            architectures.
                        </p>
                        <p>
                            I take pride in transforming ambiguous user requirements into well-structured UML diagrams,
                            high-fidelity wireframes, and scalable software solutions.
                        </p>
                    </div>

                    <div class="glass-card about-card">
                        <h3><i class="fa-solid fa-bullseye"></i> Career Objectives & Interests</h3>
                        <p><strong>Primary Goal:</strong> To secure a challenging Software Engineering or Web
                            Development internship where I can apply SAD methodologies to solve real-world industry
                            problems.</p>
                        <ul class="objective-list">
                            <li>Mastering Agile software development lifecycles and CI/CD pipelines.</li>
                            <li>Designing intuitive, accessible (WCAG AA), user-centric interfaces.</li>
                            <li>Contributing to open-source software and departmental ICT innovation.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- 3. EDUCATION SECTION -->
        <section id="education" class="section">
            <div class="container">
                <div class="section-header">
                    <span class="section-tag"><i class="fa-solid fa-graduation-cap"></i> Academic Journey</span>
                    <h2 class="section-title">Education & Highlights</h2>
                    <p class="section-subtitle">Academic record and relevant coursework at University of Vavuniya.</p>
                </div>

                <div class="timeline">
                    <!-- Education Item 1 -->
                    <div class="timeline-item">
                        <div class="timeline-dot"></div>
                        <div class="glass-card timeline-content">
                            <span class="timeline-date">2023 – Present</span>
                            <h3>BSc (Hons) in Information & Communication Technology</h3>
                            <p><strong>Faculty of Technological Studies | University of Vavuniya</strong></p>
                            <p style="margin-top: 0.5rem; font-size: 0.9rem;">
                                Current Cumulative GPA: <strong>3.82 / 4.00</strong> (Dean's List for Academic
                                Excellence)
                            </p>
                            <div class="coursework-badges">
                                <span class="badge">System Analysis & Design</span>
                                <span class="badge">Web Technologies</span>
                                <span class="badge">DBMS & SQL</span>
                                <span class="badge">Data Structures & Algo</span>
                                <span class="badge">Software Engineering</span>
                            </div>
                        </div>
                    </div>

                    <!-- Education Item 2 -->
                    <div class="timeline-item">
                        <div class="timeline-dot"></div>
                        <div class="glass-card timeline-content">
                            <span class="timeline-date">2020 – 2022</span>
                            <h3>G.C.E. Advanced Level (Physical Science Stream)</h3>
                            <p><strong>Central College, Sri Lanka</strong></p>
                            <p style="margin-top: 0.5rem; font-size: 0.9rem;">
                                Passed with 3 As (Combined Mathematics, Physics, Chemistry). Z-Score: 1.845.
                            </p>
                            <div class="coursework-badges">
                                <span class="badge">Mathematics</span>
                                <span class="badge">Physics</span>
                                <span class="badge">Chemistry</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 4. SKILLS SECTION -->
        <section id="skills" class="section">
            <div class="container">
                <div class="section-header">
                    <span class="section-tag"><i class="fa-solid fa-code"></i> Competencies</span>
                    <h2 class="section-title">Skills & Expertise</h2>
                    <p class="section-subtitle">Categorized breakdown of technical proficiencies and core soft skills.
                    </p>
                </div>

                <div class="skills-filter">
                    <button class="filter-btn active" data-skill-filter="all">All Skills</button>
                    <button class="filter-btn" data-skill-filter="frontend">Frontend & Web</button>
                    <button class="filter-btn" data-skill-filter="sad">SAD & Modeling</button>
                    <button class="filter-btn" data-skill-filter="tools">Database & Tools</button>
                    <button class="filter-btn" data-skill-filter="soft">Soft Skills</button>
                </div>

                <div class="skills-grid" id="skillsContainer">
                    <!-- HTML5 / CSS3 -->
                    <div class="glass-card skill-card" data-category="frontend">
                        <div class="skill-header">
                            <span class="skill-title"><i class="fa-brands fa-html5" style="color: #e34f26;"></i> HTML5 &
                                CSS3</span>
                            <span class="skill-level">95%</span>
                        </div>
                        <div class="skill-progress-bar">
                            <div class="skill-progress-fill" style="width: 95%;"></div>
                        </div>
                    </div>

                    <!-- JavaScript -->
                    <div class="glass-card skill-card" data-category="frontend">
                        <div class="skill-header">
                            <span class="skill-title"><i class="fa-brands fa-js" style="color: #f7df1e;"></i> JavaScript
                                (ES6+)</span>
                            <span class="skill-level">90%</span>
                        </div>
                        <div class="skill-progress-bar">
                            <div class="skill-progress-fill" style="width: 90%;"></div>
                        </div>
                    </div>

                    <!-- React.js -->
                    <div class="glass-card skill-card" data-category="frontend">
                        <div class="skill-header">
                            <span class="skill-title"><i class="fa-brands fa-react" style="color: #61dafb;"></i>
                                React.js / Vite</span>
                            <span class="skill-level">85%</span>
                        </div>
                        <div class="skill-progress-bar">
                            <div class="skill-progress-fill" style="width: 85%;"></div>
                        </div>
                    </div>

                    <!-- UML & SAD -->
                    <div class="glass-card skill-card" data-category="sad">
                        <div class="skill-header">
                            <span class="skill-title"><i class="fa-solid fa-diagram-project"
                                    style="color: var(--accent-primary);"></i> UML & SAD Diagrams</span>
                            <span class="skill-level">92%</span>
                        </div>
                        <div class="skill-progress-bar">
                            <div class="skill-progress-fill" style="width: 92%;"></div>
                        </div>
                    </div>

                    <!-- Requirements Spec -->
                    <div class="glass-card skill-card" data-category="sad">
                        <div class="skill-header">
                            <span class="skill-title"><i class="fa-solid fa-file-contract"
                                    style="color: var(--accent-secondary);"></i> Requirements Eng (FR/NFR)</span>
                            <span class="skill-level">90%</span>
                        </div>
                        <div class="skill-progress-bar">
                            <div class="skill-progress-fill" style="width: 90%;"></div>
                        </div>
                    </div>

                    <!-- Database -->
                    <div class="glass-card skill-card" data-category="tools">
                        <div class="skill-header">
                            <span class="skill-title"><i class="fa-solid fa-database" style="color: #336791;"></i> MySQL
                                & PostgreSQL</span>
                            <span class="skill-level">88%</span>
                        </div>
                        <div class="skill-progress-bar">
                            <div class="skill-progress-fill" style="width: 88%;"></div>
                        </div>
                    </div>

                    <!-- Git / GitHub -->
                    <div class="glass-card skill-card" data-category="tools">
                        <div class="skill-header">
                            <span class="skill-title"><i class="fa-brands fa-github"></i> Git & Version Control</span>
                            <span class="skill-level">88%</span>
                        </div>
                        <div class="skill-progress-bar">
                            <div class="skill-progress-fill" style="width: 88%;"></div>
                        </div>
                    </div>

                    <!-- Analytical Thinking -->
                    <div class="glass-card skill-card" data-category="soft">
                        <div class="skill-header">
                            <span class="skill-title"><i class="fa-solid fa-brain"
                                    style="color: var(--accent-primary);"></i> Analytical Problem Solving</span>
                            <span class="skill-level">94%</span>
                        </div>
                        <div class="skill-progress-bar">
                            <div class="skill-progress-fill" style="width: 94%;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 5. PROJECTS SECTION -->
        <section id="projects" class="section">
            <div class="container">
                <div class="section-header">
                    <span class="section-tag"><i class="fa-solid fa-laptop-code"></i> Case Studies</span>
                    <h2 class="section-title">Featured Projects</h2>
                    <p class="section-subtitle">Real-world applications engineered following full System Analysis &
                        Design lifecycles.</p>
                </div>

                <div class="projects-grid">
                    <!-- Project 1: AgriConnect -->
                    <div class="glass-card project-card">
                        <div class="project-img-wrapper">
                            <img src="assets/agriconnect_preview.png" alt="AgriConnect Project Preview"
                                class="project-img">
                            <span class="project-category-tag">Full-Stack / SAD</span>
                        </div>
                        <div class="project-content">
                            <h3 class="project-title">AgriConnect</h3>
                            <p class="project-problem">
                                <strong>Problem:</strong> Local agricultural producers faced market information gaps and
                                supply chain delays when connecting with buyers in Sri Lanka.
                            </p>
                            <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 1rem;">
                                <strong>My Contribution:</strong> Lead System Analyst & Frontend Developer. Created full
                                UML Use-Case & Activity diagrams, designed interactive yield pricing dashboard.
                            </p>
                            <div class="project-tools">
                                <span class="tool-tag">HTML5/CSS3</span>
                                <span class="tool-tag">JavaScript</span>
                                <span class="tool-tag">Node.js</span>
                                <span class="tool-tag">UML</span>
                            </div>
                            <div class="project-actions">
                                <button class="btn btn-secondary btn-sm open-modal-btn" data-project="agriconnect"><i
                                        class="fa-solid fa-eye"></i> Details</button>
                                <a href="https://github.com/shehanhirusha/AgriConnect" target="_blank"
                                    class="btn btn-primary btn-sm"><i class="fa-brands fa-github"></i> GitHub</a>
                            </div>
                        </div>
                    </div>

                    <!-- Project 2: VavuCampus -->
                    <div class="glass-card project-card">
                        <div class="project-img-wrapper">
                            <img src="assets/vavucampus_preview.png" alt="VavuCampus Project Preview"
                                class="project-img">
                            <span class="project-category-tag">Web Portal</span>
                        </div>
                        <div class="project-content">
                            <h3 class="project-title">VavuCampus Portal</h3>
                            <p class="project-problem">
                                <strong>Problem:</strong> Fragmented lecture resource sharing and schedule conflict
                                handling across ICT department streams.
                            </p>
                            <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 1rem;">
                                <strong>My Contribution:</strong> Designed system wireframes, timetable conflict
                                resolution logic, and note-sharing REST API.
                            </p>
                            <div class="project-tools">
                                <span class="tool-tag">React.js</span>
                                <span class="tool-tag">Vite</span>
                                <span class="tool-tag">Express</span>
                                <span class="tool-tag">PostgreSQL</span>
                            </div>
                            <div class="project-actions">
                                <button class="btn btn-secondary btn-sm open-modal-btn" data-project="vavucampus"><i
                                        class="fa-solid fa-eye"></i> Details</button>
                                <a href="https://github.com/shehanhirusha/VavuCampus" target="_blank"
                                    class="btn btn-primary btn-sm"><i class="fa-brands fa-github"></i> GitHub</a>
                            </div>
                        </div>
                    </div>

                    <!-- Project 3: Medity -->
                    <div class="glass-card project-card">
                        <div class="project-img-wrapper">
                            <img src="assets/medity_preview.png" alt="Medity Project Preview" class="project-img">
                            <span class="project-category-tag">UI/UX & Web</span>
                        </div>
                        <div class="project-content">
                            <h3 class="project-title">Medity Health System</h3>
                            <p class="project-problem">
                                <strong>Problem:</strong> Inefficient appointment scheduling leading to extended waiting
                                times in regional healthcare outpatient clinics.
                            </p>
                            <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 1rem;">
                                <strong>My Contribution:</strong> Conducted requirements specification (FR1-FR5), built
                                responsive booking UI with glassmorphism aesthetics.
                            </p>
                            <div class="project-tools">
                                <span class="tool-tag">JavaScript</span>
                                <span class="tool-tag">CSS</span>
                                <span class="tool-tag">LocalStorage</span>
                                <span class="tool-tag">Wireframing</span>
                            </div>
                            <div class="project-actions">
                                <button class="btn btn-secondary btn-sm open-modal-btn" data-project="medity"><i
                                        class="fa-solid fa-eye"></i> Details</button>
                                <a href="https://github.com/shehanhirusha/Medity" target="_blank"
                                    class="btn btn-primary btn-sm"><i class="fa-brands fa-github"></i> GitHub</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 6. EXPERIENCE & ACTIVITIES SECTION -->
        <section id="experience" class="section">
            <div class="container">
                <div class="section-header">
                    <span class="section-tag"><i class="fa-solid fa-users"></i> Engagement</span>
                    <h2 class="section-title">Leadership & Activities</h2>
                    <p class="section-subtitle">Volunteering, departmental roles, competitions, and technical
                        achievements.</p>
                </div>

                <div class="exp-grid">
                    <div class="glass-card exp-card">
                        <h3 class="exp-role">Executive Committee Member</h3>
                        <p class="exp-org">ICT Student Circle, University of Vavuniya</p>
                        <p class="exp-date">2024 – Present</p>
                        <p>Co-organized departmental technical workshops, GitHub training sessions, and annual hackathon
                            logistical planning.</p>
                    </div>

                    <div class="glass-card exp-card">
                        <h3 class="exp-role">Hackathon Finalist</h3>
                        <p class="exp-org">National Smart Cities Hackathon 2024</p>
                        <p class="exp-date">2024</p>
                        <p>Engineered a working web prototype for urban waste tracking within 24 hours under intense
                            competition constraints.</p>
                    </div>

                    <div class="glass-card exp-card">
                        <h3 class="exp-role">Peer Tutor (Web Dev & Git)</h3>
                        <p class="exp-org">Faculty of Technological Studies</p>
                        <p class="exp-date">2023 – 2024</p>
                        <p>Mentored 40+ first-year ICT students in basic HTML5/CSS3 styling, Git repository workflow,
                            and simple JS scripting.</p>
                    </div>
                </div>

                <!-- LinkedIn Career Sharing Evidence Section -->
                <div class="glass-card linkedin-evidence-card">
                    <div class="linkedin-header">
                        <i class="fa-brands fa-linkedin" style="font-size: 2.2rem; color: #0a66c2;"></i>
                        <div>
                            <h3 style="font-size: 1.2rem;">LinkedIn Portfolio Post & Featured Evidence</h3>
                            <p style="font-size: 0.875rem; color: var(--text-muted);">Demonstrating career promotion &
                                professional web presence (Assignment Requirement #6).</p>
                        </div>
                    </div>
                    <p style="font-size: 0.925rem; line-height: 1.6;">
                        "Excited to share my System Analysis and Design (SAD) Professional Portfolio website! Built from
                        the ground up featuring UML specifications, responsive UI, and full project case studies. Check
                        out the live URL and GitHub source!"
                    </p>
                    <a href="https://www.linkedin.com/in/shehan-hirusha-33bb52411?utm_source=share_via&utm_content=profile&utm_medium=member_android"
                        target="_blank"
                        style="display: inline-flex; align-items: center; gap: 0.4rem; margin-top: 0.65rem; font-weight: 600; color: var(--accent-primary);">
                        <i class="fa-solid fa-arrow-up-right-from-square"></i> View Shehan Hirusha's LinkedIn Profile
                    </a>
                    <img src="assets/linkedin_evidence.png" alt="LinkedIn Career Post Evidence" class="linkedin-img">
                </div>
            </div>
        </section>

        <!-- 7. CV SECTION -->
        <section id="cv" class="section">
            <div class="container">
                <div class="glass-card cv-section-card">
                    <i class="fa-solid fa-file-pdf cv-icon"></i>
                    <h2 class="section-title">Curriculum Vitae</h2>
                    <p class="section-subtitle" style="margin-bottom: 2rem;">
                        View or download an updated, comprehensive copy of my professional CV in PDF format.
                    </p>
                    <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                        <button class="btn btn-primary" id="openCvModalBtn"><i class="fa-solid fa-expand"></i> Preview
                            CV Online</button>
                        <a href="CV_Shehan_Hirusha.pdf" download="CV_Shehan_Hirusha.pdf" class="btn btn-secondary"><i
                                class="fa-solid fa-download"></i> Download CV (PDF)</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- 8. CONTACT & LINKS SECTION -->
        <section id="contact" class="section">
            <div class="container">
                <div class="section-header">
                    <span class="section-tag"><i class="fa-solid fa-paper-plane"></i> Get In Touch</span>
                    <h2 class="section-title">Contact & Professional Links</h2>
                    <p class="section-subtitle">Feel free to reach out for internship opportunities, project
                        collaborations, or inquiries.</p>
                </div>

                <div class="contact-grid">
                    <div class="glass-card contact-info-card">
                        <h3 style="margin-bottom: 1.5rem; color: var(--accent-primary);">Contact Information</h3>

                        <div class="contact-method">
                            <div class="contact-icon"><i class="fa-solid fa-envelope"></i></div>
                            <div>
                                <h4>Email Address</h4>
                                <a href="mailto:shehan.hirusha@vau.ac.lk">shehan.hirusha@vau.ac.lk</a>
                            </div>
                        </div>

                        <div class="contact-method">
                            <div class="contact-icon"><i class="fa-solid fa-location-dot"></i></div>
                            <div>
                                <h4>Institution Location</h4>
                                <p style="font-size: 0.95rem;">Faculty of Technological Studies, University of Vavuniya,
                                    Sri Lanka</p>
                            </div>
                        </div>

                        <div class="contact-method">
                            <div class="contact-icon"><i class="fa-brands fa-linkedin"></i></div>
                            <div>
                                <h4>LinkedIn Profile</h4>
                                <a href="https://www.linkedin.com/in/shehan-hirusha-33bb52411?utm_source=share_via&utm_content=profile&utm_medium=member_android"
                                    target="_blank">linkedin.com/in/shehan-hirusha-33bb52411</a>
                            </div>
                        </div>

                        <div class="contact-method">
                            <div class="contact-icon"><i class="fa-brands fa-github"></i></div>
                            <div>
                                <h4>GitHub Repository</h4>
                                <a href="https://github.com/shehanhirusha" target="_blank">github.com/shehanhirusha</a>
                            </div>
                        </div>
                    </div>

                    <form class="glass-card contact-form" id="contactForm">
                        <h3 style="margin-bottom: 0.5rem; color: var(--text-primary);">Send a Message</h3>

                        <div class="form-group">
                            <label for="name">Your Name *</label>
                            <input type="text" id="name" class="form-input" placeholder="e.g. Dr. John Doe" required>
                        </div>

                        <div class="form-group">
                            <label for="email">Your Email *</label>
                            <input type="email" id="email" class="form-input" placeholder="e.g. john@example.com"
                                required>
                        </div>

                        <div class="form-group">
                            <label for="subject">Subject *</label>
                            <input type="text" id="subject" class="form-input" placeholder="e.g. Internship Inquiry"
                                required>
                        </div>

                        <div class="form-group">
                            <label for="message">Message *</label>
                            <textarea id="message" class="form-input" placeholder="Write your message here..."
                                required></textarea>
                        </div>

                        <button type="submit" class="btn btn-primary"><i class="fa-solid fa-paper-plane"></i> Send
                            Message</button>
                    </form>
                </div>
            </div>
        </section>
    </main>

    <!-- Project Detail Modal Reader -->
    <div class="modal" id="projectModal">
        <div class="glass-card modal-content">
            <button class="modal-close" id="modalClose"><i class="fa-solid fa-xmark"></i></button>
            <div id="modalBody">
                <!-- Injected via JavaScript -->
            </div>
        </div>
    </div>

    <!-- CV Interactive Preview Modal -->
    <div class="modal" id="cvModal">
        <div class="glass-card modal-content" style="max-width: 850px; height: 90vh;">
            <button class="modal-close" id="cvModalClose"><i class="fa-solid fa-xmark"></i></button>
            <h3 style="margin-bottom: 1rem; color: var(--accent-primary);">CV Document Preview</h3>
            <iframe src="CV_Shehan_Hirusha.pdf"
                style="width: 100%; height: calc(100% - 60px); border: none; border-radius: var(--radius-md);"></iframe>
        </div>
    </div>

    <!-- Toast Notification Container -->
    <div class="toast-container" id="toastContainer"></div>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2026 Shehan Hirusha | System Analysis & Design Individual Assignment | University of Vavuniya</p>
            <p style="font-size: 0.8rem; margin-top: 0.4rem; color: var(--text-muted);">Hand-crafted with HTML5, CSS3
                Custom Properties, Vanilla JavaScript & SAD Principles.</p>
        </div>
    </footer>

    <!-- Interactive JavaScript -->
    <script src="script.js"></script>
</body>

</html>