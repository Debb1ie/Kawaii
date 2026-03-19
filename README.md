# ✿ Kawaii World 🐍 · Python Edition ✿

> a super chootiepatootie website built with Python + Flask (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧

---

## 🌸 What is this??

A fully kawaii, chibi-themed website where **Python does ALL the work** — generating HTML, serving pages, and powering a mini REST API with cute features like mood pickers, bubble walls, fun facts, and a sticker box!! The frontend is pure HTML + CSS + vanilla JS with zero frameworks. uwu ✿

---

## 🐍 Tech Stack

| Layer | Tech |
|---|---|
| Backend | Python 3 + Flask |
| Frontend | HTML5 · CSS3 · Vanilla JS |
| Fonts | Fredoka One · Nunito (Google Fonts) |
| Data | Python lists & dicts (no database needed!) |
| APIs | Flask JSON endpoints |

---

## 📁 Project Structure

```
kawaii_app/
│
├── app.py          ← everything lives here! 🐍
└── README.md       ← you are here ♡
```

`app.py` is a single-file app that contains:
- All kawaii data (friends, moods, stickers, facts) as Python constants
- HTML builder functions that generate page sections from Python data
- The full HTML/CSS/JS template as a Python f-string
- Flask routes for the page and all API endpoints

---

## 🚀 How to Run

**1. Install Flask**
```bash
pip install flask
```

**2. Run the app**
```bash
python app.py
```

**3. Open your browser**
```
http://localhost:5000
```

That's it!! Python will print a kawaii little message in your terminal~ 🌸

---

## 🎀 Features

### 🐱 Chibi Hero Character
A hand-drawn SVG cat-girl with:
- Blinking eyes animation
- Pulsing blush cheeks
- Floating up-and-down animation
- Orbiting sparkle emojis
- A tiny 🐍 snake friend on her hand hehe

### 👯 Friends Gallery
8 clickable chibi friends (Mochi, Yuki, Kumo, Hoshi, Midori, Shiro, Niji, Kuro). Click one and they say a random cute greeting — all greeting strings are defined in Python's `GREETINGS` list.

### 🌈 Mood Picker
8 moods to choose from. Selecting one shows a personalised kawaii message with a matching pastel gradient background. All mood data lives in Python's `MOODS` list.

### 🧠 Fun Kawaii Facts
Powered by a real Flask API endpoint! Clicking "New Fact" calls `GET /api/fact` and Python randomly serves one from the `FUN_FACTS` list using `random.choice()`.

### 💬 Bubble Wall
Type a message and it becomes a colourful gradient bubble pill. Submitting calls `POST /api/bubble` — Python picks a random colour scheme from `BUBBLE_GRADIENTS` and returns it as JSON.

### 🎀 Sticker Box
30 stickers defined in Python's `STICKERS` list. Tapping one triggers a confetti burst animation.

### ✨ Extra Magic
- 🌸 Sakura cursor (custom CSS cursor)
- 🎉 Confetti burst on button click
- 🌸 Floating background emoji particles
- 💫 Smooth scroll navigation
- 📱 Fully responsive layout

---

## 🔌 API Endpoints

| Method | Endpoint | What Python does |
|---|---|---|
| `GET` | `/` | Renders full kawaii HTML page |
| `GET` | `/api/fact` | Returns a random fun fact as JSON |
| `POST` | `/api/bubble` | Returns a random bubble gradient as JSON |
| `GET` | `/api/greeting?name=Mochi` | Returns a random greeting for a friend |

### Example responses

**GET /api/fact**
```json
{
  "emoji": "💖",
  "text": "💖 Otters hold hands while sleeping so they don't drift apart!"
}
```

**POST /api/bubble**
```json
{
  "bg": "linear-gradient(135deg,#ffd6ec,#ffb8d8)",
  "color": "#8b3070"
}
```

**GET /api/greeting?name=Yuki**
```json
{
  "greeting": "Yuki says: 'OMG you found me!! 💕'"
}
```

---

## 🛠 How to Customise

### Add a new friend
In `app.py`, add a dict to the `FRIENDS` list:
```python
FRIENDS = [
    ...
    {"emoji": "🐨", "name": "Maru", "desc": "eucalyptus fanatic 🌿", "color": "#d4f0c0"},
]
```
Python auto-generates the card HTML — no template editing needed! ✿

### Add a new mood
```python
MOODS = [
    ...
    {"emoji": "🌊", "label": "Chill", "msg": "Ocean vibes only~ 🌊", "bg": "#b8f0ff,#80d8ff"},
]
```

### Add more fun facts
```python
FUN_FACTS = [
    ...
    "🐨 Koalas sleep up to 22 hours a day — goals honestly!!",
]
```

### Add more stickers
```python
STICKERS = [..., "🍄", "🪷", "🫶"]
```

---

## 💝 Credits

Built with lots of love, Python magic, and kawaii energy~

```
(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧  made with Python 🐍 + Flask 🌶 + pure kawaii spirit ✿
```
