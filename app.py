from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuração para evitar respostas HTML
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config['JSON_SORT_KEYS'] = False

@app.route('/check_number', methods=['POST'])
def check_number():
    # Verifica explicitamente o Content-Type
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415
    
    try:
        data = request.get_json()
        number = int(data['number'])
        return jsonify({
            "status": "success",
            "number": number,
            "result": "PAR" if number % 2 == 0 else "ÍMPAR"
        })
    except KeyError:
        return jsonify({"error": "Campo 'number' faltando"}), 400
    except ValueError:
        return jsonify({"error": "O valor deve ser um número inteiro"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
