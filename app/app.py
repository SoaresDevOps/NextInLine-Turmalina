from flask import Flask, render_template
from flask_socketio import SocketIO

# Configuração básica
app = Flask(__name__, static_folder='static', template_folder='static')
socketio = SocketIO(app, cors_allowed_origins="*")

# Página do formulário (envio)
@app.route('/')
def index():
    return render_template('index.html')

# Página da TV (painel)
@app.route('/resultado')
def resultado():
    return render_template('resultado.html')

# 🔥 EVENTO PRINCIPAL (ÚNICO E CORRETO)
@socketio.on('chamada')
def handle_chamada(data):
    print("Nova chamada recebida:", data)  # debug no terminal
    socketio.emit('receive_chamada', data)

# Rodar servidor
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
