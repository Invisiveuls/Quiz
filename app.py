from flask import Flask, request, send_file
import cv2
import numpy as np
import io

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # exemplo de processamento
    _, buf = cv2.imencode('.png', gray)
    return send_file(io.BytesIO(buf.tobytes()), mimetype='image/png')

if __name__ == '__main__':
    app.run()
