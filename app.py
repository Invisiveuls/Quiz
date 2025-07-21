from flask import Flask, request, jsonify
import base64
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/image', methods=['POST'])
def handle_image():
    try:
        data = request.json
        if 'image' not in data:
            return jsonify({'error': 'Imagem não enviada'}), 400

        b64_str = data['image']
        img_data = base64.b64decode(b64_str)
        np_arr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Processamento opcional (ex: converter para tons de cinza)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, jpeg = cv2.imencode('.jpg', gray)
        encoded = base64.b64encode(jpeg.tobytes()).decode('utf-8')

        return jsonify({'message': 'Imagem recebida com sucesso', 'preview': encoded})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
