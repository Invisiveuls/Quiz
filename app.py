from flask import Flask, request, jsonify
import requests
import re
import html

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyCrAZlp9ayGCTMfGEaaMXloERIzn8se6vs"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def limpar_texto(texto):
    texto = html.unescape(texto)
    texto = texto.encode().decode('unicode_escape')
    texto = re.sub(r'\\[nrt]', ' ', texto)
    texto = re.sub(r'\\+', '', texto)
    texto = re.sub(r'\"', '', texto)
    texto = re.sub(r'[\U00010000-\U0010ffff]', '', texto)
    texto = re.sub(r'<.*?>', '', texto)
    texto = re.sub(r'\s+', ' ', texto)
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
        resposta = res.json()
        texto = resposta["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"resposta": limpar_texto(texto)})
    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == "__main__":
    app.run()
