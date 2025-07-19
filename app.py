from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.route("/process_image", methods=["POST"])
def process_image():
    try:
        data = request.json
        img_base64 = data["image"]
        img_bytes = base64.b64decode(img_base64)
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Processamento com OpenCV (ex: converter para tons de cinza)
        processed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, buffer = cv2.imencode('.png', processed)
        img_base64 = base64.b64encode(buffer).decode("utf-8")
        return jsonify({"image": img_base64})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
