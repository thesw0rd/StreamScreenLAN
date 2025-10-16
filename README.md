# 🖥️ StreamScreenLAN

A lightweight local network screen streaming tool over **HTTP** — view your desktop from any device in the same LAN, directly in a browser.

---

## 🚀 Features
- Stream your desktop over HTTP with minimal setup  
- Works in any modern browser (Chrome, Firefox, Edge, Safari)  
- No VLC, OBS, or external player required  
- Low latency (~1 s)  
- Cross-platform (Windows, Linux, macOS)

---

## 🧰 Installation
```bash
git clone https://github.com/thesw0rd/StreamScreenLAN.git
cd StreamScreenLAN
pip install -r requirements.txt
````

---

## ▶️ Run

```bash
python screen_stream.py
```

Then open in a browser (on this or another device in your LAN):

```
http://<your_computer_IP>:8080/
```

---

## 📸 How it works

`mss` captures screen frames → `OpenCV` encodes to JPEG →
`Flask` serves them as an MJPEG stream over HTTP.
The browser renders it as a live video feed.

---


💡 *Fast, simple, and browser-friendly screen streaming for your local network.*

