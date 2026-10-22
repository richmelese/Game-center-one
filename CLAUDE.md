# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Games Hub** — a curated collection of 142+ playable HTML5 browser games, deployed as a zero-build static site to GitHub Pages. No Node.js, no bundler, no build step.

Live site: `https://sausi-7.github.io/games/`

## Architecture

### Entry Points
- `index.html` — minimal HTML shell; all content is rendered by JavaScript
- `site/app.js` — all landing page logic (~500 lines): registry fetch, card grid, modal iframe player, search/filter, i18n, theme toggle
- `site/styles.css` — all styles; theming via CSS variables on `data-theme` attribute
- `games/registry.json` — single source of truth for all games and category definitions

### How It Works
1. `site/app.js` fetches `games/registry.json` on load
2. Renders a filterable card grid (real-time search by name/tags/category)
3. Clicking a card opens the game in a sandboxed `<iframe>` modal
4. Deep linking via URL hash: `#play=<slug>` auto-opens a game

### Game Structure
Each game lives at `games/<category>/<slug>/`:
```
games/arcade/snake/
  index.html      # required; loaded in iframe; must use relative paths
  assets/         # images, audio (keep total < 5MB)
  mechanics.js    # game logic (optional split)
  config.json     # optional game-specific config
```

### Registry Entry Schema
```json
{
  "slug": "snake",
  "name": "Snake",
  "category": "arcade",
  "path": "games/arcade/snake/index.html",
  "tech": "phaser",
  "tags": ["classic", "arcade"],
  "description": "~80 char pitch"
}
```
Valid `tech` values: `phaser` | `three` | `html`  
Valid categories: `arcade`, `puzzle`, `shooter`, `racing`, `sports`, `platformer`, `casual`, `board`, `word-quiz`, `3d`

## Development

**No build step.** Open `index.html` directly in a browser, or serve it with any static file server:

```bash
# Python
python -m http.server 8080

# Node (if available)
npx serve .
```

There are no tests, no linter config, and no package.json. Validate changes by opening the site in a browser and checking the browser console for errors.

## Code Style

- Vanilla JS only — no TypeScript, no React, no framework
- 2-space indentation, double quotes
- All CDN libraries (Phaser 3, Three.js) are loaded via `<script>` tags; never install them locally

## Adding a Game

1. Create `games/<category>/<slug>/index.html` (and supporting files)
2. Add an entry to `games/registry.json`
3. Game `index.html` must use **relative paths only** — it runs inside an iframe

## Deployment

Push to `main` → GitHub Actions (`.github/workflows/pages.yml`) uploads the entire repo to GitHub Pages. No manual deploy steps.

## i18n

The landing page supports English (`en`) and Hindi (`hi`). Translation strings live inside `site/app.js` in the `TRANSLATIONS` object. Add new strings to both locales.
