---
layout: layout.njk
title: Accueil
lang: fr
description: Portfolio personnel de Thomas Lemaitre - Développeur, Créateur, Passionné d'Open Source
---

<div class="hero">
    <h1>Salut, je suis {{ author.name }}</h1>
    <p>{{ author.bio.fr }}</p>
</div>

<section>
    <h2>Projets En Vedette</h2>
    <div class="projects-grid">
        {% for project in projects | slice(0, 3) %}
        <div class="project-card">
            <h3>{{ project.title.fr }}</h3>
            <p>{{ project.description.fr }}</p>
            <a href="{{ project.link }}" class="project-link" target="_blank" rel="noopener noreferrer">
                Voir le Projet →
            </a>
        </div>
        {% endfor %}
    </div>
</section>

<section>
    <h2>Me Contacter</h2>
    <p>Je suis toujours intéressé par de nouvelles opportunités et collaborations. N'hésitez pas à me contacter si vous souhaitez travailler ensemble ou simplement dire bonjour !</p>
    <p>
        <a href="{{ author.linkedin }}" target="_blank" rel="noopener noreferrer">Connectez-vous avec moi sur LinkedIn</a> ou 
        <a href="{{ author.github }}" target="_blank" rel="noopener noreferrer">consultez mon GitHub</a>
    </p>
</section>
