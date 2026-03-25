#!/usr/bin/env python3
"""Generate all premium HTML pages for Cyprien's portfolio."""

import os

BASE_DIR = os.path.dirname(__file__)

# Template HTML structure for pages
NAV_TEMPLATE = '''    <!-- NAVBAR -->
    <nav class="sticky top-0 z-50 bg-zinc-950/80 backdrop-blur-md border-b border-zinc-800">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <div class="flex-shrink-0">
                    <a href="index.html" class="text-sm font-bold text-zinc-50">CC</a>
                </div>
                <div class="hidden md:flex items-center gap-8">
                    <a href="index.html" class="text-sm text-zinc-400 hover:text-zinc-50 transition-colors">Accueil</a>
                    <a href="bts-sio.html" class="text-sm text-zinc-400 hover:text-zinc-50 transition-colors">BTS SIO</a>
                    <a href="a-propos.html" class="text-sm text-zinc-400 hover:text-zinc-50 transition-colors">À propos</a>
                    <a href="competences.html" class="text-sm text-zinc-400 hover:text-zinc-50 transition-colors">Compétences</a>
                    <a href="projets.html" class="text-sm text-zinc-400 hover:text-zinc-50 transition-colors">Projets</a>
                    <a href="certifications.html" class="text-sm text-zinc-400 hover:text-zinc-50 transition-colors">Certifications</a>
                    <a href="contact.html" class="text-sm text-zinc-400 hover:text-zinc-50 transition-colors">Contact</a>
                </div>
                <button id="mobileMenuBtn" class="md:hidden text-zinc-50">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                </button>
            </div>
        </div>
        <div id="mobileMenu" class="hidden md:hidden border-t border-zinc-800 bg-zinc-900/50 backdrop-blur">
            <div class="px-4 py-4 space-y-2">
                <a href="index.html" class="block text-sm text-zinc-400 hover:text-zinc-50 py-2">Accueil</a>
                <a href="bts-sio.html" class="block text-sm text-zinc-400 hover:text-zinc-50 py-2">BTS SIO</a>
                <a href="a-propos.html" class="block text-sm text-zinc-400 hover:text-zinc-50 py-2">À propos</a>
                <a href="competences.html" class="block text-sm text-zinc-400 hover:text-zinc-50 py-2">Compétences</a>
                <a href="projets.html" class="block text-sm text-zinc-400 hover:text-zinc-50 py-2">Projets</a>
                <a href="certifications.html" class="block text-sm text-zinc-400 hover:text-zinc-50 py-2">Certifications</a>
                <a href="contact.html" class="block text-sm text-zinc-400 hover:text-zinc-50 py-2">Contact</a>
            </div>
        </div>
    </nav>'''

FOOTER_TEMPLATE = '''    <!-- FOOTER -->
    <footer class="border-t border-zinc-800 bg-zinc-900/50 py-12">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-3 gap-8 mb-8">
                <div>
                    <p class="font-semibold text-zinc-50 mb-2">Cyprien Cavoli</p>
                    <p class="text-sm text-zinc-400">BTS SIO • SISR • Grenoble</p>
                </div>
                <div>
                    <p class="font-semibold text-zinc-50 mb-3">Navigation</p>
                    <nav class="space-y-1 text-sm">
                        <a href="index.html" class="text-zinc-400 hover:text-zinc-50 transition-colors block">Accueil</a>
                        <a href="projets.html" class="text-zinc-400 hover:text-zinc-50 transition-colors block">Projets</a>
                        <a href="competences.html" class="text-zinc-400 hover:text-zinc-50 transition-colors block">Compétences</a>
                        <a href="contact.html" class="text-zinc-400 hover:text-zinc-50 transition-colors block">Contact</a>
                    </nav>
                </div>
                <div>
                    <p class="font-semibold text-zinc-50 mb-3">Réseaux</p>
                    <div class="flex gap-4">
                        <a href="https://www.linkedin.com/in/cyprien-cavoli/" target="_blank" class="w-9 h-9 rounded bg-zinc-800 text-zinc-400 hover:text-cyan-400 hover:bg-zinc-700 transition-colors flex items-center justify-center">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.475-2.236-1.986-2.236-1.081 0-1.722.728-2.004 1.431-.103.25-.129.599-.129.948v5.426h-3.554s.05-8.814 0-9.737h3.554v1.375c.43-.664 1.199-1.61 2.92-1.61 2.135 0 3.736 1.395 3.736 4.393v5.579zM5.337 8.855c-1.144 0-1.915-.759-1.915-1.71 0-.956.769-1.71 1.956-1.71 1.187 0 1.915.754 1.948 1.71 0 .951-.768 1.71-1.989 1.71zm1.581 11.597H3.751V9.567h3.167v10.885zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0"/></svg>
                        </a>
                    </div>
                </div>
            </div>
            <div class="border-t border-zinc-800 pt-8 text-center text-sm text-zinc-500">
                <p>© 2026 Cyprien Cavoli. Lycée Louise Michel, Grenoble.</p>
            </div>
        </div>
    </footer>

    <script>
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        const mobileMenu = document.getElementById('mobileMenu');

        mobileMenuBtn?.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });

        document.querySelectorAll('#mobileMenu a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
            });
        });

        const revealElements = document.querySelectorAll('[data-reveal]');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.animation = 'fade-up 0.6s ease-out';
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        revealElements.forEach(el => {
            el.style.opacity = '0';
            observer.observe(el);
        });

        const currentPage = window.location.pathname.split('/').pop() || 'index.html';
        document.querySelectorAll('nav a').forEach(link => {
            const href = link.getAttribute('href');
            if (href === currentPage) {
                link.classList.add('text-zinc-50', 'font-semibold');
                link.classList.remove('text-zinc-400');
            }
        });
    </script>
</body>
</html>'''

