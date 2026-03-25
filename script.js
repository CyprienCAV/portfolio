/*==============================================
  PORTFOLIO CYPRIEN CAVOLI - JavaScript
  =============================================*/

// ==================== MENU BURGER ====================
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const mobileMenu = document.getElementById('mobileMenu');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
        
        // Fermer le menu quand on clique sur un lien
        const mobileLinks = mobileMenu.querySelectorAll('a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenu.classList.add('hidden');
            });
        });
    }
});

// ========================================
// MENU BURGER RESPONSIVE
// ========================================
function initializeMenuBurger() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('nav ul');
    const navLinks = document.querySelectorAll('nav ul a');

    if (!menuToggle || !navMenu) return;

    // Toggle menu au clic
    menuToggle.addEventListener('click', function(e) {
        e.stopPropagation();
        menuToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Fermer le menu au clic sur un lien
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            menuToggle.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // Fermer le menu au clic en dehors
    document.addEventListener('click', function(e) {
        if (!e.target.closest('header')) {
            menuToggle.classList.remove('active');
            navMenu.classList.remove('active');
        }
    });

    // Fermer le menu au scroll
    window.addEventListener('scroll', function() {
        menuToggle.classList.remove('active');
        navMenu.classList.remove('active');
    });
}

// ========================================
// NAVIGATION ACTIVE
// ========================================
function updateActiveNavLink() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('nav a').forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage || (currentPage === '' && href === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}
const projects = {
    1: {
        title: "Nom du Projet 1",
        type: "Cours / Groupe",
        shortDescription: "Description courte du premier projet",
        fullDescription: "Description détaillée du projet 1. Expliquez les objectifs, le contexte et ce qui a été réalisé.",
        technologies: ["HTML", "CSS", "JavaScript"],
        skills: ["Développement web", "UI/UX", "Front-end"],
        challenges: "Défis rencontrés et solutions apportées...",
        results: "Résultats et apprentissages...",
        personalRole: "Qu'avez-vous personnellement réalisé ?",
        links: {
            demo: "#"
        }
    },
    2: {
        title: "Nom du Projet 2", 
        type: "Stage",
        shortDescription: "Description courte du deuxième projet",
        fullDescription: "Description détaillée du projet 2. Intégration web, backend, base de données...",
        technologies: ["PHP", "MySQL", "Apache"],
        skills: ["Développement Backend", "Base de données", "Architecture"],
        challenges: "Défis rencontrés et solutions apportées...",
        results: "Résultats et apprentissages...",
        personalRole: "Qu'avez-vous personnellement réalisé ?",
        links: {
            demo: "#"
        }
    },
    3: {
        title: "Nom du Projet 3",
        type: "Personnel",
        shortDescription: "Description courte du troisième projet",
        fullDescription: "Description détaillée du projet 3. Scripting automation, DevOps...",
        technologies: ["Python", "Linux", "Docker"],
        skills: ["Scripting", "DevOps", "Infrastructure"],
        challenges: "Défis rencontrés et solutions apportées...",
        results: "Résultats et apprentissages...",
        personalRole: "Qu'avez-vous personnellement réalisé ?",
        links: {
            demo: "#"
        }
    }
};

// ========================================
// MODALES DE PROJETS
// ========================================
function openProjectModal(projectId) {
    const modal = document.getElementById('projectModal');
    const project = projects[projectId];
    
    if (project) {
        displayProjectDetails(project);
        modal.classList.remove('hidden');
    }
}

function closeProjectModal() {
    const modal = document.getElementById('projectModal');
    modal.classList.add('hidden');
}

function initializeProjectModals() {
    const modal = document.getElementById('projectModal');
    
    // Fermer modal au clic en dehors
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.classList.add('hidden');
        }
    });
    
    // Fermer modal au Escape
    window.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            modal.classList.add('hidden');
        }
    });
}

