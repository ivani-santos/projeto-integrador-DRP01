#define rotas relacionadas aos perfis, planta = perfis
from flask import Blueprint, render_template

profile = Blueprint('profile', __name__)

@profile.route('/perfil-cliente')
def perfil_cliente():
    return render_template("perfil_cliente.html")