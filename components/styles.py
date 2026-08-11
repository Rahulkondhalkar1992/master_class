"""Classic study-material document viewer styles."""

import streamlit as st


def inject_styles() -> None:
    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --bg: #070b14;
  --paper: rgba(11, 17, 32, 0.88);
  --azure: #0078D4;
  --azure-bright: #00A4EF;
  --cyan: #22D3EE;
  --purple: #8B5CF6;
  --text: #F8FAFC;
  --muted: #94A3B8;
  --border: rgba(148, 163, 184, 0.16);
  --gold: #E8D5A3;
}

html, body, [class*="css"] {
  font-family: 'Outfit', sans-serif !important;
}

.stApp {
  background:
    radial-gradient(ellipse 70% 40% at 15% 0%, rgba(0, 120, 212, 0.14), transparent 55%),
    radial-gradient(ellipse 50% 30% at 90% 8%, rgba(139, 92, 246, 0.08), transparent 50%),
    var(--bg) !important;
  color: var(--text);
}

#MainMenu, footer, header, .stDeployButton { visibility: hidden; display: none !important; }

/* Hide Streamlit sidebar completely */
section[data-testid="stSidebar"],
div[data-testid="stSidebar"],
button[kind="header"],
[data-testid="collapsedControl"] {
  display: none !important;
  width: 0 !important;
  min-width: 0 !important;
}

.block-container {
  max-width: 920px !important;
  padding-top: 1.25rem !important;
  padding-bottom: 3rem !important;
}

.gradient-text {
  background: linear-gradient(120deg, #F8FAFC 8%, #00A4EF 42%, #22D3EE 68%, #E8D5A3 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* —— Hero —— */
.doc-hero {
  position: relative;
  overflow: hidden;
  border: 1px solid var(--border);
  border-radius: 22px;
  padding: 2rem 1.5rem 1.6rem;
  margin-bottom: 1rem;
  background: linear-gradient(160deg, rgba(11,17,32,0.95), rgba(5,8,22,0.98));
  box-shadow: 0 24px 60px rgba(0,0,0,0.35);
}

.doc-hero-glow {
  position: absolute;
  width: 280px; height: 280px;
  right: -40px; top: -80px;
  background: radial-gradient(circle, rgba(0,120,212,0.35), transparent 70%);
  pointer-events: none;
  animation: soft-glow 8s ease-in-out infinite;
}

.doc-hero-grid {
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(0,164,239,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,164,239,0.04) 1px, transparent 1px);
  background-size: 36px 36px;
  mask-image: radial-gradient(ellipse at center, black 25%, transparent 78%);
  pointer-events: none;
}

.doc-hero-inner { position: relative; z-index: 2; }

.doc-kicker {
  font-size: 0.72rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--gold);
  font-weight: 600;
  margin-bottom: 0.65rem;
}

.doc-hero-title {
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 700;
  line-height: 1.12;
  margin: 0 0 0.75rem 0;
  letter-spacing: -0.02em;
}

.doc-hero-lead {
  color: var(--muted);
  font-size: 1.02rem;
  line-height: 1.65;
  max-width: 640px;
  margin: 0 0 0.9rem 0;
}

.hero-badges {
  display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.2rem 0 0.75rem;
}
.hero-badge {
  display: inline-flex; align-items: center;
  padding: 0.32rem 0.65rem; border-radius: 999px;
  font-size: 0.72rem; font-weight: 650;
  color: #E0F2FE;
  background: linear-gradient(135deg, rgba(0,120,212,0.28), rgba(34,211,238,0.12));
  border: 1px solid rgba(0,164,239,0.35);
}

.hero-tech-strip {
  font-size: 0.82rem; font-weight: 600; letter-spacing: 0.04em; color: var(--cyan);
  margin-bottom: 1rem;
}

.doc-hero-visual {
  display: flex; flex-wrap: wrap; align-items: center; gap: 1rem;
  margin-top: 0.5rem;
}

.doc-hero-core {
  width: 120px; height: 120px; border-radius: 50%;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  text-align: center;
  background: radial-gradient(circle at 30% 30%, rgba(0,164,239,0.35), rgba(11,17,32,0.95));
  border: 1px solid rgba(0,164,239,0.45);
  box-shadow: 0 0 36px rgba(0,120,212,0.28);
}
.doc-hero-core .core-icon { font-size: 1.5rem; }
.doc-hero-core .core-title { font-size: 0.68rem; font-weight: 700; letter-spacing: 0.12em; }
.doc-hero-core .core-sub { font-size: 0.58rem; color: var(--muted); }

