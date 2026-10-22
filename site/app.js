/* =========================================================
   Ethio Telecom Games Portal — Application Logic
   ========================================================= */

const DEFAULT_LOCALE = "en";
const LOCALE_STORAGE_KEY = "ethio_telecom_language";

const I18N = {
  en: {
    "brand.name": "ethio telecom",
    "hero.badge": "CONNECTING YOUR POTENTIAL",
    "hero.titleLine1": "140+ Playable Games.",
    "hero.titleLine2": "Powered by Ethio Telecom.",
    "hero.subtitle": "Explore our rich digital gaming universe directly on your phone or PC. Instant play, zero installs, pure entertainment.",
    "cta.playRandom": "Play Random",
    "cta.browseAll": "Browse Catalog",
    "btn.qryPPText": "Qry PP of your phone",
    "btn.modifyInfoText": "Modify Information",
    "search.placeholder": "Search games — name, tag, category…",
    "empty.noMatches": "No games match your search criteria.",
    "empty.clearFilters": "Clear filters",
    "footer.licensed": "© Ethio Telecom. All rights reserved. Connecting your entertainment potential.",
    "footer.language": "Language:",
    "footer.press": "Press",
    "footer.toSearch": "to search",
    "footer.toClose": "to close game",
    "footer.forRandom": "for random game",
    "footer.aboutDesc": "Ethiopia's premier digital entertainment portal. Play 140+ games instantly on any device with zero downloads.",
    "footer.linksTitle": "Quick Links",
    "footer.linkCatalog": "140+ Games Catalog",
    "footer.linkCategories": "Browse Categories",
    "footer.linkRandom": "Play Random Game",
    "footer.servicesTitle": "Telecom & Connectivity",
    "footer.servInstant": "Instant Play · No Install",
    "footer.serv4g": "Optimized for 4G & 5G",
    "footer.servSupport": "Customer Support: 994",
    "footer.shortcutsTitle": "Shortcuts",
    "footer.backToTop": "Back to Top ↑",
    "footer.helpline": "Ethio Telecom · Addis Ababa, Ethiopia · Helpline: 994",
    "modal.defaultTitle": "—",
    "aria.toggleTheme": "Toggle color mode",
    "aria.filterGames": "Filter games",
    "aria.categories": "Categories",
    "aria.toggleFullscreen": "Toggle fullscreen",
    "aria.restartGame": "Restart game",
    "aria.openInNewTab": "Open in new tab",
    "aria.close": "Close",
    "title.fullscreen": "Fullscreen",
    "title.restart": "Restart",
    "title.openInNewTab": "Open in new tab",
    "title.close": "Close",
    "title.game": "Game",
    "nav.catalog": "All Games",
    "nav.categories": "Categories",
    "title.forRandom": "Play a random game (Shortcut: R)",
    "errors.registryLoad": "Couldn't load games registry. Please ensure the local server is running.",
    "stats.games": "games",
    "filters.all": "All",
    "card.tech.phaser": "Phaser",
    "card.tech.three": "Three.js",
    "card.tech.html": "HTML5",
    "card.aria.play": "Play {name}",
  },
  am: {
    "brand.name": "ኢትዮ ቴሌኮም",
    "hero.badge": "አቅምዎን እናገናኛለን",
    "hero.titleLine1": "140+ የሚጫወቱ ጌሞች።",
    "hero.titleLine2": "በኢትዮ ቴሌኮም የቀረበ።",
    "hero.subtitle": "በስልክዎ ወይም በኮምፒውተርዎ ያለምንም ጭነት ወዲያውኑ የሚጫወቱዋቸው የHTML5 እና 3D ጌሞች ስብስብ።",
    "cta.playRandom": "በዕድል ይጫወቱ",
    "cta.browseAll": "ሁሉንም ይመልከቱ",
    "nav.catalog": "ሁሉም ጌሞች",
    "nav.categories": "የጌም ምድቦች",
    "title.forRandom": "በዕድል ጌም ይጫወቱ (አቋራጭ: R)",
    "btn.qryPPText": "የስልክ ጥቅል ይፈልጉ (Qry PP)",
    "btn.modifyInfoText": "መረጃ አሻሽል (Modify Info)",
    "search.placeholder": "ጌሞችን ይፈልጉ — ስም፣ ዓይነት፣ ምድብ…",
    "empty.noMatches": "ምንም ጌም አልተገኘም።",
    "empty.clearFilters": "ማጣሪያዎችን አጽዳ",
    "footer.licensed": "© ኢትዮ ቴሌኮም መብቱ በህግ የተጠበቀ ነው። ዲጂታል አቅምዎን እናገናኛለን።",
    "footer.language": "ቋንቋ:",
    "footer.press": "ይጫኑ",
    "footer.toSearch": "ለመፈለግ",
    "footer.toClose": "ለመዝጋት",
    "footer.forRandom": "በዕድል ለመጫወት",
    "footer.aboutDesc": "የኢትዮጵያ ቀዳሚው ዲጂታል መዝናኛ ፖርታል። 140+ ጌሞችን ያለምንም ጭነት በስልክዎ ወይም በኮምፒውተርዎ ይጫወቱ።",
    "footer.linksTitle": "ፈጣን ማውጫ",
    "footer.linkCatalog": "የ140+ ጌሞች ዝርዝር",
    "footer.linkCategories": "የጌም ምድቦች",
    "footer.linkRandom": "በዕድል ጌም ይጫወቱ",
    "footer.servicesTitle": "ቴሌኮም እና ትስስር",
    "footer.servInstant": "ያለምንም ጭነት ወዲያውኑ የሚጫወት",
    "footer.serv4g": "ለ4G እና 5G ፍጥነት የተዘጋጀ",
    "footer.servSupport": "የደንበኞች አገልግሎት: 994",
    "footer.shortcutsTitle": "የኪቦርድ አቋራጮች",
    "footer.backToTop": "ወደ ላይ ተመለስ ↑",
    "footer.helpline": "ኢትዮ ቴሌኮም · አዲስ አበባ፣ ኢትዮጵያ · የእርዳታ መስመር: 994",
    "modal.defaultTitle": "—",
    "aria.toggleTheme": "ገጽታ ይቀይሩ",
    "aria.filterGames": "ጌሞችን ይምረጡ",
    "aria.categories": "ምድቦች",
    "aria.toggleFullscreen": "ሙሉ ገጽታ",
    "aria.restartGame": "እንደገና ጀምር",
    "aria.openInNewTab": "በአዲስ ታብ ክፈት",
    "aria.close": "ዝጋ",
    "title.fullscreen": "ሙሉ ገጽታ",
    "title.restart": "እንደገና ጀምር",
    "title.openInNewTab": "በአዲስ ታብ ክፈት",
    "title.close": "ዝጋ",
    "title.game": "ጌም",
    "errors.registryLoad": "የጌም ዝርዝር መጫን አልተቻለም።",
    "stats.games": "ጌሞች አሉ",
    "filters.all": "ሁሉም ጌሞች",
    "card.tech.phaser": "Phaser",
    "card.tech.three": "Three.js",
    "card.tech.html": "HTML5",
    "card.aria.play": "{name}ን ይጫወቱ",
  }
};

