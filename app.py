from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyCrAZlp9ayGCTMfGEaaMXloERIzn8se6vs"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

@app.route('/gemini', methods=['POST'])
def gemini():
    data = request.get_json()
    pergunta = data.get('pergunta', '')
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": pergunta}
                ]
            }
        ]
    }
    try:
        res = requests.post(URL, json=payload)
        res.raise_for_status()
        resposta = res.json()
        texto = resposta["candidates"][0]["content"]["parts"][0]["text"]
        texto = texto.replace("\\n", " ")  # Remove \n literal
        return jsonify({"resposta": texto})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
