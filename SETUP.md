# Publishing This Portfolio — Setup Guide

Everything below assumes you've unzipped the repo folder somewhere on your machine. Total time: about 20 minutes for GitHub, another 30 if you do GitHub Pages.

---

## Part 1 — Fill in the placeholders first

Before you push anything, edit `README.md` at the repo root. Three placeholders need your real values:

```markdown
[LinkedIn](#) · [morrisseyventuresllc.com](https://morrisseyventuresllc.com) · [Email](#)
```

Replace `(#)` with your actual LinkedIn URL and a `mailto:` link. Decide whether you want a public email address — a lot of people use a dedicated one for job search rather than their primary.

Also review the credential line at the top and confirm it's exactly how you want it stated.

---

## Part 2 — Repository setup

### Naming

Name the repo **`grc-portfolio`**. Not `chris-morrissey-portfolio`, not `cybersecurity-stuff`. When it appears in a URL on your resume — `github.com/yourhandle/grc-portfolio` — it should say what it is.

### Create it on GitHub

1. Go to github.com → **New repository**
2. Name: `grc-portfolio`
3. Description: `Cybersecurity GRC portfolio — risk programs, FedRAMP Rev5 authorization package, and FedRAMP 20x KSI validation engine. All organizations fictional.`
4. **Public**
5. Do **not** initialize with a README, .gitignore, or license — you already have all three

### Push from your machine

```bash
cd path/to/grc-portfolio

git init
git add .
git commit -m "Initial commit: three GRC portfolio projects"
git branch -M main
git remote add origin https://github.com/YOUR-HANDLE/grc-portfolio.git
git push -u origin main
```

If you have 2FA enabled (you should), you'll need a personal access token instead of a password, or use the GitHub CLI:

```bash
gh auth login
gh repo create grc-portfolio --public --source=. --remote=origin --push
```

### Configure the repo after pushing

**Topics** (right sidebar → gear icon next to About). These drive GitHub search:

```
grc  cybersecurity  fedramp  nist-800-53  risk-management
compliance  iso27001  nist-csf  fedramp-20x  rmf  security-assessment
```

**About section** — set the description and check "Releases" and "Packages" off. Nothing to release.

**Disable Issues and Wiki** (Settings → Features). This is a portfolio, not a software project. Leaving them on invites empty tabs.

**Social preview image** (Settings → Social preview). Optional but worth doing — when you share the link on LinkedIn, a custom image beats a generic GitHub card. A simple title card works.

---

## Part 3 — What to verify after pushing

Click through these yourself before you send the link anywhere:

- [ ] Root README renders correctly, tables aren't broken
- [ ] The fictional-company warning is visible **without scrolling**
- [ ] All three project links work
- [ ] Click a PDF link — it should preview in-browser, not download
- [ ] Click an .xlsx link — GitHub will say it can't render it; confirm the PDF alternative is right next to it
- [ ] `src/ksi_validator.py` displays with syntax highlighting
- [ ] The JSON files render in GitHub's JSON viewer
- [ ] Read the whole root README on your phone. Most recruiters will.

---

## Part 4 — GitHub Pages (the bridge to your website)

This gives you a browsable site at `yourhandle.github.io/grc-portfolio` from the same markdown, with no extra maintenance. It's also the natural precursor to the morrisseyventuresllc.com section — same content, and later you point a subdomain at it.

### Enable it

1. Settings → Pages
2. Source: **Deploy from a branch**
3. Branch: `main`, folder: `/ (root)`
4. Save

Wait 2–3 minutes. Then add a `_config.yml` at the repo root:

```yaml
title: GRC Portfolio — Chris Morrissey
description: Risk programs, FedRAMP authorization packages, and continuous validation engineering
theme: jekyll-theme-cayman
show_downloads: false
```

`cayman` is clean and readable. Alternatives worth trying: `minima`, `jekyll-theme-slate`, `jekyll-theme-architect`.

Commit and push — Pages rebuilds automatically.

### Later: custom subdomain

When you're ready to connect it to your domain:

1. Add a `CNAME` file at the repo root containing exactly: `portfolio.morrisseyventuresllc.com`
2. In your DNS provider, add a CNAME record: `portfolio` → `YOUR-HANDLE.github.io`
3. Settings → Pages → Custom domain → enter the same value → check **Enforce HTTPS**

DNS propagation takes anywhere from minutes to a few hours.

---

## Part 5 — The morrisseyventuresllc.com section

Two approaches, depending on how much you want to maintain.

### Option A — Subdomain pointing at GitHub Pages (recommended to start)

`portfolio.morrisseyventuresllc.com` → the Pages site above.

**Pros:** zero duplicate maintenance, updates when you push, looks professional, free.
**Cons:** visual style is the Jekyll theme, not your brand.

This is the right first move. Do it now, upgrade later if it matters.

### Option B — Native section on the main site

A `/portfolio` or `/capabilities` section built into your existing site.

**Recommended structure:**

```
/portfolio
├── Overview page — the three-project argument, one paragraph each
├── /portfolio/grc-program        → Project 1 summary + artifact links
├── /portfolio/fedramp-ato        → Project 2 summary + artifact links
└── /portfolio/fedramp-20x        → Project 3 summary + live validator output
```

**Content strategy:** don't duplicate the READMEs. The website pages should be **shorter and more visual** than GitHub — 200–300 words per project, one or two screenshots, a clear "view full artifacts on GitHub" link. GitHub is where the depth lives; the website is the storefront.

**What to put on the site that isn't on GitHub:**
- Screenshots of the artifacts (a risk register with the conditional formatting visible is genuinely compelling at a glance)
- A short "how I work" statement
- The three-project arc as a visual timeline
- Contact / availability

**Critical for the business site:** the fictional-company disclaimer needs to be *more* prominent here, not less. On a consulting company's website, a document titled "System Security Plan" could be misread as client work. A visible banner on every portfolio page — "Demonstration artifacts. All organizations fictional. No client work depicted." — protects you.

---

## Part 6 — Ongoing

**When you update an artifact,** regenerate the PDF so the two stay in sync:

```bash
# macOS/Linux with LibreOffice installed
soffice --headless --convert-to pdf --outdir pdf artifacts/updated_file.xlsx
```

**Commit messages matter here** more than in a normal repo, because your commit history is visible and reads as a record of ongoing work. `Update risk register scoring methodology` beats `update`.

**Consider a CHANGELOG** if you keep iterating. A portfolio that visibly evolves over months is more credible than one that appeared fully formed in a single commit.

**Pin the repo** on your GitHub profile (profile → Customize your pins).

---

## Part 7 — Using the link

**On your resume:** put it in the header next to LinkedIn, not buried in a projects section.

**In applications:** when a field asks for a portfolio or website, this is it.

**On LinkedIn:** add it to Featured. Don't just post the link — post one of the artifacts as a document with a short writeup, and link the repo from there. The FedRAMP 20x drift finding is the strongest single post you have, because almost nobody has published practical 20x work yet.

**In interviews:** have the repo open in a tab before the call starts. When they ask about a project, you're sharing a screen in four seconds instead of hunting for a file.
