from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        data = request.get_json()
        img_b64 = data.get("image_base64", "")

        # Decodificar imagem
        img_data = base64.b64decode(img_b64)
        nparr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Processar (converter para cinza)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Codificar de volta
        _, buffer = cv2.imencode('.jpg', gray)
        result_b64 = base64.b64encode(buffer).decode('utf-8')

        return jsonify({"processed_image": result_b64})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