// Category Emojis
const CATEGORY_EMOJI_FALLBACK = {
  puzzle: "🧩",
  arcade: "🕹️",
  shooter: "🎯",
  racing: "🏎️",
  sports: "⚽",
  platformer: "🏃",
  casual: "🎈",
  board: "♟️",
  "word-quiz": "📝",
  "3d": "🌐",
};

// Ethio Telecom tailored category color gradients (combining Dark Blue, Lemon Green, and crisp accents)
const CATEGORY_GRAD = {
  puzzle:     ["#0072BC", "#004573"],
  arcade:     ["#8DC63F", "#5b8720"],
  shooter:    ["#0072BC", "#1b3a4b"],
  racing:     ["#e65100", "#bf360c"],
  sports:     ["#8DC63F", "#2e7d32"],
  platformer: ["#0288d1", "#01579b"],
  casual:     ["#8DC63F", "#0072BC"],
  board:      ["#455a64", "#263238"],
  "word-quiz":["#0072BC", "#283593"],
  "3d":       ["#0072BC", "#8DC63F"],
};

// Game emojis
const GAME_EMOJI = {
  "2048": "🔢", "tetris": "🟦", "curve-snake": "🐍",
  "snake-and-ladder": "🎲", "chess": "♟️", "ludo": "🎲", "tic-tac-toe": "⭕",
  "rock-paper-scissors": "✊", "carrom": "🪙", "sudoku": "🔢",
  "memory": "🧠", "memory-cards": "🧠", "pacman": "👻", "flappy": "🐤",
  "mario": "🍄", "doodle-jump": "⬆️", "bubble-shooter": "🫧", "bubble-pop": "🫧",
  "candy-crush": "🍬", "candy-crusher": "🍬", "fruit-merge": "🍇",
  "fruit-basket": "🧺", "fruit-cosmics": "🍓", "cooking": "👨‍🍳",
  "buttermilk": "🥛", "wordle": "🅰️", "words-of-wonder": "🔠",
  "math-quest": "➕", "quiz": "❓", "football": "⚽", "basketball": "🏀",
  "bowling": "🎳", "cricket-123": "🏏", "table-tennis": "🏓",
  "archer": "🏹", "penalty": "🥅",
  "bird-shooter": "🐦", "alien-battle": "👾", "fighter-jet": "✈️",
  "fighter-fury": "✈️", "sniper": "🔭", "shooter": "🔫", "shoot-enemy": "🎯",
  "cannon-blaster": "💥", "robot-destruction": "🤖", "vaccine-shooter": "💉",
  "tower-shooter": "🗼", "tee-shooter": "🏌️", "thunder-god": "⚡",
  "shadow-shooter": "🌑", "space-fighter": "🚀", "trench-defence": "🪖",
  "gunman": "🤠", "gun-run": "🔫", "projectile-enemy": "🎯",
  "survivor": "🧟",
  "car-race": "🏎️", "road-fighter": "🚗", "one-car": "🚙", "two-cars": "🚗",
  "two-cars-ai": "🤖", "endless-runner": "🏃", "forest-runner": "🌲",
  "shadow-runner": "🌑", "survival-run": "🏃", "straight-rush": "💨",
  "antigravity": "🌀", "cool-platformer": "🦘", "flip-jump": "🔄",
  "parkour": "🤸", "devil-king": "😈", "level-devil": "😈",
  "that-level-again-1": "🔁", "that-level-again-2": "🔁",
  "that-level-again-3": "🔁", "that-level-again-4": "🔁",
  "that-level-again-5": "🔁",
  "stack-tower": "🏗️", "cosmic-cleaner": "🧹", "orbital-outpost": "🛰️",
  "planet-visitor": "🪐", "planet-war": "🪐",
  "hex-puzzle": "⬡", "cut-rope": "✂️", "connected": "🔗", "link": "🔗",
  "laser-bounce": "💡", "circuit-bulb": "💡", "signal-circuit": "📡",
  "colour-pour": "🧪", "screw-master": "🔩",
  "shape-collector": "🔷", "perfect-square": "⬜", "tile-tap": "🎹",
  "slide-puzzle": "🧩", "pathfinder": "🧭", "number-merge": "🔢",
  "four-dots": "🔵", "cargo-stack": "📦", "pairing": "🃏",
  "line-trap": "✏️", "unruly": "⚪", "6oct": "🔶", "square-one": "🔲",
  "circle-path": "⭕", "color-dash": "🎨", "balance-stack": "📚",
  "bomb-blast": "💣", "boom-dots": "💥", "bug-smasher": "🐛",
  "whack-a-bug": "🐞", "tap-target": "🎯", "kaiju-krush": "🦖",
  "crowd-control": "👥", "crossy-road": "🛣️", "road-cross": "🛣️",
  "red-light-green-light": "🚦", "glass-step": "🪟", "swipe-assassin": "🗡️",
  "fly-monkey": "🐒", "hungry-player": "😋", "jump-dot": "⬆️",
  "demon": "👹", "abhita": "✨", "ellars": "✨", "dream-weaver": "💭",
  "endless-mafia": "🕴️", "dodge-enemy": "💨", "dodge-master": "💨",
  "catch-me-if-you-can": "🏃", "collector": "💎", "pirates": "🏴‍☠️",
  "spaceman": "👨‍🚀", "space-waves": "🌊", "sky-high": "🪂",
  "luma-bounce": "🟡", "stick-game": "🪵", "stick-toss": "🪵",
  "breakoid": "🧱", "window-shooter": "🪟", "tile": "🎹",
};

