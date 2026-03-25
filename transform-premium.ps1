# ===== TRANSFORM ALL PAGES TO PREMIUM DESIGN SYSTEM =====
$portfolioPath = "c:\Users\Cyprien\SPIE ICS\Portofolio"
$filesToProcess = @(
    "bts-sio.html",
    "certifications.html", 
    "competences.html",
    "contact.html",
    "cv.html",
    "projets.html"
)

# Navigation Template (Premium)
$premiumNav = @"
<body style="background: var(--surface-dark); color: var(--text-primary);">
    <!-- HEADER FLUID BAR PREMIUM -->
    <header>
        <div class="navbar-container">
            <a href="index.html" class="nav-logo">Cyprien Cavoli</a>
            
            <ul class="nav-menu" id="navMenu">
                <li class="nav-item">
                    <a href="index.html" class="nav-link navLink" data-page="index.html">Accueil</a>
                </li>
                <li class="nav-item">
                    <a href="bts-sio.html" class="nav-link navLink" data-page="bts-sio.html">BTS SIO</a>
                </li>
                <li class="nav-item">
                    <a href="a-propos.html" class="nav-link navLink" data-page="a-propos.html">À propos</a>
                </li>
                <li class="nav-item">
                    <a href="competences.html" class="nav-link navLink" data-page="competences.html">Compétences</a>
                </li>
                <li class="nav-item">
                    <a href="projets.html" class="nav-link navLink" data-page="projets.html">Projets</a>
                </li>
                <li class="nav-item">
                    <a href="certifications.html" class="nav-link navLink" data-page="certifications.html">Certifications</a>
                </li>
                <li class="nav-item">
                    <a href="contact.html" class="nav-link navLink" data-page="contact.html">Contact</a>
                </li>
            </ul>
            
            <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                    <path d="M3 12h18M3 6h18M3 18h18" stroke-width="2" stroke-linecap="round"/>
                </svg>
            </button>
        </div>
    </header>
"@

# Premium Footer Template
$premiumFooter = @"
    <!-- FOOTER PREMIUM -->
    <footer>
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-section footer-brand">
                    <div class="footer-logo">CC</div>
                    <div>
                        <h3 style="font-size: var(--text-sm); margin: 0;">Cyprien Cavoli</h3>
                        <p style="color: var(--text-secondary); font-size: var(--text-xs); margin: 4px 0 0 0;">BTS SIO • SISR • Grenoble</p>
                    </div>
                </div>

                <div class="footer-section">
                    <h3>Navigation</h3>
                    <div class="footer-links">
                        <a href="index.html" class="footer-link">Accueil</a>
                        <a href="bts-sio.html" class="footer-link">BTS SIO</a>
                        <a href="a-propos.html" class="footer-link">À propos</a>
                        <a href="competences.html" class="footer-link">Compétences</a>
                        <a href="projets.html" class="footer-link">Projets</a>
                        <a href="certifications.html" class="footer-link">Certifications</a>
                        <a href="contact.html" class="footer-link">Contact</a>
                    </div>
                </div>

                <div class="footer-section">
                    <h3>Contact Direct</h3>
                    <div class="footer-links">
                        <a href="mailto:cyprien.cavoli@gmail.com" class="footer-link">cyprien.cavoli@gmail.com</a>
                        <a href="tel:+33783844341" class="footer-link">+33 7 83 84 43 41</a>
                        <a href="https://www.linkedin.com/in/cyprien-cavoli/" target="_blank" class="footer-link">LinkedIn</a>
                    </div>
                </div>

                <div class="footer-section">
                    <h3>Actions</h3>
                    <div class="footer-links">
                        <button onclick="openCVModal()" class="btn btn-primary" style="width: 100%; text-align: center; display: flex; align-items: center; justify-content: center; margin-top: 8px;">Voir mon CV</button>
                        <a href="assets/cv/CV_Cyprien_Cavoli.pdf" download class="footer-link" style="margin-top: 12px; display: inline-block;">Télécharger CV</a>
                    </div>
                </div>
            </div>

            <div class="footer-divider">
                <p class="footer-meta">© 2024–2026 Cyprien Cavoli • Lycée Louise Michel, Grenoble</p>
                <p class="footer-meta">Disponible 24/7 — Étudiant</p>
            </div>
        </div>
    </footer>

    <!-- MODAL CV PREMIUM -->
    <div class="modal-overlay" id="cvModal">
        <div class="modal-content">
            <button class="modal-close" onclick="closeCVModal()" aria-label="Close CV modal">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M18 6L6 18M6 6l12 12"/>
                </svg>
            </button>
            <iframe class="modal-pdf" src="assets/cv/CV_Cyprien_Cavoli.pdf#toolbar=0" title="Cyprien Cavoli CV"></iframe>
        </div>
    </div>
