---
layout: layout.njk
title: Projects
lang: en
description: Explore my projects and open-source contributions
---

<div class="projects-hero">
    <div class="projects-hero-content">
        <h1>My Projects</h1>
        <p class="projects-hero-subtitle">A collection of my work showcasing different aspects of software development, automation, and open-source contributions.</p>
    </div>
</div>

<div class="projects-stats">
    <div class="stat-card">
        <div class="stat-number">{{ projects.length }}</div>
        <div class="stat-label">Projects</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">100%</div>
        <div class="stat-label">Open Source</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">∞</div>
        <div class="stat-label">Learning</div>
    </div>
</div>
<div class="projects-section">
    <div class="section-header">
        <h2>Featured Work</h2>
        <p>Each project represents a unique challenge and learning opportunity</p>
    </div>
    <div class="projects-grid">{% for project in projects %}<div class="project-card">
            <div class="project-card-header">
                <div class="project-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
                    </svg>
                </div>
                <h3>{{ project.title.en }}</h3>
                <div class="project-meta">
                    <span class="project-type">Open Source</span>
                </div>
            </div>
            <div class="project-card-body">
                <p>{{ project.description.en }}</p>
            </div>
            <div class="project-card-footer">
                <a href="{{ project.link }}" class="project-link primary" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/>
                    </svg>
                    View Project
                </a>
                <a href="{{ project.link }}" class="project-link secondary" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 00-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0020 4.77 5.07 5.07 0 0019.91 1S18.73.65 16 2.48a13.38 13.38 0 00-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 005 4.77a5.44 5.44 0 00-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 009 18.13V22"/>
                    </svg>
                    Source Code
                </a>
            </div>
        </div>{% endfor %}</div>
</div>
<div class="projects-cta">
    <div class="cta-content">
        <h2>Open Source Philosophy</h2>
        <p>I believe in the power of open source software and try to contribute back to the community whenever possible. All of my projects are open source and available on GitHub.</p>
        
        <div class="cta-features">
            <div class="cta-feature">
                <div class="cta-icon">⭐</div>
                <div class="cta-text">
                    <h3>Star Projects</h3>
                    <p>Show your support by starring repositories you find useful</p>
                </div>
            </div>
            <div class="cta-feature">
                <div class="cta-icon">🐛</div>
                <div class="cta-text">
                    <h3>Report Issues</h3>
                    <p>Help improve the projects by reporting bugs and issues</p>
                </div>
            </div>
            <div class="cta-feature">
                <div class="cta-icon">🔧</div>
                <div class="cta-text">
                    <h3>Contribute</h3>
                    <p>Submit pull requests and help make the projects better</p>
                </div>
            </div>
            <div class="cta-feature">
                <div class="cta-icon">💡</div>
                <div class="cta-text">
                    <h3>Share Ideas</h3>
                    <p>Suggest new features and improvements</p>
                </div>
            </div>
        </div>
        
        <div class="cta-buttons">
            <a href="{{ author.github }}" class="cta-button primary" target="_blank" rel="noopener noreferrer">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 00-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0020 4.77 5.07 5.07 0 0019.91 1S18.73.65 16 2.48a13.38 13.38 0 00-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 005 4.77a5.44 5.44 0 00-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 009 18.13V22"/>
                </svg>
                View All on GitHub
            </a>
            <a href="/en/about/" class="cta-button secondary">
                Learn More About Me
            </a>
        </div>
    </div>
</div>