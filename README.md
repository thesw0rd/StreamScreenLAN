# 🖥️ StreamScreenLAN

A lightweight, cross-platform tool for streaming your desktop over **HTTP** within your local network — viewable directly in any browser.

---

## 🚀 Features
- Cross-platform (Windows / Linux / macOS)  
- Stream your desktop directly to any browser — no VLC, OBS, or plugins  
- Adjustable FPS, JPEG quality, and port  
- Simple command-line arguments  
- Low CPU usage, low latency (~1s)  
- Multiple clients supported simultaneously  

---

## 🧰 Installation

```bash
git clone https://github.com/thesw0rd/StreamScreenLAN.git
cd StreamScreenLAN
pip install -r requirements.txt
````

---

## ▶️ Usage

Start the stream:

```bash
python screen_stream.py
```

Then open in your browser (on this or any device in your LAN):

```
http://<your_computer_IP>:8080/
```

---

## ⚙️ Options

You can customize parameters when launching:

```bash
python screen_stream.py [options]
```

| Option      | Description                 | Default |
| ----------- | --------------------------- | ------- |
| `--port`    | HTTP server port            | `8080`  |
| `--monitor` | Monitor index (1 = primary) | `1`     |
| `--fps`     | Frames per second           | `15`    |
| `--quality` | JPEG image quality (1–100)  | `70`    |

Example:

```bash
python screen_stream.py --port 5000 --fps 10 --quality 60
```

---

## 📸 How It Works

1. **mss** captures the screen cross-platform
2. **OpenCV** encodes frames to JPEG
3. **Flask** serves an MJPEG stream over HTTP
4. Any browser renders it as a live video feed

---

## ⚡ Tips

* Lower `--fps` or `--quality` if CPU usage is high
* Works best on a wired LAN for minimal latency
* Can be embedded into an `<img>` tag for dashboards or monitoring pages

---

💡 *Fast, clean, and cross-platform screen streaming — your desktop in a browser within seconds.*
