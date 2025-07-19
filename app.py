from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def check_par_impar():
    numero = request.form.get('numero', '')
    try:
        n = int(numero)
        return 'Par' if n % 2 == 0 else 'Ímpar'
    except:
        return 'Entrada inválida'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
