from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

def base64_to_image(base64_str):
    img_data = base64.b64decode(base64_str)
    np_arr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return img

def image_to_base64(img):
    _, buffer = cv2.imencode('.jpg', img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    return img_base64

@app.route('/process_image', methods=['POST'])
def process_image():
    data = request.get_json()
    img_base64 = data.get('image_base64', '')
    if not img_base64:
        return jsonify({"erro": "Imagem não enviada"}), 400
    
    img = base64_to_image(img_base64)
    if img is None:
        return jsonify({"erro": "Imagem inválida"}), 400

    # Processamento (ex: converter para cinza)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Converter de volta para 3 canais para não ter problema no retorno
    processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    img_processada_base64 = image_to_base64(processed_img)
    return jsonify({"image_base64": img_processada_base64})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
