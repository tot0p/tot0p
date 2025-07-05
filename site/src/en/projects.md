---
layout: layout.njk
title: Projects
lang: en
description: Explore my projects and open-source contributions
---

# My Projects

Here are some of the projects I've been working on. Each represents a different aspect of my interests and skills in software development.

<div class="projects-grid">
    {% for project in projects %}
    <div class="project-card">
        <h3>{{ project.title.en }}</h3>
        <p>{{ project.description.en }}</p>
        <a href="{{ project.link }}" class="project-link" target="_blank" rel="noopener noreferrer">
            View Project →
        </a>
    </div>
    {% endfor %}
</div>

## Open Source Philosophy

I believe in the power of open source software and try to contribute back to the community whenever possible. All of my projects are open source and available on GitHub.

If you find any of my projects useful, feel free to:
- ⭐ Star the repository
- 🐛 Report issues
- 🔧 Submit pull requests
- 💡 Suggest new features


