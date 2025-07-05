---
layout: layout.njk
title: Home
lang: en
description: Personal portfolio of Thomas Lemaitre - Developer, Creator, Open Source Enthusiast
---

<div class="hero">
    <h1>Hi, I'm {{ author.name }}</h1>
    <p>{{ author.bio.en }}</p>
</div>

<section>
    <h2>Featured Projects</h2>
    <div class="projects-grid">{% for project in projects %}{% if loop.index <= 3 %}<div class="project-card">
            <div class="project-card-header">
                <h3>{{ project.title.en }}</h3>
            </div>
            <div class="project-card-body">
                <p>{{ project.description.en }}</p>
            </div>
            <div class="project-card-footer">
                <a href="{{ project.link }}" class="project-link" target="_blank" rel="noopener noreferrer">
                    View Project
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M7 17L17 7M17 7H7M17 7V17"/>
                    </svg>
                </a>
            </div>
        </div>{% endif %}{% endfor %}</div>
</section>

<section>
    <h2>Get in Touch</h2>
    <p>I'm always interested in new opportunities and collaborations. Feel free to reach out if you'd like to work together or just want to say hello!</p>
    <p>
        <a href="{{ author.linkedin }}" target="_blank" rel="noopener noreferrer">Connect with me on LinkedIn</a> or 
        <a href="{{ author.github }}" target="_blank" rel="noopener noreferrer">check out my GitHub</a>
    </p>
</section>