.doc-hero-pills { display: flex; flex-wrap: wrap; gap: 0.4rem; max-width: 360px; }
.doc-hero-pills span {
  padding: 0.35rem 0.65rem; border-radius: 999px; font-size: 0.72rem; font-weight: 600;
  border: 1px solid rgba(0,164,239,0.25); background: rgba(15,23,42,0.85);
}

@keyframes soft-glow {
  0%, 100% { opacity: 0.7; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.05); }
}

/* —— Sticky TOC —— */
.doc-toc {
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 0.75rem 0.85rem;
  margin: 0 0 1.25rem;
  background: rgba(5, 8, 22, 0.92);
  backdrop-filter: blur(12px);
  box-shadow: 0 10px 28px rgba(0,0,0,0.25);
}
.sticky-toc { position: sticky; top: 0.35rem; z-index: 100; }
.toc-title {
  font-size: 0.68rem; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--gold); font-weight: 650; margin-bottom: 0.45rem;
}
.toc-row { display: flex; flex-wrap: wrap; gap: 0.35rem; }
.toc-chip {
  display: inline-flex; align-items: center; gap: 0.35rem;
  text-decoration: none !important; color: var(--text) !important;
  font-size: 0.75rem; font-weight: 600;
  padding: 0.4rem 0.55rem; border-radius: 999px;
  border: 1px solid rgba(148,163,184,0.2);
  background: rgba(15,23,42,0.9);
  transition: border-color 0.2s ease, background 0.2s ease;
}
.toc-chip:hover {
  border-color: rgba(0,164,239,0.45);
  background: rgba(0,120,212,0.15);
}
.toc-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem; color: var(--cyan);
}

/* —— Document paper —— */
.doc-paper {
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 0.25rem 0.15rem 1rem;
  background: var(--paper);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.03);
}

.doc-chapter { margin: 0.5rem 0 0.85rem; scroll-margin-top: 4.5rem; }
.chapter-meta {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 0.25rem;
}
.chapter-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem; letter-spacing: 0.08em; color: var(--cyan); font-weight: 600;
}
.chapter-top {
  font-size: 0.75rem; color: var(--muted) !important; text-decoration: none !important;
}
.chapter-top:hover { color: var(--cyan) !important; }
.chapter-title {
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-size: clamp(1.55rem, 3vw, 2rem);
  font-weight: 700; margin: 0.15rem 0 0.35rem; letter-spacing: -0.01em;
}
.chapter-sub { color: var(--muted); font-size: 0.95rem; margin: 0; line-height: 1.55; }

.doc-rule {
  border: none; border-top: 1px solid var(--border);
  margin: 1.4rem 0;
}

.plan-intro {
  color: var(--muted); font-size: 0.95rem; line-height: 1.6;
  padding: 0.85rem 1rem; border-left: 3px solid var(--azure);
  background: rgba(0,120,212,0.08); border-radius: 0 12px 12px 0;
  margin-bottom: 0.85rem;
}

.doc-flow {
  display: flex; flex-wrap: wrap; gap: 0.4rem; align-items: center;
  margin: 0.5rem 0 0.75rem; color: var(--muted);
}
.doc-flow-node {
  padding: 0.35rem 0.65rem; border-radius: 999px; font-size: 0.78rem; font-weight: 600;
  color: var(--text); border: 1px solid rgba(0,164,239,0.3);
  background: rgba(15,23,42,0.85);
}

/* Cards */
.ala-card {
  background: rgba(15, 23, 42, 0.72);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 1.1rem 1rem;
  height: 100%;
  transition: border-color 0.2s ease, transform 0.2s ease;
  margin-bottom: 0.35rem;
}
.ala-card:hover {
  border-color: rgba(0,164,239,0.4);
  transform: translateY(-2px);
}
.ala-card .card-icon { font-size: 1.45rem; margin-bottom: 0.45rem; }
.ala-card .card-title { font-size: 1rem; font-weight: 650; margin-bottom: 0.3rem; }
.ala-card .card-body { font-size: 0.9rem; color: var(--muted); line-height: 1.5; margin: 0; }

.live-pill-row { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0.6rem 0 1rem; }
.live-pill {
  display: inline-flex; align-items: center; gap: 0.35rem;
  padding: 0.4rem 0.75rem; border-radius: 999px; font-size: 0.78rem; font-weight: 600;
  border: 1px solid rgba(34,197,94,0.35); background: rgba(34,197,94,0.1);
}
.live-dot {
  width: 7px; height: 7px; border-radius: 50%; background: #22c55e;
}

.section-divider { height: 1rem; }

