from flask import Flask, request, jsonify
import base64
import cv2
import numpy as np
import face_recognition

app = Flask(__name__)

# Carregue imagem conhecida e codificação
known_image = face_recognition.load_image_file("known.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

@app.route('/send_frame', methods=['GET'])
def process_frame():
    img_b64 = request.args.get('image')
    if not img_b64:
        return jsonify({"error": "No image received"}), 400

    try:
        img_bytes = base64.b64decode(img_b64)
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_img)
        face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

        results = []
        for encoding in face_encodings:
            matches = face_recognition.compare_faces([known_encoding], encoding)
            results.append(matches[0])

        return jsonify({"faces_detected": len(face_locations), "matches": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
