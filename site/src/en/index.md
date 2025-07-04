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
    <div class="projects-grid">
        {% for project in projects | slice(0, 3) %}
        <div class="project-card">
            <h3>{{ project.title.en }}</h3>
            <p>{{ project.description.en }}</p>
            <a href="{{ project.link }}" class="project-link" target="_blank" rel="noopener noreferrer">
                View Project →
            </a>
        </div>
        {% endfor %}
    </div>
</section>

<section>
    <h2>Get in Touch</h2>
    <p>I'm always interested in new opportunities and collaborations. Feel free to reach out if you'd like to work together or just want to say hello!</p>
    <p>
        <a href="{{ author.linkedin }}" target="_blank" rel="noopener noreferrer">Connect with me on LinkedIn</a> or 
        <a href="{{ author.github }}" target="_blank" rel="noopener noreferrer">check out my GitHub</a>
    </p>
</section>