const els = {
  grid: document.getElementById("grid"),
  empty: document.getElementById("empty"),
  search: document.getElementById("search-input"),
  filters: document.getElementById("filters"),
  stats: document.getElementById("stats"),
  themeToggle: document.getElementById("theme-toggle"),
  themeIcon: document.querySelector(".theme-icon"),
  randomBtn: document.getElementById("random-game"),
  clearFilters: document.getElementById("clear-filters"),
  languageSelect: document.getElementById("language-select"),
  
  // Game Player Modal
  modal: document.getElementById("modal"),
  modalTitle: document.getElementById("modal-title"),
  modalChip: document.getElementById("modal-chip"),
  modalFrame: document.getElementById("modal-frame"),
  modalOpen: document.getElementById("modal-open"),
  modalReload: document.getElementById("modal-reload"),
  modalFs: document.getElementById("modal-fullscreen"),
  
};

const state = {
  games: [],
  categories: [],
  q: "",
  category: "all",
  locale: DEFAULT_LOCALE,
};

// ---------- Initialization ----------
init();

async function init() {
  state.locale = loadLanguage();
  document.documentElement.lang = state.locale;
  loadTheme();
  applyI18n();

  if (els.languageSelect) els.languageSelect.value = state.locale;

  attachUiEvents();

  try {
    const res = await fetch("games/registry.json", { cache: "no-store" });
    if (!res.ok) throw new Error(`registry fetch ${res.status}`);
    const data = await res.json();
    state.games = data.games || [];
    state.categories = data.categories || [];
  } catch (err) {
    console.error("Failed to load registry:", err);
    els.grid.innerHTML = `<p style="grid-column:1/-1;color:var(--text-dim);text-align:center;padding:40px">
      ${t("errors.registryLoad")}</p>`;
    return;
  }

  renderStats();
  renderFilters();
  renderGrid();
  hydrateFromHash();
}