"@

# Premium Scripts Template
$premiumScripts = @"
    <script>
        // ===== NAVIGATION ACTIVE STATE =====
        function setActiveNavLink() {
            const currentPage = window.location.pathname.split('/').pop() || 'index.html';
            document.querySelectorAll('.navLink').forEach(link => {
                const href = link.getAttribute('data-page');
                if (href === currentPage || (currentPage === '' && href === 'index.html')) {
                    link.classList.add('active');
                } else {
                    link.classList.remove('active');
                }
            });
        }

        // ===== MOBILE MENU TOGGLE =====
        const navToggle = document.getElementById('navToggle');
        const navMenu = document.getElementById('navMenu');

        navToggle?.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });

        navMenu?.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
            });
        });

        // ===== CV MODAL FUNCTIONS =====
        const cvModal = document.getElementById('cvModal');

        function openCVModal() {
            cvModal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeCVModal() {
            cvModal.classList.remove('active');
            document.body.style.overflow = 'auto';
        }

        // Close modal on overlay click
        cvModal?.addEventListener('click', (e) => {
            if (e.target === cvModal) {
                closeCVModal();
            }
        });

        // Close modal on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && cvModal?.classList.contains('active')) {
                closeCVModal();
            }
        });

        // ===== INITIALIZE =====
        setActiveNavLink();

        // ===== SCROLL REVEAL =====
        const revealElements = document.querySelectorAll('[data-reveal]');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.animation = 'slideInUp 0.6s cubic-bezier(0.33, 0.66, 0.66, 1) forwards';
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        revealElements.forEach(el => {
            el.style.opacity = '0';
            observer.observe(el);
        });

        window.openCVModal = openCVModal;
        window.closeCVModal = closeCVModal;
    </script>
"@

# Process each file
foreach ($file in $filesToProcess) {
    $filePath = Join-Path $portfolioPath $file
    Write-Host "Processing: $file"
    
    if (Test-Path $filePath) {
        # Read file content
        $content = Get-Content -Path $filePath -Raw -Encoding UTF8
        
        # Step 1: Add premium CSS link to head if not already there
        if ($content -notmatch 'assets/css/premium.css') {
            $content = $content -replace '(<title>[^<]+</title>)', "`$1`n    <link rel=`"stylesheet`" href=`"assets/css/premium.css`">"
        }
        
        # Step 2: Replace old navbar with premium nav (match body tag and following nav)
        $content = $content -replace '(?s)<body[^>]*>.*?</nav>\s*(?=<main|<section|<div)', $premiumNav
        
        # Replace old body tag patterns if premium nav replacement didn't work
        if ($content -notmatch 'HEADER FLUID BAR PREMIUM') {
            $content = $content -replace '(?s)<body[^>]*>.*?</nav>\s*(?=<main|<section)', $premiumNav
        }
        
        # Step 3: Remove old footer and replace with premium footer
        $content = $content -replace '(?s)    <!-- FOOTER.*?</footer>', $premiumFooter
        
        # Step 4: Replace all scripts at the end before closing body tag
        $content = $content -replace '(?s)    <script>.*?</script>\s*</body>', $premiumScripts + "`n</body>"
        
        # Write file back
        Set-Content -Path $filePath -Value $content -Encoding UTF8
        Write-Host "✓ Transformed: $file"
    } else {
        Write-Host "✗ File not found: $file"
    }
}

Write-Host "`nPremium transformation completed!"
