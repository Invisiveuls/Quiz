from flask import Flask, request, jsonify
from PIL import Image, ImageOps
import io
import base64

app = Flask(__name__)

@app.route('/image', methods=['POST'])
def process_image():
    try:
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({"error": "Campo 'image' não encontrado"}), 400

        img_data = base64.b64decode(data['image'])
        image = Image.open(io.BytesIO(img_data)).convert('RGB')
        processed = ImageOps.invert(image)

        buffer = io.BytesIO()
        processed.save(buffer, format='PNG')
        encoded_result = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Para debug, imprime os primeiros caracteres da base64
        print("Base64 length:", len(encoded_result))
        print("Base64 preview:", encoded_result[:100])

        return encoded_result  # Retorna só a string base64 pura, sem JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
