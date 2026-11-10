import itertools, re, sys, pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent
_ids = itertools.count(1)

def emblem(cls="emblem", label=None):
    gid = f"zg{next(_ids)}"
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'''<svg class="{cls}" viewBox="0 0 516 300" {aria} xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0.35"><stop offset="0" class="stop-3"/><stop offset="0.5" class="stop-1"/><stop offset="1" class="stop-2"/></linearGradient></defs><path class="blade blade-1" fill="url(#{gid})" d="M2 119 L92 30 Q120 4 168 4 L513 4 L370 96 Q334 119 290 119 Z"/><path class="blade blade-2" fill="url(#{gid})" d="M2 297 L178 190 Q206 167 244 167 L493 167 L408 262 Q370 297 318 297 Z"/></svg>'''

I = {
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "star": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.5l2.9 6 6.6.8-4.9 4.5 1.3 6.5L12 17l-5.9 3.3 1.3-6.5L2.5 9.3l6.6-.8z"/></svg>',
 "sun": '<svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></svg>',
 "moon": '<svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M5 8h14M3 16h14"/></svg>',
 "pad": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6.5 7h11a4.5 4.5 0 0 1 4.4 5.4l-.9 4.3a2.6 2.6 0 0 1-4.6 1L14.8 16H9.2l-1.6 1.7a2.6 2.6 0 0 1-4.6-1l-.9-4.3A4.5 4.5 0 0 1 6.5 7z"/><path d="M7.5 10.5v3M6 12h3M15.5 11h.01M17.5 13h.01"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="2.5" width="12" height="19" rx="3"/><path d="M10.5 18.5h3"/></svg>',
 "pen": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19l7-7 2.5 2.5-7 7H12z"/><path d="M18 13l-1.5-7.5L3 2l3.5 13.5L14 17"/><circle cx="10" cy="10" r="1.6"/><path d="M3 2l5.8 5.8"/></svg>',
 "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 20h18"/><path d="M5 16l4.5-5 3.5 3 6-7"/><path d="M15 7h4v4"/></svg>',
 "check": '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
}

NAV = [("index.html", "Home"), ("games.html", "Games"), ("apps.html", "Apps"), ("about.html", "About"), ("contact.html", "Contact")]

def header(active):
    links = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a></li>' for h, t in NAV
    )
    return f'''<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="Zevoro home">{emblem()}<span class="brand-word">ZEVORO</span></a>
    <ul class="nav-links" id="nav-links">{links}<li class="mobile-cta"><a class="btn btn--gold" href="contact.html">Start a project {I["arrow"]}</a></li></ul>
    <div class="nav-actions">
      <button class="icon-btn theme-toggle" type="button" aria-label="Toggle theme">{I["sun"]}{I["moon"]}</button>
      <a class="btn btn--gold btn--sm nav-cta" href="contact.html">Start a project</a>
      <button class="icon-btn menu-btn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links">{I["menu"]}</button>
    </div>
  </div>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="index.html" aria-label="Zevoro home">{emblem()}<span class="brand-word">ZEVORO</span></a>
        <p>An independent mobile game and app studio in Lahore, Pakistan. 2D and 3D games and practical apps, with growth built in from day one.</p>
      </div>
      <div class="footer-col"><h4>Work</h4><ul><li><a href="games.html">Games</a></li><li><a href="apps.html">Apps</a></li><li><a href="index.html#services">Services</a></li></ul></div>
      <div class="footer-col"><h4>Studio</h4><ul><li><a href="about.html">About</a></li><li><a href="about.html#team">Work with us</a></li><li><a href="contact.html">Contact</a></li></ul></div>
      <div class="footer-col"><h4>Follow</h4><ul><li><a href="#">Instagram</a></li><li><a href="https://www.linkedin.com/company/zevoro/" target="_blank" rel="noopener">LinkedIn</a></li><li><a href="#">X / Twitter</a></li><li><a href="#">YouTube</a></li></ul></div>
    </div>
    <div class="footer-bottom"><span>&copy; <span data-year>2026</span> Zevoro. All rights reserved.</span><span>Lahore, Pakistan</span></div>
  </div>
</footer>'''

