"""
✿ Kawaii World ✿
A chootiepatootie website built with Python + Flask (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
"""

from flask import Flask, render_template_string, jsonify, request
import random
import html

app = Flask(__name__)

# ── Data defined in Python! ──────────────────────────────────────────────────

FRIENDS = [
    {"emoji": "🐰", "name": "Mochi",   "desc": "fluffy & soft ♡",       "color": "#ffb8d8"},
    {"emoji": "🐱", "name": "Yuki",    "desc": "loves milk tea ✿",       "color": "#c8b8ff"},
    {"emoji": "🐻", "name": "Kumo",    "desc": "cloud dreamer ☁",        "color": "#b8e4ff"},
    {"emoji": "🦊", "name": "Hoshi",   "desc": "star collector ⭐",       "color": "#ffe8a0"},
    {"emoji": "🐸", "name": "Midori",  "desc": "rain puddle fan 🌧",      "color": "#b8f0d0"},
    {"emoji": "🐧", "name": "Shiro",   "desc": "snow & cuddles ❄",       "color": "#d8f0ff"},
    {"emoji": "🦄", "name": "Niji",    "desc": "rainbow chaser 🌈",      "color": "#ffd6f0"},
    {"emoji": "🐼", "name": "Kuro",    "desc": "bamboo muncher 🎋",      "color": "#e0ffe0"},
]

GREETINGS = [
    "Uwu hello bestie!!",
    "*waves tiny paws* 🐾",
    "OMG you found me!! 💕",
    "*nuzzles you softly*",
    "You're so cute for clicking me!!",
    "HIIIIII 🌸✨",
    "My favourite human!! 🥺",
    "*does a little spin*",
]

MOODS = [
    {"emoji": "😊", "label": "Happy",    "msg": "Spread that sunshine energy!! 🌈", "bg": "#fff9c4,#ffd870"},
    {"emoji": "🥰", "label": "In Love",  "msg": "Your heart is full of sparkles!! 💖", "bg": "#ffd6ec,#ffb8d8"},
    {"emoji": "😴", "label": "Sleepy",   "msg": "Nap time is always valid 💤☁",    "bg": "#ddd8ff,#c8beff"},
    {"emoji": "🤩", "label": "Excited",  "msg": "LETS GOOO the vibes are immaculate!! ✨", "bg": "#fff0b0,#ffdf70"},
    {"emoji": "🥺", "label": "Sad",      "msg": "Sending you the biggest virtual hug 🫂💕", "bg": "#d8eeff,#b8d8ff"},
    {"emoji": "😤", "label": "Grumpy",   "msg": "Valid!! Let it out, we're here for you 🌩", "bg": "#ffe4d4,#ffc8a8"},
    {"emoji": "🌸", "label": "Kawaii",   "msg": "You ARE the kawaii energy we needed!! ✿", "bg": "#ffd6ec,#f0c8ff"},
    {"emoji": "🍡", "label": "Snacky",   "msg": "Dangoooo time, go treat yourself!! 🍡🍰", "bg": "#e8ffe0,#c8f0b0"},
]

STARTER_BUBBLES = [
    "kawaii forever~ 🌸", "*pops bubble*", "uwu 🥺", "hello fren!! 💕",
    "this place is so cute!!", "✨ magical ✨", "🍡🍡🍡", "i love it here!!",
    "best website ever omg", "squishyyyyy 🥰",
]

BUBBLE_GRADIENTS = [
    ("linear-gradient(135deg,#ffd6ec,#ffb8d8)", "#8b3070"),
    ("linear-gradient(135deg,#d8d0ff,#c0b0ff)", "#4a2090"),
    ("linear-gradient(135deg,#b8f0e0,#90e0cc)", "#1a6050"),
    ("linear-gradient(135deg,#b8e4ff,#90ccff)", "#1a4070"),
    ("linear-gradient(135deg,#ffe8b0,#ffd880)", "#705010"),
    ("linear-gradient(135deg,#ffd6f0,#ffb8e8)", "#702050"),
]

STICKERS = [
    "🌸","🍡","🎀","🦋","🌈","💖","⭐","🍓","🐰","🌙",
    "✨","🎐","🍭","🐱","💝","🌷","🍰","🎠","🐣","🌺",
    "💫","🧁","🌻","🦄","🎶","🍑","🐾","🌟","🎁","🫧",
]

FUN_FACTS = [
    "🌸 The word 'kawaii' (可愛い) literally means 'lovable' in Japanese!",
    "🐰 Rabbits can't vomit — so they just stay cute forever!",
    "✨ Starfish have no brain but are still adorable!",
    "🍡 Mochi was first made over 1,300 years ago in Japan!",
    "🦋 Butterflies taste with their feet uwu!",
    "💖 Otters hold hands while sleeping so they don't drift apart!",
    "🌈 A group of flamingos is called a 'flamboyance' — iconic!!",
    "🐱 Cats purr at frequencies that can heal bones ✿",
]


