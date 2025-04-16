from db import db

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)  # Ex: '2000-01-01'
    cidade = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    
class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
     