// Afficher les détails du projet dans la modal
function displayProjectDetails(project) {
    const modal = document.getElementById('projectModal');
    const modalContent = document.getElementById('modalContent');
    
    modalContent.innerHTML = `
        <h2 class="text-3xl font-bold text-accent-blue">${project.title}</h2>
        <p class="text-gray-400">${project.fullDescription}</p>
        
        <div class="grid grid-cols-2 gap-4">
            <div>
                <h4 class="font-bold text-accent-violet mb-2">Technologies utilisées</h4>
                <div class="flex flex-wrap gap-2">
                    ${project.technologies.map(tech => `<span class="px-3 py-1 rounded text-xs font-medium bg-accent-blue/20 text-accent-blue">${tech}</span>`).join('')}
                </div>
            </div>
            <div>
                <h4 class="font-bold text-accent-pink mb-2">Compétences mobilisées</h4>
                <p class="text-sm text-gray-300">${project.skills.join(', ')}</p>
            </div>
        </div>
        
        <div>
            <h4 class="font-bold text-accent-blue mb-2">Défis et solutions</h4>
            <p class="text-gray-400">${project.challenges}</p>
        </div>
        
        <div>
            <h4 class="font-bold text-accent-violet mb-2">Résultats et apprentissages</h4>
            <p class="text-gray-400">${project.results}</p>
        </div>
        
        <div>
            <h4 class="font-bold text-accent-pink mb-2">Mon rôle personnel</h4>
            <p class="text-gray-400">${project.personalRole}</p>
        </div>
        
        <div class="flex gap-3 pt-4">
            ${project.links.demo !== '#' ? `<a href="${project.links.demo}" target="_blank" class="px-4 py-2 bg-accent-violet text-white rounded-lg hover:bg-accent-violet/80 transition-colors">Voir la démo</a>` : ''}
        </div>
    `;
}

// ===== FORMULAIRE DE CONTACT =====
function initializeContactForm() {
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Récupérer les données du formulaire
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const subject = document.getElementById('subject').value.trim();
            const message = document.getElementById('message').value.trim();

            // Valider les champs
            if (!name || !email || !subject || !message) {
                showFormMessage('Veuillez remplir tous les champs.', 'error');
                return;
            }

            // Valider l'email
            if (!isValidEmail(email)) {
                showFormMessage('Veuillez entrer une adresse email valide.', 'error');
                return;
            }

            // Afficher un message de succès (pas de vrai envoi backend)
            showFormMessage('Message envoyé avec succès ! Merci de votre message. Je vous répondrai dès que possible.', 'success');

            // Réinitialiser le formulaire
            contactForm.reset();

            // Masquer le message après 5 secondes
            setTimeout(function() {
                if (formMessage) {
                    formMessage.style.display = 'none';
                }
            }, 5000);
        });
    }
}

// Afficher un message du formulaire
function showFormMessage(text, type) {
    const formMessage = document.getElementById('formMessage');
    if (!formMessage) return;
    
    formMessage.textContent = text;
    formMessage.className = `py-3 px-4 rounded-lg text-center font-semibold ${
        type === 'error' ? 'bg-red-500/20 text-red-300 border border-red-500/50' : 'bg-green-500/20 text-green-300 border border-green-500/50'
    }`;
    formMessage.style.display = 'block';
}

// Valider une adresse email
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// ===== ANIMATIONS AU SCROLL =====
function initializeScrollAnimations() {
    // Utiliser Intersection Observer pour animer les éléments au scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Animer les cartes de projets, compétences, etc.
    const animateElements = document.querySelectorAll(
        '.project-card, .skill-item, .cert-card, .option-card'
    );

    animateElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'all 0.3s ease';
        observer.observe(element);
    });
}

// ===== SMOOTH SCROLLING POUR ANCRES =====
// (déjà géré par scroll-behavior: smooth en CSS)

// ===== FONCTIONS UTILITAIRES =====

// Copier du texte dans le presse-papiers (optionnel, pour futur développement)
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        console.log('Texte copié !');
    }).catch(function(err) {
        console.error('Erreur lors de la copie :', err);
    });
}

// Détecter le thème sombre (optionnel, pour futur développement)
function isDarkMode() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
}

// ===== CONSOLE WELCOME MESSAGE (DEBUG) =====
console.log('%cBienvenue sur le Portfolio BTS SIO ! 🎓', 'font-size: 20px; color: #2563eb; font-weight: bold;');
console.log('%cPour modifier le contenu, éditez les données dans script.js et le HTML.', 'font-size: 12px; color: #64748b;');

// ===== INITIALISATION AU CHARGEMENT DE LA PAGE =====
document.addEventListener('DOMContentLoaded', function() {
    initializeProjectModals();
    initializeContactForm();
    initializeScrollAnimations();
    updateActiveNavLink();
    
    // Mettre à jour la navigation active au scroll
    window.addEventListener('scroll', updateActiveNavLink);
});
