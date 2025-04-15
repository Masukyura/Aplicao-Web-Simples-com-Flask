from main import app
from flask import render_template
from controllers import produto_controller, cliente_controller

app = Blueprint('app', __name__)

#Rotas
@app.route("/")
def index():
    return render_template("index.html")

# Página de produtos (lista)
@app.route('/produtos')
def listar_produtos():
    return produto_controller.listar_produtos()

# Página de clientes (lista)
@app.route('/clientes')
def listar_clientes():
    return cliente_controller.listar_clientes()