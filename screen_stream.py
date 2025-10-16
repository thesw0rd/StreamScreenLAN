#!/usr/bin/env python3
"""
StreamScreenLAN — simple cross-platform screen streaming over HTTP.
View your desktop in any browser on the same local network.
"""

from flask import Flask, Response
import cv2
import numpy as np
import mss
import time
import platform
import argparse

app = Flask(__name__)

# --- Parse command line options ---
parser = argparse.ArgumentParser(description="Stream your screen over HTTP (LAN)")
parser.add_argument("--port", type=int, default=8080, help="HTTP port (default: 8080)")
parser.add_argument("--monitor", type=int, default=1, help="Monitor index (default: 1)")
parser.add_argument("--fps", type=int, default=15, help="Frames per second (default: 15)")
parser.add_argument("--quality", type=int, default=70, help="JPEG quality (1–100, default: 70)")
args = parser.parse_args()


def gen_frames():
    """Capture screen and yield JPEG frames"""
    with mss.mss() as sct:
        monitors = sct.monitors
        if args.monitor >= len(monitors):
            print(f"[WARN] Monitor {args.monitor} not found, using primary instead.")
            monitor = monitors[1]
        else:
            monitor = monitors[args.monitor]

        print(f"[INFO] Streaming monitor {args.monitor}: {monitor['width']}x{monitor['height']}")

        frame_time = 1.0 / args.fps
        while True:
            start_time = time.time()

            # Capture screen
            img = np.array(sct.grab(monitor))

            # Convert BGRA → BGR
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

            # Encode as JPEG
            success, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), args.quality])
            if not success:
                continue

            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n'
            )

            # Simple frame limiter
            elapsed = time.time() - start_time
            if elapsed < frame_time:
                time.sleep(frame_time - elapsed)


@app.route('/')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    system = platform.system()
    print(f"[INFO] Starting StreamScreenLAN on {system}")
    print(f"[INFO] Access stream at: http://<your_ip>:{args.port}/")

    app.run(host='0.0.0.0', port=args.port, threaded=True)
