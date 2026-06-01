import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add fonts
font_links = """  <title>Aklas Beladp - Daily Report Dashboard</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>"""
content = re.sub(r'  <title>Aklas Beladp - Daily Report Dashboard</title>\s*<style>', font_links, content)

# 2. Replace Hero CSS
new_hero_css = """    /* ===== HERO ===== */
    :root {
      --gold: #FFD700;
      --gold-glow: rgba(255, 215, 0, 0.5);
      --cyan: #00E5FF;
      --cyan-glow: rgba(0, 229, 255, 0.5);
      --red: #FF3B5C;
      --red-glow: rgba(255, 59, 92, 0.5);
      --purple: #B44AFF;
      --purple-glow: rgba(180, 74, 255, 0.5);
      --green: #00E676;
      --green-glow: rgba(0, 230, 118, 0.5);
      --bg-primary: #0a0a0f;
      --bg-secondary: #12121a;
      --card-bg: rgba(255, 255, 255, 0.03);
      --card-border: rgba(255, 255, 255, 0.08);
    }

    .hero-section {
      font-family: 'Rajdhani', sans-serif;
      position: relative;
      width: 100%;
      height: 100vh;
      min-height: 700px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      perspective: 1200px;
      overflow: hidden;
    }

    /* Background layers */
    .bg-layer {
      position: absolute;
      inset: 0;
      z-index: 0;
    }

    .bg-gradient {
      background: radial-gradient(ellipse at 20% 50%, rgba(255, 140, 0, 0.08) 0%, transparent 50%),
                  radial-gradient(ellipse at 80% 50%, rgba(180, 74, 255, 0.06) 0%, transparent 50%),
                  radial-gradient(ellipse at 50% 0%, rgba(0, 229, 255, 0.05) 0%, transparent 50%),
                  linear-gradient(180deg, var(--bg-primary) 0%, #0d0d15 50%, var(--bg-primary) 100%);
      animation: bgRotate 30s linear infinite;
    }

    @keyframes bgRotate {
      0% { filter: hue-rotate(0deg); }
      100% { filter: hue-rotate(360deg); }
    }

    .bg-grid {
      background-image:
        linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px);
      background-size: 60px 60px;
      opacity: 0.5;
    }

    /* Particles */
    .particles-container {
      position: absolute;
      inset: 0;
      z-index: 1;
      overflow: hidden;
    }

    .particle {
      position: absolute;
      border-radius: 50%;
      pointer-events: none;
      animation: particleFloat linear infinite;
    }

    @keyframes particleFloat {
      0% { transform: translateY(100vh) translateX(0) scale(0); opacity: 0; }
      10% { opacity: 1; scale: 1; }
      90% { opacity: 1; }
      100% { transform: translateY(-10vh) translateX(100px) scale(0.5); opacity: 0; }
    }

    /* Floating orbs */
    .orb {
      position: absolute;
      border-radius: 50%;
      filter: blur(40px);
      opacity: 0.3;
      pointer-events: none;
    }

    .orb-1 {
      width: 400px; height: 400px;
      background: radial-gradient(circle, rgba(255,215,0,0.3), transparent);
      top: -100px; left: -100px;
      animation: orbFloat1 15s ease-in-out infinite;
    }

    .orb-2 {
      width: 350px; height: 350px;
      background: radial-gradient(circle, rgba(0,229,255,0.2), transparent);
      bottom: -100px; right: -100px;
      animation: orbFloat2 18s ease-in-out infinite;
    }

    .orb-3 {
      width: 300px; height: 300px;
      background: radial-gradient(circle, rgba(180,74,255,0.2), transparent);
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      animation: orbFloat3 20s ease-in-out infinite;
    }

    @keyframes orbFloat1 {
      0%, 100% { transform: translate(0, 0) scale(1); }
      33% { transform: translate(80px, 60px) scale(1.1); }
      66% { transform: translate(-40px, 100px) scale(0.9); }
    }

    @keyframes orbFloat2 {
      0%, 100% { transform: translate(0, 0) scale(1); }
      33% { transform: translate(-70px, -50px) scale(1.15); }
      66% { transform: translate(50px, -80px) scale(0.85); }
    }

    @keyframes orbFloat3 {
      0%, 100% { transform: translate(-50%, -50%) scale(1); }
      50% { transform: translate(-30%, -70%) scale(1.2); }
    }

    /* Header / Title area */
    .hero-header {
      position: relative;
      z-index: 10;
      text-align: center;
      margin-bottom: 50px;
      opacity: 0;
      animation: headerEntrance 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      animation-delay: 0.3s;
    }

    @keyframes headerEntrance {
      0% { opacity: 0; transform: translateY(-40px) scale(0.95); filter: blur(10px); }
      100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
    }

    .hero-title {
      font-family: 'Orbitron', sans-serif;
      font-size: clamp(1.8rem, 4vw, 3.5rem);
      font-weight: 800;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      background: linear-gradient(135deg, #fff 0%, #e0e0e0 50%, #FFD700 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 12px;
      position: relative;
      line-height: 1.2;
    }

    .hero-title::after {
      content: '';
      position: absolute;
      bottom: -8px;
      left: 50%;
      transform: translateX(-50%);
      width: 80%;
      height: 2px;
      background: linear-gradient(90deg, transparent, var(--gold), transparent);
      animation: lineGlow 3s ease-in-out infinite;
    }

    @keyframes lineGlow {
      0%, 100% { opacity: 0.3; width: 80%; }
      50% { opacity: 1; width: 100%; }
    }

    .hero-subtitle {
      font-family: 'Rajdhani', sans-serif;
      font-size: clamp(1rem, 2vw, 1.5rem);
      font-weight: 400;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: rgba(255, 255, 255, 0.5);
    }

    /* Cards scene */
    .cards-scene {
      position: relative;
      z-index: 10;
      width: 100%;
      max-width: 1300px;
      height: 420px;
      perspective: 1500px;
      transform-style: preserve-3d;
      margin: 0 auto;
    }

    .cards-arc {
      position: relative;
      width: 100%;
      height: 100%;
      transform-style: preserve-3d;
      transition: transform 0.1s ease-out;
    }

    /* Card styles */
    .report-card {
      position: absolute;
      width: 200px;
      height: 300px;
      transform-style: preserve-3d;
      cursor: pointer;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease;
      animation: cardEntrance 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      opacity: 0;
    }

    @keyframes cardEntrance {
      0% { opacity: 0; transform: translateY(80px) rotateX(20deg) scale(0.8); }
      100% { opacity: 1; transform: translateY(0) rotateX(0) scale(1); }
    }

    .report-card:nth-child(1) { animation-delay: 0.5s; }
    .report-card:nth-child(2) { animation-delay: 0.7s; }
    .report-card:nth-child(3) { animation-delay: 0.9s; }
    .report-card:nth-child(4) { animation-delay: 1.1s; }
    .report-card:nth-child(5) { animation-delay: 1.3s; }

    .card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      border-radius: 20px;
      transform-style: preserve-3d;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Card background with glassmorphism */
    .card-face {
      position: absolute;
      inset: 0;
      border-radius: 20px;
      background: linear-gradient(145deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.02) 100%);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(255,255,255,0.1);
      overflow: hidden;
      transform-style: preserve-3d;
    }

    /* Metallic edge */
    .card-face::before {
      content: '';
      position: absolute;
      inset: 0;
      border-radius: 20px;
      padding: 1.5px;
      background: linear-gradient(145deg, rgba(255,255,255,0.3), rgba(255,255,255,0.05), rgba(255,255,255,0.2));
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      pointer-events: none;
    }

    /* Inner glow */
    .card-face::after {
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: radial-gradient(circle at 50% 50%, var(--accent-glow) 0%, transparent 60%);
      opacity: 0.15;
      pointer-events: none;
      transition: opacity 0.4s ease;
    }

    .report-card:hover .card-face::after {
      opacity: 0.3;
    }

    /* Shine sweep */
    .shine-layer {
      position: absolute;
      inset: 0;
      border-radius: 20px;
      overflow: hidden;
      pointer-events: none;
      z-index: 5;
    }

    .shine-layer::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 60%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.12), transparent);
      transform: skewX(-20deg);
      animation: shineSweep 4s ease-in-out infinite;
    }

    @keyframes shineSweep {
      0%, 100% { left: -100%; }
      50% { left: 150%; }
    }

    /* Card content */
    .card-content {
      position: relative;
      z-index: 2;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px 20px;
      text-align: center;
    }

    .card-symbol {
      font-family: 'Orbitron', sans-serif;
      font-size: 0.7rem;
      font-weight: 500;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.4);
      margin-bottom: 8px;
    }

    .card-title {
      font-family: 'Orbitron', sans-serif;
      font-size: 2.8rem;
      font-weight: 900;
      letter-spacing: 0.05em;
      color: var(--accent);
      margin-bottom: 6px;
      text-shadow: 0 0 30px var(--accent-glow), 0 0 60px var(--accent-glow);
      line-height: 1;
      transition: text-shadow 0.4s ease;
    }

    .report-card:hover .card-title {
      text-shadow: 0 0 40px var(--accent-glow), 0 0 80px var(--accent-glow), 0 0 120px var(--accent-glow);
    }

    .card-divider {
      width: 50%;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--accent), transparent);
      margin: 14px 0;
      opacity: 0.5;
    }

    .card-label {
      font-family: 'Rajdhani', sans-serif;
      font-size: 0.85rem;
      font-weight: 400;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.45);
      margin-bottom: 10px;
    }

    .card-value {
      font-family: 'Orbitron', sans-serif;
      font-size: 3.5rem;
      font-weight: 900;
      color: #fff;
      line-height: 1;
      text-shadow: 0 0 20px rgba(255,255,255,0.3);
      position: relative;
    }

    .card-value::after {
      content: '';
      position: absolute;
      bottom: -4px;
      left: 50%;
      transform: translateX(-50%);
      width: 60%;
      height: 2px;
      background: var(--accent);
      border-radius: 2px;
      box-shadow: 0 0 10px var(--accent-glow);
      opacity: 0.6;
    }

    /* Card corner decorations */
    .card-corner {
      position: absolute;
      width: 20px;
      height: 20px;
      z-index: 3;
    }

    .card-corner-tl {
      top: 10px; left: 10px;
      border-top: 2px solid var(--accent);
      border-left: 2px solid var(--accent);
      border-radius: 4px 0 0 0;
      opacity: 0.5;
    }

    .card-corner-tr {
      top: 10px; right: 10px;
      border-top: 2px solid var(--accent);
      border-right: 2px solid var(--accent);
      border-radius: 0 4px 0 0;
      opacity: 0.5;
    }

    .card-corner-bl {
      bottom: 10px; left: 10px;
      border-bottom: 2px solid var(--accent);
      border-left: 2px solid var(--accent);
      border-radius: 0 0 0 4px;
      opacity: 0.5;
    }

    .card-corner-br {
      bottom: 10px; right: 10px;
      border-bottom: 2px solid var(--accent);
      border-right: 2px solid var(--accent);
      border-radius: 0 0 4px 0;
      opacity: 0.5;
    }

    /* Card floating animation */
    @keyframes cardFloat1 {
      0%, 100% { transform: translateY(0px) rotateY(0deg); }
      50% { transform: translateY(-15px) rotateY(2deg); }
    }

    @keyframes cardFloat2 {
      0%, 100% { transform: translateY(0px) rotateY(0deg); }
      50% { transform: translateY(-20px) rotateY(-2deg); }
    }

    @keyframes cardFloat3 {
      0%, 100% { transform: translateY(0px) rotateY(0deg); }
      50% { transform: translateY(-12px) rotateY(1deg); }
    }

    @keyframes cardFloat4 {
      0%, 100% { transform: translateY(0px) rotateY(0deg); }
      50% { transform: translateY(-18px) rotateY(-1deg); }
    }

    @keyframes cardFloat5 {
      0%, 100% { transform: translateY(0px) rotateY(0deg); }
      50% { transform: translateY(-10px) rotateY(1.5deg); }
    }

    /* Card neon border animation */
    .neon-border {
      position: absolute;
      inset: -2px;
      border-radius: 22px;
      z-index: 0;
      overflow: hidden;
    }

    .neon-border::before {
      content: '';
      position: absolute;
      inset: 0;
      border-radius: 22px;
      padding: 2px;
      background: conic-gradient(from 0deg, transparent, var(--accent), transparent, var(--accent), transparent);
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      animation: neonRotate 6s linear infinite;
      opacity: 0.5;
      transition: opacity 0.4s ease;
    }

    .report-card:hover .neon-border::before {
      opacity: 1;
    }

    @keyframes neonRotate {
      0% { filter: hue-rotate(0deg); }
      100% { filter: hue-rotate(360deg); }
    }

    /* Card glow behind */
    .card-glow {
      position: absolute;
      top: 50%;
      left: 50%;
      width: 120%;
      height: 120%;
      transform: translate(-50%, -50%);
      background: radial-gradient(ellipse, var(--accent-glow) 0%, transparent 70%);
      opacity: 0;
      transition: opacity 0.4s ease;
      pointer-events: none;
      z-index: -1;
      filter: blur(30px);
    }

    .report-card:hover .card-glow {
      opacity: 0.25;
    }

    /* Reflection under cards */
    .card-reflection {
      position: absolute;
      bottom: -40px;
      left: 50%;
      transform: translateX(-50%) scaleY(-0.3);
      width: 80%;
      height: 60px;
      background: linear-gradient(to bottom, var(--accent-glow), transparent);
      opacity: 0;
      filter: blur(10px);
      transition: opacity 0.4s ease;
      pointer-events: none;
    }

    .report-card:hover .card-reflection {
      opacity: 0.15;
    }

    /* Hover lift effect */
    .report-card:hover {
      filter: brightness(1.15);
    }

    .report-card:hover .card-inner {
      transform: translateY(-20px) scale(1.05);
    }

    /* Card specific floating delays */
    .report-card:nth-child(1) { --float-anim: cardFloat1; }
    .report-card:nth-child(2) { --float-anim: cardFloat2; }
    .report-card:nth-child(3) { --float-anim: cardFloat3; }
    .report-card:nth-child(4) { --float-anim: cardFloat4; }
    .report-card:nth-child(5) { --float-anim: cardFloat5; }

    /* Ambient light lines */
    .ambient-line {
      position: absolute;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
      z-index: 1;
    }

    .ambient-line:nth-child(1) { top: 20%; width: 100%; }
    .ambient-line:nth-child(2) { top: 40%; width: 80%; left: 10%; }
    .ambient-line:nth-child(3) { top: 60%; width: 60%; left: 20%; }
    .ambient-line:nth-child(4) { top: 80%; width: 100%; }

    /* Bottom info */
    .bottom-bar {
      position: absolute;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 20;
      display: flex;
      align-items: center;
      gap: 20px;
      opacity: 0;
      animation: headerEntrance 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      animation-delay: 1.8s;
    }

    .bottom-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: rgba(255,255,255,0.2);
      transition: background 0.3s;
      cursor: pointer;
    }

    .bottom-dot.active {
      background: var(--gold);
      box-shadow: 0 0 10px var(--gold-glow);
    }

    /* Status indicator */
    .live-indicator {
      position: absolute;
      top: 80px; /* adjusted to clear navbar */
      right: 40px;
      z-index: 20;
      display: flex;
      align-items: center;
      gap: 10px;
      opacity: 0;
      animation: headerEntrance 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      animation-delay: 1.5s;
    }

    .live-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #00E676;
      animation: livePulse 2s ease-in-out infinite;
      box-shadow: 0 0 10px rgba(0, 230, 118, 0.5);
    }

    @keyframes livePulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.5; transform: scale(0.8); }
    }

    .live-text {
      font-family: 'Orbitron', sans-serif;
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.2em;
      color: #00E676;
    }

    /* Top left logo area */
    .logo-area {
      position: absolute;
      top: 80px; /* adjusted to clear navbar */
      left: 40px;
      z-index: 20;
      display: flex;
      align-items: center;
      gap: 12px;
      opacity: 0;
      animation: headerEntrance 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      animation-delay: 1.5s;
    }

    .logo-icon {
      width: 36px;
      height: 36px;
      border-radius: 10px;
      background: linear-gradient(135deg, var(--gold), #FF8C00);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Orbitron', sans-serif;
      font-weight: 900;
      font-size: 0.8rem;
      color: #000;
      box-shadow: 0 0 20px var(--gold-glow);
    }

    .logo-text {
      font-family: 'Orbitron', sans-serif;
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.15em;
      color: rgba(255,255,255,0.7);
    }

    /* Responsive */
    @media (max-width: 1200px) {
      .cards-scene {
        height: 380px;
      }
      .report-card {
        width: 170px;
        height: 260px;
      }
      .card-title {
        font-size: 2.2rem;
      }
      .card-value {
        font-size: 2.8rem;
      }
    }

    @media (max-width: 900px) {
      .cards-scene {
        height: 340px;
        max-width: 100%;
        padding: 0 10px;
      }
      .report-card {
        width: 150px;
        height: 230px;
      }
      .card-title {
        font-size: 1.8rem;
      }
      .card-value {
        font-size: 2.4rem;
      }
      .card-content {
        padding: 16px 12px;
      }
      .hero-title {
        font-size: 1.5rem;
      }
      .hero-subtitle {
        font-size: 0.9rem;
      }
    }

    @media (max-width: 600px) {
      .cards-scene {
        height: 300px;
      }
      .report-card {
        width: 130px;
        height: 200px;
      }
      .card-title {
        font-size: 1.5rem;
      }
      .card-value {
        font-size: 2rem;
      }
      .card-symbol {
        font-size: 0.6rem;
      }
      .card-label {
        font-size: 0.7rem;
      }
      .hero-header {
        margin-bottom: 30px;
      }
      .logo-area {
        left: 20px;
        top: 80px;
      }
      .live-indicator {
        right: 20px;
        top: 80px;
      }
    }
"""

