"""Global CSS design system for Azure Learnings Academy."""

import streamlit as st


def inject_styles() -> None:
    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --bg: #050816;
  --bg-secondary: #0B1120;
  --bg-card: rgba(15, 23, 42, 0.72);
  --azure: #0078D4;
  --azure-bright: #00A4EF;
  --cyan: #22D3EE;
  --purple: #8B5CF6;
  --text: #F8FAFC;
  --muted: #94A3B8;
  --border: rgba(148, 163, 184, 0.16);
  --glow: rgba(0, 120, 212, 0.35);
  --radius: 16px;
  --radius-sm: 10px;
}

html, body, [class*="css"] {
  font-family: 'Outfit', sans-serif !important;
}

.stApp {
  background:
    radial-gradient(ellipse 80% 50% at 20% -10%, rgba(0, 120, 212, 0.18), transparent 50%),
    radial-gradient(ellipse 60% 40% at 90% 10%, rgba(139, 92, 246, 0.12), transparent 45%),
    radial-gradient(ellipse 50% 30% at 50% 100%, rgba(34, 211, 238, 0.08), transparent 40%),
    var(--bg) !important;
  color: var(--text);
}

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

div[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #070b18 0%, #0B1120 100%) !important;
  border-right: 1px solid var(--border);
  min-width: 260px !important;
  max-width: 280px !important;
}

div[data-testid="stSidebar"] > div:first-child {
  padding-top: 1rem;
}

.sidebar-brand {
  padding: 0.4rem 0.6rem 1rem;
  margin-bottom: 0.5rem;
  border-bottom: 1px solid var(--border);
}

.sidebar-brand .brand-top {
  font-size: 0.72rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--cyan);
  font-weight: 600;
}

.sidebar-brand .brand-name {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text);
  line-height: 1.25;
  margin-top: 0.2rem;
}

.sidebar-brand .brand-sub {
  font-size: 0.78rem;
  color: var(--muted);
  margin-top: 0.15rem;
}

.nav-section-label {
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  color: var(--muted);
  font-weight: 600;
  margin: 0.85rem 0.35rem 0.35rem;
  text-transform: uppercase;
}

div[data-testid="stSidebar"] .stButton > button {
  width: 100%;
  justify-content: flex-start;
  text-align: left;
  background: transparent !important;
  border: 1px solid transparent !important;
  color: var(--muted) !important;
  border-radius: 10px !important;
  padding: 0.55rem 0.75rem !important;
  font-weight: 500 !important;
  font-size: 0.92rem !important;
  transition: all 0.2s ease;
  box-shadow: none !important;
}

div[data-testid="stSidebar"] .stButton > button:hover {
  background: rgba(0, 120, 212, 0.12) !important;
  color: var(--text) !important;
  border-color: rgba(0, 164, 239, 0.25) !important;
}

div[data-testid="stSidebar"] .stButton > button[kind="primary"] {
  background: linear-gradient(135deg, rgba(0, 120, 212, 0.28), rgba(34, 211, 238, 0.12)) !important;
  color: var(--text) !important;
  border: 1px solid rgba(0, 164, 239, 0.35) !important;
  box-shadow: 0 0 18px rgba(0, 120, 212, 0.15) !important;
}

.badge-soon {
  display: inline-block;
  font-size: 0.62rem;
  padding: 0.1rem 0.4rem;
  border-radius: 999px;
  background: rgba(139, 92, 246, 0.25);
  color: #c4b5fd;
  margin-left: 0.35rem;
  vertical-align: middle;
}

.page-header {
  margin-bottom: 1.5rem;
}

.page-header .page-icon {
  font-size: 1.8rem;
  margin-bottom: 0.35rem;
}

.page-header h1 {
  font-size: 2rem !important;
  font-weight: 700 !important;
  margin: 0 0 0.4rem 0 !important;
  letter-spacing: -0.02em;
}

.page-header p {
  color: var(--muted);
  font-size: 1.02rem;
  margin: 0;
  max-width: 720px;
}

