import os, json

base = os.path.expanduser('~/mao-landing')
blog_dir = os.path.join(base, 'blog')
os.makedirs(blog_dir, exist_ok=True)

# ── CSS shared across all blog pages ─────────────────────────────────────────
SHARED_CSS = """
    * { margin: 0; padding: 0; box-sizing: border-box; }
    :root {
      --heritage:    #06231c;
      --terracotta:  #bf4b2e;
      --terra-light: #d46140;
      --parchment:   #fdfaf4;
      --parch-deep:  #f5f1e8;
      --parch-mid:   #f0eee9;
      --text:        #2a2825;
      --text-muted:  #6b665e;
      --border:      #e5e0d5;
      --on-heritage: #e8efeb;
      --white:       #ffffff;
      --green:       #1a4d2e;
      --green-bg:    #eef6f0;
    }
    body { font-family: 'Public Sans', sans-serif; background: var(--parchment); color: var(--text); }

    /* ── NAV ── */
    nav {
      position: sticky; top: 0; z-index: 100;
      background: var(--heritage);
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 40px; height: 64px;
    }
    .nav-logo {
      display: flex; align-items: center; gap: 10px;
      color: var(--on-heritage); text-decoration: none;
      font-family: 'Fraunces', serif; font-size: 18px; font-weight: 700;
    }
    .nav-links { display: flex; align-items: center; gap: 28px; }
    .nav-links a {
      color: var(--on-heritage); text-decoration: none;
      font-size: 14px; opacity: 0.85; transition: opacity 0.2s;
    }
    .nav-links a:hover { opacity: 1; }
    .btn-nav {
      background: var(--terracotta); color: white !important;
      padding: 8px 18px; border-radius: 8px; font-weight: 600;
      opacity: 1 !important; transition: background 0.2s !important;
    }
    .btn-nav:hover { background: var(--terra-light) !important; }

    /* ── FOOTER ── */
    footer { background: var(--heritage); color: var(--on-heritage); margin-top: 80px; }
    .footer-inner { max-width: 1200px; margin: 0 auto; padding: 60px 40px 32px; }
    .footer-top { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 48px; margin-bottom: 48px; }
    .footer-logo { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
    .footer-logo-name { font-family: 'Fraunces', serif; font-size: 18px; font-weight: 700; }
    .footer-tagline { font-size: 13px; opacity: 0.65; line-height: 1.6; max-width: 260px; }
    .footer-col h4 { font-size: 12px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; opacity: 0.5; margin-bottom: 14px; }
    .footer-col a { display: block; color: var(--on-heritage); text-decoration: none; font-size: 14px; opacity: 0.75; margin-bottom: 8px; transition: opacity 0.2s; }
    .footer-col a:hover { opacity: 1; }
    .footer-bottom { border-top: 1px solid rgba(232,239,235,0.12); padding-top: 24px; display: flex; justify-content: space-between; align-items: center; }
    .footer-bottom p { font-size: 13px; opacity: 0.45; }
    .footer-bottom-links { display: flex; gap: 20px; }
    .footer-bottom-links a { color: var(--on-heritage); text-decoration: none; font-size: 13px; opacity: 0.45; transition: opacity 0.2s; }
    .footer-bottom-links a:hover { opacity: 0.8; }

    @media (max-width: 768px) {
      nav { padding: 0 20px; }
      .nav-links .hide-mobile { display: none; }
      .footer-top { grid-template-columns: 1fr 1fr; gap: 32px; }
      .footer-inner { padding: 40px 20px 24px; }
      .footer-bottom { flex-direction: column; gap: 12px; text-align: center; }
    }
"""

NAV_HTML = """  <nav>
    <a href="/" class="nav-logo">
      <img src="https://gnwfrffneehpknyaygeb.supabase.co/storage/v1/object/public/assets/MAO%20Workforce%20Logo-4.png" alt="MAO Workforce" style="height:36px;width:auto;border-radius:4px;" />
      MAO Workforce
    </a>
    <div class="nav-links">
      <a href="/#features" class="hide-mobile">Features</a>
      <a href="/#compliance" class="hide-mobile">Compliance</a>
      <a href="/#pricing" class="hide-mobile">Pricing</a>
      <a href="/faq">Help</a>
      <a href="/blog" style="opacity:1;font-weight:600;">Blog</a>
      <a href="https://portal.maoworkforce.com">Log in</a>
      <a href="https://portal.maoworkforce.com" class="btn-nav" style="color: white !important;">Start free</a>
    </div>
  </nav>"""