content = re.sub(r'    /\* ===== HERO ===== \*/.*?    /\* ===== SECTION TITLE ===== \*/', new_hero_css + '\n    /* ===== SECTION TITLE ===== */', content, flags=re.DOTALL)

# 3. Replace Hero HTML
new_hero_html = """  <!-- ===== HERO ===== -->
  <section class="hero-section" id="home">
    <!-- Background layers -->
    <div class="bg-layer bg-gradient"></div>
    <div class="bg-layer bg-grid"></div>

    <!-- Floating orbs -->
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>

    <!-- Particles -->
    <div class="particles-container" id="particlesContainer"></div>

    <!-- Ambient lines -->
    <div class="ambient-line"></div>
    <div class="ambient-line"></div>
    <div class="ambient-line"></div>
    <div class="ambient-line"></div>

    <!-- Logo -->
    <div class="logo-area">
      <div class="logo-icon">RD</div>
      <div class="logo-text">REPORT DASHBOARD</div>
    </div>

    <!-- Live indicator -->
    <div class="live-indicator">
      <div class="live-dot"></div>
      <div class="live-text">LIVE</div>
    </div>

    <!-- Header -->
    <div class="hero-header">
      <h1 class="hero-title">LIVE REPORT DASHBOARD</h1>
      <p class="hero-subtitle">Dynamic 3D Performance Cards</p>
    </div>

    <!-- Cards scene -->
    <div class="cards-scene" id="cardsScene">
      <div class="cards-arc" id="cardsArc">

        <!-- Card 1: GM -->
        <div class="report-card" data-index="0" data-accent="var(--gold)" style="--accent: var(--gold); --accent-glow: var(--gold-glow);">
          <div class="card-glow"></div>
          <div class="card-reflection"></div>
          <div class="neon-border"></div>
          <div class="card-inner" id="cardInner0">
            <div class="card-face">
              <div class="card-corner card-corner-tl"></div>
              <div class="card-corner card-corner-tr"></div>
              <div class="card-corner card-corner-bl"></div>
              <div class="card-corner card-corner-br"></div>
              <div class="shine-layer"></div>
              <div class="card-content">
                <div class="card-symbol">● REPORT</div>
                <div class="card-title">GM</div>
                <div class="card-divider"></div>
                <div class="card-label">Report</div>
                <div class="card-value">75</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 2: LS1 -->
        <div class="report-card" data-index="1" data-accent="var(--cyan)" style="--accent: var(--cyan); --accent-glow: var(--cyan-glow);">
          <div class="card-glow"></div>
          <div class="card-reflection"></div>
          <div class="neon-border"></div>
          <div class="card-inner" id="cardInner1">
            <div class="card-face">
              <div class="card-corner card-corner-tl"></div>
              <div class="card-corner card-corner-tr"></div>
              <div class="card-corner card-corner-bl"></div>
              <div class="card-corner card-corner-br"></div>
              <div class="shine-layer"></div>
              <div class="card-content">
                <div class="card-symbol">● REPORT</div>
                <div class="card-title">LS1</div>
                <div class="card-divider"></div>
                <div class="card-label">Report</div>
                <div class="card-value">17</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 3: AK -->
        <div class="report-card" data-index="2" data-accent="var(--red)" style="--accent: var(--red); --accent-glow: var(--red-glow);">
          <div class="card-glow"></div>
          <div class="card-reflection"></div>
          <div class="neon-border"></div>
          <div class="card-inner" id="cardInner2">
            <div class="card-face">
              <div class="card-corner card-corner-tl"></div>
              <div class="card-corner card-corner-tr"></div>
              <div class="card-corner card-corner-bl"></div>
              <div class="card-corner card-corner-br"></div>
              <div class="shine-layer"></div>
              <div class="card-content">
                <div class="card-symbol">● REPORT</div>
                <div class="card-title">AK</div>
                <div class="card-divider"></div>
                <div class="card-label">Report</div>
                <div class="card-value">17</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 4: LS2 -->
        <div class="report-card" data-index="3" data-accent="var(--purple)" style="--accent: var(--purple); --accent-glow: var(--purple-glow);">
          <div class="card-glow"></div>
          <div class="card-reflection"></div>
          <div class="neon-border"></div>
          <div class="card-inner" id="cardInner3">
            <div class="card-face">
              <div class="card-corner card-corner-tl"></div>
              <div class="card-corner card-corner-tr"></div>
              <div class="card-corner card-corner-bl"></div>
              <div class="card-corner card-corner-br"></div>
              <div class="shine-layer"></div>
              <div class="card-content">
                <div class="card-symbol">● REPORT</div>
                <div class="card-title">LS2</div>
                <div class="card-divider"></div>
                <div class="card-label">Report</div>
                <div class="card-value">37</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 5: LS3 -->
        <div class="report-card" data-index="4" data-accent="var(--green)" style="--accent: var(--green); --accent-glow: var(--green-glow);">
          <div class="card-glow"></div>
          <div class="card-reflection"></div>
          <div class="neon-border"></div>
          <div class="card-inner" id="cardInner4">
            <div class="card-face">
              <div class="card-corner card-corner-tl"></div>
              <div class="card-corner card-corner-tr"></div>
              <div class="card-corner card-corner-bl"></div>
              <div class="card-corner card-corner-br"></div>
              <div class="shine-layer"></div>
              <div class="card-content">
                <div class="card-symbol">● REPORT</div>
                <div class="card-title">LS3</div>
                <div class="card-divider"></div>
                <div class="card-label">Report</div>
                <div class="card-value">33</div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- Bottom dots -->
    <div class="bottom-bar">
      <div class="bottom-dot active" data-slide="0"></div>
      <div class="bottom-dot" data-slide="1"></div>
      <div class="bottom-dot" data-slide="2"></div>
      <div class="bottom-dot" data-slide="3"></div>
      <div class="bottom-dot" data-slide="4"></div>
    </div>
  </section>"""

