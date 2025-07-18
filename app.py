from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/parimpar', methods=['POST'])
def parimpar():
    num = request.form.get('num')
    try:
        n = int(num)
        res = "Par" if n % 2 == 0 else "Ímpar"
    except:
        res = "Número inválido"
    return jsonify({'result': res})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
