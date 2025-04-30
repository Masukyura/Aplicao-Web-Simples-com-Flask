from flask import Blueprint
from app.controller import (
    index,
    listar_clientes,
    cad_cliente,
    edit_cliente,
    delete_cliente,
    produtos,
    cad_produto,
    edit_produto,
    delete_produto,
)

view = Blueprint("view", __name__)

view.add_url_rule("/", view_func=index)
view.add_url_rule("/clientes", view_func=listar_clientes)
view.add_url_rule("/cad-cliente", view_func=cad_cliente, methods=["GET", "POST"])
view.add_url_rule("/edit-cliente/<int:id>", view_func=edit_cliente, methods=["GET", "POST"])
view.add_url_rule("/delete-cliente/<int:id>", view_func=delete_cliente, methods=["POST"])
view.add_url_rule("/produtos", view_func=produtos)
view.add_url_rule("/cad-produto", view_func=cad_produto, methods=["GET", "POST"])
view.add_url_rule("/edit-produto/<int:id>", view_func=edit_produto, methods=["GET", "POST"])
view.add_url_rule("/delete-produto/<int:id>", view_func=delete_produto, methods=["POST"])

