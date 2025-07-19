import os
import cv2
import numpy as np
import base64
import io
from flask import Flask, request, jsonify

app = Flask(__name__)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

@app.route('/image', methods=['POST'])
def process_image():
    try:
        data = request.get_json()
        if 'image' not in data:
            return jsonify({"error": "Campo 'image' não encontrado"}), 400

        img_data = base64.b64decode(data['image'])
        npimg = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        _, buffer = cv2.imencode('.png', img)
        encoded_result = base64.b64encode(buffer).decode('utf-8')

        return encoded_result, 200, {'Content-Type': 'text/plain'}

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