# ── Python generates the full HTML ───────────────────────────────────────────

def build_friends_html():
    cards = ""
    for f in FRIENDS:
        cards += f"""
        <div class="friend-card" onclick="greetFriend('{f['name']}', '{f['emoji']}')"
             style="--card-color:{f['color']}">
          <span class="friend-emoji">{f['emoji']}</span>
          <div class="friend-name">{f['name']}</div>
          <div class="friend-desc">{f['desc']}</div>
        </div>"""
    return cards

def build_moods_html():
    btns = ""
    for m in MOODS:
        btns += f"""<button class="mood-btn" onclick="setMood('{m['emoji']}','{html.escape(m['label'])}','{html.escape(m['msg'])}','{m['bg']}')">{m['emoji']} {m['label']}</button>\n"""
    return btns

def build_starter_bubbles_html():
    items = ""
    for i, text in enumerate(STARTER_BUBBLES):
        bg, color = BUBBLE_GRADIENTS[i % len(BUBBLE_GRADIENTS)]
        items += f'<div class="bubble-pill" style="background:{bg};color:{color}">{html.escape(text)}</div>\n'
    return items

def build_stickers_html():
    items = ""
    for s in STICKERS:
        items += f'<div class="sticker" onclick="popSticker(event)">{s}</div>\n'
    return items

def build_greetings_js():
    return str(GREETINGS).replace("'", "\\'").replace('"', '\\"') \
        .replace("[", "['").replace("]", "']") \
        .replace(", '", "','").replace("['", '["').replace("']","']")


KAWAII_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>✿ Kawaii World · Python Edition ✿</title>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Fredoka+One&display=swap" rel="stylesheet">
<style>
:root{{
  --pink:#ff85c0;--soft-pink:#ffd6ec;--lavender:#c9b8ff;
  --mint:#b8f0e0;--peach:#ffc8a0;--yellow:#ffe87a;
  --sky:#b8e4ff;--white:#fffafd;--deep-pink:#ff4fa3;--text:#5a3060;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{
  font-family:'Nunito',sans-serif;background:var(--white);color:var(--text);
  overflow-x:hidden;
  cursor:url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32'><text y='26' font-size='26'>🌸</text></svg>") 10 10,auto;
}}

/* BG FLOATIES */
.bg-floaties{{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}}
.floatie{{position:absolute;animation:floatUp linear infinite;opacity:0.16;font-size:2rem}}
@keyframes floatUp{{
  0%{{transform:translateY(110vh) rotate(0deg);opacity:0}}
  10%{{opacity:0.16}} 90%{{opacity:0.16}}
  100%{{transform:translateY(-10vh) rotate(360deg);opacity:0}}
}}

/* CONFETTI */
.confetti-piece{{
  position:fixed;width:10px;height:10px;border-radius:50%;
  pointer-events:none;z-index:9999;
  animation:confettiFall 1.1s ease-out forwards;
}}
@keyframes confettiFall{{
  0%{{transform:translate(0,0) scale(1) rotate(0deg);opacity:1}}
  100%{{transform:translate(var(--tx),var(--ty)) scale(0) rotate(720deg);opacity:0}}
}}

