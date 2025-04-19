from flask import Blueprint, request, redirect, render_template, flash, url_for
from app.model import Usuario, Produto
from db import db

controller = Blueprint('controller', __name__)

# Página inicial
@controller.route('/')
def index():
    return render_template('index.html')

# Cadastrar cliente
@controller.route('/cad-cliente', methods=['GET', 'POST'])
def cad_cliente():
    if request.method == 'POST':
        nome = request.form["nome"]
        email = request.form["email"]
        data_nascimento = request.form["data_nascimento"]
        cidade = request.form["cidade"]
        telefone = request.form["telefone"]

        if not nome or not email or not data_nascimento or not cidade or not telefone:
            flash("Todos os campos são obrigatórios!", "error")
            return redirect(url_for("controller.cad_cliente"))
        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(data_nascimento, str) or not isinstance(cidade, str) or not isinstance(telefone, str):
            flash("Todos os campos devem ser do tipo string!", "error")
            return redirect(url_for("controller.cad_cliente"))
        
        import re
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome):
            flash("Nome deve conter apenas letras e espaços!", "error")
            return redirect(url_for("controller.cad_cliente"))
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", cidade):
            flash("Cidade deve conter apenas letras e espaços!", "error")
            return redirect(url_for("controller.cad_cliente"))

        if not telefone.isdigit():
            flash("Telefone deve conter apenas números!", "error")
            return redirect(url_for("controller.cad_cliente"))
        
        if not re.fullmatch(r"[^@]+@[a-zA-Z]+\.[a-zA-Z]+", email):
            flash("E-mail inválido! Digite um endereço válido como nome@dominio.com", "error")
            return redirect(url_for("controller.cad_cliente"))

        if not data_nascimento:
            flash("Data de nascimento deve ser preenchida!", "error")
            return redirect(url_for("controller.cad_cliente"))
        
                

        novo_usuario = Usuario(
            nome=nome,
            email=email,
            data_nascimento=data_nascimento,
            cidade=cidade,
            telefone=telefone
        )

        db.session.add(novo_usuario)
        db.session.commit()
        flash("Cliente cadastrado com sucesso!", "success")
        return redirect(url_for("controller.clientes"))
    
    return render_template("cad-cliente.html")

#Editar cliente
@controller.route("/edit-cliente/<int:id>", methods=['GET', 'POST'])
def edit_cliente(id):
    cliente = Usuario.query.get_or_404(id)

    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.email = request.form['email']
        cliente.data_nascimento = request.form['data_nascimento']
        cliente.cidade = request.form['cidade']
        cliente.telefone = request.form['telefone']

        if not cliente.nome or not cliente.email or not cliente.data_nascimento or not cliente.cidade or not cliente.telefone:
            flash("Todos os campos são obrigatórios!", "error")
            return redirect(url_for("controller.edit_cliente", id=id))
        if not isinstance(cliente.nome, str) or not isinstance(cliente.email, str) or not isinstance(cliente.data_nascimento, str) or not isinstance(cliente.cidade, str) or not isinstance(cliente.telefone, str):
            flash("Todos os campos devem ser do tipo string!", "error")
            return redirect(url_for("controller.edit_cliente", id=id))
        
        import re
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", cliente.nome):
            flash("Nome deve conter apenas letras e espaços!", "error")
            return redirect(url_for("controller.edit_cliente", id=id))
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", cliente.cidade):
            flash("Cidade deve conter apenas letras e espaços!", "error")
            return redirect(url_for("controller.edit_cliente", id=id))

        if not cliente.telefone.isdigit():
            flash("Telefone deve conter apenas números!", "error")
            return redirect(url_for("controller.edit_cliente", id=id))
        
        if not re.fullmatch(r"[^@]+@[a-zA-Z]+\.[a-zA-Z]+", cliente.email):
            flash("E-mail inválido! Digite um endereço válido como nome@dominio.com", "error")
            return redirect(url_for("controller.edit_cliente", id=id))

        if not cliente.data_nascimento:
            flash("Data de nascimento deve ser preenchida!", "error")
            return redirect(url_for("controller.edit_cliente", id=id))
                

        db.session.commit()
        flash("Cliente atualizado com sucesso!", "success")
        return redirect(url_for('controller.clientes'))

    return render_template("edit-cliente.html", cliente=cliente)


# Listar clientes
@controller.route("/clientes")
def clientes():
    lista = Usuario.query.all()
    return render_template("clientes.html", clientes=lista)

