# Shield Guard

A security-focused blog built with Jekyll and the Minimal Mistakes theme, deployed on GitHub Pages.

## Local Development

To run this site locally:

1. Install Ruby and Bundler
2. Install dependencies: `bundle install`
3. Start the development server: `bundle exec jekyll serve`
4. Open your browser to `http://localhost:4000`

## GitHub Pages Deployment

### Step 1: Clone the Repository

```bash
# Clone the Shield Guard repository
git clone https://github.com/Axon-Shield/shield-guard.github.io.git
cd shield-guard.github.io
```

### Step 2: Add Your Content and Push

```bash
# Add all files
git add .

# Commit your changes
git commit -m "Update Jekyll site with blog posts"

# Push to GitHub
git push origin main
```

### Step 3: GitHub Pages is Auto-Configured

The site is already configured for GitHub Pages and will be automatically available at:
`https://axon-shield.github.io`

**Note:** Since this uses the `shield-guard.github.io` repository name, GitHub Pages will automatically serve it as an organization site.

## Adding Content

### Blog Posts

Create new files in `_posts/` with the format: `YYYY-MM-DD-title.md`

Each post will be available at: `https://axon-shield.github.io/post-title/` (slug format)

### Customization

- Edit `_config.yml` for site settings
- Modify layouts in `_layouts/` (if you create custom ones)
- Add custom CSS in `assets/css/main.scss`
- Update author bio and social links in `_config.yml`

## Documentation

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Minimal Mistakes Theme Documentation](https://mmistakes.github.io/minimal-mistakes/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
