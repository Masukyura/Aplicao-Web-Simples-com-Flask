from flask import Flask, render_template, request, redirect, url_for
from controllers import produto_controller, cliente_controller
from db import db
from model import Usuario, Produto

app = Flask(__name__)

# Rota inicial
@app.route("/")
def index():
    return render_template("index.html")

# Lista de produtos
@app.route("/produtos")
def listar_produtos():
    return produto_controller.listar_produtos()

# Lista de clientes
@app.route("/clientes")
def listar_clientes():
    return cliente_controller.listar_clientes()

@app.route("/cadastrar-cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        data_nascimento = request.form["data_nascimento"]
        cidade = request.form["cidade"]
        telefone = request.form["telefone"]

        novo_usuario = Usuario(
            nome=nome,
            email=email,
            data_nascimento=data_nascimento,
            cidade=cidade,
            telefone=telefone
        )

        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for("cad-cliente"))  # após cadastro, volta pra lista
    
    # Aqui ele renderiza o formulário normalmente em GET
    return render_template("cad-cliente.html")

# Cadastro de produto
@app.route("/cadastrar-produto", methods=["GET", "POST"])
def cadastrar_produto():
    if request.method == "POST":
        nome = request.form["nome"]
        preco = float(request.form["preco"])
        estoque = int(request.form["estoque"])
        marca = request.form["marca"]
        categoria = request.form["categoria"]

        novo_produto = Produto(
            nome=nome,
            preco=preco,
            estoque=estoque,
            marca=marca,
            categoria=categoria
        )
        db.session.add(novo_produto)
        db.session.commit()
        return redirect(url_for("cad-produto"))  # ou cadastrar_produto
    
    return render_template("cad-produto.html")
