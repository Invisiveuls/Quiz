from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyBNAH9GQmuhjT45HizNxfXokZT__gGLxHI"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

@app.route('/gemini', methods=['POST'])
def gemini():
    user_text = request.form.get('text', '')
    payload = {
        "prompt": {
            "text": user_text
        },
        "maxOutputTokens": 100
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        # Ajuste conforme resposta real da API
        text = result.get('candidates', [{}])[0].get('output', '')
        return jsonify({"response": text})
    else:
        return jsonify({"response": "Erro na API"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
