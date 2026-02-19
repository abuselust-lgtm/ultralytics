from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image
import base64
import io
import random

app = Flask(__name__)
model = YOLO("yolov8n.pt")

@app.route('/nudge', methods= )
def nudge():
    data = request.json
    if not data or 'image' not in data:
        return jsonify({"dx": 0, "dy": 0}), 400

    try:
        img_bytes = base64.b64decode(data )
        img = Image.open(io.BytesIO(img_bytes))
        results = model(img, conf=0.35, imgsz=416)

        if len(results[0].boxes) > 0:
            # Get first detected box (x1,y1,x2,y2)
            box = results[0 0 0 2]) / 2  # center x
            cy = (box[1 3]) / 2  # center y
            dx = int((cx - 960) * 0.25 + random.randint(-5, 5))
            dy = int((cy - 540) * 0.25 + random.randint(-5, 5))
            if random.random() > 0.55:  # occasional nudge
                return jsonify({"dx": dx, "dy": dy})
    except Exception as e:
        print(f"Error: {e}")
    
    return jsonify({"dx": 0, "dy": 0})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
