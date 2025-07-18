from flask import Flask, request, jsonify
import requests
import re
import html
import os

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyCrAZlp9ayGCTMfGEaaMXloERIzn8se6vs"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def limpar_texto(texto):
    texto = html.unescape(texto)               # Converte entidades HTML
    texto = texto.replace("\\n", " ")          # Remove \n literal
    texto = texto.encode().decode('unicode_escape')
    texto = re.sub(r'\\[rt]', ' ', texto)      # Remove \r \t literal
    texto = re.sub(r'\\+', '', texto)           # Remove barras extras
    texto = re.sub(r'\"', '', texto)            # Remove aspas
    texto = re.sub(r'[\U00010000-\U0010ffff]', '', texto)  # Remove emojis
    texto = re.sub(r'<.*?>', '', texto)         # Remove tags HTML
    texto = re.sub(r'\s+', ' ', texto)          # Remove espaços extras
    return texto.strip()

@app.route("/gemini", methods=["POST"])
def gemini():
    data = request.get_json()
    prompt = data.get("pergunta", "")
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        res = requests.post(GEMINI_URL, json=payload)
        res.raise_for_status()
        resposta = res.json()
        texto = resposta["candidates"][0]["content"]["parts"][0]["text"]
        texto_limpo = limpar_texto(texto)
        return jsonify({"resposta": texto_limpo})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
