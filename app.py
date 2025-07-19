from flask import Flask, request, jsonify
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    data = request.get_json()
    img_b64 = data['image'].split(',')[1]
    img_bytes = base64.b64decode(img_b64)
    img = Image.open(io.BytesIO(img_bytes)).convert('L')  # cinza

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    img_out_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    return jsonify({'image': 'data:image/png;base64,' + img_out_b64})

if __name__ == '__main__':
    app.run()