/* NAV */
nav{{
  position:fixed;top:1rem;left:50%;transform:translateX(-50%);z-index:100;
  background:rgba(255,255,255,0.84);backdrop-filter:blur(14px);
  border:2px solid rgba(255,180,230,0.5);border-radius:999px;
  padding:0.5rem 1.5rem;display:flex;gap:1rem;align-items:center;
  box-shadow:0 4px 24px rgba(200,100,200,0.15);
}}
.nav-link{{
  font-family:'Fredoka One',cursive;font-size:0.95rem;
  color:#b06fc0;text-decoration:none;padding:0.3rem 0.8rem;border-radius:999px;
  transition:background 0.2s,color 0.2s;
}}
.nav-link:hover{{background:linear-gradient(135deg,#ff4fa3,#c084fc);color:white}}

/* HERO */
.hero{{
  position:relative;z-index:1;min-height:100vh;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;padding:2rem;
  background:linear-gradient(160deg,#fff0fa 0%,#ffe8f5 30%,#f0e8ff 60%,#e8f8ff 100%);
}}
.hero-badge{{
  font-family:'Fredoka One',cursive;font-size:0.85rem;
  background:linear-gradient(135deg,#ff4fa3,#c084fc);color:white;
  padding:0.3rem 1.2rem;border-radius:999px;margin-bottom:1rem;
  animation:fadeSlide 0.5s ease both;letter-spacing:1px;
}}
.hero-title{{
  font-family:'Fredoka One',cursive;
  font-size:clamp(2.4rem,7vw,5.2rem);line-height:1.1;
  background:linear-gradient(135deg,#ff4fa3,#c084fc,#38bdf8);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 2px 8px rgba(255,100,200,0.25));
  animation:titlePop 0.8s cubic-bezier(.34,1.56,.64,1) both;
}}
@keyframes titlePop{{from{{transform:scale(0.4) rotate(-8deg);opacity:0}}to{{transform:scale(1);opacity:1}}}}
.hero-sub{{margin-top:0.5rem;font-size:clamp(1rem,2.5vw,1.3rem);font-weight:700;color:#b06fc0;animation:fadeSlide 0.8s 0.3s ease both}}
.python-badge{{
  margin-top:0.8rem;font-size:0.8rem;font-weight:700;
  background:rgba(255,255,255,0.7);border:2px solid #e0c8f0;
  border-radius:999px;padding:0.25rem 1rem;color:#9060b0;
  animation:fadeSlide 0.8s 0.5s ease both;
}}
@keyframes fadeSlide{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:translateY(0)}}}}

/* CHIBI */
.chibi-hero{{position:relative;margin:1.5rem 0;animation:chibiFloat 3s ease-in-out infinite}}
@keyframes chibiFloat{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-18px)}}}}
.chibi-svg{{width:clamp(150px,26vw,240px);filter:drop-shadow(0 10px 30px rgba(255,100,200,0.3))}}
.eye{{animation:blink 4s ease-in-out infinite;transform-origin:center}}
@keyframes blink{{0%,44%,56%,100%{{transform:scaleY(1)}}50%{{transform:scaleY(0.04)}}}}
.cheek{{animation:cheekPulse 2.5s ease-in-out infinite}}
@keyframes cheekPulse{{0%,100%{{opacity:0.55}}50%{{opacity:1}}}}
.sparkle-wrap{{position:absolute;inset:-24px;pointer-events:none}}
.sparkle{{position:absolute;font-size:1.3rem;animation:sparkleSpin 2s ease-in-out infinite}}
@keyframes sparkleSpin{{0%,100%{{transform:scale(1) rotate(0deg)}}50%{{transform:scale(1.5) rotate(180deg)}}}}

/* CTA */
.cta-btn{{
  margin-top:1.2rem;padding:0.85rem 2.8rem;
  font-family:'Fredoka One',cursive;font-size:1.2rem;color:white;
  background:linear-gradient(135deg,#ff4fa3,#c084fc);border:none;border-radius:999px;
  cursor:pointer;box-shadow:0 6px 24px rgba(255,80,170,0.4),0 0 0 4px rgba(255,200,235,0.5);
  transition:transform 0.15s,box-shadow 0.15s;animation:fadeSlide 0.8s 0.7s ease both;
}}
.cta-btn:hover{{transform:scale(1.08) rotate(-1deg);box-shadow:0 10px 32px rgba(255,80,170,0.55)}}
.cta-btn:active{{transform:scale(0.95)}}
.scroll-hint{{margin-top:2rem;font-size:0.85rem;color:#c090d0;animation:bounce 1.5s ease-in-out infinite}}
@keyframes bounce{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(6px)}}}}

/* SECTIONS */
section{{position:relative;z-index:1;padding:5rem 1.5rem}}
.section-title{{
  text-align:center;font-family:'Fredoka One',cursive;
  font-size:clamp(1.8rem,4vw,2.8rem);margin-bottom:0.3rem;
  background:linear-gradient(135deg,#ff4fa3,#c084fc);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}}
.section-sub{{text-align:center;color:#b06fc0;font-size:0.95rem;font-weight:700;margin-bottom:2.5rem}}

/* FRIENDS */
.friends-section{{background:linear-gradient(180deg,#fff0fa,#f0eaff)}}
.friends-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:1.4rem;max-width:920px;margin:0 auto}}
.friend-card{{
  background:white;border-radius:24px;padding:1.8rem 1rem 1.4rem;
  text-align:center;box-shadow:0 4px 20px rgba(200,100,200,0.12);
  cursor:pointer;transition:transform 0.2s,box-shadow 0.2s;position:relative;overflow:hidden;
}}
.friend-card::before{{
  content:'';position:absolute;inset:0;border-radius:22px;
  background:var(--card-color);opacity:0;transition:opacity 0.3s;z-index:0;
}}
.friend-card:hover::before{{opacity:0.35}}
.friend-card:hover{{transform:translateY(-8px) scale(1.05);box-shadow:0 14px 36px rgba(200,100,200,0.22)}}
.friend-card>*{{position:relative;z-index:1}}
.friend-emoji{{font-size:3.5rem;display:block;margin-bottom:0.5rem;animation:wiggle 2.5s ease-in-out infinite}}
@keyframes wiggle{{0%,100%{{transform:rotate(-3deg)}}50%{{transform:rotate(3deg)}}}}
.friend-card:nth-child(2) .friend-emoji{{animation-delay:0.4s}}
.friend-card:nth-child(3) .friend-emoji{{animation-delay:0.8s}}
.friend-card:nth-child(4) .friend-emoji{{animation-delay:1.2s}}
.friend-card:nth-child(5) .friend-emoji{{animation-delay:1.6s}}
.friend-card:nth-child(6) .friend-emoji{{animation-delay:2s}}
.friend-card:nth-child(7) .friend-emoji{{animation-delay:0.6s}}
.friend-card:nth-child(8) .friend-emoji{{animation-delay:1s}}
.friend-name{{font-family:'Fredoka One',cursive;font-size:1.1rem;color:var(--text)}}
.friend-desc{{font-size:0.78rem;color:#b06fc0;margin-top:0.3rem;font-weight:700}}
.greeting-toast{{
  text-align:center;margin-top:1.6rem;
  font-family:'Fredoka One',cursive;font-size:1.3rem;color:#c084fc;
  animation:popIn 0.4s cubic-bezier(.34,1.56,.64,1);
}}
@keyframes popIn{{from{{transform:scale(0.6);opacity:0}}to{{transform:scale(1);opacity:1}}}}

/* MOOD */
.mood-section{{background:linear-gradient(180deg,#f0eaff,#e8f8ff)}}
.mood-bar{{display:flex;flex-wrap:wrap;gap:0.8rem;justify-content:center;max-width:720px;margin:0 auto 2rem}}
.mood-btn{{
  padding:0.65rem 1.4rem;font-family:'Fredoka One',cursive;font-size:1rem;
  border:3px solid #e8c8f8;border-radius:999px;background:white;cursor:pointer;
  transition:transform 0.15s,box-shadow 0.15s,background 0.2s;color:var(--text);
  box-shadow:0 3px 12px rgba(180,100,200,0.12);
}}
.mood-btn:hover{{transform:scale(1.1);box-shadow:0 6px 20px rgba(180,100,200,0.25)}}
.mood-display{{
  max-width:460px;margin:0 auto;background:white;border-radius:28px;
  padding:2rem;text-align:center;box-shadow:0 8px 32px rgba(180,100,200,0.15);
  animation:popIn 0.4s cubic-bezier(.34,1.56,.64,1);display:none;
}}
.mood-big-emoji{{font-size:5rem;display:block;animation:moodBounce 0.5s cubic-bezier(.34,1.56,.64,1)}}
@keyframes moodBounce{{from{{transform:scale(0) rotate(-20deg)}}to{{transform:scale(1) rotate(0)}}}}
.mood-label{{font-family:'Fredoka One',cursive;font-size:1.6rem;color:var(--text);margin-top:0.4rem}}
.mood-msg{{font-size:0.95rem;color:#b06fc0;margin-top:0.3rem;font-weight:700}}

/* FUN FACT */
.fact-section{{background:linear-gradient(180deg,#e8f8ff,#f0f8ff)}}
.fact-box{{
  max-width:600px;margin:0 auto;background:white;border-radius:28px;
  padding:2.5rem;text-align:center;box-shadow:0 8px 32px rgba(100,150,220,0.15);
}}
.fact-emoji{{font-size:4rem;display:block;margin-bottom:1rem}}
.fact-text{{font-size:1.1rem;font-weight:700;color:var(--text);line-height:1.6}}
.fact-btn{{
  margin-top:1.5rem;padding:0.7rem 2rem;font-family:'Fredoka One',cursive;font-size:1rem;
  color:white;background:linear-gradient(135deg,#38bdf8,#818cf8);border:none;border-radius:999px;
  cursor:pointer;box-shadow:0 4px 14px rgba(100,150,250,0.3);transition:transform 0.15s;
}}
.fact-btn:hover{{transform:scale(1.08)}}

/* BUBBLES */
.bubbles-section{{background:linear-gradient(180deg,#f0f8ff,#fff0fa)}}
.bubble-form{{max-width:540px;margin:0 auto 2.5rem;display:flex;gap:0.75rem}}
.bubble-input{{
  flex:1;padding:0.8rem 1.2rem;font-family:'Nunito',sans-serif;font-size:1rem;font-weight:700;
  border:2.5px solid #e8c0f0;border-radius:999px;outline:none;background:white;color:var(--text);
  transition:border-color 0.2s,box-shadow 0.2s;
}}
.bubble-input:focus{{border-color:#c084fc;box-shadow:0 0 0 4px rgba(192,132,252,0.2)}}
.bubble-send{{
  padding:0.8rem 1.5rem;font-family:'Fredoka One',cursive;font-size:1rem;color:white;
  background:linear-gradient(135deg,#ff4fa3,#c084fc);border:none;border-radius:999px;
  cursor:pointer;transition:transform 0.15s;box-shadow:0 4px 14px rgba(255,80,170,0.3);
}}
.bubble-send:hover{{transform:scale(1.08)}}
.bubble-send:active{{transform:scale(0.95)}}
.bubbles-wall{{max-width:740px;margin:0 auto;display:flex;flex-wrap:wrap;gap:1rem;justify-content:center}}
.bubble-pill{{
  padding:0.6rem 1.3rem;border-radius:999px;font-weight:700;font-size:0.95rem;
  box-shadow:0 3px 12px rgba(180,100,200,0.18);animation:pilPop 0.4s cubic-bezier(.34,1.56,.64,1) both;
  max-width:260px;word-break:break-word;text-align:center;
}}
@keyframes pilPop{{from{{transform:scale(0);opacity:0}}to{{transform:scale(1);opacity:1}}}}

/* STICKERS */
.stickers-section{{background:linear-gradient(180deg,#fff0fa,#fffafd)}}
.stickers-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(90px,1fr));gap:1rem;max-width:680px;margin:0 auto}}
.sticker{{
  aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-size:2.8rem;
  background:white;border-radius:20px;box-shadow:0 4px 16px rgba(200,100,200,0.12);
  cursor:pointer;transition:transform 0.2s,box-shadow 0.2s;user-select:none;
}}
.sticker:hover{{transform:scale(1.2) rotate(5deg);box-shadow:0 8px 28px rgba(200,100,200,0.25)}}
.sticker:active{{transform:scale(0.85)}}

/* FOOTER */
footer{{
  position:relative;z-index:1;text-align:center;padding:3rem 1rem;
  background:linear-gradient(135deg,#ffd6ec,#e8d8ff);
  font-family:'Fredoka One',cursive;font-size:1.1rem;color:#b06fc0;
}}
.footer-hearts{{font-size:1.5rem;animation:heartBeat 1s ease-in-out infinite}}
@keyframes heartBeat{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.25)}}}}
.footer-python{{
  margin-top:0.6rem;font-size:0.82rem;font-weight:700;
  background:rgba(255,255,255,0.6);border-radius:999px;padding:0.2rem 1rem;
  display:inline-block;color:#9060b0;
}}

@media(max-width:520px){{
  nav{{gap:0.4rem;padding:0.4rem 0.8rem}}
  .nav-link{{font-size:0.78rem;padding:0.2rem 0.5rem}}
  .friends-grid{{grid-template-columns:repeat(2,1fr)}}
  .stickers-grid{{grid-template-columns:repeat(auto-fill,minmax(75px,1fr))}}
}}
</style>
</head>
<body>

<!-- BG FLOATIES -->
<div class="bg-floaties" id="floaties"></div>

<!-- CONFETTI CONTAINER -->
<div id="confetti-container"></div>

<!-- NAV -->
<nav>
  <span style="font-size:1.2rem">🌸</span>
  <a href="#friends" class="nav-link">Friends</a>
  <a href="#mood" class="nav-link">Mood</a>
  <a href="#fact" class="nav-link">Facts</a>
  <a href="#bubbles" class="nav-link">Bubbles</a>
  <a href="#stickers" class="nav-link">Stickers</a>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-badge">🐍 Python Edition 🐍</div>
  <h1 class="hero-title">✿ Kawaii World ✿</h1>
  <p class="hero-sub">a super chootiepatootie place (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧</p>
  <p class="python-badge">🐍 Proudly generated by Python + Flask ✿</p>

  <div class="chibi-hero">
    <div class="sparkle-wrap">
      <span class="sparkle" style="top:5%;left:3%;animation-delay:0s">⭐</span>
      <span class="sparkle" style="top:12%;right:0%;animation-delay:0.5s">✨</span>
      <span class="sparkle" style="bottom:18%;left:0%;animation-delay:1s">🌟</span>
      <span class="sparkle" style="bottom:8%;right:5%;animation-delay:1.5s">💫</span>
      <span class="sparkle" style="top:48%;left:-6%;animation-delay:2s">⭐</span>
    </div>
    <svg class="chibi-svg" viewBox="0 0 200 270" xmlns="http://www.w3.org/2000/svg">
      <!-- Body -->
      <ellipse cx="100" cy="218" rx="50" ry="36" fill="#ffc8e8"/>
      <ellipse cx="72" cy="238" rx="22" ry="12" fill="#ff85c0" opacity="0.7"/>
      <ellipse cx="128" cy="238" rx="22" ry="12" fill="#ff85c0" opacity="0.7"/>
      <ellipse cx="100" cy="246" rx="32" ry="14" fill="#ffd6ec"/>
      <!-- Arms -->
      <ellipse cx="51" cy="212" rx="14" ry="9" fill="#ffe0c8" transform="rotate(-22,51,212)"/>
      <ellipse cx="149" cy="212" rx="14" ry="9" fill="#ffe0c8" transform="rotate(22,149,212)"/>
      <circle cx="40" cy="220" r="9" fill="#ffe8d5"/>
      <circle cx="160" cy="220" r="9" fill="#ffe8d5"/>
      <!-- tiny snake on hand -->
      <path d="M36,218 Q34,212 38,208 Q42,204 40,200" stroke="#7bc67e" stroke-width="3" fill="none" stroke-linecap="round"/>
      <circle cx="40" cy="199" r="3" fill="#4caf50"/>
      <line x1="40" y1="196" x2="38" y2="193" stroke="#f44336" stroke-width="1.2" stroke-linecap="round"/>
      <line x1="40" y1="196" x2="42" y2="193" stroke="#f44336" stroke-width="1.2" stroke-linecap="round"/>
      <!-- Legs -->
      <rect x="83" y="248" width="14" height="22" rx="7" fill="#ffc8e8"/>
      <rect x="103" y="248" width="14" height="22" rx="7" fill="#ffc8e8"/>
      <ellipse cx="90" cy="270" rx="12" ry="6" fill="#a855f7"/>
      <ellipse cx="110" cy="270" rx="12" ry="6" fill="#a855f7"/>
      <!-- Big head -->
      <circle cx="100" cy="114" r="68" fill="#ffe8d5"/>
      <!-- Hair back -->
      <ellipse cx="100" cy="58" rx="60" ry="44" fill="#c084fc"/>
      <!-- Cat ears -->
      <polygon points="55,45 45,12 72,35" fill="#c084fc"/>
      <polygon points="58,42 50,22 70,36" fill="#ffb8d8"/>
      <polygon points="145,45 155,12 128,35" fill="#c084fc"/>
      <polygon points="142,42 150,22 130,36" fill="#ffb8d8"/>
      <!-- Hair front -->
      <ellipse cx="100" cy="80" rx="64" ry="50" fill="#c084fc"/>
      <ellipse cx="68" cy="92" rx="20" ry="26" fill="#c084fc"/>
      <ellipse cx="132" cy="92" rx="20" ry="26" fill="#c084fc"/>
      <ellipse cx="100" cy="90" rx="18" ry="22" fill="#c084fc"/>
      <!-- Face -->
      <circle cx="100" cy="117" r="54" fill="#fff0e8"/>
      <!-- Eyes -->
      <ellipse cx="82" cy="112" rx="14" ry="16" fill="white"/>
      <ellipse cx="118" cy="112" rx="14" ry="16" fill="white"/>
      <ellipse class="eye" cx="82" cy="114" rx="8" ry="10" fill="#5a3060"/>
      <ellipse class="eye" cx="118" cy="114" rx="8" ry="10" fill="#5a3060"/>
      <circle cx="78" cy="109" r="3.2" fill="white"/>
      <circle cx="114" cy="109" r="3.2" fill="white"/>
      <circle cx="85" cy="118" r="1.5" fill="white"/>
      <circle cx="121" cy="118" r="1.5" fill="white"/>
      <!-- Lashes -->
      <line x1="70" y1="98" x2="68" y2="92" stroke="#5a3060" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="79" y1="96" x2="78" y2="90" stroke="#5a3060" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="87" y1="96" x2="88" y2="90" stroke="#5a3060" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="113" y1="96" x2="112" y2="90" stroke="#5a3060" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="121" y1="96" x2="122" y2="90" stroke="#5a3060" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="130" y1="98" x2="132" y2="92" stroke="#5a3060" stroke-width="1.5" stroke-linecap="round"/>
      <!-- Cheeks -->
      <ellipse class="cheek" cx="62" cy="126" rx="17" ry="11" fill="#ff85c0" opacity="0.6"/>
      <ellipse class="cheek" cx="138" cy="126" rx="17" ry="11" fill="#ff85c0" opacity="0.6"/>
      <!-- Cat whiskers -->
      <line x1="62" y1="130" x2="40" y2="126" stroke="#c084fc" stroke-width="1.2" stroke-linecap="round" opacity="0.7"/>
      <line x1="62" y1="134" x2="40" y2="134" stroke="#c084fc" stroke-width="1.2" stroke-linecap="round" opacity="0.7"/>
      <line x1="138" y1="130" x2="160" y2="126" stroke="#c084fc" stroke-width="1.2" stroke-linecap="round" opacity="0.7"/>
      <line x1="138" y1="134" x2="160" y2="134" stroke="#c084fc" stroke-width="1.2" stroke-linecap="round" opacity="0.7"/>
      <!-- Nose -->
      <path d="M97,130 L100,134 L103,130 Q100,128 97,130Z" fill="#ff85c0"/>
      <!-- Mouth -->
      <path d="M90,136 Q100,146 110,136" stroke="#ff85c0" stroke-width="2.5" fill="none" stroke-linecap="round"/>
      <!-- Hair bow -->
      <path d="M83,70 Q100,58 117,70 Q100,62 83,70Z" fill="#ff4fa3"/>
      <circle cx="100" cy="66" r="7" fill="#ff85c0"/>
      <!-- Python logo small -->
      <text x="155" y="90" font-size="13" opacity="0.8">🐍</text>
    </svg>
  </div>

  <button class="cta-btn" onclick="burstConfetti(event)">🎉 Sprinkle Magic! 🎉</button>
  <p class="scroll-hint">✦ scroll for more cuteness ✦ ↓</p>
</section>

<!-- FRIENDS -->
<section id="friends" class="friends-section">
  <h2 class="section-title">✨ Meet the Friends ✨</h2>
  <p class="section-sub">click them to say hi~ (Python picked them all!) (｡♥‿♥｡)</p>
  <div class="friends-grid">
    {build_friends_html()}
  </div>
  <div id="greeting-area"></div>
</section>

<!-- MOOD -->
<section id="mood" class="mood-section">
  <h2 class="section-title">🌈 What's Your Mood? 🌈</h2>
  <p class="section-sub">Python mixed {len(MOODS)} moods just for you~ (っ◕‿◕)っ</p>
  <div class="mood-bar">
    {build_moods_html()}
  </div>
  <div class="mood-display" id="mood-display">
    <span class="mood-big-emoji" id="mood-emoji"></span>
    <div class="mood-label" id="mood-label"></div>
    <div class="mood-msg" id="mood-msg"></div>
  </div>
</section>

<!-- FUN FACT -->
<section id="fact" class="fact-section">
  <h2 class="section-title">🧠 Fun Kawaii Facts 🧠</h2>
  <p class="section-sub">Python serves fresh facts via API~ ✿</p>
  <div class="fact-box">
    <span class="fact-emoji" id="fact-emoji">🌸</span>
    <p class="fact-text" id="fact-text">Click the button to get a kawaii fun fact!</p>
    <button class="fact-btn" onclick="getFact()">✨ New Fact! ✨</button>
  </div>
</section>

<!-- BUBBLES -->
<section id="bubbles" class="bubbles-section">
  <h2 class="section-title">💬 Bubble Wall 💬</h2>
  <p class="section-sub">leave a cute message~ Python adds the colours! ✿</p>
  <div class="bubble-form">
    <input class="bubble-input" id="bubble-input" placeholder="type something kawaii... ♡"
           maxlength="50" onkeyup="if(event.key==='Enter')addBubble()"/>
    <button class="bubble-send" onclick="addBubble()">Send ✈</button>
  </div>
  <div class="bubbles-wall" id="bubbles-wall">
    {build_starter_bubbles_html()}
  </div>
</section>

<!-- STICKERS -->
<section id="stickers" class="stickers-section">
  <h2 class="section-title">🎀 Sticker Box 🎀</h2>
  <p class="section-sub">Python picked {len(STICKERS)} stickers~  tap to make them pop! (≧◡≦)</p>
  <div class="stickers-grid">
    {build_stickers_html()}
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-hearts">💖 💜 💙 💚 💛 🧡 💖</div>
  <p style="margin-top:0.8rem">made with lots of love &amp; kawaii energy (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧</p>
  <div class="footer-python">🐍 Powered by Python {'{'}__import__('sys').version.split()[0]{'}'} + Flask</div>
</footer>

<script>
// ── Floating background emojis ──────────────────────────────────────────────
const bgEmojis = ['🌸','🌼','✨','💫','⭐','🦋','🍡','🌙','🎀','💕','🍭','🌈','🐰','🍓','💝','🐍'];
const floatContainer = document.getElementById('floaties');
for (let i = 0; i < 20; i++) {{
  const el = document.createElement('span');
  el.className = 'floatie';
  el.textContent = bgEmojis[i % bgEmojis.length];
  el.style.cssText = `left:${{Math.random()*100}}%;animation-duration:${{10+Math.random()*14}}s;animation-delay:-${{Math.random()*16}}s;font-size:${{1.2+Math.random()*1.4}}rem`;
  floatContainer.appendChild(el);
}}

// ── Confetti ─────────────────────────────────────────────────────────────────
const confColors = ['#ff4fa3','#c084fc','#38bdf8','#fbbf24','#34d399','#fb923c','#f472b6'];
let cId = 0;
function burstConfetti(e, count=30, cx=null, cy=null) {{
  cx = cx ?? e.clientX; cy = cy ?? e.clientY;
  const container = document.getElementById('confetti-container');
  for (let i = 0; i < count; i++) {{
    const c = document.createElement('div');
    c.className = 'confetti-piece';
    c.style.cssText = `left:${{cx}}px;top:${{cy}}px;background:${{confColors[Math.floor(Math.random()*confColors.length)]}};--tx:${{(Math.random()-.5)*280}}px;--ty:${{(Math.random()-1.1)*220}}px`;
    container.appendChild(c);
    setTimeout(() => c.remove(), 1200);
  }}
}}

// ── Friends ──────────────────────────────────────────────────────────────────
const greetings = {GREETINGS};
let greetTimer;
function greetFriend(name, emoji) {{
  clearTimeout(greetTimer);
  const area = document.getElementById('greeting-area');
  const g = greetings[Math.floor(Math.random()*greetings.length)];
  area.innerHTML = `<div class="greeting-toast">${{emoji}} ${{name}} says: "${{g}}"</div>`;
  greetTimer = setTimeout(() => area.innerHTML = '', 3000);
}}

// ── Mood ─────────────────────────────────────────────────────────────────────
function setMood(emoji, label, msg, bg) {{
  const d = document.getElementById('mood-display');
  d.style.display = 'block';
  d.style.background = `linear-gradient(135deg,${{bg}})`;
  // re-trigger animation
  const e = document.getElementById('mood-emoji');
  e.replaceWith(e.cloneNode(true));
  document.getElementById('mood-emoji').textContent = emoji;
  document.getElementById('mood-label').textContent = label + '!';
  document.getElementById('mood-msg').textContent = msg;
  document.querySelectorAll('.mood-btn').forEach(b => {{
    b.style.background = b.textContent.includes(label) ? 'linear-gradient(135deg,#ff4fa3,#c084fc)' : '';
    b.style.color = b.textContent.includes(label) ? 'white' : '';
  }});
}}

// ── Fun Facts (fetch from Python API) ───────────────────────────────────────
async function getFact() {{
  try {{
    const res = await fetch('/api/fact');
    const data = await res.json();
    document.getElementById('fact-text').textContent = data.text.replace(/^[^\\s]+\\s/, '');
    document.getElementById('fact-emoji').textContent = data.emoji;
  }} catch(e) {{
    document.getElementById('fact-text').textContent = 'Oops! Python is napping~ 💤';
  }}
}}
getFact(); // load one on start

// ── Bubbles (post to Python API) ─────────────────────────────────────────────
async function addBubble() {{
  const input = document.getElementById('bubble-input');
  const text = input.value.trim();
  if (!text) return;
  try {{
    const res = await fetch('/api/bubble', {{
      method: 'POST', headers:{{'Content-Type':'application/json'}},
      body: JSON.stringify({{text}})
    }});
    const data = await res.json();
    const wall = document.getElementById('bubbles-wall');
    const pill = document.createElement('div');
    pill.className = 'bubble-pill';
    pill.style.background = data.bg;
    pill.style.color = data.color;
    pill.textContent = text;
    wall.prepend(pill);
    input.value = '';
    if (wall.children.length > 20) wall.lastChild.remove();
  }} catch(e) {{
    console.error(e);
  }}
}}

// ── Sticker pop ──────────────────────────────────────────────────────────────
function popSticker(e) {{
  const r = e.currentTarget.getBoundingClientRect();
  burstConfetti(null, 14, r.left+r.width/2, r.top+r.height/2);
}}
</script>
</body>
</html>
"""


# ── Flask Routes ─────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template_string(KAWAII_HTML)


@app.route('/api/fact')
def api_fact():
    """Python randomly picks a fun fact ✿"""
    fact = random.choice(FUN_FACTS)
    emoji = fact.split()[0]
    return jsonify({"emoji": emoji, "text": fact})


@app.route('/api/bubble', methods=['POST'])
def api_bubble():
    """Python randomly assigns a bubble colour ✿"""
    bg, color = random.choice(BUBBLE_GRADIENTS)
    return jsonify({"bg": bg, "color": color})


@app.route('/api/greeting')
def api_greeting():
    name = request.args.get('name', 'fren')
    g = random.choice(GREETINGS)
    return jsonify({"greeting": f"{name} says: '{g}'"})


if __name__ == '__main__':
    print("✿ Kawaii World is running~ (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
    print("🐍 Open http://localhost:5000 in your browser!")
    app.run(debug=True, port=5000)
