---
layout: layout.njk
title: Projets
lang: fr
description: Explorez mes projets et contributions open-source
---

# Mes Projets

Voici quelques-uns des projets sur lesquels j'ai travaillé. Chacun représente un aspect différent de mes intérêts et compétences en développement logiciel.

<div class="projects-grid">
    {% for project in projects %}
    <div class="project-card">
        <h3>{{ project.title.fr }}</h3>
        <p>{{ project.description.fr }}</p>
        <a href="{{ project.link }}" class="project-link" target="_blank" rel="noopener noreferrer">
            Voir le Projet →
        </a>
    </div>
    {% endfor %}
</div>

## Philosophie Open Source

Je crois au pouvoir des logiciels open source et j'essaie de contribuer à la communauté chaque fois que possible. Tous mes projets sont open source et disponibles sur GitHub.

Si vous trouvez mes projets utiles, n'hésitez pas à :
- ⭐ Mettre une étoile au dépôt
- 🐛 Signaler des problèmes
- 🔧 Soumettre des pull requests
- 💡 Suggérer de nouvelles fonctionnalités

