from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

GEMINI_KEY = "AIzaSyCrAZlp9ayGCTMfGEaaMXloERIzn8se6vs"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_KEY}"

def limpar_texto(texto):
    # Remove emojis e espaços extras
    texto = re.sub(r'[\U0001F600-\U0001F64F]', '', texto)
    texto = re.sub(r'\\n', ' ', texto)
    return texto.strip()

@app.route('/gemini', methods=['POST'])
def gemini():
    data = request.json
    texto = data.get('texto', '')

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": texto}
                ]
            }
        ]
    }

    headers = {"Content-Type": "application/json"}

    r = requests.post(GEMINI_URL, json=payload, headers=headers)
    try:
        resposta = r.json()["candidates"][0]["content"]["parts"][0]["text"]
    except:
        resposta = "Erro na resposta da API."

    resposta_limpa = limpar_texto(resposta)
    return jsonify({"resposta": resposta_limpa})
