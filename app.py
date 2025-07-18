from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    data = request.get_json()
    img_b64 = data['image']
    img_bytes = base64.b64decode(img_b64)
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Exemplo: converter para cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, buf = cv2.imencode('.png', gray)
    img_b64_out = base64.b64encode(buf).decode('utf-8')

    return jsonify({"image": img_b64_out})

if __name__ == "__main__":
    app.run()