THEME_BOOT = '''<script>(function(){try{var t=localStorage.getItem("zevoro-theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t);}catch(e){}})();</script>'''
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Michroma&family=Sora:wght@500;600;700&display=swap">'
FAVICON = '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 516 300%27%3E%3Cpath fill=%27%23d6b068%27 d=%27M2 119 L92 30 Q120 4 168 4 L513 4 L370 96 Q334 119 290 119 Z M2 297 L178 190 Q206 167 244 167 L493 167 L408 262 Q370 297 318 297 Z%27/%3E%3C/svg%3E">'

def page(fname, title, desc, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0d0d0f">
{FAVICON}
{FONTS}
<link rel="stylesheet" href="styles.css">
{THEME_BOOT}
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>
{header(fname)}
<main id="main">
{body}
</main>
{FOOTER}
<script src="main.js"></script>
</body>
</html>
'''

I["target"] = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="0.8" fill="currentColor"/></svg>'
I["play"] = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.6 2.8c-.3.3-.4.7-.4 1.2v16c0 .5.1.9.4 1.2l9-9.2-9-9.2zm10.4 7.8 2.6-2.6L6.4 1.8c-.3-.2-.6-.3-.9-.2l9.5 9zm0 2.8-9.5 9c.3.1.6 0 .9-.2l11.2-6.2-2.6-2.6zm3.9-4.6-2.9 1.6L18.9 13l3-1.6c.9-.5.9-1.4 0-1.9z"/></svg>'

PHONE = "+92 329 9928811"
PHONE_RAW = "+923299928811"
LINKEDIN = "https://www.linkedin.com/company/zevoro/"

def cta(title="Have a game or app in mind?", text="Tell us what you want to build. We will come back with questions, a rough plan and a growth strategy for launch."):
    return f'''<section class="section--tight"><div class="wrap"><div class="cta-band">{emblem("bg-blades")}
  <div><h2>{title}</h2><p>{text}</p></div>
  <div class="cta-actions"><a class="btn btn--gold" href="contact.html">Start a project {I["arrow"]}</a><a class="btn btn--ghost" href="games.html">See our games</a></div>
</div></div></section>'''

# ------------- data -------------
GAMES = [
 dict(n="Skyforge Rush", m="Sf", g="action", gl="Action · 3D runner", d="Sprint across floating forge-islands, chain wall-runs and outrun a collapsing sky.", s="dev", sl="In development", c=("#3a2414", "#120a06", "#ff9a4d"), p="Android · iOS"),
 dict(n="Crown &amp; Coin", m="Cc", g="casual", gl="Casual · Idle builder", d="Grow a tiny kingdom into a trading empire. It keeps earning while you are away.", s="dev", sl="In development", c=("#2e2a12", "#100e05", "#f2d06b"), p="Android · iOS"),
 dict(n="Neon Drift", m="Nd", g="racing action", gl="Racing · Arcade", d="One-thumb drift racing through rain-soaked city loops with weekly ghost leagues.", s="dev", sl="In development", c=("#101a3d", "#05081a", "#6f8cff"), p="Android · iOS"),
]

def game_card(g):
    a, b, c = g["c"]
    if g.get("url"):
        foot = f'<span class="rating">{I["star"]} {g["r"]}</span><span>{g["dl"]} downloads</span>'
        link = f'<a class="link-arrow" href="{g["url"]}" target="_blank" rel="noopener">Get it on Google Play {I["arrow"]}</a>'
    else:
        foot = '<span>Coming soon</span><span>Android · iOS</span>'
        link = ""
    return f'''<article class="game-card" data-genre="{g["g"]}">
  <div class="art" style="--a:{a};--b:{b};--c:{c}"><span class="art-badge" data-status="{g["s"]}">{g["sl"]}</span><span class="art-mono" aria-hidden="true">{g["m"]}</span></div>
  <div class="card-body"><h3>{g["n"]}</h3><p>{g["d"]}</p><div class="card-tags"><span class="tag">{g["gl"]}</span><span class="tag">{g["p"]}</span></div>{link}</div>
  <div class="card-foot">{foot}</div>
</article>'''

def featured_game(eyebrow="Coming soon", heading="Skyforge Rush"):
    return f'''<div class="wrap split">
    <div class="art" style="--a:#3a2414;--b:#120a06;--c:#ff9a4d;border-radius:20px;aspect-ratio:4/3" aria-hidden="true"><span class="art-badge" data-status="dev">In development</span><span class="art-mono" style="font-size:4rem">Sf</span></div>
    <div class="split-copy">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{heading}</h2>
      <p class="lede">Our first 3D title. Sprint across floating forge-islands, chain wall-runs and outrun a collapsing sky, in short runs made for one more try.</p>
      <ul class="feature-list" style="font-size:1rem">
        <li>3D endless runner built in Unity</li>
        <li>Android and iOS</li>
        <li>Being tested with real players before launch</li>
      </ul>
      <div class="hero-actions"><a class="btn btn--gold" href="contact.html">Get launch updates {I["arrow"]}</a></div>
    </div>
  </div>'''

APPS = [
 dict(n="Lumen Notes", m="Ln", cat="Productivity", d="Notes that link themselves. Write fast, find anything, sync across phone and tablet.", f=["Offline-first sync", "Handwriting search", "Shared notebooks"], c=("#2b2f45", "#121524", "#9fb2ff")),
 dict(n="PocketLedger", m="Pl", cat="Finance", d="A calm budgeting app for freelancers. Splits income, tracks invoices and sets tax aside.", f=["Bank-grade encryption", "Invoice reminders", "Multi-currency"], c=("#2b2a14", "#121106", "#f2d06b")),
 dict(n="FitPulse", m="Fp", cat="Health &amp; fitness", d="Ten-minute workouts that adapt to your week, with wearable sync and streaks that stick.", f=["Apple Health &amp; Google Fit", "Adaptive plans", "Coach audio"], c=("#3a1a1a", "#150707", "#ff8a7a")),
 dict(n="Wayfare", m="Wf", cat="Travel", d="Plan a trip with friends in one shared timeline: flights, stays, budgets and maps.", f=["Live shared itinerary", "Expense splitting", "Offline maps"], c=("#123228", "#06130f", "#6fe0b0")),
]

def app_card(a):
    x, y, z = a["c"]
    feats = "".join(f"<li>{f}</li>" for f in a["f"])
    return f'''<article class="app-card">
  <div class="app-icon" style="--a:{x};--b:{y};--c:{z}" aria-hidden="true">{a["m"]}</div>
  <div class="meta"><span class="app-cat">{a["cat"]}</span><h3>{a["n"]}</h3><p>{a["d"]}</p><ul class="feature-list">{feats}</ul>
  <div class="app-stores"><span class="tag">Concept</span><span class="tag">Android · iOS</span></div></div>
</article>'''

SERVICES = [
 ("pad", "2D &amp; 3D mobile games", "Unity games for Android and iOS, from a fast first prototype to a polished store launch.", ["Unity &amp; C#", "2D and 3D art pipelines", "Android &amp; iOS"]),
 ("phone", "Practical mobile apps", "User-focused apps that solve one problem well and stay easy to use every day.", ["Clean, simple UX", "Android &amp; iOS", "Analytics from day one"]),
 ("target", "ASO, UA &amp; monetization", "Growth planned alongside development, not after it. Store listings, user acquisition and revenue models that fit the product.", ["Google Play &amp; App Store ASO", "User acquisition", "IAP, subscriptions &amp; ads"]),
 ("chart", "Data-driven iteration", "We measure how people really play and use the product, then improve what the numbers point to.", ["Retention &amp; engagement", "Lifetime value (LTV)", "A/B testing"]),
]

APP_SERVICES = [
 ("pen", "Product planning", "Clear scope, priorities and success metrics agreed before development starts.", ["Discovery sessions", "MVP scoping", "Success metrics"]),
 ("phone", "Android &amp; iOS builds", "Apps that feel at home on every phone and are simple to keep using.", ["Android &amp; iOS", "User-focused design", "Accessibility in mind"]),
 ("target", "Monetization", "Revenue models that fit the product and respect the people using it.", ["In-app purchases", "Subscriptions", "Ads, done carefully"]),
 ("chart", "Launch &amp; growth", "Store optimisation, user acquisition and analytics so the app finds its audience.", ["Google Play &amp; App Store ASO", "User acquisition", "Retention analytics"]),
]

def services_html(src=None):
    out = []
    for ic, t, d, items in (src or SERVICES):
        lis = "".join(f"<li>{x}</li>" for x in items)
        out.append(f'<div class="service"><div class="service-icon">{I[ic]}</div><h3>{t}</h3><p>{d}</p><ul>{lis}</ul></div>')
    return '<div class="services">' + "".join(out) + "</div>"

PROCESS = '''<div class="process process--3">
      <div class="step"><span class="step-num">STEP 01</span><h3>Prototype fast</h3><p>We get a playable game or clickable app onto real devices in weeks, not months, so ideas are judged on how they feel.</p></div>
      <div class="step"><span class="step-num">STEP 02</span><h3>Test with real players</h3><p>Real people try the build early. We watch where they smile, where they get stuck and where they leave.</p></div>
      <div class="step"><span class="step-num">STEP 03</span><h3>Scale what the data supports</h3><p>Retention, engagement and LTV tell us what to double down on. We invest in what works and cut what does not.</p></div>
    </div>'''

# ------------- pages -------------
HOME = f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow">Mobile game &amp; app studio · Lahore</span>
      <h1>Games worth replaying. <span class="gold-text">Apps worth keeping.</span></h1>
      <p class="lede">Zevoro is an independent studio building 2D and 3D mobile games and practical apps for players worldwide, with user acquisition, ASO and monetization built in from day one.</p>
      <div class="hero-actions"><a class="btn btn--gold" href="games.html">Explore our games {I["arrow"]}</a><a class="btn btn--ghost" href="contact.html">Start a project</a></div>
      <div class="hero-meta"><span>Unity</span><span>Android &amp; iOS</span><span>ASO &amp; UA</span><span>Monetization</span></div>
    </div>
    <div class="hero-stage" aria-hidden="true">
      <div class="stage-panel"></div>
      {emblem("stage-emblem")}
      <div class="stage-word">ZEVORO</div>
      <div class="chip-float chip-a"><strong>Android + iOS</strong><span>Every launch</span></div>
      <div class="chip-float chip-b"><strong>2D &amp; 3D</strong><span>Unity games</span></div>
    </div>
  </div>
</section>

<section class="section--tight" aria-label="Studio at a glance">
  <div class="wrap">
    <div class="stats">
      <div class="stat"><span class="stat-num">2024</span><span class="stat-label">Founded in Lahore</span></div>
      <div class="stat"><span class="stat-num">2</span><span class="stat-label">Platforms: Android &amp; iOS</span></div>
      <div class="stat"><span class="stat-num">2D<em>/</em>3D</span><span class="stat-label">Unity games</span></div>
      <div class="stat"><span class="stat-num">Day <em>1</em></span><span class="stat-label">Growth planning starts</span></div>
    </div>
  </div>
</section>

<section class="section">
  {featured_game()}
</section>

<section class="section section--alt" id="services">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">What we do</span><h2>Build and growth, in one team</h2><p class="lede">Most studios build first and think about growth later. We do both together, so every game and app launches with a plan to find its players.</p></div>
    {services_html()}
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="split-copy">
      <span class="eyebrow">Apps</span>
      <h2>Practical apps with game-level polish</h2>
      <p class="lede">The care we put into game feel goes into our apps too: quick to open, smooth to use and simple enough that people keep coming back.</p>
      <ul class="feature-list" style="font-size:1rem">
        <li>Designed around one clear job for the user</li>
        <li>Monetization through IAP, subscriptions or ads, chosen to fit</li>
        <li>Analytics in place before launch, not after</li>
      </ul>
      <div><a class="btn btn--ghost" href="apps.html">See what we build {I["arrow"]}</a></div>
    </div>
    <div class="phones" aria-hidden="true">
      <div class="phone"><div class="screen" style="--sa:#1c2133;--sb:#0a0c14">
        <div class="s-title">Budget</div><div class="s-card"><span>Saved this month</span><span class="s-big">$2,480</span><div class="s-bar gold"></div></div>
        <div class="s-card"><span>Upcoming</span><div class="s-bar" style="width:80%"></div><div class="s-bar" style="width:55%"></div></div>
        <div class="s-row"><div class="s-tile g"></div><div class="s-tile"></div><div class="s-tile"></div></div>
      </div></div>
      <div class="phone"><div class="screen" style="--sa:#2a1414;--sb:#0e0606">
        <div class="s-title">Workout</div><div class="s-card"><span>Today · 10 min</span><span class="s-big">Core &amp; mobility</span></div>
        <div class="s-row"><div class="s-tile g"></div><div class="s-tile g"></div><div class="s-tile"></div><div class="s-tile"></div></div>
        <div class="s-card"><span>Streak</span><div class="s-bar gold" style="width:70%"></div></div>
      </div></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">How we work</span><h2>Prototype, test, then scale</h2></div>
    {PROCESS}
  </div>
</section>

{cta()}
'''

GAMES_PAGE = f'''
<section class="page-hero">
  {emblem("bg-blades")}
  <div class="wrap">
    <span class="eyebrow">Games</span>
    <h1>Worlds made for <span class="gold-text">one more round</span></h1>
    <p class="lede">2D and 3D mobile games built in Unity for Android and iOS. Easy to start, satisfying to master, and tuned with real player data.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(24px,3vw,40px)">
  {featured_game("Our first 3D game", "Skyforge Rush")}
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">All games</span><h2>In the pipeline</h2></div>
    <div class="filters" role="group" aria-label="Filter games by genre">
      <button class="filter" type="button" data-filter="all" aria-pressed="true">All games</button>
            <button class="filter" type="button" data-filter="casual" aria-pressed="false">Casual</button>
      <button class="filter" type="button" data-filter="action" aria-pressed="false">Action</button>
      <button class="filter" type="button" data-filter="racing" aria-pressed="false">Racing</button>
    </div>
    <div class="grid-3 games-grid">{"".join(game_card(g) for g in GAMES)}</div>
    <p class="empty-note" hidden>No games in this genre yet. Check back soon.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">How our games are made</span><h2>Fun first, then growth</h2></div>
    <div class="values">
      <div class="value"><span class="k">Feel</span><h3>Game feel first</h3><p>We tune controls, camera and feedback until the core action is fun before adding anything else.</p></div>
      <div class="value"><span class="k">Players</span><h3>Tested with real players</h3><p>Early builds go to real people. Their behaviour, not our guesses, decides what we build next.</p></div>
      <div class="value"><span class="k">Growth</span><h3>Built to be found</h3><p>Store listings, user acquisition and monetization are planned while the game is being made.</p></div>
    </div>
  </div>
</section>

{cta("Want us to build your game?", "Bring a concept, a pitch deck or just a genre you love. We are also open to working with publishers.")}
'''

APPS_PAGE = f'''
<section class="page-hero">
  {emblem("bg-blades")}
  <div class="wrap">
    <span class="eyebrow">Apps</span>
    <h1>Apps that earn a place on the <span class="gold-text">home screen</span></h1>
    <p class="lede">Practical, user-focused mobile apps for Android and iOS, with the same attention to feel and growth we give our games.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(24px,3vw,40px)">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">App concepts</span><h2>The kind of apps we build</h2></div>
    <div class="grid-2">{"".join(app_card(a) for a in APPS)}</div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">What we offer</span><h2>Everything an app needs to launch and grow</h2></div>
    {services_html(APP_SERVICES)}
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="split-copy">
      <span class="eyebrow">Tools</span>
      <h2>Proven tools, chosen per project</h2>
      <p class="lede">We pick the stack that gets the product to players fastest and keeps it easy to improve after launch.</p>
    </div>
    <div class="stack">
      <span>Unity</span><span>C#</span><span>Android</span><span>iOS</span><span>Firebase</span><span>Google Play Console</span><span>App Store Connect</span><span>AdMob</span><span>Unity Ads</span><span>Figma</span>
    </div>
  </div>
</section>

{cta("Got an app idea?", "Send us a short description. We will come back with the questions that matter and a realistic plan for a first release.")}
'''

AUDIENCES = [
 ("Publishers", "Looking for a studio that ships games and understands UA and monetization? Let's talk."),
 ("Investors", "We are building a portfolio of mobile games and apps with growth in mind from day one."),
 ("Developers", "Unity and mobile developers who care about game feel and clean code."),
 ("Designers", "Game artists, UI and UX designers who want to see their work in players' hands."),
]

ABOUT_PAGE = f'''
<section class="page-hero">
  {emblem("bg-blades")}
  <div class="wrap">
    <span class="eyebrow">About Zevoro</span>
    <h1>An independent studio from <span class="gold-text">Lahore</span></h1>
    <p class="lede">Zevoro builds 2D and 3D mobile games and practical apps for players worldwide, with growth built in from day one.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(24px,3vw,40px)">
  <div class="wrap story">
    <h2>Building and growth, together</h2>
    <div class="story-copy">
      <p>Most studios build first and think about growth later. <strong>Zevoro does both together.</strong></p>
      <p>Alongside development, we bring hands-on experience in <strong>user acquisition</strong>, <strong>App Store Optimization</strong> on Google Play and the App Store, <strong>monetization</strong> through IAP, subscriptions and ads, and <strong>analytics</strong>.</p>
      <p>Our mark is two blades moving the same way: one for games, one for apps, both cut from the same material.</p>
    </div>
  </div>
</section>

<section class="section--tight"><div class="wrap"><div class="stats">
  <div class="stat"><span class="stat-num">2024</span><span class="stat-label">Founded</span></div>
  <div class="stat"><span class="stat-num">2<em>–</em>10</span><span class="stat-label">People in the studio</span></div>
  <div class="stat"><span class="stat-num">LHR</span><span class="stat-label">Lahore, Pakistan</span></div>
  <div class="stat"><span class="stat-num">4</span><span class="stat-label">Core services</span></div>
</div></div></section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">How Zevoro works</span><h2>Prototype fast, test with real players, scale what the data supports</h2></div>
    {PROCESS}
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">What we value</span><h2>How we make decisions</h2></div>
    <div class="values">
      <div class="value"><span class="k">Craft</span><h3>Polish is a feature</h3><p>The last ten percent of detail is what players remember. We plan time for it from the start.</p></div>
      <div class="value"><span class="k">Data</span><h3>Let the numbers decide</h3><p>Retention, engagement and lifetime value guide what we build next, not hunches.</p></div>
      <div class="value"><span class="k">Ownership</span><h3>Ship it, then grow it</h3><p>Launch day is the start. We keep improving the product and how people find it.</p></div>
    </div>
  </div>
</section>

<section class="section" id="team">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Let's connect</span><h2>Who we want to work with</h2><p class="lede">Zevoro is open to working with publishers, investors, developers and designers.</p></div>
    <div class="process">{"".join(f'<div class="step"><h3>{t}</h3><p>{d}</p></div>' for t, d in AUDIENCES)}</div>
  </div>
</section>

{cta("Want to work with us?", "Whether you are a publisher, an investor or someone who wants to join the team, we would like to hear from you.")}
'''

CONTACT_PAGE = f'''
<section class="page-hero">
  {emblem("bg-blades")}
  <div class="wrap">
    <span class="eyebrow">Contact</span>
    <h1>Let&rsquo;s build something <span class="gold-text">people love</span></h1>
    <p class="lede">Tell us about your game, app or partnership idea. We are open to working with publishers, investors, developers and designers.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(24px,3vw,40px)">
  <div class="wrap contact-grid">
    <div class="form-card">
      <form class="form" id="contact-form" novalidate>
        <div class="field" data-field="name"><label for="f-name">Your name</label><input id="f-name" name="name" type="text" autocomplete="name" placeholder="Alex Morgan"><span class="err" aria-live="polite"></span></div>
        <div class="field" data-field="email"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" placeholder="you@company.com"><span class="err" aria-live="polite"></span></div>
        <div class="field field--full"><span style="font-weight:700;font-size:.88rem" id="type-label">What is this about?</span>
          <div class="choice-row" role="radiogroup" aria-labelledby="type-label">
            <input type="radio" id="t-game" name="type" value="Game" checked><label for="t-game">A game</label>
            <input type="radio" id="t-app" name="type" value="App"><label for="t-app">An app</label>
            <input type="radio" id="t-growth" name="type" value="Growth"><label for="t-growth">ASO &amp; growth</label>
            <input type="radio" id="t-partner" name="type" value="Partnership"><label for="t-partner">Publishing or investment</label>
            <input type="radio" id="t-job" name="type" value="Job"><label for="t-job">Joining the team</label>
          </div>
        </div>
        <div class="field"><label for="f-budget">Budget range</label><select id="f-budget" name="budget"><option>Not sure yet</option><option>Under $10k</option><option>$10k – $30k</option><option>$30k – $75k</option><option>$75k+</option><option>Not applicable</option></select></div>
        <div class="field"><label for="f-time">Timeline</label><select id="f-time" name="timeline"><option>Flexible</option><option>Within 1 month</option><option>1–3 months</option><option>3–6 months</option><option>6+ months</option></select></div>
        <div class="field field--full" data-field="message"><label for="f-msg">Details</label><textarea id="f-msg" name="message" placeholder="What is it, who is it for, and where are you today (idea, design, live game or app)?"></textarea><span class="err" aria-live="polite"></span></div>
        <div class="form-foot"><small>We only use your details to reply to you.</small><button class="btn btn--gold" type="submit">Send message {I["arrow"]}</button></div>
      </form>
      <div class="form-success" id="form-success" tabindex="-1" hidden>
        <div class="success-mark">{I["check"]}</div>
        <h3>Thanks, <span data-name></span>. Your message is ready.</h3>
        <p>This form is not connected to an inbox yet, so nothing was sent. Until it is, call us on {PHONE} or message us on LinkedIn.</p>
        <div><button class="btn btn--ghost" type="button" id="form-again">Write another message</button></div>
      </div>
    </div>

    <aside class="info-list" aria-label="Contact details">
      <div class="info-item"><span class="k">Phone</span><div class="copy-row"><a class="v" id="phone-1" href="tel:{PHONE_RAW}">{PHONE}</a><button class="copy-btn" type="button" data-copy="{PHONE_RAW}" aria-controls="phone-1">Copy</button></div><p>Calls and WhatsApp, Monday to Friday.</p></div>
      <div class="info-item"><span class="k">Studio</span><span class="v">Lahore, Punjab 54000</span><p>Pakistan. Working with players and partners worldwide.</p></div>
      <div class="info-item"><span class="k">LinkedIn</span><a class="v link-arrow" style="font-size:1.05rem" href="{LINKEDIN}" target="_blank" rel="noopener">linkedin.com/company/zevoro {I["arrow"]}</a><p>Follow our launches and studio news.</p></div>
      <div class="info-item"><span class="k">Open to</span><span class="v">Publishers, investors, developers &amp; designers</span></div>
    </aside>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">FAQ</span><h2>Before you get in touch</h2></div>
    <div class="faq">
      <details><summary>How much does a mobile game or app cost?</summary><p>It depends on scope. A focused prototype usually takes a few weeks, while a launch-ready product takes a few months. After a short call we send a written estimate with a cost range and timeline.</p></details>
      <details><summary>Do you work with startups and first-time founders?</summary><p>Yes. We help shape the concept, plan a first version and build it with you, with a growth plan for launch.</p></details>
      <details><summary>Do you work with publishers?</summary><p>Yes. We are open to publishing partnerships and to building games for publishers who need a reliable Unity studio.</p></details>
      <details><summary>Can you help grow a game or app that is already live?</summary><p>Yes. We can review your store listing, monetization and analytics, then plan ASO, user acquisition and retention improvements.</p></details>
      <details><summary>Which platforms do you build for?</summary><p>Android and iOS. Our games are built in Unity in 2D or 3D, and our apps are built for both stores.</p></details>
    </div>
  </div>
</section>
'''

PAGES = [
 ("index.html", "Zevoro", "Zevoro is an independent mobile game and app studio in Lahore building 2D and 3D games and practical apps, with growth built in from day one.", HOME),
 ("games.html", "Games · Zevoro", "Mobile games in development at Zevoro, a Unity studio in Lahore.", GAMES_PAGE),
 ("apps.html", "Apps · Zevoro", "iOS and Android apps designed and built by Zevoro.", APPS_PAGE),
 ("about.html", "About · Zevoro", "About Zevoro, an independent mobile game and app studio founded in Lahore in 2024.", ABOUT_PAGE),
 ("contact.html", "Contact · Zevoro", "Start a game or app project with Zevoro.", CONTACT_PAGE),
]

for fname, title, desc, body in PAGES:
    (OUT / fname).write_text(page(fname, title, desc, body))
print("written", [p[0] for p in PAGES])