// ---------- Theme ----------
function loadTheme() {
  const saved = localStorage.getItem("ethio_theme");
  const initial = saved || "light";
  setTheme(initial);
}
function setTheme(t) {
  document.documentElement.dataset.theme = t;
  if (els.themeIcon) {
    els.themeIcon.textContent = t === "light" ? "☀️" : "🌙";
  }
  localStorage.setItem("ethio_theme", t);
}

// ---------- UI Event Attachments ----------
function attachUiEvents() {
  // Language Selector
  if (els.languageSelect) {
    els.languageSelect.addEventListener("change", (e) => {
      setLanguage(e.target.value);
      applyI18n();
      renderStats();
      renderFilters();
      renderGrid();
    });
  }

  // Theme Toggle
  if (els.themeToggle) {
    els.themeToggle.addEventListener("click", () => {
      setTheme(document.documentElement.dataset.theme === "light" ? "dark" : "light");
    });
  }

  // Search input
  if (els.search) {
    els.search.addEventListener("input", (e) => {
      state.q = e.target.value.trim().toLowerCase();
      renderGrid();
    });
  }

  // Random Game CTA
  if (els.randomBtn) {
    els.randomBtn.addEventListener("click", playRandom);
  }

  // Clear Filters
  if (els.clearFilters) {
    els.clearFilters.addEventListener("click", () => {
      state.q = "";
      state.category = "all";
      if (els.search) els.search.value = "";
      renderFilters();
      renderGrid();
    });
  }

  // Game Player Modal close buttons
  if (els.modal) {
    els.modal.querySelectorAll("[data-close]").forEach((el) =>
      el.addEventListener("click", closeModal)
    );
  }
  if (els.modalReload) {
    els.modalReload.addEventListener("click", () => {
      const src = els.modalFrame.getAttribute("src");
      els.modalFrame.setAttribute("src", "about:blank");
      requestAnimationFrame(() => els.modalFrame.setAttribute("src", src));
    });
  }
  if (els.modalFs) {
    els.modalFs.addEventListener("click", () => {
      const target = els.modal.querySelector(".modal__panel");
      if (!document.fullscreenElement) target.requestFullscreen?.();
      else document.exitFullscreen?.();
    });
  }

  // Global Keyboard Shortcuts
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      if (els.modal && !els.modal.hidden) { closeModal(); return; }
    }
    if (e.target.matches("input, textarea, select")) return;
    if (e.key === "/") {
      e.preventDefault();
      if (els.search) els.search.focus();
    } else if (e.key.toLowerCase() === "r" && els.modal && els.modal.hidden) {
      playRandom();
    }
  });

  // Hash routing
  window.addEventListener("hashchange", hydrateFromHash);
}

