from flask import Flask, request, send_file
from PIL import Image, ImageOps
import io

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_image():
    file = request.files['image']
    image = Image.open(file.stream)
    
    # Exemplo: inverter cores
    processed_image = ImageOps.invert(image.convert('RGB'))

    buffer = io.BytesIO()
    processed_image.save(buffer, format='PNG')
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run()
