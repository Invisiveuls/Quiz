from flask import Flask, request

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_par_impar():
    numero = request.form.get('numero', '')
    try:
        n = int(numero)
        if n % 2 == 0:
            return 'Par'
        else:
            return 'Ímpar'
    except:
        return 'Entrada inválida'

if __name__ == '__main__':
    app.run()
