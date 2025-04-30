from flask import render_template, request, redirect, url_for, flash
from app.model import Usuario, Produto
from db import db
import re

# --- CLIENTES ---

def index():
    return render_template("index.html")

def listar_clientes():
    lista = Usuario.query.all()
    return render_template("clientes.html", clientes=lista)

def cad_cliente():
    if request.method == 'POST':
        nome = request.form["nome"].strip()
        email = request.form["email"].strip()
        data_nascimento = request.form["data_nascimento"]
        cidade = request.form["cidade"].strip()
        telefone = request.form["telefone"].strip()

        if not nome or not email or not data_nascimento or not cidade or not telefone:
            flash("Todos os campos são obrigatórios!", "error")
            return redirect(url_for("view.cad_cliente"))

        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome):
            flash("Nome deve conter apenas letras e espaços!", "error")
            return redirect(url_for("view.cad_cliente"))

        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", cidade):
            flash("Cidade deve conter apenas letras e espaços!", "error")
            return redirect(url_for("view.cad_cliente"))

        if not re.fullmatch(r"[^@]+@[a-zA-Z]+\.[a-zA-Z]+", email):
            flash("E-mail inválido! Digite um endereço válido como nome@dominio.com", "error")
            return redirect(url_for("view.cad_cliente"))

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
        return redirect(url_for("view.listar_clientes"))

    return render_template("cad-cliente.html")

def edit_cliente(id):
    cliente = Usuario.query.get_or_404(id)

    if request.method == 'POST':
        cliente.nome = request.form['nome'].strip()
        cliente.email = request.form['email'].strip()
        cliente.data_nascimento = request.form['data_nascimento']
        cliente.cidade = request.form['cidade'].strip()
        cliente.telefone = request.form['telefone'].strip()

        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", cliente.nome):
            flash("Nome deve conter apenas letras e espaços!", "error")
            return redirect(url_for("view.edit_cliente", id=id))

        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", cliente.cidade):
            flash("Cidade deve conter apenas letras e espaços!", "error")
            return redirect(url_for("view.edit_cliente", id=id))

        if not re.fullmatch(r"[^@]+@[a-zA-Z]+\.[a-zA-Z]+", cliente.email):
            flash("E-mail inválido! Digite um endereço válido como nome@dominio.com", "error")
            return redirect(url_for("view.edit_cliente", id=id))

        db.session.commit()
        flash("Cliente atualizado com sucesso!", "success")
        return redirect(url_for("view.listar_clientes"))

    return render_template("edit-cliente.html", cliente=cliente)

def delete_cliente(id):
    cliente = Usuario.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    flash("Cliente excluído com sucesso!", "success")
    return redirect(url_for("view.listar_clientes"))

# --- PRODUTOS ---

def produtos():
    lista = Produto.query.all()
    return render_template("produtos.html", produtos=lista)

def cad_produto():
    if request.method == 'POST':
        nome = request.form["nome"].strip()
        marca = request.form["marca"].strip()
        categoria = request.form["categoria"].strip()

        try:
            preco = float(request.form["preco"])
            estoque = int(request.form["estoque"])
            quantidade = int(request.form["quantidade"])
        except ValueError:
            flash("Preço, estoque e quantidade devem ser valores numéricos válidos!", "error")
            return redirect(url_for("view.cad_produto"))

        if not nome or not marca or not categoria:
            flash("Todos os campos são obrigatórios!", "error")
            return redirect(url_for("view.cad_produto"))

        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome) or not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", marca) or not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", categoria):
            flash("Nome, marca e categoria devem conter apenas letras e espaços!", "error")
            return redirect(url_for("view.cad_produto"))

        if preco <= 0 or estoque <= 0 or quantidade <= 0:
            flash("Preço, estoque e quantidade devem ser maiores que zero!", "error")
            return redirect(url_for("view.cad_produto"))

        if estoque < quantidade:
            flash("Estoque não pode ser menor que a quantidade!", "error")
            return redirect(url_for("view.cad_produto"))

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
        return redirect(url_for("view.produtos"))

    return render_template("cad-produto.html")

def edit_produto(id):
    produto = Produto.query.get_or_404(id)

    if request.method == 'POST':
        produto.nome = request.form['nome'].strip()
        produto.marca = request.form['marca'].strip()
        produto.categoria = request.form['categoria'].strip()

        try:
            produto.preco = float(request.form['preco'])
            produto.estoque = int(request.form['estoque'])
            produto.quantidade = int(request.form['quantidade'])
        except ValueError:
            flash("Preço, estoque e quantidade devem ser valores numéricos válidos!", "error")
            return redirect(url_for("view.edit_produto", id=id))

        if not produto.nome or not produto.marca or not produto.categoria:
            flash("Todos os campos são obrigatórios!", "error")
            return redirect(url_for("view.edit_produto", id=id))

        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", produto.nome) or not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", produto.marca) or not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", produto.categoria):
            flash("Nome, marca e categoria devem conter apenas letras e espaços!", "error")
            return redirect(url_for("view.edit_produto", id=id))

        if produto.preco <= 0 or produto.estoque <= 0 or produto.quantidade <= 0:
            flash("Preço, estoque e quantidade devem ser maiores que zero!", "error")
            return redirect(url_for("view.edit_produto", id=id))

        if produto.estoque < produto.quantidade:
            flash("Estoque não pode ser menor que a quantidade!", "error")
            return redirect(url_for("view.edit_produto", id=id))

        db.session.commit()
        flash("Produto atualizado com sucesso!", "success")
        return redirect(url_for('view.produtos'))

    return render_template("edit-produto.html", produto=produto)

def delete_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    flash("Produto excluído com sucesso!", "success")
    return redirect(url_for("view.produtos"))


