from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Servidor Flask Online!'

@app.route('/toast', methods=['POST'])
def toast():
    msg = request.form.get('msg', 'Olá do servidor')
    return jsonify({'toast_msg': msg})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)