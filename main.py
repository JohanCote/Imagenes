from flask import Flask
from rutas.imagen import routes_imangen

app = Flask(__name__)
app.register_blueprint(routes_imangen)

if __name__ == '__main__':
    app.run(debug=True, port="6000", host="0.0.0.0")