FOOTER_HTML = """  <footer>
    <div class="footer-inner">
      <div class="footer-top">
        <div>
          <div class="footer-logo">
            <img src="https://gnwfrffneehpknyaygeb.supabase.co/storage/v1/object/public/assets/MAO%20Workforce%20Logo-4.png" alt="MAO Workforce" style="height:32px;width:auto;border-radius:4px;filter:brightness(0) invert(1);opacity:0.8;" />
            <span class="footer-logo-name">MAO Workforce</span>
          </div>
          <p class="footer-tagline">HR and payroll software built for Philippine businesses. Statutory compliant, always.</p>
        </div>
        <div class="footer-col">
          <h4>Product</h4>
          <a href="/#features">Features</a>
          <a href="/#pricing">Pricing</a>
          <a href="/#compliance">Compliance</a>
          <a href="/faq">Help</a>
          <a href="https://portal.maoworkforce.com">Log in</a>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <a href="#">About</a>
          <a href="mailto:hello@maoworkforce.com">Contact</a>
          <a href="/blog">Blog</a>
        </div>
        <div class="footer-col">
          <h4>Legal</h4>
          <a href="/privacy.html">Privacy Policy</a>
          <a href="/terms.html">Terms of Service</a>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 MAO Workforce | Powered by LeviO. All rights reserved.</p>
        <div class="footer-bottom-links">
          <a href="/privacy.html">Privacy</a>
          <a href="/terms.html">Terms</a>
          <a href="mailto:hello@maoworkforce.com">hello@maoworkforce.com</a>
        </div>
      </div>
    </div>
  </footer>"""

# ── posts.json ────────────────────────────────────────────────────────────────
posts = [
  {
    "slug": "introducing-mao-workforce",
    "title": "Introducing MAO Workforce: HR & Payroll Built for Philippine Businesses",
    "date": "2026-06-18",
    "category": "Product Update",
    "excerpt": "We built MAO Workforce because payroll in the Philippines shouldn't require an accountant on speed dial. Here's the story behind the product and what we're building.",
    "readTime": "4 min read",
    "author": "Abegail Unay"
  }
]

with open(os.path.join(blog_dir, 'posts.json'), 'w') as f:
    json.dump(posts, f, indent=2)
print("✓ blog/posts.json")

