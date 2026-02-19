from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image
import base64, io, random

app = Flask(__name__)
model = YOLO("yolov8n.pt")

@app.route('/nudge', methods= )
def nudge():
    data = request.json
    img_bytes = base64.b64decode(data )
    img = Image.open(io.BytesIO(img_bytes))
    results = model(img, conf=0.35, imgsz=416)
    if len(results[0].boxes) > 0:
       @app.route('/nudge', methods=['POST'])
def nudge():
    data = request.json
    if not data or 'image' not in data:
        return jsonify({"dx": 0, "dy": 0}), 400

    img_bytes = base64.b64decode(data['image'])
    img = Image.open(io.BytesIO(img_bytes))
    results = model(img, conf=0.35, imgsz=416)

    if len(results[0].boxes) > 0:
        box = results[0 0 0].cpu().numpy()  # first box
        cx = (box[0 2 1 3]) / 2
        dx = int((cx - 960) * 0.25 + random.randint(-5, 5))
        dy = int((cy - 540) * 0.25 + random.randint(-5, 5))
        if random.random() > 0.55:
            return jsonify({"dx": dx, "dy": dy})
    return jsonify({"dx": 0, "dy": 0})
