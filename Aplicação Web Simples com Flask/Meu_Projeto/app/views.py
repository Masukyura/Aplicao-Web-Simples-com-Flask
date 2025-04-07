from main import app
from flask import render_template


#Rotas
@app.route("/")
def base():
    return render_template("base.html")