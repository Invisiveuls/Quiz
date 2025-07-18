from flask import Flask, request

app = Flask(__name__)

@app.route('/process_image_raw', methods=['POST'])
def process_image_raw():
    print("Requisição recebida!")  # Para ver no console
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
