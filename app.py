from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyCrAZlp9ayGCTMfGEaaMXloERIzn8se6vs"

@app.route("/gemini", methods=["POST"])
def gemini():
    data = request.get_json()
    text = data.get("text", "")
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
        body = {
            "contents": [
                {
                    "parts": [
                        {"text": text}
                    ]
                }
            ]
        }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url, json=body, headers=headers, timeout=30)
        r.raise_for_status()
        res_json = r.json()
        result = res_json['candidates'][0]['content']['parts'][0]['text']
        return jsonify({"resposta": result})
    except Exception as e:
        return jsonify({"resposta": "Erro: " + str(e)}), 500

@app.route("/")
def home():
    return "Servidor Gemini online."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