/* Coming soon clubbed */
.wip-banner {
  display: flex; align-items: center; gap: 0.55rem;
  padding: 0.75rem 0.9rem; border-radius: 12px; margin-bottom: 0.85rem;
  border: 1px dashed rgba(139,92,246,0.45);
  background: rgba(139,92,246,0.1);
  color: #c4b5fd; font-size: 0.88rem; font-weight: 500;
}
.wip-pulse {
  width: 8px; height: 8px; border-radius: 50%; background: #a78bfa;
  box-shadow: 0 0 0 0 rgba(167,139,250,0.5);
  animation: pulse-ring 2.4s ease-out infinite;
}
@keyframes pulse-ring {
  0% { box-shadow: 0 0 0 0 rgba(167,139,250,0.45); }
  70% { box-shadow: 0 0 0 10px rgba(167,139,250,0); }
  100% { box-shadow: 0 0 0 0 rgba(167,139,250,0); }
}
.wip-card {
  border: 1px solid var(--border); border-radius: 14px;
  padding: 1rem 1.05rem; margin-bottom: 0.7rem;
  background: linear-gradient(145deg, rgba(15,23,42,0.9), rgba(11,17,32,0.75));
  transition: border-color 0.2s ease;
}
.wip-card:hover { border-color: rgba(139,92,246,0.4); }
.wip-card-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem; }
.wip-icon { font-size: 1.4rem; }
.wip-status {
  font-size: 0.68rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;
  padding: 0.25rem 0.55rem; border-radius: 999px;
  background: rgba(139,92,246,0.22); color: #c4b5fd;
}
.wip-title { font-weight: 700; font-size: 1.05rem; margin-bottom: 0.25rem; }
.wip-body { color: var(--muted); font-size: 0.9rem; margin: 0 0 0.55rem; line-height: 1.5; }
.cs-chip {
  display: inline-block; margin: 0.15rem 0.2rem 0 0;
  padding: 0.22rem 0.5rem; border-radius: 999px; border: 1px solid var(--border);
  font-size: 0.72rem; color: var(--muted);
}