content = re.sub(r'  <!-- ===== HERO ===== -->.*?  <!-- ===== ABOUT ===== -->', new_hero_html + '\n\n  <!-- ===== ABOUT ===== -->', content, flags=re.DOTALL)


# 4. Replace Hero JS
new_hero_js = """    // ===== New Hero Script =====
    (function() {
      'use strict';

      const heroSection = document.getElementById('home');
      const cardsScene = document.getElementById('cardsScene');
      const cardsArc = document.getElementById('cardsArc');
      const cards = document.querySelectorAll('.report-card');
      const cardInners = document.querySelectorAll('.card-inner');
      const particlesContainer = document.getElementById('particlesContainer');
      const bottomDots = document.querySelectorAll('.bottom-dot');

      if(!cardsScene) return;

      // Position cards in arc layout
      function positionCards() {
        const sceneWidth = cardsScene.offsetWidth;
        const cardWidth = cards[0].offsetWidth;
        const totalWidth = cards.length * (cardWidth + 20);
        const startX = (sceneWidth - totalWidth) / 2;
        const centerY = cardsScene.offsetHeight / 2;
        
        cards.forEach((card, index) => {
          const angle = ((index - (cards.length - 1) / 2) * 18) * (Math.PI / 180);
          const x = startX + index * (cardWidth + 20) + cardWidth / 2;
          const y = centerY - Math.cos(angle) * 30;

          card.style.left = (x - cardWidth / 2) + 'px';
          card.style.top = y + 'px';
          card.style.transform = `translateY(0) rotateY(${angle * 5}deg) rotateX(${Math.sin(angle) * 3}deg)`;

          // Set floating animation
          const floatDuration = 4 + index * 0.5;
          const floatDelay = index * 0.3;
          card.style.animation = `cardEntrance 1s cubic-bezier(0.16, 1, 0.3, 1) forwards, cardFloat${(index % 5) + 1} ${floatDuration}s ease-in-out ${floatDelay}s infinite`;
        });
      }

      // Create particles
      function createParticles() {
        const colors = ['rgba(255,215,0,0.6)', 'rgba(0,229,255,0.5)', 'rgba(255,59,92,0.5)', 'rgba(180,74,255,0.5)', 'rgba(0,230,118,0.5)', 'rgba(255,255,255,0.3)'];
        for (let i = 0; i < 50; i++) {
          const particle = document.createElement('div');
          particle.classList.add('particle');
          const size = Math.random() * 4 + 1;
          const color = colors[Math.floor(Math.random() * colors.length)];
          particle.style.width = size + 'px';
          particle.style.height = size + 'px';
          particle.style.background = color;
          particle.style.boxShadow = `0 0 ${size * 2}px ${color}`;
          particle.style.left = Math.random() * 100 + '%';
          particle.style.animationDuration = (Math.random() * 15 + 10) + 's';
          particle.style.animationDelay = (Math.random() * 10) + 's';
          particlesContainer.appendChild(particle);
        }
      }

      // Mouse parallax effect
      let mouseX = 0, mouseY = 0;
      let targetRotX = 0, targetRotY = 0;
      let currentRotX = 0, currentRotY = 0;

      document.addEventListener('mousemove', function(e) {
        if(!cardsScene.matches(':hover')) return; // only rotate when interacting near scene
        mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
        mouseY = (e.clientY / window.innerHeight - 0.5) * 2;

        targetRotY = mouseX * 8;
        targetRotX = -mouseY * 5;

        // Individual card tilt
        cards.forEach((card, index) => {
          const rect = card.getBoundingClientRect();
          const cardCenterX = rect.left + rect.width / 2;
          const cardCenterY = rect.top + rect.height / 2;
          const deltaX = (e.clientX - cardCenterX) / rect.width;
          const deltaY = (e.clientY - cardCenterY) / rect.height;

          const tiltX = deltaY * -8;
          const tiltY = deltaX * 8;

          cardInners[index].style.transform = `rotateX(${tiltX}deg) rotateY(${tiltY}deg)`;
        });
      });

      // Smooth animation loop for scene rotation
      function animateScene() {
        currentRotX += (targetRotX - currentRotX) * 0.05;
        currentRotY += (targetRotY - currentRotY) * 0.05;

        cardsArc.style.transform = `rotateX(${currentRotX}deg) rotateY(${currentRotY}deg)`;

        requestAnimationFrame(animateScene);
      }

      // Reset card tilt on mouse leave
      document.addEventListener('mouseleave', function() {
        targetRotX = 0;
        targetRotY = 0;
        cardInners.forEach(function(inner) {
          inner.style.transform = '';
        });
      });

      // Bottom dots interaction
      bottomDots.forEach(function(dot) {
        dot.addEventListener('click', function() {
          bottomDots.forEach(function(d) { d.classList.remove('active'); });
          dot.classList.add('active');
        });
      });

      // Card hover sound-like visual feedback
      cards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
          const index = parseInt(this.getAttribute('data-index'));
          bottomDots.forEach(function(d) { d.classList.remove('active'); });
          bottomDots[index].classList.add('active');
        });
      });

      // Initialize
      function init() {
        createParticles();
        positionCards();
        animateScene();
      }

      // Handle resize
      let resizeTimeout;
      window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(positionCards, 150);
      });

      // Start
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
      } else {
        init();
      }
    })();
"""

content = re.sub(r'    // ===== Reports Data =====.*?    // ===== History Table \(random sample\) =====', new_hero_js + '\n    // ===== History Table (random sample) =====', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