.gradient-text {
  background: linear-gradient(120deg, #F8FAFC 10%, #00A4EF 45%, #22D3EE 70%, #8B5CF6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-wrap {
  position: relative;
  border: 1px solid var(--border);
  border-radius: 24px;
  overflow: hidden;
  background:
    linear-gradient(145deg, rgba(11, 17, 32, 0.92), rgba(5, 8, 22, 0.95));
  padding: 2.2rem 1.8rem 2rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
}

.hero-wrap::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(0, 164, 239, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 164, 239, 0.05) 1px, transparent 1px);
  background-size: 42px 42px;
  mask-image: radial-gradient(ellipse at center, black 20%, transparent 75%);
  pointer-events: none;
}

.hero-wrap::after {
  content: "";
  position: absolute;
  width: 280px;
  height: 280px;
  right: -60px;
  top: -80px;
  background: radial-gradient(circle, rgba(0, 120, 212, 0.35), transparent 70%);
  pointer-events: none;
}

.hero-content {
  position: relative;
  z-index: 2;
}

.hero-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.78rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--cyan);
  font-weight: 600;
  margin-bottom: 0.85rem;
}

.hero-title {
  font-size: clamp(1.85rem, 4vw, 2.75rem);
  font-weight: 800;
  line-height: 1.15;
  margin: 0 0 0.9rem 0;
  letter-spacing: -0.03em;
}

.hero-subtitle {
  color: var(--muted);
  font-size: 1.05rem;
  line-height: 1.65;
  max-width: 640px;
  margin: 0 0 1.4rem 0;
}

.hero-network {
  position: relative;
  min-height: 280px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 0.5rem;
}

.hero-core {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  background: radial-gradient(circle at 30% 30%, rgba(0, 164, 239, 0.35), rgba(11, 17, 32, 0.95));
  border: 1px solid rgba(0, 164, 239, 0.45);
  box-shadow: 0 0 40px rgba(0, 120, 212, 0.35), inset 0 0 30px rgba(34, 211, 238, 0.1);
  animation: pulse-glow 4s ease-in-out infinite;
  z-index: 2;
}

.hero-core .core-icon { font-size: 1.8rem; }
.hero-core .core-title {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  margin-top: 0.25rem;
}
.hero-core .core-sub {
  font-size: 0.62rem;
  color: var(--muted);
  letter-spacing: 0.04em;
}

.tech-orbit {
  position: absolute;
  inset: 0;
}

.tech-pill {
  position: absolute;
  padding: 0.4rem 0.75rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  background: rgba(15, 23, 42, 0.85);
  border: 1px solid rgba(0, 164, 239, 0.28);
  color: var(--text);
  backdrop-filter: blur(8px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
  animation: float-y 6s ease-in-out infinite;
}

.tech-pill:nth-child(1) { top: 8%; left: 12%; animation-delay: 0s; }
.tech-pill:nth-child(2) { top: 18%; right: 10%; animation-delay: 0.8s; }
.tech-pill:nth-child(3) { top: 48%; left: 4%; animation-delay: 1.4s; }
.tech-pill:nth-child(4) { top: 52%; right: 6%; animation-delay: 0.4s; }
.tech-pill:nth-child(5) { bottom: 14%; left: 18%; animation-delay: 1.1s; }
.tech-pill:nth-child(6) { bottom: 10%; right: 16%; animation-delay: 1.8s; }
.tech-pill:nth-child(7) { top: 4%; left: 48%; animation-delay: 0.6s; }
.tech-pill:nth-child(8) { bottom: 4%; left: 45%; animation-delay: 1.5s; }

@keyframes float-y {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 0 30px rgba(0, 120, 212, 0.3), inset 0 0 20px rgba(34, 211, 238, 0.08); }
  50% { box-shadow: 0 0 50px rgba(0, 164, 239, 0.5), inset 0 0 30px rgba(34, 211, 238, 0.15); }
}

.ala-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.25rem 1.2rem;
  height: 100%;
  transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
  backdrop-filter: blur(10px);
}