// ---------- Stats Bar ----------
function renderStats() {
  if (!els.stats) return;
  const counts = {};
  for (const g of state.games) counts[g.category] = (counts[g.category] || 0) + 1;
  const top = state.categories
    .map((c) => ({ c, n: counts[c.id] || 0 }))
    .sort((a, b) => b.n - a.n)
    .slice(0, 4);

  els.stats.innerHTML = `
    <span class="stat"><span class="stat__num">${state.games.length}</span> ${t("stats.games")}</span>
    ${top.map(({ c, n }) => `<span class="stat"><span class="stat__num">${n}</span> ${c.emoji} ${c.label}</span>`).join("")}
  `;
}

// ---------- Sub Menu Category Filters ----------
function renderFilters() {
  if (!els.filters) return;
  const counts = {};
  for (const g of state.games) counts[g.category] = (counts[g.category] || 0) + 1;
  const all = `<button class="chip" type="button" data-cat="all" aria-pressed="${state.category === "all"}">
    ${t("filters.all")} <span class="chip__count">${state.games.length}</span>
  </button>`;
  const cats = state.categories
    .map((c) => `<button class="chip" type="button" data-cat="${c.id}" aria-pressed="${state.category === c.id}">
      <span aria-hidden="true">${c.emoji}</span> ${c.label}
      <span class="chip__count">${counts[c.id] || 0}</span>
    </button>`)
    .join("");

  els.filters.innerHTML = all + cats;
  els.filters.querySelectorAll(".chip").forEach((btn) =>
    btn.addEventListener("click", () => {
      state.category = btn.dataset.cat;
      renderFilters();
      renderGrid();
    })
  );
}

// ---------- Games Grid ----------
function renderGrid() {
  if (!els.grid) return;
  const filtered = state.games.filter((g) => {
    if (state.category !== "all" && g.category !== state.category) return false;
    if (!state.q) return true;
    const hay = `${g.name} ${g.category} ${(g.tags || []).join(" ")} ${g.description}`.toLowerCase();
    return hay.includes(state.q);
  });

  if (!filtered.length) {
    els.grid.innerHTML = "";
    if (els.empty) els.empty.hidden = false;
    return;
  }
  if (els.empty) els.empty.hidden = true;

  els.grid.innerHTML = filtered.map(renderCard).join("");
  els.grid.querySelectorAll(".card").forEach((card) =>
    card.addEventListener("click", () => openGame(card.dataset.slug))
  );
}

function renderCard(g) {
  const thumbSrc = `assets/thumbnails/${g.slug}.png`;
  const emoji = GAME_EMOJI[g.slug] || CATEGORY_EMOJI_FALLBACK[g.category] || "🎮";
  const grad = CATEGORY_GRAD[g.category] || ["#0072BC", "#004573"];
  const cat = state.categories.find((c) => c.id === g.category);
  const techLabel = g.tech === "phaser" ? t("card.tech.phaser") : g.tech === "three" ? t("card.tech.three") : t("card.tech.html");
  return `
    <button class="card" data-slug="${g.slug}" data-category="${g.category}"
      style="--card-c1:${grad[0]};--card-c2:${grad[1]}" aria-label="${escapeAttr(t("card.aria.play", { name: g.name }))}">
      <div class="card__art">
        <img class="card__img" src="${thumbSrc}" alt="${escapeAttr(g.name)}" loading="lazy" width="480" height="300" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" />
        <div class="card__fallback" style="display:none;" aria-hidden="true">
          <span class="card__emoji">${emoji}</span>
        </div>
        <span class="card__play" aria-hidden="true">▶</span>
      </div>
      <div class="card__body">
        <h3 class="card__title headline-small">${escapeHtml(g.name)}</h3>
        <p class="card__desc body-text">${escapeHtml(g.description || "")}</p>
        <div class="card__meta">
          <span class="card__chip">${cat?.emoji || ""} ${cat?.label || g.category}</span>
          <span class="card__tech">${techLabel}</span>
        </div>
      </div>
    </button>
  `;
}

