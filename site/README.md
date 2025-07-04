# Thomas Lemaitre - Personal Portfolio

A bilingual (English/French) static portfolio website built with [Eleventy (11ty)](https://11ty.dev), featuring a modern dark theme and responsive design.

## 🚀 Features

- **Bilingual Support**: Complete English and French versions
- **Dark Theme**: Modern, accessible dark mode design
- **Responsive Design**: Optimized for desktop and mobile
- **Static Site**: Fast loading, SEO-friendly
- **GitHub Pages Ready**: Easy deployment to GitHub Pages

## 🛠️ Technologies Used

- **Eleventy (11ty)**: Static site generator
- **Nunjucks**: Templating engine
- **Markdown**: Content creation
- **CSS3**: Styling with custom properties
- **JSON**: Data management

## 📁 Project Structure

```
src/
├── _data/
│   ├── author.json      # Author information
│   └── projects.json    # Project data
├── _includes/
│   └── layout.njk       # Base layout template
├── css/
│   └── style.css        # Styles and dark theme
├── en/                  # English pages
│   ├── index.md
│   ├── projects.md
│   └── about.md
├── fr/                  # French pages
│   ├── index.md
│   ├── projets.md
│   └── à-propos.md
└── index.md             # Main homepage
```

## 🏃‍♂️ Getting Started

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Run development server**:
   ```bash
   npm run dev
   ```

3. **Build for production**:
   ```bash
   npm run build
   ```

## 🌐 Deployment

The site is configured for GitHub Pages deployment. The built site will be in the `_site` directory.

### GitHub Pages Setup

1. Push your code to a GitHub repository
2. Go to Settings > Pages
3. Select source: GitHub Actions or Deploy from a branch
4. Choose the `_site` folder or set up a GitHub Action for automatic builds

## 🎨 Customization

### Adding Projects

Edit `src/_data/projects.json` to add new projects:

```json
{
  "title": {
    "en": "Project Name",
    "fr": "Nom du Projet"
  },
  "description": {
    "en": "English description",
    "fr": "Description française"
  },
  "link": "https://github.com/username/project"
}
```

### Modifying Author Information

Edit `src/_data/author.json` to update personal information:

```json
{
  "name": "Your Name",
  "email": "your.email@example.com",
  "github": "https://github.com/yourusername",
  "bio": {
    "en": "Your English bio",
    "fr": "Votre bio en français"
  }
}
```

### Theme Customization

The dark theme is defined using CSS custom properties in `src/css/style.css`. You can modify colors by updating the `:root` variables:

```css
:root {
  --bg-primary: #0d1117;
  --text-primary: #e6edf3;
  --text-accent: #58a6ff;
  /* ... other variables */
}
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/tot0p/portfolio/issues).

## 📧 Contact

Thomas Lemaitre - [GitHub](https://github.com/tot0p)