.ala-card:hover {
  transform: translateY(-4px);
  border-color: rgba(0, 164, 239, 0.4);
  box-shadow: 0 12px 32px rgba(0, 120, 212, 0.15);
}

.ala-card .card-icon {
  font-size: 1.6rem;
  margin-bottom: 0.65rem;
}

.ala-card .card-title {
  font-size: 1.02rem;
  font-weight: 650;
  margin-bottom: 0.4rem;
  color: var(--text);
}

.ala-card .card-body {
  font-size: 0.92rem;
  color: var(--muted);
  line-height: 1.55;
  margin: 0;
}

.feature-row {
  display: flex;
  gap: 1rem;
  align-items: flex-start;
  padding: 1.1rem 1.15rem;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: rgba(11, 17, 32, 0.65);
  margin-bottom: 0.85rem;
  transition: border-color 0.2s ease;
}

.feature-row:hover {
  border-color: rgba(0, 164, 239, 0.35);
}

.feature-row .fr-icon {
  font-size: 1.5rem;
  min-width: 2rem;
}

.feature-row .fr-title {
  font-weight: 650;
  margin-bottom: 0.25rem;
}

.feature-row .fr-body {
  color: var(--muted);
  font-size: 0.92rem;
  margin: 0;
}

.roadmap-step {
  position: relative;
  display: flex;
  gap: 1rem;
  padding: 1rem 1.1rem;
  margin-bottom: 0.65rem;
  border-radius: var(--radius);
  border: 1px solid var(--border);
  background: rgba(11, 17, 32, 0.7);
  transition: all 0.2s ease;
}

.roadmap-step:hover {
  border-color: rgba(0, 164, 239, 0.4);
  transform: translateX(4px);
}

.roadmap-num {
  width: 42px;
  height: 42px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.85rem;
  background: linear-gradient(135deg, rgba(0, 120, 212, 0.35), rgba(34, 211, 238, 0.15));
  border: 1px solid rgba(0, 164, 239, 0.35);
  flex-shrink: 0;
}

.roadmap-connector {
  text-align: center;
  color: var(--cyan);
  opacity: 0.55;
  font-size: 0.9rem;
  margin: -0.2rem 0 0.3rem 1.3rem;
}

.flow-rail {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  align-items: center;
  justify-content: center;
  margin: 1rem 0 1.5rem;
}

.flow-node {
  padding: 0.55rem 0.9rem;
  border-radius: 999px;
  border: 1px solid rgba(0, 164, 239, 0.3);
  background: rgba(15, 23, 42, 0.85);
  font-size: 0.82rem;
  font-weight: 600;
}

.flow-arrow {
  color: var(--cyan);
  opacity: 0.6;
}

.exp-badge {
  display: inline-block;
  padding: 0.35rem 0.7rem;
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 650;
  letter-spacing: 0.06em;
  margin-bottom: 0.6rem;
}

