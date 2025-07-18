from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

API_KEY = "AIzaSyCrAZlp9ayGCTMfGEaaMXloERIzn8se6vs"

def limpar_texto(texto):
    # Remove caracteres unicode fora do ASCII básico
    return re.sub(r'[^\x00-\x7F]+','', texto)

@app.route("/gemini", methods=["POST"])
def gemini():
    data = request.get_json()
    text = data.get("text", "")
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
        body = {
            "contents": [
                {"parts": [{"text": text}]}
            ]
        }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url, json=body, headers=headers, timeout=30)
        r.raise_for_status()
        res = r.json()
        resultado_raw = res['candidates'][0]['content']['parts'][0]['text']
        resultado_limpo = limpar_texto(resultado_raw)
        return jsonify({"resposta": resultado_limpo})
    except Exception as e:
        return jsonify({"resposta": "Erro: " + str(e)}), 500

@app.route("/")
def home():
    return "Servidor Gemini online."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