# ── blog/index.html ───────────────────────────────────────────────────────────
blog_index = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Blog — MAO Workforce</title>
  <meta name="description" content="Product updates, HR guides, and payroll insights for Philippine businesses from the MAO Workforce team." />
  <meta property="og:title" content="Blog — MAO Workforce" />
  <meta property="og:description" content="Product updates, HR guides, and payroll insights for Philippine businesses." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://maoworkforce.com/blog" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,600;0,700;1,400&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
{SHARED_CSS}

    /* ── BLOG INDEX ── */
    .blog-hero {{
      background: var(--heritage);
      padding: 72px 40px 64px;
      text-align: center;
    }}
    .blog-hero-eyebrow {{
      display: inline-block;
      background: rgba(232,239,235,0.12);
      color: var(--on-heritage);
      font-size: 12px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase;
      padding: 6px 14px; border-radius: 20px; margin-bottom: 20px;
    }}
    .blog-hero h1 {{
      font-family: 'Fraunces', serif;
      font-size: clamp(36px, 5vw, 56px);
      color: var(--on-heritage);
      font-weight: 700; line-height: 1.1;
      margin-bottom: 16px;
    }}
    .blog-hero p {{
      font-size: 18px; color: rgba(232,239,235,0.7);
      max-width: 520px; margin: 0 auto;
      line-height: 1.6;
    }}

    .blog-main {{
      max-width: 1100px; margin: 0 auto; padding: 64px 40px;
    }}

    /* category filter */
    .blog-filters {{
      display: flex; gap: 10px; margin-bottom: 48px; flex-wrap: wrap;
    }}
    .filter-btn {{
      padding: 7px 18px; border-radius: 20px; font-size: 13px; font-weight: 600;
      border: 1.5px solid var(--border); background: transparent; color: var(--text-muted);
      cursor: pointer; transition: all 0.2s; font-family: 'Public Sans', sans-serif;
    }}
    .filter-btn.active, .filter-btn:hover {{
      background: var(--heritage); border-color: var(--heritage); color: white;
    }}

    /* post grid */
    .posts-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 32px;
    }}
    .post-card {{
      background: white;
      border: 1px solid var(--border);
      border-radius: 16px;
      overflow: hidden;
      transition: transform 0.2s, box-shadow 0.2s;
      text-decoration: none;
      color: inherit;
      display: flex; flex-direction: column;
    }}
    .post-card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 12px 32px rgba(6,35,28,0.1);
    }}
    .post-card-body {{ padding: 28px; flex: 1; display: flex; flex-direction: column; }}
    .post-meta {{
      display: flex; align-items: center; gap: 10px;
      margin-bottom: 14px; flex-wrap: wrap;
    }}
    .category-badge {{
      font-size: 11px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;
      padding: 4px 10px; border-radius: 12px;
    }}
    .badge-product {{ background: #eef6f0; color: #1a4d2e; }}
    .badge-hr {{ background: #fef3ef; color: #8b2a12; }}
    .post-date {{ font-size: 12px; color: var(--text-muted); }}
    .post-read-time {{ font-size: 12px; color: var(--text-muted); }}
    .post-card h2 {{
      font-family: 'Fraunces', serif;
      font-size: 20px; font-weight: 700;
      line-height: 1.3; margin-bottom: 10px;
      color: var(--text);
    }}
    .post-excerpt {{
      font-size: 14px; color: var(--text-muted);
      line-height: 1.65; flex: 1;
    }}
    .post-card-footer {{
      padding: 16px 28px;
      border-top: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between;
    }}
    .post-author {{ font-size: 13px; color: var(--text-muted); font-weight: 500; }}
    .read-more {{
      font-size: 13px; font-weight: 600; color: var(--terracotta);
      display: flex; align-items: center; gap: 4px;
    }}

    /* empty state */
    .empty-state {{ text-align: center; padding: 80px 20px; color: var(--text-muted); }}
    .empty-state h3 {{ font-family: 'Fraunces', serif; font-size: 24px; margin-bottom: 8px; color: var(--text); }}

    /* CTA banner */
    .blog-cta {{
      background: var(--heritage);
      border-radius: 20px;
      padding: 56px 48px;
      text-align: center;
      margin-top: 80px;
    }}
    .blog-cta h2 {{
      font-family: 'Fraunces', serif;
      font-size: 32px; color: var(--on-heritage);
      margin-bottom: 12px;
    }}
    .blog-cta p {{ color: rgba(232,239,235,0.7); margin-bottom: 28px; font-size: 16px; }}
    .btn-cta {{
      display: inline-block;
      background: var(--terracotta); color: white;
      padding: 14px 32px; border-radius: 10px;
      font-weight: 700; font-size: 15px; text-decoration: none;
      transition: background 0.2s;
    }}
    .btn-cta:hover {{ background: var(--terra-light); }}

    @media (max-width: 768px) {{
      .blog-hero {{ padding: 48px 20px 40px; }}
      .blog-main {{ padding: 40px 20px; }}
      .posts-grid {{ grid-template-columns: 1fr; }}
      .blog-cta {{ padding: 40px 24px; }}
    }}
  </style>
</head>
<body>

{NAV_HTML}

  <div class="blog-hero">
    <div class="blog-hero-eyebrow">MAO Blog</div>
    <h1>Insights for Philippine<br>Business Owners</h1>
    <p>Product updates, HR guides, and payroll insights — straight from the team building MAO Workforce.</p>
  </div>

  <div class="blog-main">
    <div class="blog-filters">
      <button class="filter-btn active" onclick="filterPosts('all', this)">All Posts</button>
      <button class="filter-btn" onclick="filterPosts('Product Update', this)">Product Updates</button>
      <button class="filter-btn" onclick="filterPosts('HR Guide', this)">HR Guides</button>
    </div>

    <div class="posts-grid" id="posts-grid">
      <!-- rendered by JS -->
    </div>

    <div class="blog-cta">
      <h2>Ready to simplify HR & payroll?</h2>
      <p>Join Philippine businesses already running payroll on MAO Workforce.</p>
      <a href="https://portal.maoworkforce.com" class="btn-cta">Start free — no credit card</a>
    </div>
  </div>

{FOOTER_HTML}

  <script>
    const posts = {json.dumps(posts)};

    function formatDate(d) {{
      return new Date(d + 'T00:00:00').toLocaleDateString('en-PH', {{ year: 'numeric', month: 'long', day: 'numeric' }});
    }}

    function badgeClass(cat) {{
      return cat === 'Product Update' ? 'badge-product' : 'badge-hr';
    }}

    function renderPosts(filtered) {{
      const grid = document.getElementById('posts-grid');
      if (!filtered.length) {{
        grid.innerHTML = '<div class="empty-state"><h3>No posts yet</h3><p>Check back soon.</p></div>';
        return;
      }}
      grid.innerHTML = filtered.map(p => `
        <a class="post-card" href="/blog/${{p.slug}}">
          <div class="post-card-body">
            <div class="post-meta">
              <span class="category-badge ${{badgeClass(p.category)}}">${{p.category}}</span>
              <span class="post-date">${{formatDate(p.date)}}</span>
              <span class="post-read-time">· ${{p.readTime}}</span>
            </div>
            <h2>${{p.title}}</h2>
            <p class="post-excerpt">${{p.excerpt}}</p>
          </div>
          <div class="post-card-footer">
            <span class="post-author">${{p.author}}</span>
            <span class="read-more">Read more →</span>
          </div>
        </a>
      `).join('');
    }}

    function filterPosts(cat, btn) {{
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderPosts(cat === 'all' ? posts : posts.filter(p => p.category === cat));
    }}

    renderPosts(posts);
  </script>
</body>
</html>"""

with open(os.path.join(blog_dir, 'index.html'), 'w') as f:
    f.write(blog_index)
print("✓ blog/index.html")

# ── blog/introducing-mao-workforce.html ──────────────────────────────────────
post_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Introducing MAO Workforce — MAO Blog</title>
  <meta name="description" content="We built MAO Workforce because payroll in the Philippines shouldn't require an accountant on speed dial. Here's the story behind the product." />
  <meta property="og:title" content="Introducing MAO Workforce: HR & Payroll Built for Philippine Businesses" />
  <meta property="og:description" content="We built MAO Workforce because payroll in the Philippines shouldn't require an accountant on speed dial." />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://maoworkforce.com/blog/introducing-mao-workforce" />
  <meta property="article:published_time" content="2026-06-18" />
  <meta property="article:author" content="Abegail Unay" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,600;0,700;1,400&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
{SHARED_CSS}

    /* ── POST PAGE ── */
    .post-header {{
      background: var(--heritage);
      padding: 72px 40px 64px;
    }}
    .post-header-inner {{ max-width: 760px; margin: 0 auto; }}
    .back-link {{
      display: inline-flex; align-items: center; gap: 6px;
      color: rgba(232,239,235,0.6); text-decoration: none;
      font-size: 13px; font-weight: 600;
      margin-bottom: 28px;
      transition: color 0.2s;
    }}
    .back-link:hover {{ color: var(--on-heritage); }}
    .post-header .post-meta {{
      display: flex; align-items: center; gap: 10px;
      margin-bottom: 20px; flex-wrap: wrap;
    }}
    .category-badge {{
      font-size: 11px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;
      padding: 4px 10px; border-radius: 12px;
    }}
    .badge-product {{ background: rgba(232,239,235,0.15); color: var(--on-heritage); }}
    .post-header .post-date, .post-header .post-read-time {{
      font-size: 13px; color: rgba(232,239,235,0.55);
    }}
    .post-header h1 {{
      font-family: 'Fraunces', serif;
      font-size: clamp(28px, 4vw, 44px);
      color: var(--on-heritage);
      font-weight: 700; line-height: 1.2;
      margin-bottom: 20px;
    }}
    .post-header .excerpt {{
      font-size: 18px; color: rgba(232,239,235,0.7);
      line-height: 1.65; max-width: 640px;
    }}
    .author-row {{
      display: flex; align-items: center; gap: 12px;
      margin-top: 32px; padding-top: 28px;
      border-top: 1px solid rgba(232,239,235,0.12);
    }}
    .author-avatar {{
      width: 40px; height: 40px; border-radius: 50%;
      background: var(--terracotta);
      display: flex; align-items: center; justify-content: center;
      font-family: 'Fraunces', serif; font-size: 16px; font-weight: 700;
      color: white; flex-shrink: 0;
    }}
    .author-name {{ font-size: 14px; font-weight: 600; color: var(--on-heritage); }}
    .author-role {{ font-size: 12px; color: rgba(232,239,235,0.5); }}

    /* ── ARTICLE BODY ── */
    .post-body {{
      max-width: 760px; margin: 0 auto; padding: 64px 40px 80px;
    }}
    .post-body h2 {{
      font-family: 'Fraunces', serif;
      font-size: 26px; font-weight: 700;
      color: var(--heritage); margin: 48px 0 16px;
      line-height: 1.3;
    }}
    .post-body h3 {{
      font-family: 'Fraunces', serif;
      font-size: 20px; font-weight: 600;
      color: var(--text); margin: 32px 0 12px;
    }}
    .post-body p {{
      font-size: 17px; line-height: 1.8;
      color: var(--text); margin-bottom: 20px;
    }}
    .post-body ul, .post-body ol {{
      padding-left: 24px; margin-bottom: 20px;
    }}
    .post-body li {{
      font-size: 17px; line-height: 1.8;
      color: var(--text); margin-bottom: 8px;
    }}
    .post-body strong {{ font-weight: 700; color: var(--text); }}
    .post-body a {{ color: var(--terracotta); text-decoration: underline; text-underline-offset: 3px; }}

    .callout {{
      background: var(--parch-deep);
      border-left: 4px solid var(--terracotta);
      border-radius: 0 12px 12px 0;
      padding: 20px 24px;
      margin: 32px 0;
    }}
    .callout p {{ margin: 0; font-size: 16px; color: var(--text-muted); font-style: italic; }}

    .divider {{ border: none; border-top: 1px solid var(--border); margin: 48px 0; }}

    /* post CTA */
    .post-cta {{
      background: var(--heritage);
      border-radius: 16px;
      padding: 40px; text-align: center;
      margin-top: 64px;
    }}
    .post-cta h3 {{
      font-family: 'Fraunces', serif;
      font-size: 24px; color: var(--on-heritage);
      margin-bottom: 10px; margin-top: 0;
    }}
    .post-cta p {{ color: rgba(232,239,235,0.65); margin-bottom: 24px; font-size: 15px; }}
    .btn-cta {{
      display: inline-block; background: var(--terracotta); color: white;
      padding: 12px 28px; border-radius: 10px;
      font-weight: 700; font-size: 15px; text-decoration: none;
      transition: background 0.2s;
    }}
    .btn-cta:hover {{ background: var(--terra-light); }}

    @media (max-width: 768px) {{
      .post-header {{ padding: 48px 20px 40px; }}
      .post-body {{ padding: 40px 20px 60px; }}
    }}
  </style>
</head>
<body>

{NAV_HTML}

  <div class="post-header">
    <div class="post-header-inner">
      <a href="/blog" class="back-link">← Back to Blog</a>
      <div class="post-meta">
        <span class="category-badge badge-product">Product Update</span>
        <span class="post-date">June 18, 2026</span>
        <span class="post-read-time">· 4 min read</span>
      </div>
      <h1>Introducing MAO Workforce: HR &amp; Payroll Built for Philippine Businesses</h1>
      <p class="excerpt">We built MAO Workforce because payroll in the Philippines shouldn't require an accountant on speed dial. Here's the story behind the product and what we're building.</p>
      <div class="author-row">
        <div class="author-avatar">A</div>
        <div>
          <div class="author-name">Abegail Unay</div>
          <div class="author-role">Founder, MAO Workforce</div>
        </div>
      </div>
    </div>
  </div>

  <div class="post-body">

    <p>If you've ever run payroll for a small business in the Philippines, you know the drill: spreadsheets, a separate payroll accountant, hours spent computing SSS, PhilHealth, and Pag-IBIG contributions, and a constant fear that you got the BIR withholding wrong.</p>

    <p>We built MAO Workforce to change that.</p>

    <h2>Why we built this</h2>

    <p>The problem isn't that Philippine labor law is complicated — it actually has a clear set of rules. The problem is that the tools available to small business owners were either built for enterprise companies with full HR departments, or so generic that they didn't account for Philippine-specific requirements at all.</p>

    <p>Business owners were stuck stitching together spreadsheets, WhatsApp messages, and Google Forms to manage their teams. Every payroll run was a manual exercise. Every attendance dispute was a conversation in a chat group. Every new hire meant another row in a sheet someone was already maintaining by hand.</p>

    <div class="callout">
      <p>"The system should just know that May 1 is a Philippine holiday and compute the right pay. I shouldn't have to look it up and add it manually every year."</p>
    </div>

    <p>That quote came from one of our early users. It stuck with us, because it captures exactly what we're trying to solve: compliance should be baked in, not bolted on.</p>

    <h2>What MAO Workforce does today</h2>

    <p>MAO Workforce is a self-serve HR and payroll platform that Philippine businesses can run independently. Here's what's live today:</p>

    <ul>
      <li><strong>Payroll automation</strong> — regular, semi-monthly, and weekly runs with automatic computation of night differentials, overtime, late deductions, and holiday pay</li>
      <li><strong>Statutory compliance</strong> — SSS, PhilHealth, Pag-IBIG, and BIR withholding computed automatically on every run</li>
      <li><strong>Attendance tracking</strong> — clock-in via kiosk, PIN, or the employee self-service portal, with shift schedules and exception handling</li>
      <li><strong>Employee self-service</strong> — employees can view payslips, file attendance corrections, request leave, and raise payroll disputes from their own portal</li>
      <li><strong>Leave management</strong> — SL, VL, and custom leave types with approval workflows and auto-deduction from payroll</li>
      <li><strong>Geofencing</strong> — restrict clock-ins to employees within range of your business location, available on the free plan</li>
    </ul>

    <p>And it's all available starting at ₱0 — free forever for businesses with up to 5 employees, with paid plans that scale as you grow.</p>

    <h2>What's coming next</h2>

    <p>We're still early. The roadmap includes BIR compliance exports (Alphalist, 2316), multi-branch payroll with cross-branch visibility, advanced analytics for workforce planning, and deeper integrations with the tools Philippine businesses already use.</p>

    <p>We're building this in public, shipping fast, and listening closely to our users. If something is broken or missing, we want to know.</p>

    <hr class="divider" />

    <p>If you're a Philippine business owner managing payroll manually — or paying for software that wasn't built with your requirements in mind — MAO Workforce is worth trying. It takes about 10 minutes to set up and no credit card is required.</p>

    <div class="post-cta">
      <h3>Try MAO Workforce free</h3>
      <p>Set up in 10 minutes. No credit card required.</p>
      <a href="https://portal.maoworkforce.com" class="btn-cta">Create your free account →</a>
    </div>

  </div>

{FOOTER_HTML}

</body>
</html>"""

post_path = os.path.join(blog_dir, 'introducing-mao-workforce.html')
with open(post_path, 'w') as f:
    f.write(post_html)
print("✓ blog/introducing-mao-workforce.html")

print()
print("All done. Run:")
print("  cd ~/mao-landing && git add -A && git commit -m 'Add /blog with index and first post' && git push")