HEAD_TEMPLATE = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style type="text/tailwindcss">
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

        @layer base {{
            * {{ text-decoration: none !important; }}
            *::before, *::after {{ text-decoration: none !important; }}
            a {{ text-decoration: none !important; }}
            a:hover {{ text-decoration: none !important; }}
            button {{ text-decoration: none !important; }}
            body {{ font-family: 'Inter', sans-serif; @apply bg-zinc-950 text-zinc-50; }}
        }}

        @keyframes fade-up {{
            from {{ opacity: 0; transform: translateY(24px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .animate-fade-up {{ animation: fade-up 0.6s ease-out forwards; }}
        .delay-100 {{ animation-delay: 100ms; }}
        .delay-200 {{ animation-delay: 200ms; }}
        .delay-300 {{ animation-delay: 300ms; }}
    </style>
</head>
<body class="bg-zinc-950 text-zinc-50 overflow-x-hidden">'''

# Page Content Templates
pages = {
    'a-propos.html': ('À Propos — Cyprien Cavoli', '''<section class="py-20 border-b border-zinc-800">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 class="text-5xl font-bold mb-6">À propos</h1>
            <p class="text-xl text-zinc-400 max-w-3xl">Étudiant passionné par technologie, infrastructure et cybersécurité. Décourez mon parcours, mes valeurs et mes ambitions.</p>
        </div>
    </section>
    <main>
        <section class="py-16" data-reveal>
            <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div class="grid md:grid-cols-2 gap-12 mb-16">
                    <div>
                        <h2 class="text-3xl font-bold mb-6">Qui suis-je?</h2>
                        <p class="text-zinc-400 mb-4 leading-relaxed">Je suis Cyprien Cavoli, étudiant en BTS SIO parcours SISR au lycée Louise Michel à Grenoble. Passionné par l'informatique, je me concentre sur l'infrastructure, la cybersécurité et l'automatisation.</p>
                        <p class="text-zinc-400 leading-relaxed">Rigoureux et curieux, j'aime relever des défis techniques et apprendre continuellement pour évoluer dans ce domaine en constante évolution.</p>
                    </div>
                    <div class="space-y-4">
                        <div class="p-4 rounded-lg bg-zinc-900 border border-zinc-800">
                            <p class="text-sm text-cyan-400 font-semibold mb-1">Localisation</p>
                            <p class="text-zinc-50">Grenoble (38000), France</p>
                        </div>
                        <div class="p-4 rounded-lg bg-zinc-900 border border-zinc-800">
                            <p class="text-sm text-indigo-400 font-semibold mb-1">Email</p>
                            <p class="text-zinc-50"><a href="mailto:cyprien.cavoli@gmail.com">cyprien.cavoli@gmail.com</a></p>
                        </div>
                        <div class="p-4 rounded-lg bg-zinc-900 border border-zinc-800">
                            <p class="text-sm text-cyan-400 font-semibold mb-1">Téléphone</p>
                            <p class="text-zinc-50">07 83 84 32 41</p>
                        </div>
                    </div>
                </div>
                <div class="p-8 rounded-lg bg-zinc-900/50 border border-zinc-800">
                    <h3 class="text-2xl font-bold mb-6">Mon parcours</h3>
                    <ul class="space-y-4 text-zinc-400">
                        <li class="flex gap-4">
                            <span class="text-cyan-400 font-semibold min-w-fit">2023-2025:</span>
                            <span>BTS SIO SISR au Lycée Louise Michel, Grenoble</span>
                        </li>
                        <li class="flex gap-4">
                            <span class="text-indigo-400 font-semibold min-w-fit">2022-2023:</span>
                            <span>Bac Pro Systèmes Numériques (mention Bien) - Lycée Vaucanson</span>
                        </li>
                        <li class="flex gap-4">
                            <span class="text-cyan-400 font-semibold min-w-fit">2020-2022:</span>
                            <span>Première & Terminale - Systèmes Numériques - Lycée Vaucanson</span>
                        </li>
                    </ul>
                </div>
            </div>
        </section>
    </main>'''),

    'projets.html': ('Projets — Cyprien Cavoli', '''<section class="py-20 border-b border-zinc-800">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 class="text-5xl font-bold mb-6">Projets</h1>
            <p class="text-xl text-zinc-400 max-w-3xl">Une sélection de projets techniques réalisés en cours et en pério stages en entreprise.</p>
        </div>
    </section>
    <main>
        <section class="py-16" data-reveal>
            <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div class="p-6 rounded-lg bg-zinc-900 border border-zinc-800 hover:border-zinc-700 transition-all delay-100 animate-fade-up">
                        <div class="w-12 h-12 rounded-lg bg-cyan-400/10 border border-cyan-400/30 flex items-center justify-center mb-4">
                            <svg class="w-6 h-6 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                        </div>
                        <h3 class="font-semibold mb-2">Déploiement AD</h3>
                        <p class="text-sm text-zinc-400 mb-4">Infrastructure Active Directory avec GPO, authentification centralisée et gestion des ressources</p>
                        <p class="text-xs text-zinc-500">Windows Server • PowerShell</p>
                    </div>
                    <div class="p-6 rounded-lg bg-zinc-900 border border-zinc-800 hover:border-zinc-700 transition-all delay-200 animate-fade-up">
                        <div class="w-12 h-12 rounded-lg bg-indigo-400/10 border border-indigo-400/30 flex items-center justify-center mb-4">
                            <svg class="w-6 h-6 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
                        </div>
                        <h3 class="font-semibold mb-2">Sécurisation Info</h3>
                        <p class="text-sm text-zinc-400 mb-4">Audit sécurité, configurati firewall et hardening système selon normes RGPD</p>
                        <p class="text-xs text-zinc-500">Cybersécurité • Compliance</p>
                    </div>
                    <div class="p-6 rounded-lg bg-zinc-900 border border-zinc-800 hover:border-zinc-700 transition-all delay-300 animate-fade-up">
                        <div class="w-12 h-12 rounded-lg bg-cyan-400/10 border border-cyan-400/30 flex items-center justify-center mb-4">
                            <svg class="w-6 h-6 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                        </div>
                        <h3 class="font-semibold mb-2">Automatisation</h3>
                        <p class="text-sm text-zinc-400 mb-4">Scripts PowerShell et Python pour déploiement automatisé et monitoring</p>
                        <p class="text-xs text-zinc-500">PowerShell • Python</p>
                    </div>
                </div>
            </div>
        </section>
    </main>'''),

    'competences.html': ('Compétences — Cyprien Cavoli', '''<section class="py-20 border-b border-zinc-800">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 class="text-5xl font-bold mb-6">Compétences</h1>
            <p class="text-xl text-zinc-400 max-w-3xl">Maîtrise techniques dans les domaines des systèmes, réseaux et sécurité informatique.</p>
        </div>
    </section>
    <main>
        <section class="py-16 bg-zinc-900/50" data-reveal>
            <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div class="grid md:grid-cols-3 gap-8">
                    <div class="delay-100 animate-fade-up">
                        <h3 class="text-xl font-semibold mb-4 text-cyan-400">Systèmes</h3>
                        <ul class="space-y-2 text-zinc-400 text-sm">
                            <li>✓ Windows Server 2019/2022</li>
                            <li>✓ Active Directory & GPO</li>
                            <li>✓ Linux (Debian, Ubuntu)</li>
                            <li>✓ Hyper-V & Proxmox</li>
                            <li>✓ Backup & DR</li>
                        </ul>
                    </div>
                    <div class="delay-200 animate-fade-up">
                        <h3 class="text-xl font-semibold mb-4 text-indigo-400">Réseaux</h3>
                        <ul class="space-y-2 text-zinc-400 text-sm">
                            <li>✓ TCP/IP & Protocols</li>
                            <li>✓ Routage & Switching</li>
                            <li>✓ Firewall & NAT</li>
                            <li>✓ VPN & Tunneling</li>
                            <li>✓ DNS & DHCP</li>
                        </ul>
                    </div>
                    <div class="delay-300 animate-fade-up">
                        <h3 class="text-xl font-semibold mb-4 text-cyan-400">Autres</h3>
                        <ul class="space-y-2 text-zinc-400 text-sm">
                            <li>✓ PowerShell & Bash</li>
                            <li>✓ Python</li>
                            <li>✓ HTML/CSS/JS</li>
                            <li>✓ Cybersécurité</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
    </main>'''),

    'certifications.html': ('Certifications — Cyprien Cavoli', '''<section class="py-20 border-b border-zinc-800">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 class="text-5xl font-bold mb-6">Certifications</h1>
            <p class="text-xl text-zinc-400 max-w-3xl">Reconnaissances professionnelles et diplômes obtenus.</p>
        </div>
    </section>
    <main>
        <section class="py-16" data-reveal>
            <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div class="space-y-4">
                    <div class="p-6 rounded-lg bg-zinc-900 border border-zinc-800 delay-100 animate-fade-up">
                        <div class="flex items-start justify-between">
                            <div>
                                <h3 class="font-semibold text-lg">Baccalauréat Professionnel Systèmes Numériques</h3>
                                <p class="text-sm text-zinc-400 mt-1">Lycée Vaucanson, Grenoble • 2023 • Mention Bien</p>
                            </div>
                            <span class="px-3 py-1 text-xs bg-cyan-400/10 border border-cyan-400/30 text-cyan-400 rounded">Diplôme</span>
                        </div>
                    </div>
                    <div class="p-6 rounded-lg bg-zinc-900 border border-zinc-800 delay-200 animate-fade-up">
                        <div class="flex items-start justify-between">
                            <div>
                                <h3 class="font-semibold text-lg">BTS SIO Option SISR</h3>
                                <p class="text-sm text-zinc-400 mt-1">Lycée Louise Michel, Grenoble • 2023-2025 (en cours)</p>
                            </div>
                            <span class="px-3 py-1 text-xs bg-indigo-400/10 border border-indigo-400/30 text-indigo-400 rounded">Formation</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>'''),

    'contact.html': ('Contact — Cyprien Cavoli', '''<section class="py-20 border-b border-zinc-800">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 class="text-5xl font-bold mb-6">Contact</h1>
            <p class="text-xl text-zinc-400 max-w-3xl">Contactez-moi pour discuter de projets, collaborations ou opportunités.</p>
        </div>
    </section>
    <main>
        <section class="py-16" data-reveal>
            <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div class="grid md:grid-cols-2 gap-12">
                    <div class="space-y-6">
                        <div class="p-6 rounded-lg bg-zinc-900 border border-zinc-800">
                            <p class="text-sm text-zinc-400 mb-2">Email</p>
                            <a href="mailto:cyprien.cavoli@gmail.com" class="text-lg font-semibold text-cyan-400 hover:text-cyan-300">cyprien.cavoli@gmail.com</a>
                        </div>
                        <div class="p-6 rounded-lg bg-zinc-900 border border-zinc-800">
                            <p class="text-sm text-zinc-400 mb-2">Téléphone</p>
                            <a href="tel:+33783843241" class="text-lg font-semibold text-indigo-400 hover:text-indigo-300">07 83 84 32 41</a>
                        </div>
                        <div class="p-6 rounded-lg bg-zinc-900 border border-zinc-800">
                            <p class="text-sm text-zinc-400 mb-4">Réseaux</p>
                            <div class="flex gap-3">
                                <a href="https://www.linkedin.com/in/cyprien-cavoli/" target="_blank" class="px-4 py-2 rounded bg-zinc-800 hover:bg-zinc-700 text-sm transition-colors">LinkedIn</a>
                            </div>
                        </div>
                    </div>
                    <div class="p-8 rounded-lg bg-zinc-900 border border-zinc-800">
                        <h3 class="text-xl font-semibold mb-6">Message rapide</h3>
                        <p class="text-sm text-zinc-400 mb-6">Vous pouvez aussi me contacter directement via email ou téléphone.</p>
                        <div class="space-y-4">
                            <div>
                                <label class="text-sm font-medium text-zinc-300 block mb-2">Votre nom</label>
                                <input type="text" placeholder="Votre nom" class="w-full px-4 py-2 rounded bg-zinc-800 border border-zinc-700 text-zinc-50 placeholder-zinc-500">
                            </div>
                            <div>
                                <label class="text-sm font-medium text-zinc-300 block mb-2">Votre email</label>
                                <input type="email" placeholder="votre@email.com" class="w-full px-4 py-2 rounded bg-zinc-800 border border-zinc-700 text-zinc-50 placeholder-zinc-500">
                            </div>
                            <div>
                                <label class="text-sm font-medium text-zinc-300 block mb-2">Message</label>
                                <textarea placeholder="Votre message..." rows="4" class="w-full px-4 py-2 rounded bg-zinc-800 border border-zinc-700 text-zinc-50 placeholder-zinc-500 resize-none"></textarea>
                            </div>
                            <button class="w-full px-4 py-2 bg-gradient-to-r from-cyan-400 to-indigo-400 text-zinc-950 font-medium rounded hover:shadow-lg hover:shadow-cyan-400/20 transition-shadow">Envoyer</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>'''),

    'cv.html': ('CV — Cyprien Cavoli', '''<section class="py-20 border-b border-zinc-800">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 class="text-5xl font-bold mb-6">Curriculum Vitae</h1>
            <p class="text-xl text-zinc-400 max-w-3xl">Mon parcours professionnel et académique.</p>
            <div class="mt-8">
                <a href="assets/cv/CV_Cyprien_Cavoli.pdf" target="_blank" class="inline-block px-6 py-3 bg-gradient-to-r from-cyan-400 to-indigo-400 text-zinc-950 font-medium rounded-lg hover:shadow-lg">
                    ⬇ Télécharger le CV (PDF)
                </a>
            </div>
        </div>
    </section>
    <main>
        <section class="py-16" data-reveal>
            <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div class="space-y-12">
                    <div>
                        <h2 class="text-2xl font-bold mb-6">Formation</h2>
                        <div class="space-y-4">
                            <div class="p-6 rounded-lg bg-zinc-900 border border-zinc-800">
                                <div class="flex justify-between items-start mb-2">
                                    <h3 class="font-semibold">BTS SIO Option SISR</h3>
                                    <span class="text-sm text-zinc-500">2023 - 2025</span>
                                </div>
                                <p class="text-zinc-400">Lycée Louise Michel, Grenoble</p>
                            </div>
                            <div class="p-6 rounded-lg bg-zinc-900 border border-zinc-800">
                                <div class="flex justify-between items-start mb-2">
                                    <h3 class="font-semibold">Bac Pro Systèmes Numériques</h3>
                                    <span class="text-sm text-zinc-500">2023</span>
                                </div>
                                <p class="text-zinc-400">Lycée Vaucanson, Grenoble (Mention Bien)</p>
                            </div>
                        </div>
                    </div>
                    <div>
                        <h2 class="text-2xl font-bold mb-6">Expérience</h2>
                        <p class="text-zinc-400">Stages et missions en cours. Consultez le PDF pour plus de détails.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>'''),
}

# Generate all pages
for filename, (title, content) in pages.items():
    filepath = os.path.join(BASE_DIR, filename)
    html_content = HEAD_TEMPLATE.format(title=title) + '\n' + NAV_TEMPLATE + '\n' + content + '\n' + FOOTER_TEMPLATE
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✓ {filename}")

print("\n✓ All pages generated successfully!")
