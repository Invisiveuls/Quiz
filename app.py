from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API Flask no Render! Use a rota /check_number para verificar se um número é par ou ímpar."

@app.route('/check_number', methods=['POST'])
def check_number():
    data = request.get_json()  # Pega os dados JSON da requisição
    
    if not data or 'number' not in data:
        return jsonify({"error": "Envie um número no formato JSON: {'number': 5}"}), 400
    
    try:
        number = int(data['number'])
        result = "PAR" if number % 2 == 0 else "ÍMPAR"
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "O valor deve ser um número inteiro!"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Render usa a porta 10000