# Cadastrar produto
@controller.route('/cad-produto', methods=['GET', 'POST'])
def cad_produto():
    if request.method == 'POST':
        nome = request.form["nome"]

        try:
            preco = float(request.form["preco"])
            estoque = int(request.form["estoque"])
            quantidade = int(request.form["quantidade"])
        except ValueError:
            flash("Preço, estoque e quantidade devem ser valores numéricos válidos!", "error")
            return redirect(url_for("controller.cad_produto"))

        marca = request.form["marca"]
        categoria = request.form["categoria"]

        if not nome or not preco or not estoque or not quantidade or not marca or not categoria:
            flash("Todos os campos são obrigatórios!", "error")
            return redirect(url_for("controller.cad_produto"))
        
        import re
        # depois dos .strip()
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome):
            flash("Nome deve conter apenas letras e espaços!", "error")
            return redirect(url_for("controller.cad_produto"))        
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", marca):
            flash("Marca deve conter apenas letras e espaços!", "error")
            return redirect(url_for("controller.cad_produto"))        
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", categoria):
            flash("Categoria deve conter apenas letras e espaços!", "error")
            return redirect(url_for("controller.cad_produto"))
        
        if estoque < quantidade:
            flash("Estoque não pode ser menor que a quantidade!", "error")
            return redirect(url_for("controller.cad_produto"))
        if preco <= 0:
            flash("Preço deve ser positivo!", "error")
            return redirect(url_for("controller.cad_produto"))
        if quantidade <= 0:
            flash("Quantidade deve ser positivo!", "error")
            return redirect(url_for("controller.cad_produto"))
        if estoque <= 0:
            flash("Estoque deve ser positivo!", "error")
            return redirect(url_for("controller.cad_produto"))
            
        
        novo_produto = Produto(
            nome=nome,
            preco=preco,
            estoque=estoque,
            quantidade=quantidade,
            marca=marca,
            categoria=categoria
        )

        db.session.add(novo_produto)
        db.session.commit()
        flash("Produto cadastrado com sucesso!", "success")
        return redirect(url_for("controller.produtos"))

    return render_template("cad-produto.html")

#Editar Produto
@controller.route("/edit-produto/<int:id>", methods=['GET', 'POST'])
def edit_produto(id):
    produto = Produto.query.get_or_404(id)

    if request.method == 'POST':
        produto.nome = request.form['nome']

        try:
            produto.preco = float(request.form['preco'])
            produto.estoque = int(request.form['estoque'])
            produto.quantidade = int(request.form['quantidade'])
        except ValueError:
            flash("Preço, estoque e quantidade devem ser valores numéricos válidos!", "error")
            return redirect(url_for("controller.edit_produto", id=id))
        
        produto.marca = request.form['marca']
        produto.categoria = request.form['categoria']

        if not produto.nome or not produto.preco or not produto.estoque or not produto.quantidade or not produto.marca or not produto.categoria:
            flash("Todos os campos são obrigatórios!", "error")
            return redirect(url_for("controller.edit_produto", id=id))
        if produto.preco <= 0:
            flash("Preço deve ser positivo!", "error")
            return redirect(url_for("controller.edit_produto", id=id))
        if produto.estoque <= 0:
            flash("Estoque deve ser positivo!", "error")
            return redirect(url_for("controller.edit_produto", id=id))
        if produto.quantidade <= 0:
            flash("Quantidade deve ser positiva!", "error")
            return redirect(url_for("controller.edit_produto", id=id))
        
        import re
        
        # Validação com regex para permitir letras e espaços
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", produto.nome):
            flash("Nome deve conter apenas letras e espaços!", "error")
            return redirect(url_for("controller.edit_produto", id=id))

        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", produto.marca):
            flash("Marca deve conter apenas letras e espaços!", "error")
            return redirect(url_for("controller.edit_produto", id=id))

        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", produto.categoria):
            flash("Categoria deve conter apenas letras e espaços!", "error")
            return redirect(url_for("controller.edit_produto", id=id))

        if produto.estoque < produto.quantidade:
            flash("Estoque não pode ser menor que a quantidade!", "error")
            return redirect(url_for("controller.edit_produto", id=id))
        
        
        db.session.commit()
        flash("Produto atualizado com sucesso!", "success")
        return redirect(url_for('controller.produtos'))

    return render_template("edit-produto.html", produto=produto)

# Listar produtos
@controller.route("/produtos")
def produtos():
    lista = Produto.query.all()
    return render_template("produtos.html", produtos=lista)


# Deletar cliente
@controller.route('/delete-cliente/<int:id>', methods=['POST'])
def delete_cliente(id):
    cliente = Usuario.query.get_or_404(id)

    try:
        db.session.delete(cliente)
        db.session.commit()
        flash("Cliente excluído com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao excluir cliente: {str(e)}", "error")

    return redirect(url_for('controller.clientes'))

# Deletar produto
@controller.route('/delete-produto/<int:id>', methods=['POST'])
def delete_produto(id):
    produto = Produto.query.get_or_404(id)

    try:
        db.session.delete(produto)
        db.session.commit()
        flash("Produto excluído com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao excluir produto: {str(e)}", "error")

    return redirect(url_for('controller.produtos'))