.badge-beginner { background: rgba(34, 197, 94, 0.18); color: #86efac; }
.badge-intermediate { background: rgba(234, 179, 8, 0.18); color: #fde047; }
.badge-advanced { background: rgba(239, 68, 68, 0.18); color: #fca5a5; }
.badge-years { background: rgba(0, 120, 212, 0.22); color: #7dd3fc; }

.question-card {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1rem 1.1rem;
  background: rgba(11, 17, 32, 0.7);
  margin-bottom: 0.75rem;
}

.question-card .q-num {
  color: var(--cyan);
  font-weight: 700;
  font-size: 0.8rem;
  margin-bottom: 0.35rem;
}

.code-panel {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: #070b14;
  padding: 1rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  color: #cbd5e1;
  min-height: 140px;
  white-space: pre-wrap;
}

.coming-soon-box {
  text-align: center;
  padding: 2.5rem 1.5rem;
  border-radius: 24px;
  border: 1px dashed rgba(139, 92, 246, 0.45);
  background:
    radial-gradient(circle at 50% 0%, rgba(139, 92, 246, 0.18), transparent 55%),
    rgba(11, 17, 32, 0.8);
  margin: 1rem 0;
}

.coming-soon-box .cs-icon {
  font-size: 3rem;
  margin-bottom: 0.75rem;
  animation: float-y 5s ease-in-out infinite;
}

.coming-soon-box h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.4rem;
}

.coming-soon-box p {
  color: var(--muted);
  max-width: 420px;
  margin: 0 auto 1rem;
}

.cs-chip {
  display: inline-block;
  margin: 0.25rem;
  padding: 0.3rem 0.65rem;
  border-radius: 999px;
  border: 1px solid var(--border);
  font-size: 0.78rem;
  color: var(--muted);
}

.support-hero-num {
  font-size: clamp(2.5rem, 6vw, 4rem);
  font-weight: 800;
  line-height: 1;
  background: linear-gradient(120deg, #00A4EF, #22D3EE);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.footer-bar {
  margin-top: 2.5rem;
  padding: 1.5rem 0 0.5rem;
  border-top: 1px solid var(--border);
  text-align: center;
  color: var(--muted);
  font-size: 0.88rem;
}

.footer-bar .footer-brand {
  color: var(--text);
  font-weight: 650;
  margin-bottom: 0.35rem;
}

.footer-bar a {
  color: var(--azure-bright);
  text-decoration: none;
}

.section-label {
  font-size: 0.78rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--cyan);
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.live-pill-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin: 1rem 0 1.4rem;
}

.live-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 0.85rem;
  border-radius: 999px;
  border: 1px solid rgba(34, 197, 94, 0.35);
  background: rgba(34, 197, 94, 0.1);
  font-size: 0.82rem;
  font-weight: 600;
}

.live-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #22c55e;
  box-shadow: 0 0 10px #22c55e;
  animation: pulse-glow 2s ease-in-out infinite;
}

div[data-testid="stExpander"] {
  background: rgba(11, 17, 32, 0.7);
  border: 1px solid var(--border);
  border-radius: var(--radius) !important;
  margin-bottom: 0.65rem;
}

div[data-testid="stExpander"] details summary p {
  font-weight: 600 !important;
}

.stButton > button[kind="primary"] {
  background: linear-gradient(135deg, #0078D4, #00A4EF) !important;
  border: none !important;
  color: white !important;
  font-weight: 650 !important;
  border-radius: 12px !important;
  padding: 0.55rem 1.1rem !important;
  box-shadow: 0 8px 24px rgba(0, 120, 212, 0.3) !important;
  transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}

.stButton > button[kind="primary"]:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 28px rgba(0, 164, 239, 0.4) !important;
}

.stButton > button[kind="secondary"] {
  background: rgba(15, 23, 42, 0.6) !important;
  border: 1px solid rgba(0, 164, 239, 0.35) !important;
  color: var(--text) !important;
  border-radius: 12px !important;
}

.stTextInput input, .stTextArea textarea, .stSelectbox > div > div {
  background: rgba(11, 17, 32, 0.85) !important;
  border-color: var(--border) !important;
  color: var(--text) !important;
  border-radius: 10px !important;
}

/* —— Home mobile-first decision UI —— */
.hero-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin: 0.15rem 0 0.85rem;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.32rem 0.65rem;
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 650;
  letter-spacing: 0.02em;
  color: #E0F2FE;
  background: linear-gradient(135deg, rgba(0, 120, 212, 0.28), rgba(34, 211, 238, 0.12));
  border: 1px solid rgba(0, 164, 239, 0.35);
}

.hero-tech-strip {
  margin-top: 0.35rem;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: var(--cyan);
}

.home-section-head {
  margin: 0.25rem 0 0.75rem;
}

.home-section-title {
  margin: 0.2rem 0 0;
  font-size: 1.45rem;
  font-weight: 750;
  letter-spacing: -0.02em;
}

