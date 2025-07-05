---
layout: layout.njk
title: Projets
lang: fr
description: Explorez mes projets et contributions open-source
---
<div class="projects-hero">
    <div class="projects-hero-content">
        <h1>Mes Projets</h1>
        <p class="projects-hero-subtitle">Une collection de mes travaux présentant différents aspects du développement logiciel, de l'automatisation et des contributions open-source.</p>
    </div>
</div>
<div class="projects-stats">
    <div class="stat-card">
        <div class="stat-number">{{ projects.length }}</div>
        <div class="stat-label">Projets</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">100%</div>
        <div class="stat-label">Open Source</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">∞</div>
        <div class="stat-label">Apprentissage</div>
    </div>
</div>
<div class="projects-section">
    <div class="section-header">
        <h2>Travaux Sélectionnés</h2>
        <p>Chaque projet représente un défi unique et une opportunité d'apprentissage</p>
    </div>
    <div class="projects-grid">{% for project in projects %}<div class="project-card">
            <div class="project-card-header">
                <div class="project-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
                    </svg>
                </div>
                <h3>{{ project.title.fr }}</h3>
                <div class="project-meta">
                    <span class="project-type">Open Source</span>
                </div>
            </div>
            <div class="project-card-body">
                <p>{{ project.description.fr }}</p>
                <div class="project-features">
                    <h4>Fonctionnalités Clés :</h4>
                    <ul>
                        <li>Intégration GitHub Actions</li>
                        <li>Workflows automatisés</li>
                        <li>Outils pour développeurs</li>
                    </ul>
                </div>
            </div>
            <div class="project-card-footer">
                <a href="{{ project.link }}" class="project-link primary" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/>
                    </svg>
                    Voir le Projet
                </a>
                <a href="{{ project.link }}" class="project-link secondary" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 00-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0020 4.77 5.07 5.07 0 0019.91 1S18.73.65 16 2.48a13.38 13.38 0 00-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 005 4.77a5.44 5.44 0 00-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 009 18.13V22"/>
                    </svg>
                    Code Source
                </a>
            </div>
        </div>{% endfor %}</div>
</div>
<div class="projects-cta">
    <div class="cta-content">
        <h2>Philosophie Open Source</h2>
        <p>Je crois au pouvoir des logiciels open source et j'essaie de contribuer à la communauté chaque fois que possible. Tous mes projets sont open source et disponibles sur GitHub.</p>
        <div class="cta-features">
            <div class="cta-feature">
                <div class="cta-icon">⭐</div>
                <div class="cta-text">
                    <h3>Mettre une Étoile</h3>
                    <p>Montrez votre soutien en mettant une étoile aux dépôts que vous trouvez utiles</p>
                </div>
            </div>
            <div class="cta-feature">
                <div class="cta-icon">🐛</div>
                <div class="cta-text">
                    <h3>Signaler des Problèmes</h3>
                    <p>Aidez à améliorer les projets en signalant les bugs et problèmes</p>
                </div>
            </div>
            <div class="cta-feature">
                <div class="cta-icon">🔧</div>
                <div class="cta-text">
                    <h3>Contribuer</h3>
                    <p>Soumettez des pull requests et aidez à améliorer les projets</p>
                </div>
            </div>
            <div class="cta-feature">
                <div class="cta-icon">💡</div>
                <div class="cta-text">
                    <h3>Partager des Idées</h3>
                    <p>Suggérez de nouvelles fonctionnalités et améliorations</p>
                </div>
            </div>
        </div>
        <div class="cta-buttons">
            <a href="{{ author.github }}" class="cta-button primary" target="_blank" rel="noopener noreferrer">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 00-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0020 4.77 5.07 5.07 0 0019.91 1S18.73.65 16 2.48a13.38 13.38 0 00-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 005 4.77a5.44 5.44 0 00-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 009 18.13V22"/>
                </svg>
                Voir Tout sur GitHub
            </a>
            <a href="/fr/about/" class="cta-button secondary">
                En Savoir Plus Sur Moi
            </a>
        </div>
    </div>
</div>