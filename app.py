from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_number', methods=['GET', 'POST'])  # Aceita ambos os métodos
def check_number():
    # Se for GET (teste via navegador)
    if request.method == 'GET':
        number = request.args.get('number', default=0, type=int)
    # Se for POST (requisição do app)
    else:
        data = request.get_json()
        number = int(data.get('number', 0))
    
    result = "PAR" if number % 2 == 0 else "ÍMPAR"
    return jsonify({"result": result, "number": number})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