.home-roadmap-preview {
  border: 1px solid var(--border);
  border-radius: 18px;
  background: rgba(11, 17, 32, 0.75);
  padding: 1rem 0.9rem;
  margin: 0.75rem 0 1rem;
}

.home-road-step {
  text-align: center;
  font-weight: 650;
  font-size: 0.98rem;
  padding: 0.55rem 0.7rem;
  border-radius: 12px;
  border: 1px solid rgba(0, 164, 239, 0.25);
  background: rgba(15, 23, 42, 0.85);
}

.home-road-arrow {
  text-align: center;
  color: var(--cyan);
  opacity: 0.7;
  font-size: 0.95rem;
  padding: 0.15rem 0;
}

.syllabus-preview-card {
  text-align: left;
  min-height: 88px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.mqn-sticky {
  display: none;
  position: sticky;
  top: 0;
  z-index: 120;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0.35rem;
  padding: 0.55rem 0.35rem;
  margin: 0.65rem 0 0.85rem;
  border-radius: 14px;
  border: 1px solid rgba(0, 164, 239, 0.28);
  background: rgba(5, 8, 22, 0.92);
  backdrop-filter: blur(10px);
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.35);
}

.mqn-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  text-decoration: none !important;
  color: var(--text) !important;
  font-size: 0.68rem;
  font-weight: 650;
  line-height: 1.2;
  padding: 0.55rem 0.2rem;
  border-radius: 10px;
  border: 1px solid rgba(148, 163, 184, 0.2);
  background: rgba(15, 23, 42, 0.9);
}

.mqn-btn.mqn-primary {
  background: linear-gradient(135deg, #0078D4, #00A4EF);
  border-color: transparent;
}

.mqn-desktop-hint {
  display: none;
  color: var(--muted);
  font-size: 0.8rem;
  margin: 0.25rem 0 0.5rem;
}

@media (max-width: 768px) {
  .hero-wrap {
    padding: 1.15rem 0.9rem 1.25rem;
    border-radius: 18px;
  }
  .hero-network,
  .desktop-only-motion {
    display: none !important;
  }
  .hero-title {
    font-size: 1.55rem !important;
    margin-bottom: 0.65rem !important;
  }
  .hero-subtitle {
    font-size: 0.95rem;
    line-height: 1.55;
    margin-bottom: 0.75rem;
  }
  .page-header {
    margin-bottom: 0.85rem;
  }
  .page-header h1 {
    font-size: 1.35rem !important;
  }
  .page-header p {
    font-size: 0.92rem;
  }
  .ala-card {
    padding: 0.95rem 0.9rem;
    margin-bottom: 0.55rem;
  }
  .ala-card:hover {
    transform: none;
  }
  .syllabus-preview-card .card-title {
    font-size: 0.98rem;
  }
  .home-section-title {
    font-size: 1.25rem;
  }
  .home-roadmap-preview {
    padding: 0.85rem;
  }
  .coming-soon-box {
    padding: 1.6rem 1rem;
  }
  .coming-soon-box .cs-icon {
    animation: none;
  }
  .live-dot {
    animation: none;
    box-shadow: none;
  }
  .tech-pill,
  .hero-core {
    animation: none !important;
  }
  .stApp {
    background: var(--bg) !important;
  }
  div[data-testid="stHorizontalBlock"] {
    gap: 0.45rem;
  }
  div[data-testid="column"] {
    width: 100% !important;
    flex: 1 1 100% !important;
    min-width: 100% !important;
  }
  .stButton > button,
  .stLinkButton > a {
    width: 100% !important;
  }
  .mqn-sticky {
    display: grid;
  }
  .mqn-desktop-hint {
    display: none;
  }
  .block-container {
    padding-left: 0.85rem !important;
    padding-right: 0.85rem !important;
    padding-top: 1rem !important;
  }
}

@media (min-width: 769px) {
  .mqn-sticky {
    display: grid;
    position: relative;
    top: auto;
    margin: 0.5rem 0 0.75rem;
  }
}
</style>
        """,
        unsafe_allow_html=True,
    )