// ---------- Modal Player ----------
function openGame(slug) {
  const g = state.games.find((x) => x.slug === slug);
  if (!g) return;
  const cat = state.categories.find((c) => c.id === g.category);
  if (els.modalTitle) els.modalTitle.textContent = g.name;
  if (els.modalChip) {
    els.modalChip.textContent = `${cat?.emoji || ""} ${cat?.label || g.category}`;
    els.modalChip.style.background = CATEGORY_GRAD[g.category]?.[0] || "var(--c-dark-blue)";
  }
  if (els.modalFrame) els.modalFrame.setAttribute("src", g.path);
  if (els.modalOpen) els.modalOpen.setAttribute("href", g.path);
  if (els.modal) els.modal.hidden = false;
  document.body.style.overflow = "hidden";
  if (location.hash !== `#play=${slug}`) {
    history.replaceState(null, "", `#play=${slug}`);
  }

  // Automatically request browser fullscreen on touch or click
  try {
    const fsEl = els.modal.querySelector(".modal__panel") || els.modal;
    if (!document.fullscreenElement && !document.webkitFullscreenElement) {
      const fn = fsEl.requestFullscreen || fsEl.webkitRequestFullscreen || fsEl.msRequestFullscreen;
      if (fn) {
        const p = fn.call(fsEl);
        if (p && p.catch) p.catch(() => {});
      }
    }
  } catch (err) {}
}

function closeModal() {
  if (!els.modal) return;
  els.modal.hidden = true;
  if (els.modalFrame) els.modalFrame.setAttribute("src", "about:blank");
  document.body.style.overflow = "";
  if (location.hash.startsWith("#play=")) {
    history.replaceState(null, "", location.pathname + location.search);
  }
  try {
    if (document.fullscreenElement || document.webkitFullscreenElement) {
      const exitFn = document.exitFullscreen || document.webkitExitFullscreen || document.msExitFullscreen;
      if (exitFn) {
        const p = exitFn.call(document);
        if (p && p.catch) p.catch(() => {});
      }
    }
  } catch (err) {}
}

function hydrateFromHash() {
  const m = location.hash.match(/^#play=([\w-]+)/);
  if (m) openGame(m[1]);
  else if (els.modal && !els.modal.hidden) closeModal();
}

function playRandom() {
  if (!state.games.length) return;
  const pool = state.category === "all"
    ? state.games
    : state.games.filter((g) => g.category === state.category);
  const pick = pool[Math.floor(Math.random() * pool.length)];
  openGame(pick.slug);
}

// ---------- Helpers & i18n ----------
function escapeHtml(s) {
  return String(s ?? "").replace(/[&<>"']/g, (c) => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c]));
}
function escapeAttr(s) { return escapeHtml(s); }

function loadLanguage() {
  const saved = localStorage.getItem(LOCALE_STORAGE_KEY);
  if (saved && I18N[saved]) return saved;
  return DEFAULT_LOCALE;
}

function setLanguage(locale) {
  state.locale = I18N[locale] ? locale : DEFAULT_LOCALE;
  localStorage.setItem(LOCALE_STORAGE_KEY, state.locale);
  document.documentElement.lang = state.locale;
}

function t(key, vars = {}) {
  const dict = I18N[state.locale] || I18N[DEFAULT_LOCALE];
  let text = dict[key] ?? key;
  for (const [name, value] of Object.entries(vars)) {
    text = text.replaceAll(`{${name}}`, String(value));
  }
  return text;
}

function applyI18n(root = document) {
  root.querySelectorAll("[data-i18n]").forEach((el) => {
    el.textContent = t(el.dataset.i18n);
  });
  root.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    el.setAttribute("placeholder", t(el.dataset.i18nPlaceholder));
  });
  root.querySelectorAll("[data-i18n-aria-label]").forEach((el) => {
    el.setAttribute("aria-label", t(el.dataset.i18nAriaLabel));
  });
  root.querySelectorAll("[data-i18n-title]").forEach((el) => {
    el.setAttribute("title", t(el.dataset.i18nTitle));
  });
}
