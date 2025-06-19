---
layout: none
---

<style>
:root {
  --primary: #4e54c8;
  --primary-light: #8f94fb;
  --accent: #f5a623;
  --bg-dark: #181a20;
  --bg-darker: #10141a;
  --text-main: #f4f4f4;
  --text-muted: #b0b3b8;
  --card-bg: #23263a;
  --card-shadow: 0 2px 16px #0003;
}
body {
  background: var(--bg-darker);
  color: var(--text-main);
  font-family: 'Segoe UI', Arial, sans-serif;
  margin: 0;
  scroll-behavior: smooth;
}
.navbar {
  position: sticky;
  top: 0;
  width: 100%;
  background: rgba(24, 26, 32, 0.97);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.7rem 2rem;
  z-index: 100;
  box-shadow: var(--card-shadow);
}
.nav-logo {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--primary);
  text-decoration: none;
}
.nav-logo svg {
  height: 2.2rem;
  width: 2.2rem;
}
.nav-links {
  display: flex;
  gap: 1.5rem;
}
.nav-link {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 1.05rem;
  font-weight: 500;
  transition: color 0.2s;
}
.nav-link:hover {
  color: var(--accent);
}
.hero {
  min-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  background: linear-gradient(135deg, var(--bg-darker) 60%, var(--bg-dark) 100%);
  position: relative;
  overflow: hidden;
}
.hero-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  z-index: 0;
  pointer-events: none;
}
.hero-content {
  position: relative;
  z-index: 1;
  padding-top: 5vh;
}
.hero-logo {
  margin-bottom: 1.5rem;
}
.hero-title {
  font-size: 2.7rem;
  font-weight: bold;
  color: var(--text-main);
  margin-bottom: 1rem;
  letter-spacing: 1px;
}
.hero-tagline {
  font-size: 1.3rem;
  color: var(--text-muted);
  margin-bottom: 2.2rem;
}
.hero-cta {
  background: linear-gradient(90deg, var(--primary), var(--primary-light));
  color: var(--bg-darker);
  font-weight: 600;
  font-size: 1.1rem;
  border: none;
  border-radius: 0.7rem;
  padding: 0.9rem 2.2rem;
  cursor: pointer;
  box-shadow: var(--card-shadow);
  transition: background 0.2s, color 0.2s;
}
.hero-cta:hover {
  background: linear-gradient(90deg, var(--primary-light), var(--primary));
  color: var(--text-main);
}
.section {
  max-width: 900px;
  margin: 0 auto;
  padding: 4rem 1.5rem 2rem 1.5rem;
}
.section-title {
  font-size: 2rem;
  color: var(--primary);
  margin-bottom: 1rem;
  text-align: center;
  letter-spacing: 1px;
}
.section-text {
  color: var(--text-muted);
  font-size: 1.1rem;
  text-align: center;
  margin-bottom: 2.5rem;
}
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  margin-bottom: 2rem;
}
.card {
  background: var(--card-bg);
  border-radius: 1.2rem;
  padding: 2rem 1.5rem;
  min-width: 220px;
  max-width: 300px;
  box-shadow: var(--card-shadow);
  text-align: center;
  flex: 1 1 220px;
  transition: transform 0.2s, box-shadow 0.2s;
}
.card:hover {
  transform: translateY(-6px) scale(1.03);
  box-shadow: 0 6px 24px #0007;
}
.card-icon {
  font-size: 2.5rem;
  color: var(--accent);
  margin-bottom: 1rem;
}
.card-title {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.card-desc {
  color: var(--text-muted);
  font-size: 1rem;
}
.mission-vision {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 2rem;
}
.mv-card {
  background: var(--card-bg);
  border-radius: 1.2rem;
  padding: 2rem 1.5rem;
  min-width: 220px;
  max-width: 350px;
  box-shadow: var(--card-shadow);
  text-align: center;
  flex: 1 1 220px;
}
.mv-title {
  color: var(--primary);
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.7rem;
}
.mv-desc {
  color: var(--text-muted);
  font-size: 1rem;
}
.steps {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  margin-bottom: 2rem;
}
.step {
  background: var(--card-bg);
  border-radius: 1.2rem;
  padding: 2rem 1.5rem;
  min-width: 180px;
  max-width: 220px;
  box-shadow: var(--card-shadow);
  text-align: center;
  flex: 1 1 180px;
}
.step-icon {
  font-size: 2.2rem;
  color: var(--accent);
  margin-bottom: 1rem;
}
.step-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.step-desc {
  color: var(--text-muted);
  font-size: 0.98rem;
}
.trusted {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  align-items: center;
  margin-bottom: 2rem;
}
.trusted-logo {
  background: #fff;
  border-radius: 0.7rem;
  padding: 0.7rem 1.2rem;
  margin: 0.5rem;
  height: 48px;
  display: flex;
  align-items: center;
  box-shadow: 0 2px 8px #0002;
}
.trusted-logo img {
  height: 32px;
  width: auto;
  display: block;
}
.testimonials {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  margin-bottom: 2rem;
}
.testimonial {
  background: var(--card-bg);
  border-radius: 1.2rem;
  padding: 2rem 1.5rem;
  min-width: 220px;
  max-width: 350px;
  box-shadow: var(--card-shadow);
  text-align: left;
  flex: 1 1 220px;
  color: var(--text-main);
  font-size: 1rem;
  position: relative;
}
.testimonial:before {
  content: '“';
  font-size: 2.5rem;
  color: var(--accent);
  position: absolute;
  left: 1rem;
  top: 0.5rem;
}
.testimonial-author {
  margin-top: 1.2rem;
  font-size: 0.98rem;
  color: var(--primary);
  font-weight: 600;
}
.notify-section {
  background: var(--card-bg);
  border-radius: 1.2rem;
  padding: 2.5rem 1.5rem;
  text-align: center;
  margin: 2rem auto 0 auto;
  max-width: 400px;
  box-shadow: var(--card-shadow);
}
.notify-title {
  color: var(--primary);
  font-size: 1.2rem;
  margin-bottom: 1rem;
}
.notify-form {
  display: flex;
  gap: 0.5rem;
  justify-content: center;
}
.notify-input {
  padding: 0.7rem 1rem;
  border-radius: 0.5rem;
  border: none;
  outline: none;
  font-size: 1rem;
  background: #222;
  color: var(--text-main);
}
.notify-btn {
  background: var(--accent);
  color: var(--bg-darker);
  border: none;
  border-radius: 0.5rem;
  padding: 0.7rem 1.2rem;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}
.notify-btn:hover {
  background: #f7b84b;
  color: var(--text-main);
}
.privacy-note {
  color: #888;
  font-size: 0.9rem;
  margin-top: 1rem;
}
footer {
  text-align: center;
  color: #666;
  padding: 2.5rem 0 1.2rem 0;
  font-size: 0.98rem;
  background: var(--card-bg);
  margin-top: 3rem;
}
.footer-social {
  margin: 1rem 0 0.5rem 0;
}
.footer-social a {
  color: var(--primary);
  margin: 0 0.5rem;
  font-size: 1.5rem;
  transition: color 0.2s;
}
.footer-social a:hover {
  color: var(--accent);
}
@media (max-width: 900px) {
  .cards, .features, .mission-vision, .steps, .testimonials, .trusted {
    flex-direction: column;
    gap: 1.2rem;
  }
  .section { padding: 2.5rem 1rem 1.5rem 1rem; }
  .navbar { padding: 0.7rem 1rem; }
}
</style>

<!-- Navbar -->
<nav class="navbar">
  <a href="#hero" class="nav-logo">
    <!-- Professional geometric logo SVG -->
    <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="4" y="4" width="40" height="40" rx="12" fill="url(#kwestLogoGrad)"/><path d="M15 33L24 15L33 33" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="24" cy="24" r="20" stroke="#fff" stroke-width="2"/><defs><linearGradient id="kwestLogoGrad" x1="4" y1="4" x2="44" y2="44" gradientUnits="userSpaceOnUse"><stop stop-color="#4e54c8"/><stop offset="1" stop-color="#8f94fb"/></linearGradient></defs></svg>
    Kwest AI
  </a>
  <div class="nav-links">
    <a href="#about" class="nav-link">About</a>
    <a href="#features" class="nav-link">Features</a>
    <a href="#how" class="nav-link">How it Works</a>
    <a href="#testimonials" class="nav-link">AI & Industry</a>
    <a href="#notify" class="nav-link">Contact</a>
  </div>
</nav>

<!-- Hero -->
<div class="hero" id="hero">
  <div class="hero-bg">
    <!-- Elegant, layered SVG wave background -->
    <svg width="100%" height="100%" viewBox="0 0 1440 400" fill="none" xmlns="http://www.w3.org/2000/svg" style="position:absolute;bottom:0;left:0;">
      <defs>
        <linearGradient id="waveGrad1" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#4e54c8" stop-opacity="0.18"/>
          <stop offset="100%" stop-color="#23263a" stop-opacity="0.32"/>
        </linearGradient>
        <linearGradient id="waveGrad2" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#8f94fb" stop-opacity="0.12"/>
          <stop offset="100%" stop-color="#10141a" stop-opacity="0.22"/>
        </linearGradient>
      </defs>
      <path d="M0,320 Q360,240 720,320 T1440,320 V400 H0 Z" fill="url(#waveGrad1)"/>
      <path d="M0,360 Q360,300 720,360 T1440,360 V400 H0 Z" fill="url(#waveGrad2)"/>
    </svg>
  </div>
  <div class="hero-content">
    <div class="hero-logo">
      <!-- Professional geometric logo SVG, larger -->
      <svg viewBox="0 0 120 120" width="90" height="90" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="100" height="100" rx="24" fill="url(#kwestHeroLogoGrad)"/><path d="M35 85L60 35L85 85" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="60" cy="60" r="48" stroke="#fff" stroke-width="3"/><defs><linearGradient id="kwestHeroLogoGrad" x1="10" y1="10" x2="110" y2="110" gradientUnits="userSpaceOnUse"><stop stop-color="#4e54c8"/><stop offset="1" stop-color="#8f94fb"/></linearGradient></defs></svg>
    </div>
    <div class="hero-title">Kwest AI</div>
    <div class="hero-tagline">Automation testing using AI agents</div>
    <a href="#notify"><button class="hero-cta">Get Notified</button></a>
  </div>
</div>

<!-- About Section -->
<div class="section" id="about">
  <div class="section-title">About Kwest AI</div>
  <div class="section-text">
    Kwest AI is revolutionizing software quality assurance with intelligent, autonomous testing agents. Our platform leverages the power of AI to automate complex testing workflows, accelerate release cycles, and ensure robust, reliable software—every time.
  </div>
  <div class="mission-vision">
    <div class="mv-card">
      <div class="mv-title">Our Mission</div>
      <div class="mv-desc">To empower teams to deliver flawless software, faster, by automating the most complex testing tasks with AI-driven agents.</div>
    </div>
    <div class="mv-card">
      <div class="mv-title">Our Vision</div>
      <div class="mv-desc">To become the world's most trusted platform for autonomous software testing, setting new standards for quality and speed.</div>
    </div>
  </div>
</div>

<!-- Features Section -->
<div class="section" id="features">
  <div class="section-title">Key Features</div>
  <div class="cards">
    <div class="card">
      <div class="card-icon">🤖</div>
      <div class="card-title">AI-Powered Agents</div>
      <div class="card-desc">Harness the intelligence of AI to create, execute, and adapt tests automatically.</div>
    </div>
    <div class="card">
      <div class="card-icon">⚡</div>
      <div class="card-title">Fast Automation</div>
      <div class="card-desc">Accelerate your testing cycles and deliver high-quality software faster than ever.</div>
    </div>
    <div class="card">
      <div class="card-icon">🔗</div>
      <div class="card-title">Seamless Integration</div>
      <div class="card-desc">Integrate easily with your existing CI/CD pipelines and development tools.</div>
    </div>
    <div class="card">
      <div class="card-icon">🛡️</div>
      <div class="card-title">Reliable & Secure</div>
      <div class="card-desc">Enterprise-grade security and reliability for your mission-critical applications.</div>
    </div>
    <div class="card">
      <div class="card-icon">📊</div>
      <div class="card-title">Insightful Analytics</div>
      <div class="card-desc">Get actionable insights and detailed reports to continuously improve your QA process.</div>
    </div>
  </div>
</div>

<!-- How It Works Section -->
<div class="section" id="how">
  <div class="section-title">How It Works</div>
  <div class="steps">
    <div class="step">
      <div class="step-icon">1️⃣</div>
      <div class="step-title">Connect</div>
      <div class="step-desc">Link your codebase and CI/CD tools in minutes.</div>
    </div>
    <div class="step">
      <div class="step-icon">2️⃣</div>
      <div class="step-title">Configure</div>
      <div class="step-desc">Set your testing goals and preferences—no code required.</div>
    </div>
    <div class="step">
      <div class="step-icon">3️⃣</div>
      <div class="step-title">Automate</div>
      <div class="step-desc">Let our AI agents generate, run, and adapt tests for you.</div>
    </div>
    <div class="step">
      <div class="step-icon">4️⃣</div>
      <div class="step-title">Analyze</div>
      <div class="step-desc">Review results, get insights, and improve continuously.</div>
    </div>
  </div>
</div>

<!-- Trusted By Section -->
<div class="section" id="trusted">
  <div class="section-title">Trusted By</div>
  <div class="trusted">
    <div class="trusted-logo"><img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg" alt="Microsoft" /></div>
    <div class="trusted-logo"><img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Logo_TV_2015.png" alt="TechVision" /></div>
    <div class="trusted-logo"><img src="https://upload.wikimedia.org/wikipedia/commons/5/51/IBM_logo.svg" alt="IBM" /></div>
    <div class="trusted-logo"><img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" alt="Google" /></div>
    <div class="trusted-logo"><img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" alt="Netflix" /></div>
  </div>
</div>

<!-- AI & Industry Section -->
<div class="section" id="testimonials">
  <div class="section-title">AI & Industry: What Companies Say</div>
  <div class="testimonials">
    <div class="testimonial">
      "AI-driven testing will be a game changer, enabling us to deliver higher quality software at unprecedented speed."
      <div class="testimonial-author">— Microsoft, 2023 Industry Report</div>
    </div>
    <div class="testimonial">
      "The future of software testing is autonomous. AI will allow teams to focus on innovation, not manual QA."
      <div class="testimonial-author">— Google Cloud, 2024 Whitepaper</div>
    </div>
    <div class="testimonial">
      "AI-powered automation is set to redefine how enterprises ensure reliability and security in their applications."
      <div class="testimonial-author">— IBM Research, 2023</div>
    </div>
  </div>
</div>

<!-- Notify/Contact Section -->
<div class="section" id="notify">
  <div class="notify-section">
    <div class="notify-title">Want to be notified when we launch?</div>
    <form class="notify-form" onsubmit="event.preventDefault(); alert('Thank you! We will notify you.');">
      <input class="notify-input" type="email" placeholder="Your email" required />
      <button class="notify-btn" type="submit">Notify Me</button>
    </form>
    <div class="privacy-note">We respect your privacy. No spam, ever.</div>
  </div>
</div>

<!-- Footer -->
<footer>
  <div class="footer-social">
    <a href="#" title="Twitter"><svg width="24" height="24" fill="currentColor"><path d="M22.46 6c-.77.35-1.6.58-2.47.69a4.3 4.3 0 0 0 1.88-2.37 8.59 8.59 0 0 1-2.72 1.04A4.28 4.28 0 0 0 16.11 4c-2.37 0-4.29 1.92-4.29 4.29 0 .34.04.67.11.99C7.69 9.13 4.07 7.3 1.64 4.6c-.37.64-.58 1.38-.58 2.17 0 1.5.76 2.82 1.92 3.6-.7-.02-1.36-.21-1.94-.53v.05c0 2.1 1.5 3.85 3.5 4.25-.36.1-.74.16-1.13.16-.28 0-.54-.03-.8-.08.54 1.7 2.1 2.94 3.95 2.97A8.6 8.6 0 0 1 2 19.54c-.29 0-.57-.02-.85-.05A12.13 12.13 0 0 0 8.29 21.5c7.55 0 11.68-6.26 11.68-11.68 0-.18-.01-.36-.02-.54A8.18 8.18 0 0 0 24 4.59a8.36 8.36 0 0 1-2.54.7z"/></svg></a>
    <a href="#" title="LinkedIn"><svg width="24" height="24" fill="currentColor"><path d="M19 0h-14c-2.76 0-5 2.24-5 5v14c0 2.76 2.24 5 5 5h14c2.76 0 5-2.24 5-5v-14c0-2.76-2.24-5-5-5zm-11 19h-3v-9h3v9zm-1.5-10.28c-.97 0-1.75-.79-1.75-1.75s.78-1.75 1.75-1.75 1.75.79 1.75 1.75-.78 1.75-1.75 1.75zm13.5 10.28h-3v-4.5c0-1.08-.02-2.47-1.5-2.47-1.5 0-1.73 1.17-1.73 2.39v4.58h-3v-9h2.88v1.23h.04c.4-.75 1.38-1.54 2.84-1.54 3.04 0 3.6 2 3.6 4.59v4.72z"/></svg></a>
    <a href="#" title="GitHub"><svg width="24" height="24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.438 9.8 8.205 11.387.6.113.82-.262.82-.582 0-.288-.012-1.243-.018-2.252-3.338.726-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.756-1.333-1.756-1.09-.745.083-.729.083-.729 1.205.085 1.84 1.237 1.84 1.237 1.07 1.834 2.807 1.304 3.492.997.108-.775.418-1.305.762-1.606-2.665-.304-5.466-1.332-5.466-5.93 0-1.31.468-2.38 1.236-3.22-.124-.303-.535-1.523.117-3.176 0 0 1.008-.322 3.3 1.23.96-.267 1.98-.399 3-.404 1.02.005 2.04.137 3 .404 2.29-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.873.12 3.176.77.84 1.235 1.91 1.235 3.22 0 4.61-2.803 5.624-5.475 5.92.43.37.823 1.102.823 2.222 0 1.606-.015 2.898-.015 3.293 0 .322.218.698.825.58C20.565 21.796 24 17.297 24 12c0-6.63-5.37-12-12-12z"/></svg></a>
  </div>
  &copy; 2024 Kwest AI. All rights reserved.
</footer>