.support-strip {
  display: flex; flex-wrap: wrap; gap: 1rem; align-items: center;
  padding: 1rem; border-radius: 14px; border: 1px solid var(--border);
  background: rgba(0,120,212,0.08); margin-bottom: 0.85rem;
}
.support-hero-num {
  font-size: clamp(2.2rem, 5vw, 3.2rem); font-weight: 800; line-height: 1;
  background: linear-gradient(120deg, #00A4EF, #22D3EE);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.support-sub { font-weight: 700; letter-spacing: 0.1em; font-size: 0.82rem; margin-bottom: 0.25rem; }
.support-strip-copy p { color: var(--muted); margin: 0; font-size: 0.9rem; line-height: 1.5; }

/* Same-window buttons */
.doc-btn {
  display: block; text-align: center; text-decoration: none !important;
  color: var(--text) !important; font-weight: 650; font-size: 0.92rem;
  padding: 0.7rem 1rem; border-radius: 12px; margin: 0.35rem 0 0.6rem;
  border: 1px solid rgba(0,164,239,0.35);
  background: rgba(15,23,42,0.75);
  transition: transform 0.15s ease, border-color 0.15s ease;
}
.doc-btn:hover {
  border-color: rgba(0,164,239,0.7);
  transform: translateY(-1px);
  color: #fff !important;
}
.doc-btn-primary {
  background: linear-gradient(135deg, #0078D4, #00A4EF) !important;
  border: none !important;
  box-shadow: 0 8px 22px rgba(0,120,212,0.28);
}

div[data-testid="stExpander"] {
  background: rgba(11, 17, 32, 0.65);
  border: 1px solid var(--border);
  border-radius: 12px !important;
  margin-bottom: 0.55rem;
}
div[data-testid="stExpander"] details summary p { font-weight: 600 !important; }

.stButton > button[kind="primary"] {
  background: linear-gradient(135deg, #0078D4, #00A4EF) !important;
  border: none !important; color: white !important; font-weight: 650 !important;
  border-radius: 12px !important;
}
.stButton > button[kind="secondary"] {
  background: rgba(15,23,42,0.6) !important;
  border: 1px solid rgba(0,164,239,0.35) !important;
  color: var(--text) !important; border-radius: 12px !important;
}
.stTextInput input, .stTextArea textarea, .stSelectbox > div > div {
  background: rgba(11,17,32,0.85) !important;
  border-color: var(--border) !important;
  color: var(--text) !important; border-radius: 10px !important;
}

.doc-footer {
  margin-top: 2rem; padding: 1.5rem 0 0.5rem;
  border-top: 1px solid var(--border);
  text-align: center; color: var(--muted); font-size: 0.88rem;
}
.doc-footer-brand { color: var(--text); font-weight: 700; margin-bottom: 0.3rem; }
.doc-footer-tag { margin: 0.4rem 0; }
.doc-footer-copy { margin-top: 0.55rem; }
.doc-footer a { color: var(--azure-bright); text-decoration: none; }

.doc-hero-glow-2 {
  left: -60px; top: auto; bottom: -100px; right: auto;
  background: radial-gradient(circle, rgba(34,211,238,0.18), transparent 70%);
}

.doc-mobile-eyebrow { display: none; }
.mobile-tech-rail { display: none; }
.mobile-hero-cta { display: none; }
.mobile-dock, .mobile-dock-spacer { display: none; }
.toc-head {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 0.45rem;
}
.toc-join {
  font-size: 0.75rem; font-weight: 700; color: var(--cyan) !important;
  text-decoration: none !important;
}

/* ========== MOBILE WOW ========== */
@media (max-width: 768px) {
  .stApp {
    background:
      radial-gradient(ellipse 90% 35% at 50% -5%, rgba(0,120,212,0.22), transparent 55%),
      radial-gradient(ellipse 70% 25% at 100% 20%, rgba(139,92,246,0.12), transparent 50%),
      #050816 !important;
  }

  .block-container {
    padding-left: 0.7rem !important;
    padding-right: 0.7rem !important;
    padding-top: 0.65rem !important;
    padding-bottom: 5.5rem !important;
    max-width: 100% !important;
  }

  .doc-kicker { display: none; }
  .doc-mobile-eyebrow {
    display: inline-block;
    font-size: 0.7rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--gold);
    font-weight: 650;
    margin-bottom: 0.45rem;
  }

  .doc-hero {
    padding: 1.15rem 1rem 1.1rem;
    border-radius: 20px;
    margin-bottom: 0.75rem;
    animation: mobile-fade-up 0.55s ease-out;
  }
  .doc-hero-title {
    font-size: clamp(1.65rem, 7.2vw, 2.05rem);
    line-height: 1.12;
    margin-bottom: 0.55rem;
  }
  .doc-hero-lead {
    font-size: 0.92rem;
    line-height: 1.55;
    margin-bottom: 0.7rem;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .doc-hero-glow { opacity: 0.55; animation: none; }
  .doc-hero-visual { margin-top: 0.35rem; }
  .doc-hero-core {
    width: 86px; height: 86px;
    box-shadow: 0 0 28px rgba(0,164,239,0.35);
  }
  .desktop-pills { display: none !important; }

  .hero-badges { gap: 0.35rem; margin-bottom: 0.65rem; }
  .hero-badge {
    font-size: 0.68rem;
    padding: 0.38rem 0.62rem;
    background: rgba(0,120,212,0.22);
  }

  .mobile-tech-rail {
    display: flex;
    gap: 0.4rem;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    margin: 0.15rem 0 0.85rem;
    padding-bottom: 0.15rem;
  }
  .mobile-tech-rail::-webkit-scrollbar { display: none; }
  .mobile-tech-rail span {
    flex: 0 0 auto;
    padding: 0.4rem 0.7rem;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 700;
    color: #E0F2FE;
    border: 1px solid rgba(0,164,239,0.35);
    background: rgba(15,23,42,0.9);
  }

  .mobile-hero-cta {
    display: grid;
    grid-template-columns: 1.2fr 1fr 0.85fr;
    gap: 0.4rem;
    margin-top: 0.85rem;
  }
  .mhc-btn {
    display: flex; align-items: center; justify-content: center;
    text-align: center; text-decoration: none !important;
    color: var(--text) !important;
    font-size: 0.72rem; font-weight: 700;
    min-height: 44px; padding: 0.55rem 0.35rem;
    border-radius: 12px;
    border: 1px solid rgba(148,163,184,0.25);
    background: rgba(15,23,42,0.92);
  }
  .mhc-primary {
    border-color: rgba(0,164,239,0.45);
    background: rgba(0,120,212,0.22);
  }
  .mhc-join {
    background: linear-gradient(135deg, #0078D4, #00A4EF);
    border: none;
    box-shadow: 0 8px 18px rgba(0,120,212,0.35);
  }

  /* Sticky horizontal chapter rail */
  .doc-toc {
    margin: 0 -0.7rem 0.9rem;
    border-radius: 0;
    border-left: none; border-right: none;
    padding: 0.65rem 0.7rem 0.7rem;
    background: rgba(5,8,22,0.96);
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
  }
  .sticky-toc {
    position: sticky;
    top: 0;
    z-index: 200;
  }
  .toc-row {
    display: flex;
    flex-wrap: nowrap;
    gap: 0.4rem;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scroll-snap-type: x mandatory;
    scrollbar-width: none;
    padding-bottom: 0.15rem;
  }
  .toc-row::-webkit-scrollbar { display: none; }
  .toc-chip {
    flex: 0 0 auto;
    scroll-snap-align: start;
    min-height: 40px;
    font-size: 0.72rem;
    padding: 0.45rem 0.7rem;
    border-radius: 999px;
    background: rgba(15,23,42,0.95);
  }
  .toc-join {
    min-height: 32px;
    display: inline-flex;
    align-items: center;
    padding: 0.25rem 0.55rem;
    border-radius: 999px;
    background: rgba(0,120,212,0.25);
  }

  .doc-paper {
    border-radius: 16px;
    padding: 0.1rem 0.05rem 1.25rem;
    border-color: rgba(148,163,184,0.12);
  }

  .doc-chapter { scroll-margin-top: 5.25rem; }
  .chapter-title {
    font-size: clamp(1.45rem, 6vw, 1.75rem);
  }
  .chapter-sub { font-size: 0.9rem; }
  .chapter-num { font-size: 0.68rem; }

  .plan-intro {
    font-size: 0.9rem;
    padding: 0.8rem 0.85rem;
  }

  .ala-card {
    padding: 1rem 0.95rem;
    margin-bottom: 0.55rem;
    border-radius: 16px;
  }
  .ala-card:hover { transform: none; }
  .ala-card .card-title { font-size: 1.02rem; }
  .ala-card .card-body { font-size: 0.92rem; line-height: 1.55; }

  div[data-testid="column"] {
    width: 100% !important;
    flex: 1 1 100% !important;
    min-width: 100% !important;
  }

  div[data-testid="stExpander"] {
    border-radius: 14px !important;
    margin-bottom: 0.6rem;
  }
  div[data-testid="stExpander"] details summary {
    min-height: 48px;
    padding-top: 0.35rem !important;
    padding-bottom: 0.35rem !important;
  }

  .stButton > button, .doc-btn {
    width: 100% !important;
    min-height: 48px !important;
    font-size: 0.95rem !important;
    border-radius: 14px !important;
  }
  .doc-btn { margin: 0.45rem 0 0.7rem; padding: 0.85rem 1rem; }

  .wip-banner {
    font-size: 0.84rem;
    line-height: 1.4;
    padding: 0.8rem 0.85rem;
  }
  .wip-pulse { animation: none; }
  .wip-card {
    border-radius: 16px;
    padding: 1rem 0.95rem;
  }
  .wip-title { font-size: 1.05rem; }

  .support-strip {
    flex-direction: column;
    align-items: flex-start;
    border-radius: 16px;
  }
  .support-hero-num { font-size: 2.6rem; }

  .live-pill { min-height: 36px; }

  /* Fixed bottom dock */
  .mobile-dock {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    position: fixed;
    left: 0; right: 0; bottom: 0;
    z-index: 300;
    gap: 0.15rem;
    padding: 0.45rem 0.45rem calc(0.45rem + env(safe-area-inset-bottom));
    border-top: 1px solid rgba(0,164,239,0.25);
    background: rgba(5, 8, 22, 0.96);
    backdrop-filter: blur(14px);
    box-shadow: 0 -12px 36px rgba(0,0,0,0.45);
  }
  .mobile-dock-spacer { display: block; height: 4.5rem; }
  .dock-item {
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: 0.12rem; text-decoration: none !important; color: var(--muted) !important;
    font-size: 0.62rem; font-weight: 650; letter-spacing: 0.02em;
    min-height: 52px; border-radius: 12px;
    padding: 0.3rem 0.2rem;
  }
  .dock-ico { font-size: 1.05rem; line-height: 1; }
  .dock-join {
    color: #fff !important;
    background: linear-gradient(135deg, #0078D4, #00A4EF);
    box-shadow: 0 6px 16px rgba(0,120,212,0.35);
  }
  .dock-wa {
    color: #86efac !important;
    background: rgba(34,197,94,0.12);
  }

  .doc-footer {
    margin-bottom: 0.5rem;
    font-size: 0.82rem;
  }

  @keyframes mobile-fade-up {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
  }
}

@media (min-width: 769px) {
  .mobile-dock, .mobile-dock-spacer, .mobile-hero-cta, .mobile-tech-rail, .doc-mobile-eyebrow {
    display: none !important;
  }
}
</style>
        """,
        unsafe_allow_html=True,
    )
